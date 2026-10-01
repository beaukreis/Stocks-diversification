# GUER DCF + dilution model. All $ in millions, shares in millions.
PRICE = 4.07
BASIC = 10.698139
PREF_CONV = 7.213115          # Series A, $22.0M stated / $3.05
W250, W305, WHI = 2.071293, 2.885246, 5.780955 - 2.071293 - 2.885246
WHI_K = (5.780955*4.00 - W250*2.50 - W305*3.05) / WHI   # implied strike of remaining warrants
OPTS, OPT_K, RSU = 0.810636, 4.00, 0.103650             # option strike ASSUMED (not disclosed in sources)
CASH, DEBT = 4.557784, 5.7

def diluted_shares(px):
    """Treasury-stock method diluted share count at price px."""
    s = BASIC + PREF_CONV + RSU            # preferred converts whenever px > 3.05; at lower px it is still a $22M claim
    for n, k in ((W250, 2.50), (W305, 3.05), (WHI, WHI_K), (OPTS, OPT_K)):
        if px > k:
            s += n * (1 - k / px)
    return s

def per_share(equity):
    """Value per share where all in-the-money instruments exercise (cash in). Iterate to fixed point."""
    px = equity / (BASIC + PREF_CONV)
    for _ in range(100):
        sh, proceeds = BASIC + RSU, 0.0
        # preferred: converts if conversion value > $22M stated value, else takes $22M off the top
        if px > 3.05:
            sh += PREF_CONV; pref_claim = 0.0
        else:
            pref_claim = 22.0
        for n, k in ((W250, 2.50), (W305, 3.05), (WHI, WHI_K), (OPTS, OPT_K)):
            if px > k:
                sh += n; proceeds += n * k
        new = max(equity + proceeds - pref_claim, 0) / sh
        if abs(new - px) < 1e-6: break
        px = new
    return px

def dcf(rev0, growth, gm, opex0, opex_g, tax, wacc, tg, da=1.3, capex_pct=0.025, nwc_pct=0.16, label=""):
    rows, rev, opex, pv, prev_rev = [], rev0, opex0, 0.0, rev0
    for i, g in enumerate(growth):
        rev = prev_rev * (1 + g)
        opex = opex * (1 + opex_g[i])
        ebit = rev * gm[i] - opex
        t = tax[i] if ebit > 0 else 0.0
        fcf = ebit * (1 - t) + da - rev * capex_pct - nwc_pct * (rev - prev_rev)
        df = (1 + wacc) ** (i + 0.75)   # mid-year-ish from Oct-2026 valuation date, first year = 2027
        pv += fcf / df
        rows.append((2027 + i, rev, ebit, ebit / rev, fcf, fcf / df))
        prev_rev = rev
    tv = rows[-1][4] * (1 + tg) / (wacc - tg)
    pv_tv = tv / (1 + wacc) ** (len(growth) - 0.25)
    ev = pv + pv_tv
    eq = ev + CASH - DEBT
    return rows, pv, pv_tv, ev, eq, per_share(eq)

REV_2026E = 31.0   # H1-26 actual 14.5 + H2 est 16.5 (backlog $13.6M supports)
OPEX_2026E = 19.0

scen = {
  "Bear": dict(growth=[0.10,0.07,0.06,0.05,0.04], gm=[0.67]*5, opex_g=[0.05]*5,
               tax=[0,0,0.10,0.23,0.23], wacc=0.15, tg=0.02),
  "Base": dict(growth=[0.20,0.15,0.12,0.10,0.08], gm=[0.695,0.70,0.70,0.70,0.70], opex_g=[0.08,0.07,0.07,0.06,0.06],
               tax=[0,0,0.10,0.23,0.23], wacc=0.13, tg=0.03),
  "Bull": dict(growth=[0.30,0.22,0.18,0.14,0.10], gm=[0.71]*5, opex_g=[0.10,0.09,0.08,0.07,0.06],
               tax=[0,0,0.10,0.23,0.23], wacc=0.12, tg=0.03),
}
out = {}
for name, p in scen.items():
    rows, pv, pvtv, ev, eq, ps = dcf(REV_2026E, opex0=OPEX_2026E, **p)
    out[name] = ps
    print(f"\n== {name}: WACC {p['wacc']:.0%}, g {p['tg']:.0%} ==")
    print(f"{'Yr':>5}{'Rev':>8}{'EBIT':>8}{'EBIT%':>8}{'UFCF':>8}{'PV':>8}")
    for y, r, e, m, f, v in rows:
        print(f"{y:>5}{r:>8.1f}{e:>8.1f}{m:>8.1%}{f:>8.1f}{v:>8.1f}")
    print(f"PV FCF {pv:.1f} | PV TV {pvtv:.1f} ({pvtv/ev:.0%} of EV) | EV {ev:.1f} | Equity {eq:.1f} | Value/share (fully diluted) ${ps:.2f} | vs price {ps/PRICE-1:+.0%}")

print("\nBase-case sensitivity (value/share):  WACC down, terminal g across")
for w in (0.10, 0.11, 0.12, 0.13, 0.14, 0.15):
    line = f"WACC {w:.0%}: "
    for g in (0.02, 0.03, 0.04):
        p = dict(scen["Base"]); p["wacc"], p["tg"] = w, g
        line += f"  g{g:.0%}=${dcf(REV_2026E, opex0=OPEX_2026E, **p)[5]:.2f}"
    print(line)

dil = diluted_shares(PRICE)
print(f"\nImplied high-strike warrant price: ${WHI_K:.2f} on {WHI:.3f}M warrants")
print(f"Basic mkt cap @${PRICE}: ${BASIC*PRICE:.1f}M | TSM diluted shares {dil:.2f}M | diluted mkt cap ${dil*PRICE:.1f}M")
ev_now = dil*PRICE + DEBT - CASH
print(f"Diluted EV ≈ ${ev_now:.1f}M")
TTM_REV, Q2_RUN, REV26 = 27.5, 8.01*4, REV_2026E
print(f"EV/TTM sales {ev_now/TTM_REV:.2f}x | EV/Q2 run-rate {ev_now/Q2_RUN:.2f}x | EV/2026E {ev_now/REV26:.2f}x | basic P/S TTM {BASIC*PRICE/TTM_REV:.2f}x")
print(f"Pref as-converted share of fully diluted (all ITM): {PREF_CONV/(BASIC+PREF_CONV+W250+W305+RSU+OPTS):.0%}")
