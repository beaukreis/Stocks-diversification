"""SmartSens Technology 思特威 (SSE STAR:688213) - FCFF DCF, CNY billions. Valuation 1 Oct 2026.
Base 2026E revenue ~CN¥10.6B (H1 4.60 + H2 ~6.0 est). Fabless CMOS image sensors (phones, auto, security/AIoT).
Shares ~0.402B (FY25 NI 1.001 / EPS 2.50). Net debt ~CN¥1.5B (inventory financing, est.)."""
import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[3] / "scripts"))
from dcf_lib import run
run(price=92.03, shares=0.402, net_cash=-1.5, base_rev=10.6, tax=0.10, capex=0.03, da=0.03, nwc=0.25, cur="CN¥",
    scenarios={
      "Bear": dict(rev=[11.0, 11.6, 12.2, 12.8, 13.4, 14.0, 14.5, 15.0, 15.5, 16.0], m=[.10, .09, .09, .09, .09, .09, .09, .09, .09, .09], wacc=.105, tg=.02, w=.30),
      "Base": dict(rev=[12.4, 14.2, 15.9, 17.4, 18.7, 19.8, 20.8, 21.7, 22.5, 23.2], m=[.13, .135, .14, .145, .15, .15, .15, .15, .15, .15], wacc=.10, tg=.025, w=.45),
      "Bull": dict(rev=[13.3, 16.0, 18.8, 21.4, 23.7, 25.7, 27.5, 29.1, 30.5, 31.8], m=[.14, .15, .16, .17, .17, .17, .17, .17, .17, .17], wacc=.095, tg=.03, w=.25),
    })
ttm = 1.001 - 0.397 + 0.528
print("P/E: TTM NI CN¥{:.2f}B -> {:.0f}x | 2026E consensus (NI 1.398, EPS 3.48) -> {:.0f}x | mkt cap CN¥{:.1f}B (US${:.1f}B)".format(ttm, 92.03*0.402/ttm, 92.03/3.48, 92.03*0.402, 92.03*0.402/7.12))
