"""TOYO Co., Ltd (NASDAQ:TOYO) - FCFF DCF, US$ millions. Valuation 1 Oct 2026.
Solar cells (Ethiopia 4GW, Vietnam 2GW) + US module plant (1GW, Houston) + planned 1.5GW Texas HJT cell plant.
H1-26: revenue US$261.0M (+88%), net income US$45.8M, EPS US$1.21; Q2 revenue US$118.2M (missed consensus).
Management expects an H2 hit from US policy changes. Base 2026E revenue ~US$460M. Shares ~41.3M after the June offering.
Net cash ~US$50M (est.) less ~US$200M of committed Texas cell-plant capex not yet spent -> -US$150M (the bear case assumes the Texas plant is cancelled, haircut=1.0); long-run capex 8% vs D&A 7%."""
import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[3] / "scripts"))
from dcf_lib import run
run(price=14.96, shares=41.3, net_cash=-150, base_rev=460, tax=0.15, capex=0.08, da=0.07, nwc=0.15, cur="$",
    scenarios={
      "Bear": dict(rev=[350, 300, 300, 310, 320, 330, 340, 350, 360, 370], m=[.06, .04, .04, .04, .04, .04, .04, .04, .04, .04], wacc=.14, tg=.0, w=.35, haircut=1.0),
      "Base": dict(rev=[520, 600, 650, 680, 700, 715, 730, 740, 750, 760], m=[.16, .15, .14, .13, .12, .12, .12, .12, .12, .12], wacc=.13, tg=.01, w=.45),
      "Bull": dict(rev=[600, 750, 850, 900, 940, 970, 1000, 1020, 1040, 1060], m=[.19, .18, .17, .16, .15, .15, .15, .15, .15, .15], wacc=.12, tg=.02, w=.20),
    })
print("P/E: H1-26 EPS US$1.21 annualised -> {:.1f}x | mkt cap US${:.0f}M".format(14.96/2.42, 14.96*41.3))
