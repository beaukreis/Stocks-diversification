"""IFBH Limited (HKEX:6603) - sum of parts: operating-business DCF (asset-light coconut water brand)
plus balance-sheet net cash. Reported in US$; per-share values converted to HK$. Valuation date 1 Oct 2026."""
PRICE_HKD = 4.14              # close 29 Sep 2026
HKD_PER_USD = 7.80
SHARES = 0.2652               # billions (≈ HK$1.09B market cap / HK$4.14; 266.67M at IPO less buybacks)
NET_CASH = 0.61 * SHARES      # US$B: aggregator net cash/share US$0.61 at 30 Jun 2026 (~US$162M; FY-25 US$162.4M)
TAX = 0.20

def ops_dcf(rev, ebit_m, wacc, tg, capex_pct=0.01, da_pct=0.008, nwc=0.10, base_rev=0.105):
    """US$B. base_rev = 2026E revenue (H1 50.4M + H2 ~55M)."""
    pv, prev = 0.0, base_rev
    for i, r in enumerate(rev):
        fcf = r * ebit_m[i] * (1 - TAX) + r * da_pct - r * capex_pct - nwc * (r - prev)
        pv += fcf / (1 + wacc) ** (i + 0.75)
        prev = r
    tv = (rev[-1] * ebit_m[-1] * (1 - TAX) + rev[-1] * (da_pct - capex_pct)) * (1 + tg) / (wacc - tg)
    return pv + tv / (1 + wacc) ** (len(rev) - 0.25)

def per_share(ops_ev, cash_haircut=0.0):
    eq = ops_ev + NET_CASH * (1 - cash_haircut)
    return eq / SHARES * HKD_PER_USD, eq

scen = {
    # 2027 .. 2031 revenue (US$B) and EBIT margins
    "Bear": dict(rev=[0.100, 0.105, 0.110, 0.113, 0.116], m=[.05, .06, .07, .07, .07], wacc=0.13, tg=0.01, haircut=0.25,
                 story="Brand damage + private-label competition; growth stalls; 25% haircut on cash (trapped/misallocated)"),
    "Base": dict(rev=[0.120, 0.135, 0.148, 0.158, 0.165], m=[.09, .11, .13, .13, .13], wacc=0.12, tg=0.02, haircut=0.0,
                 story="Supply normalises in 2027; revenue recovers to ~94% of FY-25 by 2031; EBIT margin 13% (2024 ~25%)"),
    "Bull": dict(rev=[0.150, 0.180, 0.200, 0.215, 0.228], m=[.13, .17, .19, .20, .20], wacc=0.10, tg=0.03, haircut=0.0,
                 story="Fast recovery, Innococo rebuilt, overseas growth; margins near pre-IPO levels"),
}
vals = {}
for k, s in scen.items():
    ev = ops_dcf(s["rev"], s["m"], s["wacc"], s["tg"])
    ps, eq = per_share(ev, s["haircut"])
    vals[k] = ps
    print(f"{k}: ops EV US${ev*1e3:.0f}M + net cash US${NET_CASH*(1-s['haircut'])*1e3:.0f}M = equity US${eq*1e3:.0f}M "
          f"-> HK${ps:.2f}/sh ({ps/PRICE_HKD-1:+.0%})  | {s['story']}")
# Governance / distress tail: operating business worth nothing, half the cash inaccessible to minorities
distress = per_share(0.0, 0.50)[0]
vals["Distress"] = distress
print(f"Distress: ops worth 0, 50% of cash inaccessible -> HK${distress:.2f}/sh ({distress/PRICE_HKD-1:+.0%})")
pw = 0.30 * vals["Bear"] + 0.40 * vals["Base"] + 0.15 * vals["Bull"] + 0.15 * vals["Distress"]
print(f"Risk-weighted (30 bear / 40 base / 15 bull / 15 distress): HK${pw:.2f} ({pw/PRICE_HKD-1:+.0%})")

mcap_usd = PRICE_HKD * SHARES / HKD_PER_USD
ttm_rev, ttm_ni = 0.1323, 0.0124
print(f"\nMarket cap HK${PRICE_HKD*SHARES:.2f}B = US${mcap_usd*1e3:.0f}M | net cash US${NET_CASH*1e3:.0f}M "
      f"(HK${NET_CASH/SHARES*HKD_PER_USD:.2f}/sh) | EV ≈ US${(mcap_usd-NET_CASH)*1e3:.0f}M")
print(f"P/E TTM {mcap_usd/ttm_ni:.1f}x | ex-cash P/E ≈ {(mcap_usd-NET_CASH)/(ttm_ni-0.0055):.1f}x (TTM interest income ~US$5.5M est.) "
      f"| price / net cash {PRICE_HKD/(NET_CASH/SHARES*HKD_PER_USD):.2f}x | P/S {mcap_usd/ttm_rev:.2f}x")
