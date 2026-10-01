"""NVIDIA (NASDAQ:NVDA) - FCFF DCF, US$ billions, fiscal years (FY28 = Feb-2027..Jan-2028). Valuation 1 Oct 2026.
Base year FY27E revenue ~$404B (Q1 81.5 + Q2 96.2 + Q3 guide 108 + Q4 ~118)."""
import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[3] / "scripts"))
from dcf_lib import run
run(price=228.38, shares=24.15, net_cash=80.0, base_rev=404.0, tax=0.15, capex=0.03, da=0.02, nwc=0.10, cur="$",
    scenarios={
      "Bear": dict(rev=[520, 480, 420, 440, 462, 485, 509, 534, 561, 589], m=[.60, .52, .42, .40, .40, .40, .40, .40, .40, .40], wacc=.11, tg=.025, w=.25),
      "Base": dict(rev=[650, 750, 760, 820, 880, 930, 975, 1015, 1050, 1080], m=[.65, .62, .55, .52, .50, .48, .46, .45, .45, .45], wacc=.10, tg=.03, w=.50),
      "Bull": dict(rev=[690, 900, 1050, 1180, 1290, 1380, 1450, 1500, 1545, 1590], m=[.66, .64, .60, .57, .55, .55, .55, .55, .55, .55], wacc=.095, tg=.035, w=.25),
    })
print("P/E: TTM (~$190B NI) {:.0f}x | FY27E (EPS ~$9.3) {:.0f}x | FY28E (EPS ~$15.7) {:.0f}x".format(228.38*24.15/190, 228.38/9.3, 228.38/15.7))
