"""Samsung Electronics (KRX:005930) - FCFF DCF, KRW trillions. Valuation 1 Oct 2026.
Base 2026E revenue ~KRW680T (Q1 133 + Q2 171.5 + H2 ~375). Shares ~6.74B (common + preferred, treated alike)."""
import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[3] / "scripts"))
from dcf_lib import run
run(price=276000, shares=6.74e-3, net_cash=167.0, base_rev=680.0, tax=0.22, capex=0.12, da=0.10, nwc=0.10, cur="₩",
    scenarios={
      "Bear": dict(rev=[650, 560, 540, 600, 640, 660, 680, 700, 720, 740], m=[.35, .12, .06, .12, .14, .12, .12, .12, .12, .12], wacc=.10, tg=.02, w=.30),
      "Base": dict(rev=[750, 680, 640, 690, 730, 760, 790, 815, 840, 860], m=[.48, .30, .18, .20, .22, .20, .18, .18, .18, .18], wacc=.09, tg=.025, w=.45),
      "Bull": dict(rev=[820, 800, 760, 800, 850, 890, 925, 955, 985, 1010], m=[.52, .42, .30, .27, .26, .25, .25, .25, .25, .25], wacc=.085, tg=.03, w=.25),
    })
print("P/E: TTM (NI ~KRW145T) {:.1f}x | 2026E (NI ~KRW240T) {:.1f}x | 2027E (~KRW360T) {:.1f}x | net cash KRW167T".format(276000*6.74e-3/145, 276000*6.74e-3/240, 276000*6.74e-3/360))
