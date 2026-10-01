"""Jiaxin International Resources 佳鑫国际资源 (HKEX:3858) - FCFF DCF, HK$ billions. Valuation 1 Oct 2026.
Bakuta open-pit tungsten mine (Kazakhstan). Base 2026E revenue ~HK$5.3B (H1 2.70 + H2 ~2.6 est.) at ~9,000t concentrate;
~13,000t/yr from 2027 after phase 2. Revenue = tonnes x realised price (H1-26 ~HK$600k/t est.). Finite mine: terminal growth 0.
Shares ~455M. Net cash ~HK$1.0B (est.)."""
import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[3] / "scripts"))
from dcf_lib import run
run(price=46.9, shares=0.455, net_cash=1.0, base_rev=5.3, tax=0.20, capex=0.05, da=0.05, nwc=0.05, cur="HK$",
    scenarios={
      "Bear": dict(rev=[5.0, 4.6, 4.3, 4.3, 4.3, 4.3, 4.3, 4.3, 4.3, 4.3], m=[.55, .48, .42, .40, .40, .40, .40, .40, .40, .40], wacc=.13, tg=0.0, w=.30),
      "Base": dict(rev=[6.76, 6.24, 5.85, 5.85, 5.85, 5.85, 5.85, 5.85, 5.85, 5.85], m=[.65, .60, .56, .55, .55, .55, .55, .55, .55, .55], wacc=.12, tg=0.0, w=.45),
      "Bull": dict(rev=[8.5, 8.5, 8.5, 8.5, 8.5, 8.5, 8.5, 8.5, 8.5, 8.5], m=[.70, .68, .66, .65, .65, .65, .65, .65, .65, .65], wacc=.11, tg=0.0, w=.25),
    })
print("P/E: H1-26 NI HK$1.54B annualised -> {:.1f}x | mkt cap HK${:.1f}B (US${:.1f}B)".format(46.9*0.455/3.08, 46.9*0.455, 46.9*0.455/7.8))
