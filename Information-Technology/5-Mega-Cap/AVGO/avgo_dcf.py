"""Broadcom (NASDAQ:AVGO) - FCFF DCF, US$ billions, fiscal years ending ~Nov. Valuation 1 Oct 2026.
Base FY26E revenue ~$107B (Q3 29.6, Q4 guide 34.8). EBIT margins are GAAP-like (after intangibles amortisation + SBC)."""
import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[3] / "scripts"))
from dcf_lib import run
run(price=351.19, shares=4.77, net_cash=-55.0, base_rev=107.0, tax=0.15, capex=0.01, da=0.06, nwc=0.05, cur="$",
    scenarios={
      "Bear": dict(rev=[135, 140, 135, 142, 149, 156, 163, 170, 177, 184], m=[.48, .46, .42, .42, .42, .42, .42, .42, .42, .42], wacc=.10, tg=.025, w=.25),
      "Base": dict(rev=[160, 200, 215, 230, 245, 258, 270, 281, 291, 300], m=[.55, .55, .53, .52, .51, .50, .50, .50, .50, .50], wacc=.095, tg=.03, w=.50),
      "Bull": dict(rev=[170, 240, 285, 320, 350, 375, 395, 412, 427, 440], m=[.58, .58, .56, .55, .54, .53, .52, .52, .52, .52], wacc=.09, tg=.035, w=.25),
    })
print("P/E (non-GAAP): TTM EPS ~$10.0 -> {:.0f}x | FY27E EPS ~$17.5 -> {:.0f}x".format(351.19/10.0, 351.19/17.5))
