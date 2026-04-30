# Architecture

This document describes the high-level architecture of the Commodity & FX Signal Bot.

## Data Flow

1. **Symbol Universe:** The list of configured symbols (Metals, Energy, Forex, Benchmarks, etc.).
2. **Universe Audit:** Validates symbol configurations and produces summaries.
3. **Data Pipeline:** Orchestrates fetching data, checking cache, and using providers.
4. **Provider:** Handles the actual data fetching from external sources (Yahoo, EVDS, FRED).
5. **Quality Report:** Computes data quality metrics like missing rows, errors.
6. **Reliability Score:** Generates a reliability score and grade based on the quality report.
7. **Universe Manifest:** Outputs the validated, scored, and graded universe to text/CSV/JSON.
8. **Strategy-ready universe:** The clean, analyzed subset of symbols passed to strategies for signal generation.

## Components
- `DataPipeline`: Coordinates data fetching and caching.
- `ProviderRegistry`: Manages data providers.
- `CacheManager`: Handles parquet file caching.
- `UniverseAnalyzer`: Evaluates the reliability of symbols based on data quality metrics.

### Phase 4 Updates
- **Timeframe Registry:** `config/timeframes.py` centralized logic for allowed intervals.
- **Market Session Model:** `config/market_sessions.py` provides approximate asset class trading behavior.
- **Scan Profile & Scheduler:** `config/scan_config.py` and `core/scan_scheduler.py` construct realistic scanning cycles ensuring symbols aren't scanned continuously when the market is closed or when not in profile.
- **Data Resampling:** `data_pipeline.py` introduces handling of `derived` timeframes like 4h using pandas resampling.

New Pipeline Hierarchy:
Symbol Universe → Timeframe Registry → Market Session Model → Scan Profile → Scan Scheduler → Data Pipeline → DownloadManager → DataLake → Manifest → Journal → (Future Strategy Engine)

### Phase 6 Updates
- **Data Quality Audit:** Systematically evaluates the health of data residing in the data lake.
- **OHLCV Cleaner:** Standardizes columns, handles duplicate timestamps, and applies basic structural fixes to DataFrames.
- **Missing Data & Outlier Analysis:** Specialized modules detect gaps, calculate missing ratios, and flag abnormal returns (outliers) without deleting them.
- **Processed Data Lake:** A dedicated storage area for cleaned and verified data, completely separate from the raw downloads, preserving the original unadulterated data.

New Extended Data Flow:
Raw Data Lake → Data Quality Audit → OHLCV Cleaner → Missing Data Analysis → Outlier Detection → Integrity Checks → Quality Scoring → Processed Data Lake → Future Indicators/Strategies/Backtests/ML

### Phase 7 Updates
- **Indicator Registry:** A centralized repository mapping indicator names to calculation functions (`IndicatorRegistry`).
- **Feature Builder:** Processes raw/cleaned OHLCV data to construct composite dataframes of multiple technical indicators.
- **Indicator Pipeline:** Orchestrates applying the Feature Builder across the entire Universe and storing the results as parquet files.
- **Feature Data Lake:** Persists generated features distinctly from raw or simply processed data (`data/lake/features/technical`).
- **Feature Store Stub:** Prepares the retrieval layer for future ML Models (`ml/feature_store.py`).

Extended Pipeline flow:
Processed Data Lake → Indicator Registry → Built-in Indicator Modules → FeatureBuilder → IndicatorPipeline → Technical Feature Store DataLake → Future Strategy/Backtest/ML

### Phase 9 Updates
- **Trend Advanced:** Adds advanced multi-parameter trend indicators (SMA, EMA, WMA, HMA, MACD, ADX, Aroon, Ichimoku) along with derivations like MA distances and slopes.
- **Trend Events:** Produces candidate 0/1 boolean events representing key technical occurrences (e.g. MA cross, MACD shift, ADX strengthening).
- **Trend Feature Set Builder:** Aggregates core trend outputs and derivations into a unified feature set, with configurable "compact" vs "full" profiles.

Extended Pipeline flow:
Processed Data Lake → Trend Indicators → Trend Feature Set → Trend Event Detection → Trend Feature Store → Future Strategy Engine
