"""Compeq Manufacturing (TWSE:2313) - FCFF DCF, NT$ billions. Valuation 1 Oct 2026.
Base 2026E revenue ~NT$83B (H1 39.5 + Q3 ~21.5 + Q4 ~22 est). HDI/LEO-satellite/AI-server PCBs. 2026 capex raised to NT$9-15B.
Shares 1.193B (NI 1.479 / EPS 1.24). Net debt ~NT$5B (est.)."""
import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[3] / "scripts"))
from dcf_lib import run
run(price=223.0, shares=1.193, net_cash=-5.0, base_rev=83.0, tax=0.20, capex=0.09, da=0.06, nwc=0.15, cur="NT$",
    scenarios={
      "Bear": dict(rev=[90, 95, 92, 98, 104, 110, 115, 120, 125, 130], m=[.10, .10, .09, .10, .10, .10, .10, .10, .10, .10], wacc=.10, tg=.02, w=.30),
      "Base": dict(rev=[105, 122, 132, 142, 152, 161, 170, 179, 187, 195], m=[.14, .15, .15, .15, .15, .15, .15, .15, .15, .15], wacc=.095, tg=.025, w=.45),
      "Bull": dict(rev=[115, 140, 160, 178, 195, 210, 224, 237, 249, 260], m=[.17, .18, .19, .19, .19, .19, .19, .19, .19, .19], wacc=.09, tg=.03, w=.25),
    })
print("P/E: H1-26 EPS 2.50 annualised -> {:.0f}x | 2026E consensus 8.04 -> {:.0f}x | 2027E consensus 12.3 -> {:.0f}x | mkt cap NT${:.0f}B (US${:.1f}B)".format(223/5.0, 223/8.04, 223/12.3, 223*1.193, 223*1.193/31.7))
