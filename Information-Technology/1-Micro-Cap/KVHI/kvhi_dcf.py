"""KVH Industries (NASDAQ:KVHI) - EBITDA-based FCF DCF + net cash. US$ millions. Valuation date 1 Oct 2026."""
PRICE = 7.21                  # close 18 Sep 2026
SHARES = 19.2                 # millions (mkt cap ~$138M / $7.21; buybacks under the $15M programme)
NET_CASH = 57.7               # Q2-26 cash, no debt
TAX = 0.21

def dcf(rev, ebitda_m, wacc, tg, capex_pct=0.055, da_pct=0.06, nwc=0.08, nol_years=3, label="", show=True):
    prev, pv = 135.0, 0.0                    # 2026E revenue (guide $130-145M; H1 = $66.0M)
    rows = []
    for i, r in enumerate(rev):
        ebitda = r * ebitda_m[i]
        ebit = ebitda - r * da_pct
        tax = 0.0 if i < nol_years else max(ebit, 0) * TAX
        fcf = ebitda - tax - r * capex_pct - nwc * (r - prev)
        pv += fcf / (1 + wacc) ** (i + 0.75)
        rows.append((2027 + i, r, ebitda, ebitda_m[i], fcf))
        prev = r
    tv = rows[-1][4] * (1 + tg) / (wacc - tg)
    pv_tv = tv / (1 + wacc) ** (len(rev) - 0.25)
    ev = pv + pv_tv
    ps = (ev + NET_CASH) / SHARES
    if show:
        print(f"\n== {label}: WACC {wacc:.0%}, g {tg:.0%} ==")
        print(f"{'Yr':>5}{'Rev':>7}{'EBITDA':>8}{'Mgn':>6}{'FCF':>7}")
        for y, r, e, m, f in rows:
            print(f"{y:>5}{r:>7.0f}{e:>8.1f}{m:>6.0%}{f:>7.1f}")
        print(f"EV ${ev:.0f}M ({pv_tv/ev:.0%} TV) + net cash ${NET_CASH:.0f}M -> ${ps:.2f}/sh ({ps/PRICE-1:+.0%})")
    return ps

base = dcf(rev=[150, 163, 173, 180, 186, 191, 195, 199, 203, 207],
           ebitda_m=[.11, .12, .13, .135, .14, .14, .14, .14, .14, .14],
           wacc=0.11, tg=0.02, label="Base: LEO reseller growth slows, margins creep up with scale")
bear = dcf(rev=[135, 132, 130, 130, 130, 130, 130, 130, 130, 130],
           ebitda_m=[.08, .07, .07, .07, .07, .07, .07, .07, .07, .07],
           wacc=0.12, tg=0.0, label="Bear: Starlink sells direct, reseller margins squeezed, legacy VSAT runs off")
bull = dcf(rev=[165, 185, 200, 212, 222, 230, 237, 243, 249, 255],
           ebitda_m=[.12, .14, .15, .16, .16, .16, .16, .16, .16, .16],
           wacc=0.10, tg=0.025, label="Bull: managed-services layer (CommBox, cyber, crew apps) lifts margins")
pw = 0.30 * bear + 0.45 * base + 0.25 * bull
print(f"\nProbability-weighted (30/45/25): ${pw:.2f} ({pw/PRICE-1:+.0%})")
mcap = PRICE * SHARES
ev = mcap - NET_CASH
print(f"Market cap ${mcap:.0f}M | net cash ${NET_CASH:.0f}M ({NET_CASH/SHARES:.2f}/sh) | EV ${ev:.0f}M | "
      f"EV/2026E EBITDA (mid $13.5M) {ev/13.5:.1f}x | EV/TTM sales {ev/124.9:.2f}x")
