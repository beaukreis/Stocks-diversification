"""Austral Resources Australia (ASX:AR1) - FCFF DCF, A$ millions; shares in millions so values are A$/share. Valuation 1 Oct 2026.
Copper cathode from Anthill ore via the Mt Kelly SX-EW plant (NW Queensland); Lady Loretta acquired (A$45.5M) and Rocklands plant restart
planned. Jun-26 quarter: 1,796t produced, 1,800t sold for A$33.1M (~A$18.4k/t). Base 2026E revenue ~A$150M.
Shares ~2,500M (Simply Wall St: mkt cap A$162.2M at A$0.065). Cash A$72.3M at 30 Jun, no debt.
Finite mine life: terminal growth 0."""
import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[3] / "scripts"))
from dcf_lib import run
run(price=0.065, shares=2500, net_cash=72, base_rev=150, tax=0.30, capex=0.12, da=0.10, nwc=0.05, cur="A$",
    scenarios={
      "Bear": dict(rev=[140, 120, 100, 100, 90, 80, 70, 60, 50, 40], m=[.12, .08, .05, .05, .05, .05, .05, .05, .05, .05], wacc=.14, tg=0.0, w=.35),
      "Base": dict(rev=[170, 220, 260, 260, 250, 240, 230, 220, 210, 200], m=[.22, .25, .25, .24, .22, .20, .20, .20, .20, .20], wacc=.13, tg=0.0, w=.45),
      "Bull": dict(rev=[200, 300, 400, 450, 450, 440, 430, 420, 410, 400], m=[.28, .32, .32, .30, .30, .30, .30, .30, .30, .30], wacc=.12, tg=0.0, w=.20),
    })
print("EV/Sales 2026E: {:.1f}x | mkt cap A${:.0f}M (US${:.0f}M)".format((0.065*2500-72)/150, 0.065*2500, 0.065*2500*0.722))
