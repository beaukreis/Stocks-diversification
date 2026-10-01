"""WUS Printed Circuit 沪电股份 (SZSE:002463) - FCFF DCF, CNY billions. Valuation 1 Oct 2026.
Base 2026E revenue ~CN¥28.8B (H1 13.69 + H2 ~15.1 est). AI-server/switch high-layer PCBs; Thailand plant profitable from Q2-26.
Shares 1.924B. Net cash ~CN¥3B (est.)."""
import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[3] / "scripts"))
from dcf_lib import run
run(price=127.8, shares=1.924, net_cash=3.0, base_rev=28.8, tax=0.15, capex=0.09, da=0.05, nwc=0.15, cur="CN¥",
    scenarios={
      "Bear": dict(rev=[32, 34, 32, 35, 38, 40, 42, 44, 46, 48], m=[.22, .19, .16, .17, .17, .17, .17, .17, .17, .17], wacc=.10, tg=.02, w=.30),
      "Base": dict(rev=[38, 46, 50, 54, 58, 61, 64, 67, 70, 72], m=[.26, .25, .23, .22, .21, .21, .21, .21, .21, .21], wacc=.09, tg=.025, w=.45),
      "Bull": dict(rev=[42, 54, 63, 71, 78, 84, 90, 95, 100, 105], m=[.28, .28, .27, .26, .25, .25, .25, .25, .25, .25], wacc=.085, tg=.03, w=.25),
    })
ttm = 3.822 - 1.683 + 2.923
print("P/E: TTM NI CN¥{:.2f}B (EPS {:.2f}) -> {:.0f}x | 2027E base NI ~CN¥{:.1f}B -> {:.0f}x | P/B ~{:.0f}x | mkt cap CN¥{:.0f}B (US${:.0f}B)".format(ttm, ttm/1.924, 127.8/(ttm/1.924), 38*.26*.85, 127.8*1.924/(38*.26*.85), 127.8/(7.85+1.3), 127.8*1.924, 127.8*1.924/7.12))
