"""Shandong Head / 山东赫达 (SZSE:002810) - FCFF DCF. CNY billions. Valuation date 1 Oct 2026."""
PRICE = 21.54                 # early/mid-Sep 2026 (TTM P/E 31x on 21 Sep is consistent)
SHARES = 0.347                # billions
NET_DEBT = 1.0                # est. incl. convertible bond (赫达转债); not retrieved
TAX = 0.15

def dcf(rev, m, wacc, tg, capex=0.08, da=0.06, nwc=0.15, base=2.45):
    pv, prev = 0.0, base
    for i, r in enumerate(rev):
        fcf = r * m[i] * (1 - TAX) + r * (da - capex) - nwc * (r - prev)
        pv += fcf / (1 + wacc) ** (i + 0.75)
        prev = r
    last = rev[-1] * m[-1] * (1 - TAX) + rev[-1] * (da * 1.0 - da * 1.15)   # maintenance capex ~1.15x D&A long-run
    tv = last * (1 + tg) / (wacc - tg) / (1 + wacc) ** (len(rev) - 0.25)
    return (pv + tv - NET_DEBT) / SHARES, pv + tv

S = {  # 2027..2036
 "Bear": ([2.55, 2.62, 2.70, 2.78, 2.85, 2.92, 2.99, 3.06, 3.13, 3.20], [.15, .13, .12, .12, .12, .12, .12, .12, .12, .12], .10, .015),
 "Base": ([2.75, 3.03, 3.27, 3.50, 3.71, 3.90, 4.06, 4.22, 4.35, 4.48], [.21, .21, .20, .19, .18, .18, .18, .18, .18, .18], .09, .025),
 "Bull": ([2.90, 3.30, 3.70, 4.05, 4.35, 4.62, 4.85, 5.05, 5.22, 5.38], [.23, .24, .24, .23, .22, .22, .22, .22, .22, .22], .085, .03),
}
v = {}
for k, (rev, m, w, g) in S.items():
    ps, ev = dcf(rev, m, w, g); v[k] = ps
    print(f"{k}: 2027-29 rev {rev[:3]} EBIT {m[:3]} | WACC {w:.1%} g {g:.1%} | EV CN¥{ev:.1f}B -> CN¥{ps:.2f}/sh ({ps/PRICE-1:+.0%})")
pw = .30 * v["Bear"] + .45 * v["Base"] + .25 * v["Bull"]
print(f"Probability-weighted (30/45/25): CN¥{pw:.2f} ({pw/PRICE-1:+.0%})")
mcap = PRICE * SHARES
print(f"Mkt cap CN¥{mcap:.2f}B (US${mcap/7.1:.2f}B) | P/E TTM {mcap/0.242:.0f}x | 2026E (~CN¥0.42B) {mcap/0.42:.0f}x | 2027E (~CN¥0.52B) {mcap/0.52:.0f}x")
