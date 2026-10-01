"""Resolute Mining (ASX:RSG) - FCFF DCF in US$ millions, per-share value converted to A$ (fx 1/0.722). Valuation 1 Oct 2026.
Syama (Mali, 80%), Mako (Senegal, 90%), Doropo (Cote d'Ivoire, under construction, first gold ~2028). Revised 2026 guidance (21 Sep):
205-225 koz at AISC US$2,250-2,350/oz. Revenue = attributable-adjusted oz x gold (base US$4,300 flat, ~spot).
EBIT margins are after minorities and Mali state take. Net cash+bullion US$317M (30 Jun) less ~US$300M remaining Doropo capex -> ~0.
Shares ~2,130M. Finite reserve life: terminal growth 0."""
import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[3] / "scripts"))
from dcf_lib import run
run(price=1.242, shares=2130, net_cash=0, base_rev=1000, tax=0.30, capex=0.10, da=0.10, nwc=0.05, fx=1/0.722, cur="A$",
    scenarios={
      "Bear": dict(rev=[800, 900, 1100, 1150, 1100, 1050, 1000, 950, 900, 850], m=[.22, .22, .22, .22, .22, .22, .22, .22, .22, .22], wacc=.14, tg=0.0, w=.30),
      "Base": dict(rev=[1050, 1290, 1630, 1720, 1630, 1590, 1550, 1500, 1460, 1420], m=[.38, .40, .40, .40, .40, .40, .40, .40, .40, .40], wacc=.12, tg=0.0, w=.45),
      "Bull": dict(rev=[1250, 1550, 1950, 2050, 1950, 1900, 1850, 1800, 1750, 1700], m=[.46, .48, .48, .48, .48, .48, .48, .48, .48, .48], wacc=.11, tg=0.0, w=.25),
    })
print("P/E: H1-26 NPAT US$162.6M annualised -> {:.1f}x | mkt cap A${:.2f}B (US${:.2f}B)".format(1.242*2130*0.722/325.2, 1.242*2.130, 1.242*2.130*0.722))
