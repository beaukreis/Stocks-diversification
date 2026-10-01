"""Forest Cabin 林清轩 (HKEX:2657) - FCFF DCF in CN¥ billions, per-share value converted to HK$ (fx 1.095). Valuation 1 Oct 2026.
Base 2026E revenue ~CN¥3.25B (H1 1.50 + H2 ~1.75 est). Premium Chinese skincare (camellia facial oils, serums, toners); 81.6% gross margin.
Shares ~140.2M (CN¥185M interim dividend / CN¥1.32). Net cash ~CN¥2.0B incl. IPO proceeds and wealth products (est.)."""
import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[3] / "scripts"))
from dcf_lib import run
run(price=49.58, shares=0.1402, net_cash=2.0, base_rev=3.25, tax=0.25, capex=0.03, da=0.025, nwc=0.05, fx=1.095, cur="HK$",
    scenarios={
      "Bear": dict(rev=[3.5, 3.7, 3.9, 4.0, 4.1, 4.2, 4.3, 4.4, 4.5, 4.6], m=[.15, .14, .14, .14, .14, .14, .14, .14, .14, .14], wacc=.11, tg=.015, w=.30),
      "Base": dict(rev=[4.0, 4.7, 5.3, 5.8, 6.2, 6.6, 6.9, 7.2, 7.5, 7.7], m=[.18, .18, .18, .18, .18, .18, .18, .18, .18, .18], wacc=.10, tg=.025, w=.45),
      "Bull": dict(rev=[4.3, 5.3, 6.2, 7.0, 7.7, 8.3, 8.8, 9.3, 9.7, 10.0], m=[.20, .20, .21, .21, .21, .21, .21, .21, .21, .21], wacc=.095, tg=.03, w=.25),
    })
ttm = 0.358 - 0.182 + 0.256
print("P/E: TTM NI CN¥{:.3f}B -> {:.1f}x | interim DPS CN¥1.32 -> {:.1%} half-year yield | mkt cap HK${:.2f}B (US${:.2f}B)".format(ttm, 49.58*0.1402/1.095/ttm, 1.32*1.095/49.58, 49.58*0.1402, 49.58*0.1402/7.8))
