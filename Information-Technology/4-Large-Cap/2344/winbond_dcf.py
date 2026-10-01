"""Winbond (TWSE:2344) through-the-cycle DCF. NT$ billions. Valuation date 1 Oct 2026.
Memory is cyclical: each scenario runs a full up-cycle and downturn rather than extrapolating peak margins."""
PRICE = 180.5                 # close 1 Oct 2026
SHARES = 4.503                # billions (Q2-26 NI 24.317B / EPS 5.40)
CASH, DEBT = 29.08, 54.24     # latest reported quarter (aggregator; may be Q1-26 data)
NCI = 0.03                    # haircut for Nuvoton minority interests
TAX = 0.20                    # Taiwan corporate income tax

Q4_26 = dict(rev=88.0, om=0.52)   # Q4-2026E, after Q3 guide of >50% operating margin

def dcf(rev, om, capex, da, wacc, tg, nwc=0.15, label="", show=True):
    prev = 268.0                                  # 2026E revenue: 38.3 + 59.8 + ~82 + ~88
    pv = 0.0
    # Q4-2026 stub (quarter weight, capex ~ NT$12B in the quarter)
    stub = Q4_26["rev"] * Q4_26["om"] * (1 - TAX) + 6.5 - 12.0
    pv += stub / (1 + wacc) ** 0.125
    rows = []
    for i, r in enumerate(rev):
        ebit = r * om[i]
        fcf = ebit * (1 - TAX) + da[i] - capex[i] - nwc * (r - prev)
        pv += fcf / (1 + wacc) ** (i + 0.75)
        rows.append((2027 + i, r, ebit, om[i], fcf))
        prev = r
    mid = rows[-1][4]
    tv = mid * (1 + tg) / (wacc - tg)
    pv_tv = tv / (1 + wacc) ** (len(rev) - 0.25)
    ev = pv + pv_tv
    eq = (ev + CASH - DEBT) * (1 - NCI)
    ps = eq / SHARES
    if show:
        print(f"\n== {label}: WACC {wacc:.0%}, terminal g {tg:.0%} ==")
        print(f"{'Yr':>5}{'Rev':>7}{'EBIT':>7}{'OM':>6}{'FCF':>7}")
        for y, r, e, m, f in rows:
            print(f"{y:>5}{r:>7.0f}{e:>7.0f}{m:>6.0%}{f:>7.0f}")
        print(f"PV FCF {pv:.0f} | PV TV {pv_tv:.0f} ({pv_tv/ev:.0%} of EV) | EV NT${ev:.0f}B | NT${ps:.0f}/sh | vs price {ps/PRICE-1:+.0%}")
    return ps

#            2027 2028 2029 2030 2031 2032 2033 2034 2035 2036
BASE_CAPEX = [60,  70,  60,  45,  40,  40,  42,  44,  46,  48]   # incl. Kaohsiung Module B (build 2027, tools 2028-29)
BASE_DA    = [26,  29,  33,  37,  39,  40,  41,  42,  43,  44]
base = dcf(rev=[420, 360, 260, 290, 340, 320, 310, 330, 350, 360],   # 2027: Kaohsiung bits ~2x, tighter supply
           om =[.52, .38, .15, .18, .28, .22, .18, .22, .24, .22],
           capex=BASE_CAPEX, da=BASE_DA, wacc=0.10, tg=0.02, label="Base: boom peaks 2027, downturn 2029")
bear = dcf(rev=[300, 210, 170, 200, 240, 220, 210, 230, 240, 250],
           om =[.38, .10, -.05, .08, .18, .12, .08, .14, .16, .15],
           capex=[55, 55, 40, 35, 35, 35, 36, 37, 38, 39], da=BASE_DA, wacc=0.11, tg=0.01,
           label="Bear: cycle turns mid-2027 (2022-23 style)")
bull = dcf(rev=[430, 450, 380, 360, 400, 420, 400, 420, 450, 470],
           om =[.55, .48, .32, .28, .33, .32, .28, .30, .31, .30],
           capex=[65, 75, 65, 50, 45, 45, 47, 49, 51, 53], da=BASE_DA, wacc=0.095, tg=0.02,
           label="Bull: AI/custom memory keeps supply tight through 2028, structurally higher margins")
pw = 0.30 * bear + 0.45 * base + 0.25 * bull
print(f"\nProbability-weighted (30 bear / 45 base / 25 bull): NT${pw:.0f} ({pw/PRICE-1:+.0%})")

eps_26 = 2.25 + 5.40 + 7.7 + 8.5
print(f"\nMarket cap NT${PRICE*SHARES:.0f}B (US${PRICE*SHARES/31.7:.1f}B @31.7) | 2026E EPS ~NT${eps_26:.1f} -> P/E {PRICE/eps_26:.1f}x | "
      f"TTM EPS 9.07 -> P/E {PRICE/9.07:.1f}x | Q3-annualised EPS ~30.8 -> {PRICE/30.8:.1f}x")
print("Mid-cycle check: revenue NT$320B x 22% OM x 0.8 tax / 4.5B sh = EPS", round(320*0.22*0.8/4.503, 1),
      "-> at 12x mid-cycle P/E =", round(12*320*0.22*0.8/4.503))
print("\nBase sensitivity (NT$/share): rows = 2027-28 peak margin shift, cols = WACC")
for shift in (-0.10, 0.0, +0.10):
    line = f"peak OM {shift:+.0%}: "
    for w in (0.09, 0.10, 0.11):
        om = [.52 + shift, .38 + shift, .15, .18, .28, .22, .18, .22, .24, .22]
        line += f"  {w:.0%}=NT${dcf(rev=[420, 360, 260, 290, 340, 320, 310, 330, 350, 360], om=om, capex=BASE_CAPEX, da=BASE_DA, wacc=w, tg=0.02, show=False):.0f}"
    print(line)
