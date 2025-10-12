# Platform Investment Execution Strategy

## Strategy: Broad Basket → Concentrate

### Rationale
1. **Diversification protects early**: Single-name risk is mitigated by broad initial deployment
2. **Monthly monitoring cadence**: Can't react daily, so broad exposure from Day 1 reduces timing risk
3. **Flexibility to concentrate later**: Can add to winners or double down on dips during monthly reviews
4. **Reduces FOMO**: If individual names rally while waiting to deploy, still caught some upside

---

## Month 1 Deployment (40% of Platform Allocation)

Deploy across Tier 1 and Tier 2 platform stocks only (compute_stack + critical_enablers):

| Tier | Score Range | Initial % | Target % (Final) | Rationale |
|------|-------------|-----------|------------------|-----------|
| **Tier 1** | ≥4.5 | 4% each | 8-10% each | Top conviction platform names |
| **Tier 2** | 4.0-4.5 | 2.5% each | 5-7% each | Strong platform names |
| **LEAPS** | Tier 1 only | 2% each | 3% each | Top 3 Tier 1 names |
| **Tier 3** | 3.5-4.0 | Skip | Skip | Will invest via product sleeve (META, AMZN, etc.) |

**Stock selection**: Reference `current_stock_scores.md` in each segment for latest tier assignments.

**Position count**: Expect ~11 total positions (3 Tier 1 + 8 Tier 2 + 3 LEAPS) - manageable for monthly monitoring.

---

## Months 2-6: Add to Positions

### Decision Framework
- **Winners (up >15%)**: Add if still <target weight and fundamentals strong
- **Losers (down >15%)**: Add aggressively if score remains high and no trigger flags
- **New info**: If score changes (earnings, hyperscaler partnership), adjust allocation

### Dry Powder Deployment Triggers
- Market correction >15%: Accelerate adds to Tier 1
- Earnings beats: Add to winners beating on AI revenue growth
- New product scores available: Rotate capital to 60% product sleeve

---

## LEAPS Strategy (5-10% of Portfolio)

### Allocation
5-10% of platform allocation in LEAPS, never exceeding 10% of total portfolio

### Selection Criteria
- **Candidates**: Tier 1 stocks only (score ≥4.5)
- **Top 3 rule**: Focus on the 3 highest-scoring Tier 1 names
- **Capital per position**: 2% of platform allocation initially, scaling to 3% at target

### How to Select Strike & Expiration

**Step 1: Check current stock price**
- Use MCP tool: `getStockPriceSnapshot` for current price
- Example: If TSM is trading at $180, note this as your reference

**Step 2: Choose expiration (12-18 months out)**
- Target: Next January or June expiration 12-18 months away
- Example: If today is Oct 2025, choose Jan 2027 or Jun 2027
- Avoid: <12 months (too much theta decay for monthly monitoring)

**Step 3: Select strike based on conviction**
- **ATM (At-the-Money)**: Strike = current price (e.g., $180 strike for $180 stock)
  - Use when: Highest conviction, want max upside exposure
  - Delta: ~0.70-0.75
- **5-10% OTM (Out-of-the-Money)**: Strike = current price + 5-10% (e.g., $190-200 strike for $180 stock)
  - Use when: Strong conviction but want lower premium cost
  - Delta: ~0.65-0.70
- **Target delta range**: 0.65-0.75 (balance leverage and decay)

**Step 4: Verify pricing & delta**
- Check option chain for premium cost
- Confirm delta is in target range (0.65-0.75)
- Calculate position size: Divide capital allocation by premium cost
- Example: $1,000 allocation ÷ $15/contract premium = ~6-7 contracts

**Decision Framework**
| Scenario | Strike Selection | Rationale |
|----------|------------------|-----------|
| Stock near 52-week low | ATM or slightly ITM | Maximize leverage on recovery |
| Stock at all-time high | 5-10% OTM | Reduce cost basis, still capture upside |
| Moderate volatility (IV <40%) | ATM | Premium is reasonable |
| High volatility (IV >60%) | 5-10% OTM | Avoid overpaying for inflated premium |

### Management
- **Review**: Monthly (same cadence as portfolio)
- **Roll or exit**: At 60 days to expiration (avoid accelerating theta decay)
- **Stop loss**: -50% on individual position (thesis broken or poor timing)
- **Take profit**: Consider rolling up and out if position is +100% and stock thesis intact

---

## Rebalancing Rules

### Trim/Exit Triggers
- Trim winners exceeding 12% of total portfolio or 1.5× target weight
- Exit if score drops below 4.0 (below Tier 2 threshold) or trigger flags activate

### Monthly Review Checklist
- [ ] Regenerate `current_stock_scores.md` files using `python3 scripts/extract_latest_scores.py platform/compute_stack && python3 scripts/extract_latest_scores.py platform/critical_enablers`
- [ ] Update scores based on latest earnings calls in stock notes
- [ ] Check hyperscaler capex commentary (MSFT, META, GOOG, AMZN earnings)
- [ ] Review trigger flags (customer concentration, inventory builds)
- [ ] Rebalance if any position >12% or <2% (due to drift)
- [ ] Assess dry powder deployment triggers
- [ ] If Tier 3 stocks (3.5-4.0) look compelling, note for product sleeve consideration
