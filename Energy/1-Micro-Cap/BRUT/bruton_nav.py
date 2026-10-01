"""Bruton Limited (OSL:BRUT) - post-demerger (4 VLCCs). Ship-by-ship equity cash-flow DCF + NAV cross-check.
US$ millions unless noted. Valuation date 1 Oct 2026. OMC Tankers (the other 8 newbuilds) was spun off 1:1 on 28 Aug 2026."""
PRICE_NOK = 48.40             # close 24 Sep 2026 (ex the Sep US$0.025 distribution)
USDNOK = 10.0
SHARES = 61.923808            # millions
DAYS = 355                    # on-hire days per year
OPEX = 10.5                   # $k/day vessel opex incl. DF-LNG premium (est.)
GA = 1.0                      # $k/day per ship corporate G&A (est.)
RATE = 0.056                  # sale-leaseback implied interest, 20-year profile, 15-year tenor

def annuity(principal, r=RATE, n=20):
    return principal * r / (1 - (1 + r) ** -n)

def balance_after(principal, years, r=RATE, n=20):
    pmt = annuity(principal, r, n)
    return pmt * (1 - (1 + r) ** -(n - years)) / r

SHIPS = [  # name, contract price, financed %, delivery (years from 1 Oct 2026), fixed charter (rate $k/d, years)
    ("Mount Vision (DF LNG)",  138.0, 0.90, 0.00, (95.0, 0.55)),   # $95k fixed to ~Apr-27, then index-linked (market)
    ("Mount Horizon (DF LNG)", 138.0, 0.90, 0.12, (105.7, 1.15)),  # $105.7k net, 12-15 months from mid-Nov 2026
    ("NTS #3 (conventional)",  122.0, 0.875, 0.85, None),          # Aug 2027
    ("NTS #4 (conventional)",  122.0, 0.875, 1.05, None),          # Oct 2027
]

def market_rate(t, deck):
    """deck: dict year_index -> $k/day; t in years from valuation date."""
    yr = int(t)
    return deck.get(yr, deck["lt"])

def ship_equity_value(ship, deck, coe, resale_15y):
    name, price, ltv, dlv, fixed = ship
    debt = price * ltv
    pmt = annuity(debt)
    pv, t = 0.0, dlv
    end = dlv + 15
    while t < end - 1e-9:
        step = min(0.25, end - t)
        if fixed and t < dlv + fixed[1]:
            tce = fixed[0]
        else:
            tce = market_rate(t, deck)
        cf = ((tce - OPEX - GA) * DAYS / 1000 * step) - pmt * step   # $M
        pv += cf / (1 + coe) ** (t + step / 2)
        t += step
    residual = resale_15y - balance_after(debt, 15)               # ship value at 15y less lease balloon
    pv += residual / (1 + coe) ** end
    equity_still_due = price * (1 - ltv) if dlv > 0.2 else 0.0    # yard equity not yet paid (est.: assume due at delivery)
    pv -= equity_still_due / (1 + coe) ** dlv
    return pv

DECKS = {
    "Bear": {0: 60, 1: 45, 2: 38, "lt": 35},
    "Base": {0: 85, 1: 62, 2: 50, "lt": 45},
    "Bull": {0: 115, 1: 90, 2: 70, "lt": 55},
}
COE = {"Bear": 0.13, "Base": 0.11, "Bull": 0.10}
RESALE15 = {"Bear": 40, "Base": 55, "Bull": 65}
NET_CASH_EST = 15.0           # $M, corporate cash net of accrued items after demerger (est.; not disclosed in sources)

vals = {}
for k in DECKS:
    total = sum(ship_equity_value(s, DECKS[k], COE[k], RESALE15[k]) for s in SHIPS) + NET_CASH_EST
    ps_usd = total / SHARES
    vals[k] = ps_usd * USDNOK
    print(f"{k}: VLCC rate deck {DECKS[k]} $k/d | CoE {COE[k]:.0%} | equity US${total:.0f}M -> "
          f"US${ps_usd:.2f} = NOK {vals[k]:.1f}/sh ({vals[k]/PRICE_NOK-1:+.0%})")
pw = 0.30 * vals["Bear"] + 0.45 * vals["Base"] + 0.25 * vals["Bull"]
print(f"Probability-weighted (30/45/25): NOK {pw:.1f} ({pw/PRICE_NOK-1:+.0%})")

# Mark-to-market NAV cross-check (charter-free broker-style values, Sep 2026)
mv = {"Mount Vision (DF LNG)": 180, "Mount Horizon (DF LNG)": 180, "NTS #3 (conventional)": 160, "NTS #4 (conventional)": 160}
debt_full = sum(s[1] * s[2] for s in SHIPS)
equity_due = sum(s[1] * (1 - s[2]) for s in SHIPS if s[3] > 0.2)
nav = sum(mv.values()) - debt_full - equity_due + NET_CASH_EST
print(f"\nMTM NAV: ship values US${sum(mv.values())}M - lease debt (full) US${debt_full:.0f}M - equity still due US${equity_due:.0f}M "
      f"+ cash US${NET_CASH_EST:.0f}M = US${nav:.0f}M -> NOK {nav/SHARES*USDNOK:.1f}/sh (P/NAV {PRICE_NOK/(nav/SHARES*USDNOK):.2f}x)")
for haircut in (0.85, 0.70):
    n2 = sum(mv.values()) * haircut - debt_full - equity_due + NET_CASH_EST
    print(f"  ship values x{haircut:.2f}: NOK {n2/SHARES*USDNOK:.1f}/sh")

mcap_usd = PRICE_NOK * SHARES / USDNOK
print(f"\nMarket cap NOK {PRICE_NOK*SHARES/1000:.2f}B = US${mcap_usd:.0f}M | distribution US$0.025/month = US$0.30/yr "
      f"-> yield {0.30*USDNOK/PRICE_NOK:.1%}")
for name, price, ltv, dlv, fixed in SHIPS:
    pmt = annuity(price * ltv)
    print(f"  {name}: lease ~US${pmt:.1f}M/yr = ${pmt*1000/365:.1f}k/d -> cash breakeven ≈ ${pmt*1000/365 + OPEX:.0f}k/d (+G&A)")
