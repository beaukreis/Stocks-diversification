"""Nanya Technology (TWSE:2408) - FCFF DCF, NT$ billions. Valuation 1 Oct 2026.
Base 2026E revenue ~NT$352B (Q1 49.1 + Q2 82.5 + H2 ~220). Heavy capex: new 5A fab (NT$346.6B)."""
import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[3] / "scripts"))
from dcf_lib import run
run(price=490.0, shares=3.424, net_cash=150.0, base_rev=352.0, tax=0.20, capex=0.16, da=0.12, nwc=0.10, cur="NT$",
    scenarios={
      "Bear": dict(rev=[380, 220, 180, 230, 260, 250, 260, 270, 280, 290], m=[.50, .05, -.05, .12, .18, .15, .15, .15, .15, .15], wacc=.11, tg=.015, w=.30),
      "Base": dict(rev=[450, 360, 250, 300, 330, 300, 310, 330, 345, 355], m=[.60, .40, .15, .25, .28, .20, .22, .22, .22, .22], wacc=.10, tg=.02, w=.45),
      "Bull": dict(rev=[520, 480, 380, 400, 440, 430, 445, 460, 475, 490], m=[.65, .55, .35, .32, .32, .30, .30, .30, .30, .30], wacc=.095, tg=.025, w=.25),
    })
print("P/E: TTM EPS 25.44 -> {:.1f}x | Q2 annualised (14.66x4) -> {:.1f}x | mkt cap NT${:.0f}B (US${:.0f}B)".format(490/25.44, 490/58.6, 490*3.424, 490*3.424/31.7))
