"""HansBiomed 한스바이오메드 (KOSDAQ:042520) - FCFF DCF, KRW billions; shares in billions so values are KRW per share. Valuation 1 Oct 2026.
Fiscal year ends September. Base FY-Sep-2026E revenue ~KRW141B (9M 101.1 + Q4 ~40 est). Tissue grafts (bone, skin/ADM), CellREDM ECM
skin booster (Hugel distributes in Korea from Apr 2026), BOUNCE breast implants, MINT Lift threads. Shares ~14.26M. Net debt ~KRW30B (est.)."""
import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[3] / "scripts"))
from dcf_lib import run
run(price=20050, shares=0.01426, net_cash=-30, base_rev=141, tax=0.20, capex=0.05, da=0.04, nwc=0.20, cur="₩",
    scenarios={
      "Bear": dict(rev=[155, 165, 175, 185, 195, 205, 215, 225, 235, 245], m=[.08, .09, .10, .10, .10, .10, .10, .10, .10, .10], wacc=.12, tg=.015, w=.30),
      "Base": dict(rev=[185, 225, 260, 290, 315, 335, 355, 370, 385, 395], m=[.15, .18, .20, .20, .20, .20, .20, .20, .20, .20], wacc=.11, tg=.025, w=.45),
      "Bull": dict(rev=[210, 270, 330, 380, 420, 455, 485, 510, 530, 550], m=[.18, .22, .24, .25, .25, .25, .25, .25, .25, .25], wacc=.105, tg=.03, w=.25),
    })
print("EV/Sales FY26E: {:.1f}x | mkt cap KRW{:.0f}B (US${:.0f}M)".format((20050*0.01426+30)/141, 20050*0.01426, 20050*14.26/1380))
