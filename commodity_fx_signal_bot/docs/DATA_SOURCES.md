# Data Sources Policy & Documentation

## Overview
This project strictly adheres to a **Zero-Budget, Free-Tier API Only** policy. We do not use paid APIs or any web scraping techniques (e.g., Selenium, BeautifulSoup). Data must be fetched programmatically via official or legally accessible free endpoints.

## Providers

### 1. Yahoo Finance (`yfinance`)
- **Usage**: Primary source for OHLCV data of Commodities and FX.
- **Limitations**:
  - Futures symbols (e.g., `GC=F`) may be delayed.
  - Foreign Exchange (FX) symbols may lack meaningful `volume` data (it may be returned as 0).
  - Subject to rate limits; excessive bulk downloading should be avoided.

### 2. EVDS (Central Bank of the Republic of Turkey)
- **Usage**: Source for Turkish macroeconomic data (e.g., Inflation/CPI, Interest Rates).
- **Setup**: Requires a free API key set via the `EVDS_API_KEY` environment variable.

### 3. FRED (Federal Reserve Economic Data)
- **Usage**: Source for US macroeconomic data (e.g., CPI, Interest Rates).
- **Setup**: Requires a free API key set via the `FRED_API_KEY` environment variable.

## Data Pipeline & Stability
To ensure system stability and compliance with our strict constraints:

- **No Scraping Bans**: We rely entirely on libraries like `yfinance` or direct API calls. If an endpoint blocks us, the system logs an error gracefully rather than breaking.
- **Alias Fallback**: If a primary symbol (e.g., `USDTRY=X`) fails to fetch, the pipeline automatically tries configured aliases (e.g., `USD/TRY`).
- **Data Quality Validation**: Downloaded data must pass strict quality checks (no all-NaN columns, no duplicate indices, no negative prices).
- **Cache System**: Parquet-based caching is implemented to minimize network requests, adhere to rate limits, and speed up testing/backtesting.
