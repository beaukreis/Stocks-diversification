"""Ashtead Technology Holdings (LSE:AT.) - FCFF DCF in GBP millions; fx=100 converts GBP/share to pence. Valuation 1 Oct 2026.
Subsea equipment rental + services. FY26 after the Aug-2026 warning: revenue ~GBP203.5M, adj. EBITA ~GBP50.3M (~25%).
Rental fleet capex ~14% of revenue, depreciation ~12%. Net debt ~GBP110M (est.). Shares ~80.4M.
Ember Infrastructure non-binding proposal: 615p cash (PUSU deadline 21 Oct 2026)."""
import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[3] / "scripts"))
from dcf_lib import run
run(price=580, shares=80.4, net_cash=-110, base_rev=203.5, tax=0.25, capex=0.14, da=0.12, nwc=0.15, fx=100, cur="p ",
    scenarios={
      "Bear": dict(rev=[195, 190, 200, 210, 218, 225, 232, 238, 244, 250], m=[.20, .18, .18, .19, .19, .19, .19, .19, .19, .19], wacc=.11, tg=.015, w=.30),
      "Base": dict(rev=[215, 235, 255, 270, 285, 297, 308, 318, 327, 335], m=[.24, .245, .25, .25, .25, .25, .25, .25, .25, .25], wacc=.10, tg=.025, w=.45),
      "Bull": dict(rev=[235, 270, 300, 325, 345, 362, 377, 390, 402, 412], m=[.26, .27, .28, .28, .28, .28, .28, .28, .28, .28], wacc=.095, tg=.03, w=.25),
    })
print("Ember 615p proposal = equity GBP{:.0f}M | at 580p P/E on FY26E adj EPS ~41p: {:.0f}x".format(6.15*80.4, 580/41))
