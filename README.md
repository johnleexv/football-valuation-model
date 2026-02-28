# football-valuation-model

A player valuation framework that applies financial asset-pricing logic to football transfer markets. Rather than competing on advanced on-ball metrics, this model treats players as assets — analyzing market price, production yield, age depreciation, contract optionality, and comparable transactions to identify mispriced players.

## Focus

Feeder leagues across Scandinavia and Switzerland where data coverage is thin and pricing inefficiencies are largest:

- **Layer 1 (Publishing):** Danish 1st Division, Norwegian OBOS-ligaen, Swiss Challenge League, Swedish Superettan
- **Layer 2 (Calibration):** Danish Superliga, Norwegian Eliteserien, Swiss Super League, Swedish Allsvenskan
- **Layer 3 (Comparable Transactions):** 15+ leagues, 370+ clubs across Europe

## Data Sources

- **API-Football** — player statistics across 20+ leagues
- **Transfermarkt** — market values, transfer fees, contract data
- **FotMob** — xG/xA for top-tier league calibration

## Tech Stack

- Python
- DuckDB
- Streamlit (dashboard)

## Status

Early development. Data ingestion and model architecture in progress.
