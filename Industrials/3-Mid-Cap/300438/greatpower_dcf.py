"""Guangzhou Great Power Energy 鹏辉能源 (SZSE:300438) - FCFF DCF, CNY billions. Valuation 1 Oct 2026.
Base 2026E revenue ~CN¥24B (H1 10.98 + H2 ~13 est). Lithium cells for energy storage (#1 in residential storage cells).
Capacity to ~100GWh by early 2027. Shares 0.503B (mkt cap 31.37B / 62.33). Net debt ~CN¥5B (est.)."""
import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[3] / "scripts"))
from dcf_lib import run
run(price=62.33, shares=0.503, net_cash=-5.0, base_rev=24.0, tax=0.15, capex=0.06, da=0.05, nwc=0.10, cur="CN¥",
    scenarios={
      "Bear": dict(rev=[26, 24, 23, 25, 27, 28, 29, 30, 31, 32], m=[.06, .03, .02, .035, .04, .04, .04, .04, .04, .04], wacc=.105, tg=.015, w=.30),
      "Base": dict(rev=[32, 36, 38, 40, 42, 44, 46, 47, 48, 49], m=[.09, .08, .07, .07, .065, .065, .065, .065, .065, .065], wacc=.095, tg=.02, w=.45),
      "Bull": dict(rev=[36, 44, 50, 55, 59, 62, 65, 67, 69, 70], m=[.10, .095, .09, .085, .08, .08, .08, .08, .08, .08], wacc=.09, tg=.025, w=.25),
    })
ttm = 0.206 - 0.0725 + 0.816
print("P/E: TTM NI ~CN¥{:.2f}B -> {:.0f}x | 2026E NI ~CN¥1.8B (est.) -> {:.0f}x | mkt cap CN¥31.4B (US${:.1f}B)".format(ttm, 31.37/ttm, 31.37/1.8, 31.37/7.12))
