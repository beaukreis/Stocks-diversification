"""WAF mine-by-mine DCF (NAV). USD cash flows per mine, attributable to WAF, converted to AUD.
Valuation date 1 Oct 2026. Production profile shaped to the company's 10-year target
(>5.3 Moz 2026-2035, peak ~596 koz in 2030), with a Kiaka tail to 2042 drawn from the 7.0 Moz reserve."""
PRICE_AUD = 3.66          # close 23 Sep 2026 (ex the 20c special dividend)
SHARES = 1.1440           # billions (20c special = A$228.8M)
AUDUSD = 0.722            # implied by H1-26 realised US$4,744 = A$6,570
# Balance sheet, A$B, 30 Jun 2026: cash 0.8763, debt 0.3881, less the 20c special paid 7 Oct 2026
NET_CASH = 0.8763 - 0.3881 - 0.2288
BULLION_OZ = 42_453
KIAKA_SALE = 0.175        # A$B from SOPAMIB for 25% of Kiaka; to be passed on as a special dividend

YEARS   = [2026.75] + list(range(2027, 2043))     # first period = Q4 2026 (quarter weight)
KIAKA   = [65, 280, 290, 300, 310, 300, 290, 280, 280, 270, 250, 240, 230, 220, 200, 180, 150]   # koz, 100% basis
SANBR   = [50, 230, 240, 270, 286, 250, 240, 230, 200, 180, 100, 0, 0, 0, 0, 0, 0]               # incl. Toega + M5 UG
GROWTH  = [0.05, 0.20, 0.18, 0.12, 0.06] + [0.0] * 12  # US$B non-sustaining capex, 100% basis (H1-26 capex ran ~A$300M+)

def nav(gold, rate, prod=1.0, cost_base=1500, royalty=0.07, kiaka_own=0.60, sanb_own=0.90,
        sanb_own_later=None, tax=0.30, leakage=0.07):
    pv = 0.0
    for i, y in enumerate(YEARS):
        t = 0.0 if i == 0 else y - 2026.75                                  # years from valuation date
        aisc = cost_base + royalty * gold                                   # royalties scale with price
        margin = (gold - aisc) * (1 - tax) / 1e6                            # US$B per koz after tax
        s_own = sanb_own if (sanb_own_later is None or y < 2028) else sanb_own_later
        k_cf = KIAKA[i] * prod * margin * kiaka_own
        s_cf = SANBR[i] * prod * margin * s_own
        capex = GROWTH[i] * (0.5 * kiaka_own + 0.5 * s_own)
        cf = (k_cf + s_cf - capex) * (1 - leakage)                           # dividend WHT, levies, repatriation
        pv += cf / (1 + rate) ** (t + 0.5 if i else 0.125)
    mines_aud = pv / AUDUSD
    bullion_aud = BULLION_OZ * gold / 1e9 / AUDUSD
    equity = mines_aud + NET_CASH + bullion_aud + KIAKA_SALE
    return mines_aud, equity, equity / SHARES

scen = {
    "Bear": dict(gold=3300, rate=0.15, prod=0.90, cost_base=1650, sanb_own_later=0.60),
    "Base": dict(gold=4300, rate=0.12),
    "Bull": dict(gold=5200, rate=0.09, prod=1.05, cost_base=1450),
}
vals = {}
for k, p in scen.items():
    m, e, ps = nav(**p)
    vals[k] = ps
    print(f"{k}: gold US${p['gold']:,} | disc {p['rate']:.0%} | mines A${m:.2f}B | equity A${e:.2f}B | A${ps:.2f}/sh | vs price {ps/PRICE_AUD-1:+.0%}")
pw = 0.25 * vals["Bear"] + 0.5 * vals["Base"] + 0.25 * vals["Bull"]
print(f"Probability-weighted A${pw:.2f} ({pw/PRICE_AUD-1:+.0%})")

print("\nBase sensitivity, A$/share (rows gold US$/oz, cols discount rate)")
print("        " + "".join(f"{r:>8.0%}" for r in (0.08, 0.10, 0.12, 0.15)))
for g in (3300, 3800, 4300, 4800, 5300):
    print(f"{g:>8,}" + "".join(f"{nav(g, r)[2]:>8.2f}" for r in (0.08, 0.10, 0.12, 0.15)))

mcap = PRICE_AUD * SHARES
print(f"\nMarket cap A${mcap:.2f}B (US${mcap*AUDUSD:.2f}B) | EV ≈ A${mcap - NET_CASH - BULLION_OZ*4300/1e9/AUDUSD:.2f}B")
print(f"Price / base NAV: {PRICE_AUD/vals['Base']:.2f}x")

# Sovereign tail: state takes control of both mines, WAF receives 20% of base mine value as compensation.
mines_base, _, _ = nav(**scen["Base"])
exprop = (0.20 * mines_base + NET_CASH + BULLION_OZ * 4300 / 1e9 / AUDUSD + KIAKA_SALE) / SHARES
risk_w = 0.25 * vals["Bear"] + 0.45 * vals["Base"] + 0.15 * vals["Bull"] + 0.15 * exprop
print(f"\nExpropriation case A${exprop:.2f}/sh | Risk-weighted (25 bear/45 base/15 bull/15 exprop) A${risk_w:.2f} ({risk_w/PRICE_AUD-1:+.0%})")
k = KIAKA[1] * 0.60 + SANBR[1] * 0.90                                   # 2027 attributable koz
fcf_usd = (k * (4300 - 1500 - 0.07 * 4300) * 0.70 / 1e3 - 0.20 * 0.75 * 1e3) * 0.93   # US$M
print(f"Check: 2027 attributable {k:.0f} koz -> FCF at US$4,300 ≈ US${fcf_usd:.0f}M ≈ A${fcf_usd/AUDUSD:.0f}M "
      f"(FCF yield on market cap {fcf_usd/AUDUSD/1e3/(PRICE_AUD*SHARES):.0%})")
