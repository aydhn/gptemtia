# Project Architecture

## Core Principles
1.  **Zero-Budget**: Free data sources, paper trading only, and free deployment logic.
2.  **No Live Trading**: Hardcoded safety constraints prevent live trade execution.
3.  **Modular Pipeline**: The system is designed with a unidirectional data flow.

## Data Flow (Phase 2)

The data retrieval and standardization process follows a strict, pipeline-driven flow:

1.  **`SymbolSpec`**: Represents the requested asset and contains metadata (name, asset class, primary symbol, and aliases).
2.  **`ProviderRegistry`**: Examines the `SymbolSpec.data_source` and injects the corresponding data provider instance (e.g., Yahoo, EVDS, FRED).
3.  **`DataPipeline`**: Orchestrates the fetching process. It manages cache checks, executes network calls, and tries alias symbols if the primary symbol fails.
4.  **Provider (`YahooProvider` / `EVDS` / `FRED`)**: Executes the actual data fetch from the external service.
5.  **`normalize_ohlcv`**: The raw data is passed through a normalizer on the base provider to ensure column names and datatypes are consistent (e.g., standardizing index timezones, filling missing FX volume).
6.  **`data_quality.py`**: The normalized data undergoes strict quality assurance (e.g., checking for negative prices, duplicate indices, or high < low anomalies).
7.  **`CacheManager`**: Once validated, the data is saved locally (Parquet format) to prevent redundant network requests in future runs.
8.  **Output**: A clean, validated `pd.DataFrame` is returned to higher-level components (Indicators, Strategies, Backtesting).

## Future Modules
-   **Indicators**: Takes OHLCV data to compute technical analysis features.
-   **Regimes**: Classifies market conditions (trend, range, volatility).
-   **Strategies**: Applies rules to generate long/short signals.
-   **Paper Trading / Backtesting**: Simulates trades.
-   **Telegram**: Sends output signals.
