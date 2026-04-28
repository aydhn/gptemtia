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
