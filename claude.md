# Claude Instructions - Investment Strategy Project

## Project Overview
This project implements a systematic AI-focused equity investment strategy with scoring frameworks for multiple market segments. The strategy is documented in `AI_AI_stock_strategy.md` with scoring methodology in `AI_scoring_sheet.md`.

**Risk Profile:** This is a **high-growth, high-risk sleeve** positioned for AI thesis upside. We tolerate >30% drawdowns in exchange for asymmetric upside if generative AI adoption accelerates. Scoring emphasizes future AI potential over current financial perfection.

## Directory Structure

```
investment_strategy/
├── claude.md                          # This file - master instructions
├── AI_AI_stock_strategy.md           # Overall investment thesis & framework
├── AI_scoring_sheet.md               # High-level scoring methodology (1-5 scale)
├── AI_watchlist_seeds.md             # Initial ticker seeds (if exists)
├── platform/                          # AI infrastructure & enablers
│   ├── compute_stack/                # Chips, foundries, cloud compute
│   └── critical_enablers.md          # Networking, memory, power, packaging
└── product/                           # AI product & distribution layers
    ├── endpoint_gatekeepers.md       # Device OS, automotive, industrial platforms
    ├── productivity_devops.md        # Office, dev tools, enterprise SaaS
    ├── commerce_ads.md               # E-commerce, advertising platforms
    ├── industrial_logistics.md       # Automation, warehouse, supply chain
    ├── healthcare_regulated.md       # Medical AI, diagnostics, compliance
    └── consumer_social_media.md      # Social, media, personalization
```

## Segment Directory Template

Developed segments (like `compute_stack/`) follow this structure:

```
platform/{segment_name}/
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
- Scoring dimensions with weights (total: 7.5)
  - AI Revenue Growth & Monetization: 2.0x
  - Competitive Positioning: 2.0x
  - Strategic Moats: 1.5x
  - Execution & Regulatory Risk: 1.0x
  - Capital Efficiency: 0.5x (quality filter, not primary driver)
  - Valuation as Thesis Discount: 0.5x (upside if AI thesis plays out, NOT traditional value)
- Sample indicators and scoring guides for each dimension
- Trigger flag definitions
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
3. Reference scoring_guide.md for dimension definitions and scoring guides
4. Score each dimension (1-5) with growth/AI thesis lens:
   - Prioritize: AI revenue growth, competitive position, moats
   - De-prioritize: Current profitability (unless burn threatens survival)
   - Reframe valuation: "How much upside remains?" not "Is this cheap?"
5. Multiply scores by weights, sum and normalize by 7.5
6. Document in stock_notes/{TICKER}.md with timestamp
7. Update watchlist table in scoring_guide.md with latest scores
8. Flag any triggers
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
**Portfolio Type:** High-growth AI sleeve (distinct from core ETF holdings)

- **Baseline anchor (35-40%):** Compute stack bellwethers (chips, foundry, tools)
- **Opportunity sleeve (60-65%):**
  - 30-35% vertical AI leaders with clear monetization
  - 15-20% endpoint gatekeepers/distribution plays
  - 10% dry powder for event-driven additions
- **Position sizing:**
  - Cap at 8-10% unless score ≥4.5 with no hard triggers
  - Pyramid into winners as KPIs beat thresholds (AI revenue >30% YoY, utilization >85%)
  - Accept concentration in top convictions (this is a growth sleeve, not index)
- **Rebalance cadence:**
  - Monthly trigger checks
  - Full rescore post-earnings
  - Harvest when position exceeds 1.5× target weight OR score momentum negative for 2 consecutive reviews

## Review Cadence
- **Full rescore:** Quarterly (post-earnings)
- **Trigger check:** Monthly
- **Major events:** Export controls, partnerships, M&A, regulatory changes
- **Harvest:** When position exceeds 1.5× target weight or score momentum negative for 2 reviews
