"""MDGL DCF: 10-year explicit unlevered FCF (2026E Q4 onward approximated by full years 2027-2036),
then a terminal value with negative growth to reflect post-patent erosion. $ in billions."""
PRICE = 503.96                 # close 30 Sep 2026
SHARES_ECON = 29.145           # Q2-26 weighted shares: common + pre-funded warrants + converted preferred + earned PSUs
EQUITY_AWARDS = 1.0            # ASSUMED net dilution from options/RSUs (treasury method); not disclosed in sources
CASH, DEBT = 0.8389, 0.350     # 30 Jun 2026: cash + marketable securities; Blue Owl term loan

def dcf(rev, gm, sga, rnd, tax, wacc, tg, nwc=0.15, label=""):
    pv, prev, rows = 0.0, 1.50, []                      # 2026E revenue base $1.50B
    for i, r in enumerate(rev):
        ebit = r * gm - sga[i] - rnd[i]
        t = tax[i] if ebit > 0 else 0.0
        fcf = ebit * (1 - t) - nwc * (r - prev)        # D&A ≈ capex for an asset-light commercial biotech
        df = (1 + wacc) ** (i + 0.75)
        pv += fcf / df
        rows.append((2027 + i, r, ebit, ebit / r, fcf))
        prev = r
    tv = rows[-1][4] * (1 + tg) / (wacc - tg)
    pv_tv = tv / (1 + wacc) ** (len(rev) - 0.25)
    ev = pv + pv_tv
    eq = ev + CASH - DEBT
    ps = eq / (SHARES_ECON + EQUITY_AWARDS) * 1000
    print(f"\n== {label}: WACC {wacc:.1%}, terminal g {tg:+.0%} ==")
    print(f"{'Yr':>5}{'Rev':>7}{'EBIT':>7}{'EBIT%':>7}{'UFCF':>7}")
    for y, r, e, m, f in rows:
        print(f"{y:>5}{r:>7.2f}{e:>7.2f}{m:>7.0%}{f:>7.2f}")
    print(f"PV FCF {pv:.2f} | PV TV {pv_tv:.2f} ({pv_tv/ev:.0%} of EV) | EV {ev:.2f}B | Equity {eq:.2f}B | ${ps:,.0f}/sh | vs price {ps/PRICE-1:+.0%}")
    return ps

TAX = [0, 0, 0.10] + [0.21] * 7
# 2027 ... 2036
base = dcf(rev=[2.10, 2.70, 3.20, 3.60, 3.90, 4.10, 4.25, 4.00, 3.40, 2.90], gm=0.885,
           sga=[1.25, 1.32, 1.38, 1.42, 1.45, 1.48, 1.50, 1.40, 1.20, 1.00],
           rnd=[0.40, 0.45, 0.48, 0.50, 0.52, 0.53, 0.54, 0.52, 0.48, 0.45],
           tax=TAX, wacc=0.095, tg=-0.05, label="Base")
bear = dcf(rev=[1.90, 2.25, 2.50, 2.65, 2.75, 2.80, 2.60, 1.80, 1.20, 0.90], gm=0.875,
           sga=[1.25, 1.30, 1.33, 1.35, 1.35, 1.35, 1.25, 0.95, 0.70, 0.55],
           rnd=[0.40, 0.43, 0.45, 0.45, 0.45, 0.45, 0.42, 0.38, 0.33, 0.30],
           tax=TAX, wacc=0.105, tg=-0.10, label="Bear")
bull = dcf(rev=[2.30, 3.10, 3.90, 4.60, 5.20, 5.60, 5.90, 6.10, 6.20, 6.25], gm=0.89,
           sga=[1.25, 1.35, 1.45, 1.52, 1.58, 1.62, 1.65, 1.68, 1.70, 1.72],
           rnd=[0.40, 0.47, 0.52, 0.56, 0.60, 0.62, 0.64, 0.65, 0.66, 0.67],
           tax=TAX, wacc=0.09, tg=0.0, label="Bull")
pw = 0.25 * bear + 0.5 * base + 0.25 * bull
print(f"\nProbability-weighted (25/50/25): ${pw:,.0f} vs price ${PRICE} ({pw/PRICE-1:+.0%})")

econ_mcap = SHARES_ECON * PRICE / 1000
ev_now = (SHARES_ECON + EQUITY_AWARDS) * PRICE / 1000 - CASH + DEBT
print(f"Economic market cap ${econ_mcap:.2f}B | EV ≈ ${ev_now:.2f}B | EV/TTM sales {ev_now/1.2836:.1f}x | "
      f"EV/2026E {ev_now/1.50:.1f}x | EV/2027E {ev_now/2.10:.1f}x | EV/2028E EBIT {ev_now/0.633:.0f}x")

# Grid: peak-sales level x exclusivity outcome. Opex scales partly with revenue (SG&A 60% fixed).
import io, contextlib
def scenario(peak, durable):
    ramp = [2.10, 2.70, 3.20, 3.60, 3.90, 4.10, 4.25]            # base path, peak $4.25B in 2033
    k = peak / 4.25
    rev = [max(1.50, r * k) if i else r * (0.6 + 0.4 * k) for i, r in enumerate(ramp)]
    tail = [rev[-1] * f for f in ((1.0, 1.0, 1.0) if durable else (0.94, 0.80, 0.68))]
    rev += tail
    sga = [1.25 * (0.6 + 0.4 * r / 2.10) if i == 0 else min(1.25 + 0.06 * i, 1.0 + 0.12 * r) for i, r in enumerate(rev)]
    rnd = [min(0.40 + 0.03 * i, 0.12 * r + 0.15) for i, r in enumerate(rev)]
    with contextlib.redirect_stdout(io.StringIO()):
        return dcf(rev=rev, gm=0.885, sga=sga, rnd=rnd, tax=TAX, wacc=0.095, tg=0.0 if durable else -0.05)
print("\nValue/share grid at 9.5% WACC (rows: peak US+EU sales; cols: exclusivity)")
print(f"{'Peak':>8}{'LOE ~2033':>12}{'Durable 2040+':>15}")
for peak in (3.0, 4.25, 5.5, 6.5):
    print(f"{'$'+str(peak)+'B':>8}{scenario(peak, False):>12,.0f}{scenario(peak, True):>15,.0f}")
