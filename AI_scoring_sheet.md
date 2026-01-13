# AI Equity Scoring Sheet

## How to Use
- Score each company 1–5 on every dimension; 1 = weak, 5 = outstanding relative to peers.
- Multiply each score by the recommended weight to get a weighted subtotal.
- Sum subtotals for the segment total, then divide by the sum of weights to normalize out of 5.
- Flag any "Trigger" items that require a manual review or position cap regardless of score.

| Scale | Description |
|------:|-------------|
| 1 | Underperforms peers; no clear AI leverage or deteriorating trend |
| 2 | Emerging capability, but evidence inconsistent or unproven |
| 3 | Competitive with sector average; proof points forming |
| 4 | Differentiated execution with durable advantages |
| 5 | Best-in-class, clear line-of-sight to compounding returns |

## Segment Scorecards

### Platform (Infrastructure & Enablers)
- `platform/compute_stack/scoring_guide.md` - Chips, foundries, cloud compute
  - NVDA, AMD, INTC, QCOM, TSM, ASML, MU, MSFT, AMZN, GOOG, META, ORCL
- `platform/critical_enablers/scoring_guide.md` - Networking, memory, power, packaging
  - AVGO, ANET, MU, SK Hynix, Samsung, PSTG, SMCI, DELL, VRT, ETN, EQIX, DLR, ASX, AMKR

### Product (AI Distribution & Applications)

**Platform independence is a key cross-cutting vector** - companies that control their own distribution (OS, hardware, dominant apps) score higher on strategic moats than those dependent on iOS/Android/web.

- `product/hardware_and_os_gatekeepers/scoring_guide.md` - Hardware + OS control (devices, operating systems)
  - AAPL, GOOGL, MSFT, META, SSNLF
- `product/productivity_devops.md` - Office, dev tools, enterprise SaaS
  - MSFT, TEAM, NOW
- `product/commerce_ads.md` - E-commerce, advertising platforms
  - AMZN, SHOP, MELI, GOOGL, META
- `product/consumer_social_media.md` - Social, media, personalization
  - META, SNAP, RDDT, NFLX, SPOT, RBLX, PINS
- `product/automotive_autonomy.md` - Autonomous driving, software-defined vehicles
  - TSLA, GM, F, RIVN, MBLY
- `product/industrial_logistics.md` - Automation, warehouse, supply chain
  - SIEGY, Schneider, John Deere, ABB
- `product/healthcare_regulated.md` - Medical AI, diagnostics, compliance
  - Intuitive Surgical, Teladoc, diagnostics providers

## Implementation Notes
- **Weight adjustment:** Total weights are 7.5 for growth-focused framework (not 6.0). Adjust by ±0.5 to reflect unique company attributes while maintaining comparability.
- **Trigger flags:** Unresolved hard triggers cap position size at 50% of target weight; soft triggers require monitoring but no automatic cap.
- **Rebalance cadence:** Quarterly post-earnings rescore; monthly trigger flag checks; event-driven rescores for major AI launches or regulatory changes.
