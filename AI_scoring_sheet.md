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
- `platform/critical_enablers.md` - Networking, memory, power, packaging

### Product (AI Distribution & Applications)
- `product/endpoint_gatekeepers.md` - Device OS, automotive, industrial platforms
- `product/productivity_devops.md` - Office, dev tools, enterprise SaaS
- `product/commerce_ads.md` - E-commerce, advertising platforms
- `product/industrial_logistics.md` - Automation, warehouse, supply chain
- `product/healthcare_regulated.md` - Medical AI, diagnostics, compliance
- `product/consumer_social_media.md` - Social, media, personalization

## Implementation Notes
- **Weight adjustment:** Total weights are 7.5 for growth-focused framework (not 6.0). Adjust by ±0.5 to reflect unique company attributes while maintaining comparability.
- **Trigger flags:** Unresolved hard triggers cap position size at 50% of target weight; soft triggers require monitoring but no automatic cap.
- **Rebalance cadence:** Quarterly post-earnings rescore; monthly trigger flag checks; event-driven rescores for major AI launches or regulatory changes.
