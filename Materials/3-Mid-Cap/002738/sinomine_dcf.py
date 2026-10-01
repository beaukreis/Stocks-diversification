"""Sinomine Resource Group 中矿资源 (SZSE:002738) - FCFF DCF, CNY billions. Valuation 1 Oct 2026.
Base 2026E revenue ~CN¥10B (lithium salts ~6.99 万t LCE capacity, caesium/rubidium, Tsumeb, Kitumba copper from 2027).
Lithium carbonate ~CN¥172k/t in Q2-26. Shares 0.7215B. Net debt ~CN¥2B (est.)."""
import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[3] / "scripts"))
from dcf_lib import run
run(price=47.89, shares=0.7215, net_cash=-2.0, base_rev=10.0, tax=0.20, capex=0.12, da=0.10, nwc=0.10, cur="CN¥",
    scenarios={
      "Bear": dict(rev=[8.0, 7.5, 8.0, 8.5, 9.0, 9.3, 9.6, 9.9, 10.2, 10.5], m=[.15, .12, .13, .14, .14, .14, .14, .14, .14, .14], wacc=.11, tg=.015, w=.30),
      "Base": dict(rev=[11.5, 12.5, 12.5, 13.0, 13.5, 14.0, 14.3, 14.6, 14.9, 15.2], m=[.30, .27, .24, .22, .22, .22, .22, .22, .22, .22], wacc=.10, tg=.02, w=.45),
      "Bull": dict(rev=[13.5, 15.5, 16.5, 17.0, 17.5, 18.0, 18.4, 18.8, 19.2, 19.6], m=[.36, .34, .31, .28, .28, .28, .28, .28, .28, .28], wacc=.095, tg=.025, w=.25),
    })
ttm = 0.458 - 0.089 + 1.15  # FY25 - H1-25 + H1-26 (preliminary midpoint)
print("P/E: TTM NI ~CN¥{:.2f}B -> {:.0f}x | mkt cap CN¥{:.1f}B (US${:.1f}B)".format(ttm, 47.89*0.7215/ttm, 47.89*0.7215, 47.89*0.7215/7.12))
