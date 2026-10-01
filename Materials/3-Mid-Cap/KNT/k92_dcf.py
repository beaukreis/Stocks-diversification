"""K92 Mining (TSX:KNT) - FCFF DCF in US$ millions, per-share value converted to C$ (fx 1.37). Valuation 1 Oct 2026.
Kainantu gold-copper mine (PNG). Stage 3 plant commissioned 2026; Stage 4 lifts run-rate toward 400 koz AuEq by late 2027/2028.
2026 guidance 190-225 koz AuEq; Q2-26 46,093 oz, AISC US$1,376/oz, revenue US$205M, cash US$349M. Gold US$4,300 flat (base).
EBIT margins include a ~10% haircut for PNG state participation/royalties. Shares ~241M. Long-life resource: terminal growth 1%."""
import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[3] / "scripts"))
from dcf_lib import run
run(price=20.60, shares=241, net_cash=349, base_rev=890, tax=0.30, capex=0.10, da=0.08, nwc=0.05, fx=1.37, cur="C$",
    scenarios={
      "Bear": dict(rev=[850, 1000, 1150, 1200, 1200, 1200, 1200, 1200, 1200, 1200], m=[.38, .40, .40, .40, .40, .40, .40, .40, .40, .40], wacc=.12, tg=.0, w=.30),
      "Base": dict(rev=[1290, 1630, 1720, 1720, 1720, 1720, 1720, 1720, 1720, 1720], m=[.55, .58, .58, .58, .58, .58, .58, .58, .58, .58], wacc=.10, tg=.01, w=.45),
      "Bull": dict(rev=[1500, 1900, 2050, 2100, 2100, 2100, 2100, 2100, 2100, 2100], m=[.60, .62, .62, .62, .62, .62, .62, .62, .62, .62], wacc=.095, tg=.015, w=.25),
    })
print("mkt cap C${:.2f}B (US${:.2f}B) | 2027E base NOPAT US${:.0f}M -> P/E ~{:.1f}x".format(20.60*0.241, 20.60*0.241/1.37, 1290*.55*.7, 20.60*241/1.37/(1290*.55*.7)))
