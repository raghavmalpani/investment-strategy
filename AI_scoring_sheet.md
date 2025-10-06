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
- `scoring/compute_stack.md`
- `scoring/critical_enablers.md`
- `scoring/endpoint_gatekeepers.md`
- `scoring/productivity_devops.md`
- `scoring/commerce_ads.md`
- `scoring/industrial_logistics.md`
- `scoring/healthcare_regulated.md`
- `scoring/consumer_social_media.md`

## Implementation Notes
- Adjust weights by ±0.5 to reflect unique company attributes, but keep total weight near 6.0 per segment for comparability.
- Maintain a watchlist where trigger flags are logged with dates and follow-up actions; unresolved flags cap position size at <50% of target weight.
- Recalculate scores quarterly post-earnings and mid-cycle when major AI product launches or regulatory events occur.
