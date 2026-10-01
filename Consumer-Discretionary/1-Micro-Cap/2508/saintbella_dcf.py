"""Saint Bella Inc. 圣贝拉 (HKEX:2508) - FCFF DCF in CN¥ billions, per-share value converted to HK$ (fx 1.095). Valuation 1 Oct 2026.
Base 2026E revenue ~CN¥1.36B (H1 0.611 + H2 ~0.75 est). Premium postpartum-care centres (Saint Bella, Babybella, Xiaobella).
Customers prepay, so growth releases working capital (nwc < 0). Shares 609.7M. Net cash ~CN¥0.6B (est.)."""
import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[3] / "scripts"))
from dcf_lib import run
run(price=3.175, shares=0.6097, net_cash=0.6, base_rev=1.36, tax=0.25, capex=0.05, da=0.04, nwc=-0.05, fx=1.095, cur="HK$",
    scenarios={
      "Bear": dict(rev=[1.45, 1.50, 1.55, 1.60, 1.65, 1.70, 1.75, 1.80, 1.85, 1.90], m=[.08, .08, .08, .08, .08, .08, .08, .08, .08, .08], wacc=.12, tg=.015, w=.30),
      "Base": dict(rev=[1.62, 1.90, 2.15, 2.35, 2.50, 2.62, 2.72, 2.80, 2.87, 2.93], m=[.11, .12, .12, .13, .13, .13, .13, .13, .13, .13], wacc=.11, tg=.025, w=.45),
      "Bull": dict(rev=[1.80, 2.25, 2.70, 3.10, 3.45, 3.75, 4.00, 4.20, 4.35, 4.50], m=[.12, .14, .15, .16, .16, .16, .16, .16, .16, .16], wacc=.105, tg=.03, w=.25),
    })
print("P/E on 2026E adj. NI ~CN¥0.14B (est.): {:.0f}x | mkt cap HK${:.2f}B (US${:.0f}M)".format(3.175*0.6097/1.095/0.14, 3.175*0.6097, 3.175*609.7/7.8))
