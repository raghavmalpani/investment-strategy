#!/usr/bin/env python3
"""
Extract latest scores from stock_notes/*.md files and create a current_stock_scores.md file.

Usage:
    python scripts/extract_latest_scores.py platform/compute_stack
    python scripts/extract_latest_scores.py platform/critical_enablers
"""

import os
import sys
import re
from datetime import datetime
from pathlib import Path


def parse_stock_note(file_path):
    """
    Parse a stock note file and extract the most recent score.

    Returns:
        tuple: (ticker, latest_date, score, score_dict) or None if no scores found
    """
    with open(file_path, 'r') as f:
        content = f.read()

    ticker = Path(file_path).stem

    # Find all date sections (## YYYY-MM-DD)
    date_pattern = r'## (\d{4}-\d{2}-\d{2})'
    dates = re.findall(date_pattern, content)

    if not dates:
        return None

    # Get the most recent date
    latest_date = max(dates)

    # Extract the section for the latest date
    section_pattern = rf'## {re.escape(latest_date)}(.*?)(?=## \d{{4}}-\d{{2}}-\d{{2}}|$)'
    section_match = re.search(section_pattern, content, re.DOTALL)

    if not section_match:
        return None

    section = section_match.group(1)

    # Extract total score (look for "**Total: X.XX / 5**" or similar)
    total_pattern = r'\*\*Total[:\s]+(\d+\.?\d*)\s*/?\s*5?\*\*'
    total_match = re.search(total_pattern, section, re.IGNORECASE)

    if not total_match:
        return None

    score = float(total_match.group(1))

    # Extract dimension scores (optional - for detailed view)
    dimension_pattern = r'-\s+([^:]+):\s*(\d+\.?\d*)/5'
    dimensions = re.findall(dimension_pattern, section)
    score_dict = {dim.strip(): float(val) for dim, val in dimensions}

    return ticker, latest_date, score, score_dict


def generate_scores_markdown(segment_path):
    """
    Generate a markdown file with all current scores for a segment.

    Args:
        segment_path: Path to segment directory (e.g., 'platform/compute_stack')
    """
    stock_notes_dir = Path(segment_path) / 'stock_notes'

    if not stock_notes_dir.exists():
        print(f"Error: {stock_notes_dir} does not exist")
        return

    scores = []

    # Process all .md files in stock_notes/
    for note_file in stock_notes_dir.glob('*.md'):
        result = parse_stock_note(note_file)
        if result:
            ticker, date, score, dimensions = result
            scores.append({
                'ticker': ticker,
                'date': date,
                'score': score,
                'dimensions': dimensions
            })

    if not scores:
        print(f"No scores found in {stock_notes_dir}")
        return

    # Sort by score (descending)
    scores.sort(key=lambda x: x['score'], reverse=True)

    # Generate markdown content
    segment_name = Path(segment_path).name
    output_lines = [
        f"# Current Stock Scores - {segment_name.replace('_', ' ').title()}",
        "",
        f"*Last updated: {datetime.now().strftime('%Y-%m-%d')}*",
        "",
        "| Ticker | Score | Last Updated |",
        "|--------|-------|--------------|"
    ]

    for item in scores:
        output_lines.append(
            f"| {item['ticker']} | {item['score']:.2f} | {item['date']} |"
        )

    output_lines.append("")
    output_lines.append("---")
    output_lines.append("")
    output_lines.append("## Score Distribution")
    output_lines.append("")

    # Group by score ranges
    tier1 = [s for s in scores if s['score'] >= 4.5]
    tier2 = [s for s in scores if 4.0 <= s['score'] < 4.5]
    tier3 = [s for s in scores if 3.5 <= s['score'] < 4.0]
    tier4 = [s for s in scores if 3.0 <= s['score'] < 3.5]
    watchlist = [s for s in scores if s['score'] < 3.0]

    output_lines.append(f"- **Tier 1 (≥4.5)**: {len(tier1)} stocks - {', '.join(s['ticker'] for s in tier1)}")
    output_lines.append(f"- **Tier 2 (4.0-4.5)**: {len(tier2)} stocks - {', '.join(s['ticker'] for s in tier2)}")
    output_lines.append(f"- **Tier 3 (3.5-4.0)**: {len(tier3)} stocks - {', '.join(s['ticker'] for s in tier3)}")
    output_lines.append(f"- **Tier 4 (3.0-3.5)**: {len(tier4)} stocks - {', '.join(s['ticker'] for s in tier4)}")
    output_lines.append(f"- **Watchlist (<3.0)**: {len(watchlist)} stocks - {', '.join(s['ticker'] for s in watchlist)}")

    # Write output file
    output_file = Path(segment_path) / 'current_stock_scores.md'
    with open(output_file, 'w') as f:
        f.write('\n'.join(output_lines))

    print(f"✓ Created {output_file}")
    print(f"  Processed {len(scores)} stocks")


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python scripts/extract_latest_scores.py <segment_path>")
        print("Example: python scripts/extract_latest_scores.py platform/compute_stack")
        sys.exit(1)

    segment_path = sys.argv[1]
    generate_scores_markdown(segment_path)
