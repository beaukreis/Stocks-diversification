"""Appen Ltd (ASX:APX) - FCFF DCF in US$ millions, per-share value converted to A$ (fx 1/0.722). Valuation 1 Oct 2026.
AI training-data services. FY26 guidance: revenue US$270-300M, underlying EBITDA margin ~5-10%. H1-26: revenue US$119.9M (+17%):
Appen China US$76.2M (+80%), Appen Global US$43.7M (-27%). Shares ~266M (est.). Net cash ~US$50M, no debt (est.)."""
import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[3] / "scripts"))
from dcf_lib import run
run(price=1.25, shares=266, net_cash=50, base_rev=285, tax=0.25, capex=0.03, da=0.03, nwc=0.10, fx=1/0.722, cur="A$",
    scenarios={
      "Bear": dict(rev=[270, 250, 240, 235, 235, 235, 235, 235, 235, 235], m=[.01, .01, .02, .02, .02, .02, .02, .02, .02, .02], wacc=.13, tg=.01, w=.35),
      "Base": dict(rev=[330, 370, 400, 425, 445, 460, 475, 485, 495, 505], m=[.05, .07, .08, .08, .08, .08, .08, .08, .08, .08], wacc=.12, tg=.02, w=.45),
      "Bull": dict(rev=[380, 450, 520, 580, 630, 670, 700, 725, 745, 760], m=[.08, .10, .11, .11, .11, .11, .11, .11, .11, .11], wacc=.115, tg=.025, w=.20),
    })
print("EV/Sales 2026E: {:.1f}x | mkt cap A${:.0f}M (US${:.0f}M)".format((1.25*266*0.722-50)/285, 1.25*266, 1.25*266*0.722))
