#!/usr/bin/env python3
"""
Calculate position sizes for Month 1 deployment based on platform capital allocation.

Usage:
    python3 scripts/calculate_positions.py --capital 50000
"""

import argparse
from pathlib import Path
import re
import json


def parse_current_stock_scores(file_path):
    """Parse current_stock_scores.md file to extract ticker and score."""
    with open(file_path, 'r') as f:
        content = f.read()

    scores = []

    # Match table rows: | TICKER | SCORE | DATE |
    pattern = r'\|\s*([A-Z]+)\s*\|\s*(\d+\.?\d*)\s*\|'
    matches = re.findall(pattern, content)

    for ticker, score in matches:
        scores.append({'ticker': ticker, 'score': float(score)})

    return scores


def load_blocklist():
    """Load blocklisted tickers from trading_restrictions.json."""
    restrictions_file = Path('platform/trading_restrictions.json')
    if not restrictions_file.exists():
        return set()

    with open(restrictions_file, 'r') as f:
        data = json.load(f)
        return {item['ticker'] for item in data.get('blocklist', [])}


def load_all_scores():
    """Load all platform scores from current_stock_scores.md files."""
    all_scores = []
    seen_tickers = set()
    blocklist = load_blocklist()

    segments = [
        'platform/compute_stack',
        'platform/critical_enablers'
    ]

    for segment in segments:
        scores_file = Path(segment) / 'current_stock_scores.md'
        if not scores_file.exists():
            continue

        scores = parse_current_stock_scores(scores_file)

        # Avoid duplicates (e.g., NVDA, MU appear in both segments)
        # Also filter out blocklisted tickers
        for stock in scores:
            if stock['ticker'] not in seen_tickers and stock['ticker'] not in blocklist:
                all_scores.append(stock)
                seen_tickers.add(stock['ticker'])

    if blocklist:
        print(f"ℹ️  Excluded blocklisted tickers: {', '.join(sorted(blocklist))}")
        print()

    return sorted(all_scores, key=lambda x: x['score'], reverse=True)


def categorize_stocks(scores):
    """Categorize stocks into tiers based on scores."""
    tier1 = [s for s in scores if s['score'] >= 4.5]
    tier2 = [s for s in scores if 4.0 <= s['score'] < 4.5]
    tier3 = [s for s in scores if 3.5 <= s['score'] < 4.0]

    return {
        'tier1': tier1,
        'tier2': tier2,
        'tier3': tier3
    }


def calculate_positions(capital, month1_pct=0.40, leaps_pct_min=0.05, leaps_pct_max=0.10):
    """
    Calculate position sizes for Month 1 deployment.

    Args:
        capital: Total platform capital
        month1_pct: Percentage to deploy in Month 1 (default 40%)
        leaps_pct_min: Minimum LEAPS allocation (default 5%)
        leaps_pct_max: Maximum LEAPS allocation (default 10%)
    """
    scores = load_all_scores()
    tiers = categorize_stocks(scores)

    # Month 1 capital deployment
    month1_capital = capital * month1_pct

    # LEAPS allocation (from total platform capital, not month1)
    leaps_min = capital * leaps_pct_min
    leaps_max = capital * leaps_pct_max

    # Use midpoint for LEAPS allocation
    leaps_allocation = (leaps_min + leaps_max) / 2

    # Calculate position sizes
    positions = []

    # Tier 1: 4% each initial
    for stock in tiers['tier1']:
        positions.append({
            'ticker': stock['ticker'],
            'tier': 1,
            'score': stock['score'],
            'pct': 0.04,
            'amount': capital * 0.04
        })

    # Tier 2: 2.5% each initial
    for stock in tiers['tier2']:
        positions.append({
            'ticker': stock['ticker'],
            'tier': 2,
            'score': stock['score'],
            'pct': 0.025,
            'amount': capital * 0.025
        })

    # Skip Tier 3 - will be covered by product sleeve

    # LEAPS: Top 3 Tier 1 stocks, 2% each (from total capital)
    leaps_positions = []
    top_tier1 = tiers['tier1'][:3]
    for stock in top_tier1:
        leaps_positions.append({
            'ticker': f"{stock['ticker']} Jan 2026 LEAPS",
            'score': stock['score'],
            'pct': 0.02,
            'amount': capital * 0.02
        })

    return {
        'capital': capital,
        'month1_capital': month1_capital,
        'equity_positions': positions,
        'leaps_positions': leaps_positions,
        'leaps_total': sum(p['amount'] for p in leaps_positions),
        'equity_total': sum(p['amount'] for p in positions),
        'tiers': tiers
    }


def print_report(results):
    """Print formatted position sizing report."""
    print("=" * 80)
    print("PLATFORM MONTH 1 POSITION SIZING")
    print("=" * 80)
    print()
    print(f"Total Platform Capital: ${results['capital']:,.0f}")
    print(f"Month 1 Deployment (40%): ${results['month1_capital']:,.0f}")
    print()
    print(f"LEAPS Allocation (5-10%): ${results['leaps_total']:,.0f} ({results['leaps_total']/results['capital']*100:.1f}%)")
    print(f"Equity Allocation: ${results['equity_total']:,.0f} ({results['equity_total']/results['capital']*100:.1f}%)")
    print()

    # Equity positions
    print("-" * 80)
    print("EQUITY POSITIONS")
    print("-" * 80)
    print(f"{'Ticker':<10} {'Tier':<6} {'Score':<8} {'% of Capital':<15} {'Amount':<15}")
    print("-" * 80)

    for pos in results['equity_positions']:
        print(f"{pos['ticker']:<10} {pos['tier']:<6} {pos['score']:<8.2f} {pos['pct']*100:<15.1f} ${pos['amount']:<14,.0f}")

    print("-" * 80)
    print(f"{'TOTAL EQUITY':<10} {'':<6} {'':<8} {results['equity_total']/results['capital']*100:<15.1f} ${results['equity_total']:<14,.0f}")
    print()

    # LEAPS positions
    print("-" * 80)
    print("LEAPS POSITIONS (Tier 1 Only)")
    print("-" * 80)
    print(f"{'Ticker':<25} {'Score':<8} {'% of Capital':<15} {'Amount':<15}")
    print("-" * 80)

    for pos in results['leaps_positions']:
        print(f"{pos['ticker']:<25} {pos['score']:<8.2f} {pos['pct']*100:<15.1f} ${pos['amount']:<14,.0f}")

    print("-" * 80)
    print(f"{'TOTAL LEAPS':<25} {'':<8} {results['leaps_total']/results['capital']*100:<15.1f} ${results['leaps_total']:<14,.0f}")
    print()

    # Summary
    total_deployed = results['equity_total'] + results['leaps_total']
    remaining = results['capital'] - total_deployed

    print("=" * 80)
    print("SUMMARY")
    print("=" * 80)
    print(f"Total Deployed (Month 1): ${total_deployed:,.0f} ({total_deployed/results['capital']*100:.1f}%)")
    print(f"Remaining Dry Powder: ${remaining:,.0f} ({remaining/results['capital']*100:.1f}%)")
    print()
    print(f"Tier 1 Stocks (≥4.5): {len(results['tiers']['tier1'])}")
    print(f"Tier 2 Stocks (4.0-4.5): {len(results['tiers']['tier2'])}")
    print(f"Tier 3 Stocks (3.5-4.0): {len(results['tiers']['tier3'])}")
    print(f"Total Positions: {len(results['equity_positions']) + len(results['leaps_positions'])}")
    print("=" * 80)


def write_output_file(results, output_path):
    """Write position sizing to a markdown file."""
    lines = [
        "# Platform Month 1 Position Sizing",
        "",
        f"**Total Platform Capital**: ${results['capital']:,.0f}",
        f"**Month 1 Deployment (40%)**: ${results['month1_capital']:,.0f}",
        "",
        "---",
        "",
        "## Equity Positions",
        "",
        "| Ticker | Tier | Score | Initial % | Initial $ | Target % (Final) | Target $ (Final) |",
        "|--------|------|-------|-----------|-----------|------------------|------------------|"
    ]

    for pos in results['equity_positions']:
        # Initial values
        initial_pct = pos['pct'] * 100
        initial_amt = pos['amount']

        # Target values based on tier
        if pos['tier'] == 1:
            target_pct = 9.0  # midpoint of 7-10%
            target_amt = results['capital'] * 0.09
        elif pos['tier'] == 2:
            target_pct = 5.5  # midpoint of 4-7%
            target_amt = results['capital'] * 0.055
        else:  # tier 3
            target_pct = 4.0  # midpoint of 3-5%
            target_amt = results['capital'] * 0.04

        lines.append(
            f"| {pos['ticker']} | {pos['tier']} | {pos['score']:.2f} | "
            f"{initial_pct:.1f}% | ${initial_amt:,.0f} | "
            f"{target_pct:.1f}% | ${target_amt:,.0f} |"
        )

    equity_total = sum(p['amount'] for p in results['equity_positions'])
    lines.append(
        f"| **TOTAL** | | | **{equity_total/results['capital']*100:.1f}%** | "
        f"**${equity_total:,.0f}** | | |"
    )

    lines.extend([
        "",
        "---",
        "",
        "## LEAPS Positions",
        "",
        "| Ticker | Score | Initial % | Initial $ | Target % (Final) | Target $ (Final) |",
        "|--------|-------|-----------|-----------|------------------|------------------|"
    ])

    for pos in results['leaps_positions']:
        initial_pct = pos['pct'] * 100
        initial_amt = pos['amount']
        target_pct = 3.0
        target_amt = results['capital'] * 0.03

        lines.append(
            f"| {pos['ticker']} | {pos['score']:.2f} | "
            f"{initial_pct:.1f}% | ${initial_amt:,.0f} | "
            f"{target_pct:.1f}% | ${target_amt:,.0f} |"
        )

    leaps_total = sum(p['amount'] for p in results['leaps_positions'])
    lines.append(
        f"| **TOTAL** | | **{leaps_total/results['capital']*100:.1f}%** | "
        f"**${leaps_total:,.0f}** | | |"
    )

    lines.extend([
        "",
        "---",
        "",
        "## Summary",
        "",
        f"- **Total Deployed (Month 1)**: ${equity_total + leaps_total:,.0f} ({(equity_total + leaps_total)/results['capital']*100:.1f}%)",
        f"- **Remaining Dry Powder**: ${results['capital'] - equity_total - leaps_total:,.0f} ({(results['capital'] - equity_total - leaps_total)/results['capital']*100:.1f}%)",
        f"- **Total Positions**: {len(results['equity_positions']) + len(results['leaps_positions'])}",
        "",
        "### Tier Distribution",
        f"- Tier 1 (≥4.5): {len(results['tiers']['tier1'])} stocks",
        f"- Tier 2 (4.0-4.5): {len(results['tiers']['tier2'])} stocks",
        f"- Tier 3 (3.5-4.0): {len(results['tiers']['tier3'])} stocks",
    ])

    with open(output_path, 'w') as f:
        f.write('\n'.join(lines))


def main():
    parser = argparse.ArgumentParser(
        description='Calculate Month 1 position sizes for platform allocation'
    )
    parser.add_argument(
        '--capital',
        type=float,
        required=True,
        help='Total platform capital (e.g., 50000)'
    )
    parser.add_argument(
        '--output',
        type=str,
        default='platform/month1_positions.md',
        help='Output file path (default: platform/month1_positions.md)'
    )

    args = parser.parse_args()

    results = calculate_positions(args.capital)
    print_report(results)

    # Write output file
    output_path = Path(args.output)
    write_output_file(results, output_path)
    print()
    print(f"✓ Position sizing saved to: {output_path}")


if __name__ == '__main__':
    main()
