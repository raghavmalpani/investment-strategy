# Claude Instructions - Investment Strategy Project

## Project Overview
This project implements a systematic AI-focused equity investment strategy with scoring frameworks for multiple market segments. The strategy is documented in `AI_AI_stock_strategy.md` with scoring methodology in `AI_scoring_sheet.md`.

## Directory Structure

```
investment_strategy/
├── claude.md                          # This file - master instructions
├── AI_AI_stock_strategy.md           # Overall investment thesis & framework
├── AI_scoring_sheet.md               # High-level scoring methodology (1-5 scale)
├── AI_watchlist_seeds.md             # Initial ticker seeds (if exists)
└── scoring/                          # Segment-specific scoring directories
    ├── compute_stack/
    ├── critical_enablers/
    ├── endpoint_gatekeepers/
    ├── productivity_devops/
    ├── commerce_ads/
    ├── industrial_logistics/
    ├── healthcare_regulated/
    └── consumer_social_media/
```

## Segment Directory Template

Each segment follows this structure:

```
scoring/{segment_name}/
├── claude.md                      # Segment-specific instructions
├── scoring_guide.md               # Dimension definitions, weights, trigger flags
├── currently_invested_stocks.md   # Portfolio allocation tracker
├── perplexity_notes/             # Research organized by date (MM-DD.md)
└── stock_notes/                  # Individual ticker analysis (TICKER.md)
```

## File Responsibilities

### Top-Level Files

**`AI_AI_stock_strategy.md`**
- Investment thesis and market segmentation
- Capital deployment framework
- Data collection playbook
- Risk/reward positioning guidelines
- **Updates:** Rarely - only when overall strategy changes

**`AI_scoring_sheet.md`**
- General 1-5 scoring scale definitions
- Links to segment-specific scorecards
- Implementation notes
- **Updates:** Rarely - foundational methodology

**`AI_watchlist_seeds.md`**
- Initial ticker lists by segment
- **Updates:** Add new watchlist candidates as discovered

### Segment-Level Files

**`scoring_guide.md`**
- Scoring dimensions with weights (should sum to ~6.0)
- Sample indicators for each dimension
- Trigger flag definitions (hard/soft)
- Watchlist table with scores
- **Updates:** Add latest scores to watchlist table after each review

**`currently_invested_stocks.md`**
- Portfolio table: ticker, shares, cost basis, value, % allocation
- **Updates:** Fill in as positions are taken; update periodically

**`perplexity_notes/MM-DD.md`**
- User-added research notes organized by date
- **Format:** Filename = `MM-DD.md` (e.g., `10-5.md`)
- **Updates:** User creates; AI reads as input

**`stock_notes/{TICKER}.md`**
- Timestamped scoring history for individual stocks
- **Format:** Append new date sections, don't overwrite
- **Updates:** After each scoring session

## Standard Workflow

### 1. Setting Up a New Segment
```
1. Create directory: scoring/{segment_name}/
2. Create subdirectories: perplexity_notes/, stock_notes/
3. Create files:
   - claude.md (segment-specific instructions)
   - scoring_guide.md (dimensions & weights)
   - currently_invested_stocks.md (empty table template)
4. Create empty .md files in stock_notes/ for each ticker
```

### 2. Scoring Stocks
```
1. Read perplexity_notes/ for latest research
2. Pull financial data via MCP tools (getStockPriceSnapshot, getCompanyFacts, etc.)
3. Reference scoring_guide.md for dimension definitions
4. Score each dimension (1-5), multiply by weight, sum and normalize
5. Document in stock_notes/{TICKER}.md with timestamp
6. Update watchlist table in scoring_guide.md with latest scores
7. Flag any triggers
```

### 3. Stock Notes Format
```markdown
## YYYY-MM-DD

### Scoring
- Dimension 1: X/5 (Weight: X.X) = X.X
- Dimension 2: X/5 (Weight: X.X) = X.X
[... all dimensions ...]
**Total: X.XX / 5**

### Key Points
- Concise bullets
- Notable changes
- Action items

### Trigger Flags
- [ ] None OR list triggers

### Sources
- Perplexity: perplexity_notes/MM-DD.md
- MCP: YYYY-MM-DD
```

## Documentation Standards

### Date Formats
- **Filenames:** `MM-DD.md` (e.g., `10-5.md`)
- **Section headers:** `YYYY-MM-DD` (e.g., `2025-10-05`)
- **Data source timestamps:** `YYYY-MM-DD`

### Writing Style
- **Concise:** Bullets over paragraphs
- **Timestamped:** Always date new entries
- **Source-referenced:** Note where data came from
- **Append-only:** Keep historical entries in stock notes
- **Scannable:** Focus on actionable insights, not verbose explanations

### MCP Tools to Use

**Primary Tools (Always use for scoring):**
- `getStockPriceSnapshot` - Current price & market cap
- `getCompanyFacts` - Company overview, employees, sector
- `getFinancialMetricsSnapshot` - Valuation ratios, margins, ROIC
- `getIncomeStatement` - Revenue, earnings, margins
- `getBalanceSheet` - Assets, liabilities, debt
- `getCashFlowStatement` - FCF, capex, cash position

**Supplemental Tool (Optional):**
- `getNews` - Recent news headlines with sentiment
  - **Use case:** Monthly news pulse check, breaking story alerts
  - **Limit to:** 5-10 articles for quick sentiment scan
  - **Note:** Perplexity notes provide deeper context; use news tool between research cycles, not as replacement

## Capital Deployment Framework
- **Baseline anchor (35-40%):** Compute stack bellwethers
- **Opportunity sleeve (60-65%):**
  - 30-35% vertical AI leaders
  - 15-20% endpoint gatekeepers
  - 10% dry powder
- **Position sizing:** Cap at 8-10% unless score ≥4.5 with no triggers
- **Rebalance:** Monthly trigger checks, full rescore post-earnings

## Review Cadence
- **Full rescore:** Quarterly (post-earnings)
- **Trigger check:** Monthly
- **Major events:** Export controls, partnerships, M&A, regulatory changes
- **Harvest:** When position exceeds 1.5× target weight or score momentum negative for 2 reviews
