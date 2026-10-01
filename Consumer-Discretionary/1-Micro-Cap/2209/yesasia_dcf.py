"""YesAsia Holdings (HKEX:2209) - FCFF DCF in US$ millions, per-share value converted to HK$ (fx 7.8). Valuation 1 Oct 2026.
Base 2026E revenue ~US$620M (H1 301.5 + H2 ~320 est). YesStyle (B2C, K-beauty e-commerce) + AsianBeautyWholesale (B2B).
Shares ~531M (mkt cap HK$1.94B / HK$3.65; the count rose ~35% vs 2025, consistent with a bonus issue - est.). Net cash ~US$20M (est.)."""
import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[3] / "scripts"))
from dcf_lib import run
run(price=3.65, shares=531, net_cash=20, base_rev=620, tax=0.24, capex=0.01, da=0.01, nwc=0.10, fx=7.8, cur="HK$",
    scenarios={
      "Bear": dict(rev=[640, 620, 630, 645, 660, 675, 690, 705, 720, 735], m=[.055, .045, .045, .045, .045, .045, .045, .045, .045, .045], wacc=.13, tg=.015, w=.30),
      "Base": dict(rev=[720, 820, 910, 990, 1060, 1120, 1170, 1210, 1250, 1280], m=[.075, .075, .07, .07, .065, .065, .065, .065, .065, .065], wacc=.12, tg=.025, w=.45),
      "Bull": dict(rev=[800, 1000, 1180, 1340, 1470, 1580, 1670, 1740, 1800, 1850], m=[.085, .085, .085, .08, .08, .08, .08, .08, .08, .08], wacc=.11, tg=.03, w=.25),
    })
ttm = 23.14 - 14.08 + 18.30
print("P/E: TTM NI US${:.1f}M -> {:.1f}x | mkt cap HK${:.2f}B (US${:.0f}M)".format(ttm, 3.65*531/7.8/ttm, 3.65*0.531, 3.65*531/7.8))
