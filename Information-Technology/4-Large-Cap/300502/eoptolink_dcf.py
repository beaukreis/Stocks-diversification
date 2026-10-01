"""Eoptolink / 新易盛 (SZSE:300502) - FCFF DCF. CNY billions. Valuation date 1 Oct 2026."""
PRICE = 455.8                 # late-Sep 2026 (derived: mkt cap CN¥635.4B / 1.394B shares)
SHARES = 1.394                # billions (after 2025 10-for-4 bonus issue)
NET_CASH = 15.0               # est. (not retrieved); inventory/prepayments to suppliers are large
TAX = 0.15

def dcf(rev, m, wacc, tg, capex=0.04, da=0.025, nwc=0.22, base=46.0):
    pv, prev = 0.0, base
    for i, r in enumerate(rev):
        fcf = r * m[i] * (1 - TAX) + r * (da - capex) - nwc * (r - prev)
        pv += fcf / (1 + wacc) ** (i + 0.75)
        prev = r
    last = rev[-1] * m[-1] * (1 - TAX) + rev[-1] * (da - capex)
    tv = last * (1 + tg) / (wacc - tg) / (1 + wacc) ** (len(rev) - 0.25)
    return (pv + tv + NET_CASH) / SHARES, pv + tv

S = {  # 2027..2036
 "Bear": ([58, 60, 52, 55, 58, 60, 62, 64, 66, 68], [.36, .28, .20, .18, .18, .18, .18, .18, .18, .18], .115, .02),
 "Base": ([72, 92, 100, 110, 119, 127, 134, 140, 145, 150], [.40, .36, .30, .27, .25, .24, .23, .23, .23, .23], .105, .03),
 "Bull": ([85, 120, 145, 165, 182, 196, 208, 218, 226, 233], [.42, .40, .36, .32, .30, .28, .27, .27, .27, .27], .10, .035),
}
v = {}
for k, (rev, m, w, g) in S.items():
    ps, ev = dcf(rev, m, w, g); v[k] = ps
    print(f"{k}: 2027-29 rev {rev[:3]} EBIT {m[:3]} | WACC {w:.1%} g {g:.1%} | EV CN¥{ev:.0f}B -> CN¥{ps:.0f}/sh ({ps/PRICE-1:+.0%})")
pw = .30 * v["Bear"] + .45 * v["Base"] + .25 * v["Bull"]
print(f"Probability-weighted (30/45/25): CN¥{pw:.0f} ({pw/PRICE-1:+.0%})")
mcap = PRICE * SHARES
print(f"Mkt cap CN¥{mcap:.0f}B (US${mcap/7.1:.0f}B) | P/E TTM {mcap/13.12:.0f}x | 2026E (~CN¥19.5B) {mcap/19.5:.0f}x | 2027E (~CN¥33B) {mcap/33:.0f}x")
