"""Zhongji Innolight / 中际旭创 (SZSE:300308, HKEX:3308) - FCFF DCF. CNY billions. Valuation date 1 Oct 2026."""
PRICE = 808.44                # A-share close 30 Sep 2026
SHARES = 1.178                # billions: ~1.1155B A (incl. 5.65M treasury) + ~62.7M H (incl. greenshoe)
NET_CASH = 60.0               # est.: H-share IPO (Jul 2026, ~HK$53-61B gross) + prior net cash - CNY5B buyback
TAX = 0.15

def dcf(rev, m, wacc, tg, capex=0.05, da=0.03, nwc=0.20, base=95.0):
    pv, prev = 0.0, base
    for i, r in enumerate(rev):
        fcf = r * m[i] * (1 - TAX) + r * (da - capex) - nwc * (r - prev)
        pv += fcf / (1 + wacc) ** (i + 0.75)
        prev = r
    last = rev[-1] * m[-1] * (1 - TAX) + rev[-1] * (da - capex)
    tv = last * (1 + tg) / (wacc - tg) / (1 + wacc) ** (len(rev) - 0.25)
    return (pv + tv + NET_CASH) / SHARES, pv + tv

S = {  # 2027..2036
 "Bear": ([120, 125, 110, 115, 120, 124, 128, 131, 134, 137], [.33, .27, .20, .18, .18, .18, .18, .18, .18, .18], .11, .02),
 "Base": ([150, 190, 210, 230, 248, 263, 276, 287, 297, 306], [.38, .35, .30, .27, .25, .24, .23, .23, .23, .23], .10, .03),
 "Bull": ([170, 230, 270, 300, 325, 345, 362, 377, 390, 402], [.40, .38, .33, .30, .28, .27, .26, .26, .26, .26], .095, .035),
}
v = {}
for k, (rev, m, w, g) in S.items():
    ps, ev = dcf(rev, m, w, g); v[k] = ps
    print(f"{k}: 2027-29 rev {rev[:3]} EBIT {m[:3]} | WACC {w:.1%} g {g:.1%} | EV CN¥{ev:.0f}B -> CN¥{ps:.0f}/sh ({ps/PRICE-1:+.0%})")
pw = .30 * v["Bear"] + .45 * v["Base"] + .25 * v["Bull"]
print(f"Probability-weighted (30/45/25): CN¥{pw:.0f} ({pw/PRICE-1:+.0%})")
mcap = PRICE * SHARES
print(f"Mkt cap CN¥{mcap:.0f}B (US${mcap/7.1:.0f}B) | P/E TTM {mcap/20.45:.0f}x | 2026E (~CN¥30B) {mcap/30:.0f}x | 2027E (~CN¥55B) {mcap/55:.0f}x")
