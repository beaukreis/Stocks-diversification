"""Jirfine Intelligent Equipment 乔锋智能 (SZSE:301603) - FCFF DCF, CNY billions. Valuation 1 Oct 2026.
Base 2026E revenue ~CN¥3.6B (H1 1.73 + H2 ~1.86 est). CNC machine tools (vertical/gantry/horizontal machining centres),
incl. special machines for liquid-cooling parts. Shares 0.1208B (mkt cap 14.58B / 120.71). Net cash ~CN¥1.0B (est.)."""
import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[3] / "scripts"))
from dcf_lib import run
run(price=120.71, shares=0.1208, net_cash=1.0, base_rev=3.6, tax=0.15, capex=0.05, da=0.03, nwc=0.25, cur="CN¥",
    scenarios={
      "Bear": dict(rev=[3.8, 3.7, 3.9, 4.1, 4.3, 4.5, 4.7, 4.9, 5.1, 5.3], m=[.13, .11, .11, .11, .11, .11, .11, .11, .11, .11], wacc=.105, tg=.015, w=.30),
      "Base": dict(rev=[4.4, 5.2, 5.9, 6.5, 7.0, 7.5, 7.9, 8.3, 8.6, 8.9], m=[.17, .165, .16, .155, .15, .15, .15, .15, .15, .15], wacc=.095, tg=.025, w=.45),
      "Bull": dict(rev=[4.8, 6.0, 7.2, 8.2, 9.0, 9.7, 10.3, 10.9, 11.4, 11.9], m=[.18, .18, .175, .17, .17, .17, .17, .17, .17, .17], wacc=.09, tg=.03, w=.25),
    })
ttm = 0.351 - 0.179 + 0.273
print("P/E: TTM NI CN¥{:.3f}B -> {:.0f}x | mkt cap CN¥14.58B (US${:.2f}B)".format(ttm, 14.58/ttm, 14.58/7.12))
