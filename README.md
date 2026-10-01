# Stocks Diversification

Fundamental equity research, organised so you can see at a glance how spread out the coverage is across **sectors** and **company sizes**.

Each analysis follows the same Simply Wall St-style framework:

- **Executive snapshot:** business model, market cap, price, TTM revenue and net income
- **Five pillars, each scored out of 6:** Valuation (DCF, P/S, P/E, PEG), Future Growth, Past Performance, Financial Health, and Dividends & Capital Returns
- **Cash-flow Sankey:** how revenue flows through to net income and free cash flow
- **Catalysts and risks:** three growth drivers and three red flags
- **Two investment scores (1–100):** one for 12 months and one for 5 years, each with a rating

## ⭐ [Highlights: Top 10 by 12-month score](Highlights/README.md)

The `Highlights` folder ranks the 10 stocks with the best 12-month score, across all sectors and sizes. It holds no copies of reports. It only names each stock and links to where its report lives.

## Coverage

The table below is generated from each stock's latest report. Don't edit it by hand. Run `python3 scripts/update_index.py` instead.

<!-- coverage:start -->
| Ticker | Company | Sector | Size | Analysis date | Price | Base fair value | 12-month score | 5-year score | Snowflake |
|---|---|---|---|---|---|---|---|---|---|
| [MDGL](Health-Care/4-Large-Cap/MDGL/MDGL-2026-10-01.md) | Madrigal Pharmaceuticals | Health Care | Large-Cap | 2026-10-01 | $503.96 | $288 | 58, Hold | 57, Hold | 14/30 |
| [GUER](Information-Technology/1-Micro-Cap/GUER/GUER-2026-10-01.md) | Guerrilla RF | Information Technology | Micro-Cap | 2026-10-01 | $4.07 | $4.12 | 59, Hold | 47, Hold | 11/30 |
| [2344](Information-Technology/4-Large-Cap/2344/2344-2026-10-01.md) | Winbond Electronics | Information Technology | Large-Cap | 2026-10-01 | NT$180.5 | NT$147 | 62, Buy | 50, Hold | 22/30 |
| [WAF](Materials/3-Mid-Cap/WAF/WAF-2026-10-01.md) | West African Resources | Materials | Mid-Cap | 2026-10-01 | A$3.66 | A$5.05 | 64, Buy | 59, Hold | 22/30 |
<!-- coverage:end -->

Rating bands: 1–20 Strong Sell · 21–40 Sell · 41–60 Hold · 61–80 Buy · 81–100 Strong Buy

## Folder structure

```
Highlights/README.md             top 10 by 12-month score (links only; generated)
scripts/update_index.py          rebuilds Highlights and the Coverage table
<Sector>/<Size tier>/<TICKER>/
    <TICKER>-<YYYY-MM-DD>.md     report (one per analysis date; older ones are kept)
    <ticker>_dcf.py              valuation model, if any (reproduces the report's numbers)
```

For example: `Information-Technology/1-Micro-Cap/GUER/GUER-2026-10-01.md`

### Sectors (the 11 GICS sectors)

| Folder | Covers, for example |
|---|---|
| `Communication-Services` | Telecoms, media, entertainment, interactive media |
| `Consumer-Discretionary` | Autos, retail, hotels and leisure, apparel |
| `Consumer-Staples` | Food, beverages, household products, grocery |
| `Energy` | Oil and gas, energy equipment and services |
| `Financials` | Banks, insurance, asset managers, fintech |
| `Health-Care` | Pharma, biotech, medical devices, providers |
| `Industrials` | Aerospace and defense, machinery, transport, building products |
| `Information-Technology` | Semiconductors, software, hardware, IT services |
| `Materials` | Chemicals, metals and mining, packaging |
| `Real-Estate` | REITs, real-estate developers and services |
| `Utilities` | Electric, gas, water, independent power producers |

### Size tiers (by market capitalisation)

| Folder | Market cap |
|---|---|
| `1-Micro-Cap` | Under $300M (includes nano-caps under $50M) |
| `2-Small-Cap` | $300M–$2B |
| `3-Mid-Cap` | $2B–$10B |
| `4-Large-Cap` | $10B–$200B |
| `5-Mega-Cap` | Over $200B |

The number prefixes keep the tiers in size order instead of alphabetical order.

## Conventions

- **Classifying a stock:** use its GICS sector and its basic market cap on the analysis date.
- **When a stock changes tier:** move its folder to the new tier with `git mv`, so the history stays attached.
- **Report header:** every report starts with a front-matter block holding its ticker, sector, tier, date, price and scores. The index script reads these fields. [CLAUDE.md](CLAUDE.md) lists them.
- **Updating an analysis:** add a new dated report next to the old one rather than overwriting it. Then run `python3 scripts/update_index.py` and commit the regenerated files with the report.
- **Empty folders:** the `.gitkeep` files exist only so Git keeps empty folders. Once a folder has real content, its `.gitkeep` can be deleted.

---

*This repository is personal research, not investment advice. Figures come from public filings and data sources as of each report's date. Each report lists its own data gaps and assumptions.*
