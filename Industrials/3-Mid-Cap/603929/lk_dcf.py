"""L&K Engineering (Suzhou) 亚翔集成 (SSE:603929) - FCFF DCF, CNY billions. Valuation 1 Oct 2026.
Base 2026E revenue ~CN¥5.5B (H1 2.55 + H2 ~3.0 est). Semiconductor cleanroom/MEP contractor; Singapore ~68% of H1 revenue.
Shares 0.21336B. Net cash ~CN¥3.5B incl. customer advances (est.). Current ~20% net margins are far above the
historical ~8-12% for cleanroom contractors, so every scenario fades margins."""
import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[3] / "scripts"))
from dcf_lib import run
run(price=123.2, shares=0.21336, net_cash=3.5, base_rev=5.5, tax=0.17, capex=0.005, da=0.005, nwc=0.05, cur="CN¥",
    scenarios={
      "Bear": dict(rev=[6.0, 5.5, 5.0, 5.2, 5.4, 5.6, 5.8, 6.0, 6.2, 6.4], m=[.16, .12, .10, .09, .09, .09, .09, .09, .09, .09], wacc=.10, tg=.015, w=.30),
      "Base": dict(rev=[8.0, 9.5, 9.0, 8.5, 8.8, 9.1, 9.4, 9.7, 10.0, 10.3], m=[.19, .17, .14, .12, .12, .12, .12, .12, .12, .12], wacc=.095, tg=.02, w=.45),
      "Bull": dict(rev=[9.5, 12.5, 13.5, 13.0, 13.4, 13.8, 14.2, 14.6, 15.0, 15.4], m=[.22, .20, .18, .16, .15, .15, .15, .15, .15, .15], wacc=.09, tg=.025, w=.25),
    })
ttm = 0.892 - 0.161 + 0.490
print("P/E: TTM NI CN¥{:.2f}B -> {:.0f}x | yield {:.1%} (CN¥1.65) | mkt cap CN¥{:.1f}B (US${:.1f}B)".format(ttm, 123.2*0.21336/ttm, 1.65/123.2, 123.2*0.21336, 123.2*0.21336/7.12))
