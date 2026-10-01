"""Powerchip Semiconductor Manufacturing (TWSE:6770) - FCFF DCF, NT$ billions. Valuation 1 Oct 2026.
Base 2026E revenue ~NT$74B (Q1 13.6 + Q2 17.3 + Q3 ~20.5 + Q4 ~23 est). Mature-node logic + DRAM foundry, 3D WoW AI foundry.
Shares ~4.6B after the 420M-share GDR. Net debt ~0 after the US$1.8B Tongluo fab sale to Micron and the GDR (est.)."""
import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[3] / "scripts"))
from dcf_lib import run
run(price=73.5, shares=4.6, net_cash=0.0, base_rev=74.0, tax=0.15, capex=0.18, da=0.16, nwc=0.10, cur="NT$",
    scenarios={
      "Bear": dict(rev=[82, 72, 62, 68, 74, 77, 80, 82, 84, 86], m=[.15, .04, -.06, .05, .08, .10, .10, .10, .10, .10], wacc=.11, tg=.015, w=.30),
      "Base": dict(rev=[92, 95, 78, 85, 92, 96, 100, 104, 107, 110], m=[.26, .26, .08, .13, .16, .15, .15, .15, .15, .15], wacc=.10, tg=.02, w=.45),
      "Bull": dict(rev=[105, 125, 130, 145, 160, 175, 188, 200, 210, 220], m=[.32, .33, .25, .26, .27, .27, .27, .27, .27, .27], wacc=.095, tg=.03, w=.25),
    })
print("P/E: 2026E EPS 6.26 (Fubon, incl. Q1 fab-sale gain) -> {:.0f}x | 2027E 6.39 -> {:.1f}x | Q2 annualised 0.76x4 -> {:.0f}x | mkt cap NT${:.0f}B (US${:.1f}B)".format(73.5/6.26, 73.5/6.39, 73.5/3.04, 73.5*4.6, 73.5*4.6/31.7))
