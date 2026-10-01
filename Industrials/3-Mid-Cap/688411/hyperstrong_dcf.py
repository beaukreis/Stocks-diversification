"""Beijing HyperStrong Technology 海博思创 (SSE STAR:688411) - FCFF DCF, CNY billions. Valuation 1 Oct 2026.
Base 2026E revenue ~CN¥15.8B (H1 6.30 + H2 ~9.5 est). Energy-storage system integrator (24 GWh shipped in 2025).
Shares 0.1827B (mkt cap 31.2B / 170.78). Net cash ~CN¥2B after H1 inventory build (est.)."""
import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[3] / "scripts"))
from dcf_lib import run
run(price=170.78, shares=0.1827, net_cash=2.0, base_rev=15.8, tax=0.15, capex=0.02, da=0.015, nwc=0.20, cur="CN¥",
    scenarios={
      "Bear": dict(rev=[17, 18, 18, 19, 20, 21, 22, 23, 24, 25], m=[.08, .07, .06, .06, .06, .06, .06, .06, .06, .06], wacc=.11, tg=.015, w=.30),
      "Base": dict(rev=[20, 24, 27, 30, 32, 34, 36, 37.5, 39, 40], m=[.11, .105, .10, .095, .09, .09, .09, .09, .09, .09], wacc=.10, tg=.02, w=.45),
      "Bull": dict(rev=[22, 28, 34, 39, 43, 46, 49, 52, 54, 56], m=[.12, .12, .115, .11, .10, .10, .10, .10, .10, .10], wacc=.095, tg=.025, w=.25),
    })
ttm = 0.951 - 0.316 + 0.632
print("P/E: TTM NI CN¥{:.2f}B -> {:.0f}x | mkt cap CN¥31.2B (US${:.1f}B)".format(ttm, 31.2/ttm, 31.2/7.12))
