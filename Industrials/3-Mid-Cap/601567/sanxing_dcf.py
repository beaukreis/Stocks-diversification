"""Ningbo Sanxing Medical Electric (SHSE:601567, short name 三星电气) - FCFF DCF. CNY billions.
Valuation date 1 Oct 2026. Two segments are folded together: power distribution/metering (~79% of H1-26
revenue) and rehabilitation hospitals (~21%)."""
PRICE = 15.40                 # est. close 29 Sep 2026 (derived; last verified print: 16.25 limit-up on 24 Sep)
SHARES = 1.405                # billions
# Q1-26 balance sheet: cash 1.127 + trading financial assets 1.445 - ST loans 0.028 - LT loans 2.762
NET_DEBT = 2.762 + 0.028 - 1.127 - 1.445
NCI = 0.04                    # minority interests (hospital JVs etc.), haircut on equity value
TAX = 0.17                    # blended: 15% HNTE domestic + higher overseas

def dcf(rev, ebit_m, wacc, tg, capex_pct=0.045, da_pct=0.032, nwc=0.20, label="", show=True):
    prev, pv, rows = 14.3, 0.0, []                     # 2026E revenue (H1 7.26 + H2 ~7.0)
    for i, r in enumerate(rev):
        ebit = r * ebit_m[i]
        fcf = ebit * (1 - TAX) + r * da_pct - r * capex_pct - nwc * (r - prev)
        pv += fcf / (1 + wacc) ** (i + 0.75)
        rows.append((2027 + i, r, ebit, ebit_m[i], fcf))
        prev = r
    tv = rows[-1][4] * (1 + tg) / (wacc - tg)
    pv_tv = tv / (1 + wacc) ** (len(rev) - 0.25)
    ev = pv + pv_tv
    eq = (ev - NET_DEBT) * (1 - NCI)
    ps = eq / SHARES
    if show:
        print(f"\n== {label}: WACC {wacc:.1%}, terminal g {tg:.1%} ==")
        print(f"{'Yr':>5}{'Rev':>7}{'EBIT':>7}{'EBIT%':>7}{'FCFF':>7}")
        for y, r, e, m, f in rows:
            print(f"{y:>5}{r:>7.1f}{e:>7.2f}{m:>7.1%}{f:>7.2f}")
        print(f"PV FCF {pv:.1f} | PV TV {pv_tv:.1f} ({pv_tv/ev:.0%} of EV) | EV CN¥{ev:.1f}B | CN¥{ps:.2f}/sh | vs price {ps/PRICE-1:+.0%}")
    return ps

#            2027   2028   2029   2030   2031   2032   2033   2034   2035   2036
base = dcf(rev=[15.7, 17.3, 18.7, 19.8, 20.8, 21.8, 22.7, 23.6, 24.4, 25.1],
           ebit_m=[.115, .130, .135, .135, .135, .13, .13, .13, .13, .13],
           wacc=0.095, tg=0.025, label="Base: low-price domestic orders roll off, overseas mix lifts margins")
bear = dcf(rev=[14.6, 15.2, 15.8, 16.3, 16.8, 17.2, 17.6, 18.0, 18.4, 18.8],
           ebit_m=[.09, .10, .105, .105, .10, .10, .10, .10, .10, .10],
           wacc=0.105, tg=0.02, label="Bear: domestic tender pricing stays weak, more hospital impairments")
bull = dcf(rev=[16.5, 19.0, 21.3, 23.2, 24.8, 26.1, 27.4, 28.5, 29.6, 30.5],
           ebit_m=[.13, .15, .16, .165, .165, .16, .16, .16, .16, .16],
           wacc=0.09, tg=0.03, label="Bull: overseas distribution (EU grid, US data-centre transformers) compounds")
pw = 0.30 * bear + 0.45 * base + 0.25 * bull
print(f"\nProbability-weighted (30/45/25): CN¥{pw:.2f} ({pw/PRICE-1:+.0%})")

print("\nBase sensitivity (CN¥/share): rows = steady-state EBIT margin, cols = WACC")
for m in (0.11, 0.13, 0.15):
    line = f"EBIT {m:.0%}: "
    for w in (0.085, 0.095, 0.105):
        line += f"  {w:.1%}=CN¥{dcf([15.7,17.3,18.7,19.8,20.8,21.8,22.7,23.6,24.4,25.1], [.115,.130]+[m]*8, w, 0.025, show=False):.2f}"
    print(line)

ttm_ni, ni_26e, ni_27e = 0.590, 1.22, 1.56
mcap = PRICE * SHARES
print(f"\nMarket cap CN¥{mcap:.1f}B (US${mcap/7.1:.1f}B @7.1) | P/E TTM {mcap/ttm_ni:.1f}x | 2026E {mcap/ni_26e:.1f}x | 2027E {mcap/ni_27e:.1f}x "
      f"| net debt CN¥{NET_DEBT:.2f}B")
