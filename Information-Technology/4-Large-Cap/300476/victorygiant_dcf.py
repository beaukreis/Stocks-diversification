"""Victory Giant Technology 胜宏科技 (SZSE:300476, HKEX:2476) - FCFF DCF, CNY billions. Valuation 1 Oct 2026.
Base 2026E revenue ~CN¥26B (H1 11.63 + H2 ~14.4 est). 2026 capex plan up to CN¥18B: the ~CN¥10B still to be spent
in H2-2026 above maintenance is deducted from net cash. Shares 0.983B (A+H; mkt cap 258.5B / 263.05)."""
import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[3] / "scripts"))
from dcf_lib import run
run(price=230.36, shares=0.983, net_cash=5.0 - 10.0, base_rev=26.0, tax=0.15, capex=0.10, da=0.07, nwc=0.15, cur="CN¥",
    scenarios={
      "Bear": dict(rev=[30, 33, 31, 34, 37, 40, 42, 44, 46, 48], m=[.22, .19, .15, .16, .17, .17, .17, .17, .17, .17], wacc=.105, tg=.02, w=.30),
      "Base": dict(rev=[36, 46, 52, 57, 61, 65, 69, 72, 75, 78], m=[.27, .26, .24, .23, .22, .22, .22, .22, .22, .22], wacc=.095, tg=.025, w=.45),
      "Bull": dict(rev=[40, 55, 66, 76, 85, 93, 100, 107, 114, 120], m=[.29, .29, .28, .27, .26, .26, .26, .26, .26, .26], wacc=.09, tg=.03, w=.25),
    })
ttm = 4.312 - 2.143 + 2.857  # FY25 - H1-25 + H1-26, CN¥B
print("P/E: TTM NI CN¥{:.2f}B -> {:.0f}x | 2027E base NI ~CN¥{:.1f}B -> {:.0f}x | mkt cap CN¥{:.0f}B (US${:.0f}B)".format(ttm, 230.36*0.983/ttm, 36*.27*.85, 230.36*0.983/(36*.27*.85), 230.36*0.983, 230.36*0.983/7.12))
