"""Shenzhen Kstar Science & Technology 科士达 (SZSE:002518) - FCFF DCF, CNY billions. Valuation 1 Oct 2026.
Base 2026E revenue ~CN¥5.8B (H1 2.59 + H2 ~3.2 est). UPS/data-centre power and cooling + PV inverters, storage, EV charging.
Shares 0.582B. Net cash ~CN¥1.5B (est.)."""
import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[3] / "scripts"))
from dcf_lib import run
run(price=35.84, shares=0.582, net_cash=1.5, base_rev=5.8, tax=0.15, capex=0.04, da=0.03, nwc=0.20, cur="CN¥",
    scenarios={
      "Bear": dict(rev=[6.2, 6.5, 6.8, 7.1, 7.4, 7.7, 8.0, 8.3, 8.6, 8.9], m=[.11, .10, .10, .10, .10, .10, .10, .10, .10, .10], wacc=.10, tg=.02, w=.30),
      "Base": dict(rev=[6.9, 8.0, 9.0, 9.9, 10.7, 11.4, 12.0, 12.6, 13.2, 13.7], m=[.13, .135, .14, .14, .14, .14, .14, .14, .14, .14], wacc=.095, tg=.025, w=.45),
      "Bull": dict(rev=[7.5, 9.2, 11.0, 12.6, 14.0, 15.2, 16.3, 17.3, 18.2, 19.0], m=[.14, .15, .16, .16, .16, .16, .16, .16, .16, .16], wacc=.09, tg=.03, w=.25),
    })
ttm = 0.63 - 0.255 + 0.290
print("P/E: TTM NI ~CN¥{:.2f}B -> {:.0f}x | 2026E (Soochow) 24.7x | mkt cap CN¥{:.1f}B (US${:.1f}B)".format(ttm, 20.87/ttm, 20.87, 20.87/7.12))
