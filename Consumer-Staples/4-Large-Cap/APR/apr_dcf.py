"""APR Corp. 에이피알 (KRX:278470) - FCFF DCF, KRW billions; shares in billions so values are KRW per share. Valuation 1 Oct 2026.
Base 2026E revenue ~KRW3.1T (Q1 ~550 est. + Q2 767.5 + H2 ~1,800 est.). Medicube skincare + AGE-R beauty devices; ~92% overseas.
Shares 37.44M (mkt cap KRW14.41T / KRW385,000 on 27 May). Net cash ~KRW0.8T (est.)."""
import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[3] / "scripts"))
from dcf_lib import run
run(price=380000, shares=0.03744, net_cash=800, base_rev=3100, tax=0.22, capex=0.02, da=0.015, nwc=0.15, cur="₩",
    scenarios={
      "Bear": dict(rev=[3400, 3400, 3300, 3400, 3500, 3600, 3700, 3800, 3850, 3900], m=[.20, .17, .15, .14, .14, .14, .14, .14, .14, .14], wacc=.105, tg=.015, w=.30),
      "Base": dict(rev=[4100, 4900, 5500, 6000, 6400, 6700, 7000, 7250, 7450, 7600], m=[.24, .23, .22, .21, .20, .20, .20, .20, .20, .20], wacc=.095, tg=.025, w=.45),
      "Bull": dict(rev=[4500, 5800, 7000, 8000, 8800, 9400, 9900, 10300, 10600, 10800], m=[.25, .25, .24, .23, .22, .22, .22, .22, .22, .22], wacc=.09, tg=.03, w=.25),
    })
ni26, ni27 = 3100*.24*.78*1.03, 4100*.24*.78*1.03
print("P/E: 2026E NI ~KRW{:.0f}B -> {:.0f}x | 2027E base ~KRW{:.0f}B -> {:.0f}x | mkt cap KRW{:.1f}T (US${:.1f}B)".format(ni26, 380000*0.03744/ni26, ni27, 380000*0.03744/ni27, 380000*0.03744/1000, 380000*0.03744/1380))
