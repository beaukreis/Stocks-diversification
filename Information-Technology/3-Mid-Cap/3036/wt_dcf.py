"""WT Microelectronics (TWSE:3036) - FCFF DCF, NT$ billions. Valuation 1 Oct 2026.
Base 2026E revenue ~NT$2,300B (H1 1,085 + Q3 guide 592 + Q4 ~620 est). A distributor: tiny capex, heavy working capital.
Net debt incl. acquisition loans and preferred shares ~NT$200B (est.); weighted shares ~1.265B (NI 9.713 / EPS 7.68)."""
import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[3] / "scripts"))
from dcf_lib import run
run(price=204.0, shares=1.265, net_cash=-200.0, base_rev=2300.0, tax=0.20, capex=0.002, da=0.002, nwc=0.10, cur="NT$",
    scenarios={
      "Bear": dict(rev=[2300, 1950, 2000, 2100, 2200, 2280, 2350, 2420, 2490, 2560], m=[.020, .016, .017, .018, .018, .018, .018, .018, .018, .018], wacc=.105, tg=.01, w=.30),
      "Base": dict(rev=[2650, 2850, 2800, 2950, 3100, 3250, 3400, 3550, 3700, 3850], m=[.023, .022, .021, .021, .021, .021, .021, .021, .021, .021], wacc=.095, tg=.015, w=.45),
      "Bull": dict(rev=[2900, 3300, 3500, 3750, 4000, 4250, 4450, 4650, 4850, 5000], m=[.024, .024, .024, .024, .024, .024, .024, .024, .024, .024], wacc=.09, tg=.02, w=.25),
    })
ttm = 3.40 + 3.52 + 5.33 + 7.68  # Q3-25, Q4-25 (FY25 11.61 less 9M), Q1-26, Q2-26
fwd = 5.33 + 7.68 + 8.03 + 8.0  # 2026E: Q1, Q2, Q3 guide midpoint, Q4 est.
print("P/E: TTM EPS ~{:.1f} -> {:.1f}x | 2026E EPS ~{:.1f} -> {:.1f}x | mkt cap NT${:.0f}B (US${:.1f}B)".format(ttm, 204/ttm, fwd, 204/fwd, 204*1.265, 204*1.265/31.7))
