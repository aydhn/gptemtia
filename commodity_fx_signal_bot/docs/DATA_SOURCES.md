# Data Sources

This document describes the data sources used by the Commodity & FX Signal Bot.

## Symbol Reliability Checks
During Phase 3, we introduced a systematic way to check and grade the reliability of data for each symbol.
The `UniverseAnalyzer` fetches data for a symbol and grades it from `A` to `F` (or `SYNTHETIC`) based on factors like:
- Successful fetch
- Enough rows
- No missing close prices
- No duplicate indices
- No negative prices
- No high/low inversion
- Valid last close price

## Yahoo Finance (yfinance)
- Used for most Commodities and Forex pairs.
- **Yahoo Missing Data Risk:** Sometimes Yahoo might drop a symbol or temporarily have missing data. The reliability scan will flag this and lower the score.
- **Alias Fallback:** If the primary symbol fails, the system will attempt to fetch data using aliases defined in the `SymbolSpec`. Using an alias reduces the reliability score by 5 points.
- **Futures Data Limitations:** Yahoo may not provide continuous contracts seamlessly, so roll dates and gaps are common.
- **FX Volume:** Volume data for Forex pairs is often missing or zero on Yahoo Finance.

## EVDS (TCMB)
- Used for Turkish macroeconomic indicators (e.g., Inflation, Interest rates).

## FRED (St. Louis Fed)
- Used for US macroeconomic indicators (e.g., CPI, Interest rates).

## Synthetic Symbols
- Symbols marked with `data_source="synthetic"` (e.g., Benchmarks) are not fetched from external providers like Yahoo. They are generated internally or bypassed to maintain perfect reliability scores ("SYNTHETIC" grade).
