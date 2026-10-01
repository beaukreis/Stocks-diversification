"""Shared FCFF DCF helper used by the per-stock model scripts.

A per-stock script defines its scenarios and calls run(). Example:

    import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[3] / "scripts"))
    from dcf_lib import run
    run(price=100, shares=1.0, net_cash=0.0, base_rev=10.0, tax=0.21,
        scenarios={"Bear": dict(rev=[...], m=[...], wacc=0.11, tg=0.02, w=0.30), ...})

Units are whatever the script uses (state them in its docstring). Revenue lists cover the explicit years
after the base year; m is the EBIT margin per year. FCFF = EBIT*(1-tax) + revenue*(da - capex) - nwc*dRevenue.
Per-share value = (EV + net_cash * (1 - cash_haircut)) / shares * fx, where fx converts to the quote currency.
"""


def value(rev, m, wacc, tg, *, base_rev, tax, shares, net_cash, capex=0.04, da=0.03, nwc=0.15,
          cash_haircut=0.0, fx=1.0):
    pv, prev = 0.0, base_rev
    for i, r in enumerate(rev):
        fcf = r * m[i] * (1 - tax) + r * (da - capex) - nwc * (r - prev)
        pv += fcf / (1 + wacc) ** (i + 0.75)
        prev = r
    last = rev[-1] * m[-1] * (1 - tax) + rev[-1] * (da - capex)
    tv = last * (1 + tg) / (wacc - tg) / (1 + wacc) ** (len(rev) - 0.25)
    ev = pv + tv
    return (ev + net_cash * (1 - cash_haircut)) / shares * fx, ev


def run(*, price, shares, net_cash, base_rev, tax, scenarios, capex=0.04, da=0.03, nwc=0.15, fx=1.0, cur=""):
    """Print each scenario and the probability-weighted value; return {name: value} plus 'weighted'."""
    out, total_w = {}, 0.0
    for name, s in scenarios.items():
        ps, ev = value(s["rev"], s["m"], s["wacc"], s["tg"], base_rev=base_rev, tax=tax, shares=shares,
                       net_cash=net_cash, capex=s.get("capex", capex), da=s.get("da", da), nwc=s.get("nwc", nwc),
                       cash_haircut=s.get("haircut", 0.0), fx=fx)
        out[name] = ps
        total_w += s["w"]
        print(f"{name:>8}: rev {s['rev'][0]:g}->{s['rev'][-1]:g} | EBIT {s['m'][0]:.0%}->{s['m'][-1]:.0%} | "
              f"WACC {s['wacc']:.1%} g {s['tg']:.1%} | EV {ev:,.1f} -> {cur}{ps:,.2f}/sh ({ps/price-1:+.0%})")
    weighted = sum(out[n] * s["w"] for n, s in scenarios.items()) / total_w
    out["weighted"] = weighted
    print(f"Probability-weighted: {cur}{weighted:,.2f} ({weighted/price-1:+.0%}) vs price {cur}{price:,.2f}")
    return out
