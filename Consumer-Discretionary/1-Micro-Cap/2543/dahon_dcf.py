"""DAHON TECH (Shenzhen) / 大行科工 (HKEX:2543) - FCFF DCF + net cash. CNY millions; per-share in HK$.
Valuation date 1 Oct 2026."""
PRICE_HKD = 27.12             # latest print found (Sep 2026; ex the CNY1.224 interim dividend on 17 Sep)
CNY_PER_HKD = 0.912
SHARES = 32.78                # millions (mkt cap HK$889M / HK$27.12)
NET_CASH = 400.0              # CNY m, est.: IPO net ~HK$350M + pre-IPO cash, less dividends; not retrieved
TAX = 0.20

def dcf(rev, m, wacc, tg, capex=0.02, da=0.015, nwc=0.15, base=925.0, cash_haircut=0.0):
    pv, prev = 0.0, base
    for i, r in enumerate(rev):
        fcf = r * m[i] * (1 - TAX) + r * (da - capex) - nwc * (r - prev)
        pv += fcf / (1 + wacc) ** (i + 0.75)
        prev = r
    last = rev[-1] * m[-1] * (1 - TAX) + rev[-1] * (da - capex)
    tv = last * (1 + tg) / (wacc - tg) / (1 + wacc) ** (len(rev) - 0.25)
    eq = pv + tv + NET_CASH * (1 - cash_haircut)
    return eq / SHARES / CNY_PER_HKD, pv + tv

S = {  # 2027..2036 revenue (CNY m) and EBIT margins
 "Bust": ([800, 700, 650, 650, 650, 650, 650, 650, 650, 650], [.08] * 10, .14, .0, 0.3),   # cycling fad fades + governance haircut
 "Bear": ([930, 930, 940, 950, 960, 970, 980, 990, 1000, 1010], [.11] * 10, .13, .01, 0.2),
 "Base": ([1110, 1275, 1405, 1515, 1605, 1685, 1755, 1810, 1865, 1920], [.16, .16, .155, .15, .15, .15, .15, .15, .15, .15], .12, .025, 0.0),
 "Bull": ([1200, 1465, 1700, 1900, 2070, 2210, 2330, 2430, 2510, 2585], [.17, .18, .18, .18, .18, .18, .18, .18, .18, .18], .10, .03, 0.0),
}
v = {}
for k, (rev, m, w, g, hc) in S.items():
    ps, ev = dcf(rev, m, w, g, cash_haircut=hc); v[k] = ps
    print(f"{k}: rev 2027/2029/2031 {rev[0]}/{rev[2]}/{rev[4]} | EBIT {m[0]:.0%}->{m[-1]:.0%} | WACC {w:.1%} g {g:.1%} "
          f"| ops EV CN¥{ev:.0f}M -> HK${ps:.2f}/sh ({ps/PRICE_HKD-1:+.0%})")
pw = .20 * v["Bust"] + .25 * v["Bear"] + .35 * v["Base"] + .20 * v["Bull"]
print(f"Risk-weighted (20 bust / 25 bear / 35 base / 20 bull): HK${pw:.2f} ({pw/PRICE_HKD-1:+.0%})")
mcap_cny = PRICE_HKD * SHARES * CNY_PER_HKD
print(f"Mkt cap HK${PRICE_HKD*SHARES:.0f}M = CN¥{mcap_cny:.0f}M (US${mcap_cny/7.1:.0f}M) | net cash CN¥{NET_CASH:.0f}M "
      f"(HK${NET_CASH/SHARES/CNY_PER_HKD:.2f}/sh) | EV CN¥{mcap_cny-NET_CASH:.0f}M | P/E TTM {mcap_cny/91.6:.1f}x "
      f"| 2026E (~CN¥125M) {mcap_cny/125:.1f}x | EV/2026E NI {(mcap_cny-NET_CASH)/125:.1f}x | div yield {2.342/(PRICE_HKD*CNY_PER_HKD):.1%}")
