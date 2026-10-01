"""Kona I 코나아이 (KOSDAQ:052400) - FCFF DCF, KRW billions; shares in billions so values are KRW per share. Valuation 1 Oct 2026.
Base 2026E revenue ~KRW330B (H1 161 + H2 ~170 est). Local-currency (지역화폐) platform operator + Kona Card + smart-card/COS business.
Shares ~14.56M (mkt cap KRW602.9B / KRW41,400). Net cash ex-customer float ~KRW150B (est.). Earnings depend on government
local-currency budgets and interest on float, so the bear case models budget cuts."""
import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[3] / "scripts"))
from dcf_lib import run
run(price=37650, shares=0.01456, net_cash=150, base_rev=330, tax=0.20, capex=0.03, da=0.03, nwc=0.0, cur="₩",
    scenarios={
      "Bear": dict(rev=[290, 270, 260, 265, 270, 275, 280, 285, 290, 295], m=[.20, .17, .15, .15, .15, .15, .15, .15, .15, .15], wacc=.12, tg=.01, w=.30),
      "Base": dict(rev=[340, 350, 360, 370, 380, 390, 400, 410, 420, 430], m=[.26, .25, .24, .23, .22, .22, .22, .22, .22, .22], wacc=.11, tg=.015, w=.45),
      "Bull": dict(rev=[380, 420, 460, 490, 520, 545, 570, 590, 610, 630], m=[.28, .28, .27, .27, .26, .26, .26, .26, .26, .26], wacc=.105, tg=.02, w=.25),
    })
ttm = 74.5 - 24.6 + 45.6
print("P/E: TTM NI KRW{:.1f}B -> {:.1f}x | dividend ~KRW2,000/sh -> {:.1%} | mkt cap KRW{:.0f}B (US${:.0f}M)".format(ttm, 37650*0.01456/ttm, 2000/37650, 37650*0.01456, 37650*14.56/1380))
