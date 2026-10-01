"""Delton Technology (Guangzhou) / 广合科技 (SZSE:001389, HKEX:1989) - FCFF DCF. CNY billions.
Valuation date 1 Oct 2026. Valued per A-share; H-shares trade at a large discount (noted separately)."""
PRICE_A = 177.59              # A-share close 28 Sep 2026
PRICE_H_HKD, CNY_PER_HKD = 108.9, 0.912   # H-share 18 Sep 2026
SHARES = 0.480                # billions: 473M (427M A + 46M H) + ~4% for planned CNY3.6B convertible (est.)
NET_CASH = 2.0                # est.: H-share IPO net HK$3.19B (Mar 2026) less capex funding; not retrieved
TAX = 0.15                    # high-tech enterprise rate

def dcf(rev, ebit_m, capex, da_pct, wacc, tg, nwc=0.15, show=True, label=""):
    prev, pv, rows = 9.2, 0.0, []                        # 2026E revenue (H1 4.39 + H2 ~4.8)
    for i, r in enumerate(rev):
        ebit = r * ebit_m[i]
        fcf = ebit * (1 - TAX) + r * da_pct[i] - capex[i] - nwc * (r - prev)
        pv += fcf / (1 + wacc) ** (i + 0.75)
        rows.append((2027 + i, r, ebit, ebit_m[i], fcf))
        prev = r
    tv = rows[-1][4] * (1 + tg) / (wacc - tg)
    pv_tv = tv / (1 + wacc) ** (len(rev) - 0.25)
    ev = pv + pv_tv
    ps = (ev + NET_CASH) / SHARES
    if show:
        print(f"\n== {label}: WACC {wacc:.1%}, g {tg:.0%} ==")
        print(f"{'Yr':>5}{'Rev':>7}{'EBIT':>7}{'EBIT%':>7}{'FCFF':>7}")
        for y, r, e, m, f in rows:
            print(f"{y:>5}{r:>7.1f}{e:>7.2f}{m:>7.1%}{f:>7.2f}")
        print(f"PV FCF {pv:.1f} | PV TV {pv_tv:.1f} ({pv_tv/ev:.0%} of EV) | EV CN¥{ev:.1f}B | CN¥{ps:.0f}/sh | vs A {ps/PRICE_A-1:+.0%}")
    return ps

#           2027  2028  2029  2030  2031  2032  2033  2034  2035  2036
base = dcf(rev=[14.3, 19.3, 23.1, 25.9, 28.0, 29.7, 31.2, 32.4, 33.4, 34.4],
           ebit_m=[.25, .25, .24, .23, .22, .21, .20, .20, .20, .20],
           capex=[5.0, 4.0, 2.8, 2.4, 2.3, 2.3, 2.4, 2.5, 2.6, 2.7],
           da_pct=[.05, .06, .065, .065, .065, .065, .065, .065, .065, .065],
           wacc=0.095, tg=0.03, label="Base: AI-server PCB boom through 2028, then normalising margins")
bear = dcf(rev=[12.5, 14.5, 15.5, 16.3, 17.0, 17.6, 18.1, 18.6, 19.1, 19.6],
           ebit_m=[.22, .19, .16, .15, .15, .15, .15, .15, .15, .15],
           capex=[5.0, 3.0, 1.6, 1.4, 1.4, 1.4, 1.5, 1.5, 1.6, 1.6],
           da_pct=[.05, .06, .065, .065, .065, .065, .065, .065, .065, .065],
           wacc=0.105, tg=0.025, label="Bear: AI capex digestion 2027-28 + price war among PCB makers")
bull = dcf(rev=[15.5, 23.0, 29.5, 34.5, 38.0, 41.0, 43.5, 45.5, 47.0, 48.5],
           ebit_m=[.27, .28, .27, .26, .25, .24, .24, .24, .24, .24],
           capex=[5.5, 5.0, 3.8, 3.2, 3.1, 3.2, 3.3, 3.4, 3.5, 3.6],
           da_pct=[.05, .06, .065, .065, .065, .065, .065, .065, .065, .065],
           wacc=0.09, tg=0.035, label="Bull: share gains at Nvidia/hyperscaler platforms, consensus-like path")
pw = 0.30 * bear + 0.45 * base + 0.25 * bull
print(f"\nProbability-weighted (30/45/25): CN¥{pw:.0f} ({pw/PRICE_A-1:+.0%} vs A-share; "
      f"{pw/(PRICE_H_HKD*CNY_PER_HKD)-1:+.0%} vs H-share)")

ttm_ni, ni26, ni27, ni28 = 1.480, 2.15, 3.5, 5.3
mcap = PRICE_A * 0.473
h_cny = PRICE_H_HKD * CNY_PER_HKD
print(f"\nA-share mkt cap (A price x all shares) CN¥{mcap:.1f}B (US${mcap/7.1:.1f}B) | P/E TTM {mcap/ttm_ni:.0f}x | "
      f"2026E {mcap/ni26:.0f}x | 2027E {mcap/ni27:.0f}x | 2028E {mcap/ni28:.0f}x")
print(f"H-share CN¥{h_cny:.1f} -> A-share premium {PRICE_A/h_cny-1:.0%}; H-share P/E 2027E {h_cny*0.473/ni27:.0f}x")
