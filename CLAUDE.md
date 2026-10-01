# Stocks Diversification: rules for Claude

This repo holds stock fundamental analyses, sorted into `<Sector>/<Size-tier>/<TICKER>/`. The full layout and tier definitions are in README.md.

## Standing task: keep Highlights current

The owner has asked that `Highlights/README.md` **always** show the current top 10 stocks ranked by 12-month score. Whenever you add, update, move or delete a report, finish with these steps in the same commit:

1. `python3 scripts/update_index.py`. This rebuilds `Highlights/README.md` and the Coverage table in `README.md`.
2. `python3 scripts/update_index.py --check`. It must print "up to date".
3. Commit the report together with both regenerated files.

Never copy a report into `Highlights/`. That folder only names stocks and links to where their reports live. Never edit `Highlights/README.md` or the Coverage table by hand.

After the push, tell the owner whether the top 10 changed: what entered, what left, and what moved.

## Adding a report

- **Path:** `<Sector>/<Size-tier>/<TICKER>/<TICKER>-YYYY-MM-DD.md`
  - `<Sector>` is one of the 11 GICS sector folders.
  - `<Size-tier>` is based on **basic** market cap on the analysis date: `1-Micro-Cap` under $300M, `2-Small-Cap` $300M–2B, `3-Mid-Cap` $2–10B, `4-Large-Cap` $10–200B, `5-Mega-Cap` over $200B.
- **Housekeeping:**
  - Delete the folder's `.gitkeep` once it has real content.
  - If a stock has moved to a different tier, `git mv` its whole ticker folder.
  - Keep older dated reports. The script only counts the latest one per ticker.
- **Front matter:** each report must start with this block, and the script validates it against the path.

  ```
  ---
  ticker: GUER
  company: Guerrilla RF
  exchange: OTCQX
  sector: Information-Technology      # must equal the sector folder name
  size_tier: 1-Micro-Cap              # must equal the tier folder name
  analysis_date: 2026-10-01           # must equal the date in the file name
  price: 4.07
  fair_value_base: 4.12               # optional
  score_12m: 59
  rating_12m: Hold
  score_5y: 47
  rating_5y: Hold
  snowflake: 11/30
  ---
  ```

- **Rating bands:** 1–20 Strong Sell, 21–40 Sell, 41–60 Hold, 61–80 Buy, 81–100 Strong Buy. The script rejects a rating that doesn't match its score.
- **Report contents:** follow the existing reports, in this order:
  1. Executive snapshot
  2. Five pillars with 6 pass/fail checks each (Valuation, Future Growth, Past Performance, Financial Health, Dividends & Capital Returns)
  3. Cash-flow Sankey
  4. Three catalysts and three risks
  5. Weighted 12-month and 5-year scores, with the working shown
  6. A data-gaps section
- **Models:** put any model script next to the report and make sure it runs.
