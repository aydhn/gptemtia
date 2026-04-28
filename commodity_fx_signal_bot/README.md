# Commodity & FX Signal Bot

A zero-budget, paper-trading Python bot for Commodity and FX signals using free data sources (Yahoo Finance, EVDS, FRED) and Telegram for notifications.

**Note:** This bot does NOT execute live trades, nor does it connect to broker APIs for live execution.

## Setup
1. `python -m venv .venv`
2. `source .venv/bin/activate`
3. `pip install -r requirements.txt`

## Execution and Scripts

- `python main.py`: Run the main application (work in progress).

### Phase 3 Commands
- `python -m scripts.run_universe_preview`: Preview the current symbol universe configuration.
- `python -m scripts.run_universe_audit`: Validates the universe and generates a universe manifest in `reports/output`.
- `python -m scripts.run_symbol_reliability_scan --limit 20 --interval 1d --period 1y`: Runs a reliability scan on the universe to check data fetching capability and quality.
- `python -m scripts.run_symbol_reliability_scan --asset-class metals --interval 1d --period 2y`: Runs a reliability scan filtered by asset class.

## Concepts (Phase 3)

- **Reliability Score:** A score from 0 to 100 representing the quality of the downloaded data. Deductions occur for missing prices, errors, duplicate indices, short datasets, etc.
- **Grade System:** Translates the score to a letter grade (A, B, C, D, F) or "SYNTHETIC" for benchmarks that don't need network fetching.
- **Alias Use:** If a primary symbol fails, the pipeline will try its aliases. Doing so costs 5 points on the reliability score.
- **Synthetic Benchmarks:** These symbols represent logical constructs (like an equal-weight portfolio) and do not fetch data from Yahoo.

**Important:** Phase 3 still does not generate trading strategies. It focuses on preparing a clean, graded, and tradeable symbol universe for the following phases.

## Concepts (Phase 4)

- **Timeframes:** The bot targets low-frequency signals using 1h, 4h (derived), 1d, 1wk. 1m/2m are generally excluded to avoid unreliable historical data from Yahoo and frequent API hits.
- **Market Sessions:** Approximate open/close times and weekend checking are added (e.g., Forex is 24/5 while Crypto trades 24/7). This stops unnecessary fetches.
- **Scan Profiles:** Determines how frequently to run. The default `balanced_swing` profile checks every hour using 4h, 1d, 1wk timeframes.
- **Scan Scheduler:** Uses profiles and market session logic to build a "scan plan" telling the bot which symbols to process during the current cycle.

### Phase 4 Commands
- `python -m scripts.run_timeframe_compatibility_audit`: Audits timeframe config, market calendars, and generates a realistic scan plan in `reports/output`.

## Lokal Veri Gölü (Phase 5)

Açıkla:
- **Neden data lake var?** Çevrimiçi veri kaynaklarından (Yahoo vs.) sürekli veri çekmek yerine veriyi kendi ortamımızda saklayarak bant genişliğinden ve süreden tasarruf ederiz. Tekrarlanan ve hatalı denemeleri önleriz.
- **Veriler nereye kaydedilir?** `data/lake/ohlcv/{data_source}/{sub_class}/{symbol}/` altında saklanır.
- **Parquet neden kullanılır?** CSV'ye göre çok daha hızlıdır ve diskte daha az yer kaplar. Pandas ile uyumludur.
- **Manifest nedir?** Veri gölünün o anki fotoğrafını (hangi dosyalar var, boyutları, kaliteleri) özetleyen bir CSV ve JSON listesidir.
- **Download journal nedir?** Her veri indirme denemesinin (başarılı ya da başarısız) kaydedildiği günlüktür. Hata tespitini kolaylaştırır.
- **Repair script ne işe yarar?** Eksik veya "D/F" notuna sahip zayıf kalitedeki veri dosyalarını otomatik tespit edip onarmak için kullanılır.

Komutlar:
- `python -m scripts.run_data_lake_update --limit 10 --period 1y`
- `python -m scripts.run_data_lake_update --asset-class metals --period 2y`
- `python -m scripts.run_data_lake_status`
- `python -m scripts.run_data_lake_repair --dry-run`
