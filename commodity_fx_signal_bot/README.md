# Commodity & FX Signal Bot

A zero-budget, paper-trading Python bot designed to generate signals for Commodities and FX using free data sources.

## Important Constraints
- **NO LIVE TRADING:** This bot is strictly meant for backtesting, paper trading, and signal generation via Telegram.
- **NO PAID APIs:** Operates purely on free public endpoints (Yahoo Finance, EVDS, FRED).
- **NO WEB SCRAPING:** Relies on robust API clients, no HTML parsing.

## Setup

Set up a virtual environment and then:
pip install -r requirements.txt

## Running Scripts and Tools

### Download Single Symbol Data
Test the fetch pipeline and cache logic for a single symbol:
python -m scripts.run_single_symbol_download --symbol GC=F --interval 1d --period 1y

### Run Bulk Data Check
Validate the health of the entire symbol universe, providing success rates and error summaries:
python -m scripts.run_bulk_data_check --limit 10 --interval 1d --period 6mo

### Run Tests
Execute the pytest suite:
pytest
