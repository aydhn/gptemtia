# Phase Log

This file tracks the completion of the project phases.

## Phase 1
- Initial repository setup.
- Core utilities (logger, exceptions, constants).
- Settings loaded from `.env`.
- Base provider and Yahoo Finance integration.
- Storage/caching mechanism (Parquet).

## Phase 2
- Data Pipeline implementation.
- Basic Data Quality checks.
- Default Symbol Universe configuration.
- EVDS and FRED provider stubs.

## Phase 3
- Extended `SymbolSpec` to include advanced metadata.
- Implemented `UniverseAnalyzer` to measure symbol data reliability and produce scores/grades.
- Added `run_universe_audit` script to validate and output a universe manifest.
- Added `run_symbol_reliability_scan` script to test data sources and produce reports (CSV, TXT).
- Expanded report builder.
- Expanded tests for symbols, analyzer, and report builder.

## Phase 4
- Timeframe registry eklendi (`config/timeframes.py`).
- Market session config eklendi (`config/market_sessions.py`).
- MarketCalendar skeleton eklendi (`core/market_calendar.py`).
- Scan profiles eklendi (`config/scan_config.py`).
- ScanScheduler skeleton eklendi (`core/scan_scheduler.py`).
- Derived timeframe/resample altyapısı eklendi (`data/data_pipeline.py`).
- Timeframe compatibility audit scripti eklendi (`scripts/run_timeframe_compatibility_audit.py`).
- Testler genişletildi (`tests/test_timeframes.py`, vb.).

## Phase 5
- DataLake eklendi.
- Manifest sistemi eklendi.
- DownloadJournal eklendi.
- DownloadManager eklendi.
- Data lake update/status/repair scriptleri eklendi.
- Derived timeframe metadata güçlendirildi.
- Testler genişletildi.

## Phase 6: Veri Doğrulama, Temizlik ve Bütünlük Katmanı
- OHLCV cleaner eklendi.
- Missing data analizi eklendi.
- Outlier detector eklendi.
- Integrity checks eklendi.
- Quality scoring eklendi.
- Cleaning report sistemi eklendi.
- Processed data lake eklendi.
- Data quality audit scripti eklendi (`run_data_quality_audit.py`).
- Data cleaning scripti eklendi (`run_data_cleaning.py`).
- Processed data status scripti eklendi (`run_processed_data_status.py`).
- Veri kalitesi için genişletilmiş testler yazıldı.

## Phase 7: Teknik İndikatör ve Feature Katmanı
- IndicatorSpec eklendi.
- IndicatorRegistry profesyonelleştirildi.
- Momentum/trend/volatility/volume/mean reversion/price action indikatörleri eklendi.
- FeatureBuilder eklendi.
- IndicatorPipeline eklendi.
- DataLake feature desteği eklendi.
- FeatureStore skeleton geliştirildi.
- Indicator preview/batch/status scriptleri eklendi.
- Testler genişletildi.

## Phase 9
- Trend advanced modülü eklendi.
- Multi SMA/EMA/WMA/HMA/MACD/ADX/Aroon eklendi.
- Ichimoku full hesaplama eklendi.
- Price-MA distance, MA slope, MA stack ve trend persistence eklendi.
- Trend event detection eklendi.
- TrendFeatureSetBuilder eklendi.
- IndicatorPipeline trend feature desteği aldı.
- DataLake trend/trend_events feature set desteği aldı.
- Trend preview/batch/status scriptleri eklendi.
- Testler genişletildi.

## Phase 10: Volatility Indicators, Feature Set, and Events

- **Added**: Volatility advanced module.
- **Added**: Multi ATR, ATR%, Bollinger, Keltner, Donchian.
- **Added**: Historical volatility, Parkinson, Garman-Klass volatility metrics.
- **Added**: Range/gap volatility metrics.
- **Added**: Volatility percentile and slope.
- **Added**: Volatility event detection.
- **Added**: VolatilityFeatureSetBuilder.
- **Updated**: IndicatorPipeline received volatility feature support.
- **Updated**: DataLake received volatility/volatility_events feature set support.
- **Added**: Volatility preview/batch/status scripts.
- **Added**: Extended tests for all new modules.


## Phase 11
- Volume advanced modülü eklendi.
- Volume usability kontrolü eklendi.
- Multi volume SMA/Z-score/relative volume eklendi.
- OBV advanced, MFI, CMF, Accumulation/Distribution, Chaikin Oscillator, PVT eklendi.
- Dollar volume ve liquidity proxy eklendi.
- Volume event detection eklendi.
- VolumeFeatureSetBuilder eklendi.
- IndicatorPipeline volume feature desteği aldı.
- DataLake volume/volume_events feature set desteği aldı.
- Volume preview/batch/status scriptleri eklendi.
- Testler genişletildi.


## Phase 12: Mean Reversion Feature Set & Candidate Events
- Mean reversion advanced modülü eklendi.
- Multi z-score, rolling mean distance, SMA/EMA distance eklendi.
- Percentile rank ve rolling minmax position eklendi.
- Bollinger reversion, channel deviation, overextension score eklendi.
- Snapback pressure ve half-life proxy eklendi.
- Mean reversion event detection eklendi.
- MeanReversionFeatureSetBuilder eklendi.
- IndicatorPipeline mean reversion feature desteği aldı.
- DataLake mean_reversion/mean_reversion_events feature set desteği aldı.
- Mean reversion preview/batch/status scriptleri eklendi.
- Testler genişletildi.

## Phase 13
- Price action advanced modülü eklendi.
- Candle anatomy, body/wick/range/close location featureları eklendi.
- Gap, inside/outside bar, breakout levels ve false breakout featureları eklendi.
- Range compression/expansion ve candle percentile eklendi.
- Consecutive candle features eklendi.
- Price action event detection eklendi.
- PriceActionFeatureSetBuilder eklendi.
- IndicatorPipeline price action feature desteği aldı.
- DataLake price_action/price_action_events feature set desteği aldı.
- Price action preview/batch/status scriptleri eklendi.
- Testler genişletildi.

### Phase 14: Divergence / Uyumsuzluk Motoru
- Pivot detection modülü eklendi.
- Regular ve hidden divergence hesaplama eklendi.
- Divergence strength eklendi.
- Multi-indicator divergence cluster eklendi.
- Divergence event detection eklendi.
- DivergenceFeatureSetBuilder eklendi.
- IndicatorPipeline divergence feature desteği aldı.
- DataLake divergence/divergence_events feature set desteği aldı.
- Divergence preview/batch/status scriptleri eklendi.
- Testler genişletildi.

## Phase 15 - Çoklu Zaman Dilimi Feature Birleştirme (MTF)
- MTF profile sistemi eklendi.
- Timeframe alignment modülü eklendi.
- No-lookahead MTF join mantığı eklendi.
- MTF loader eklendi.
- MTF feature joiner eklendi.
- MTF context skorları eklendi.
- MTF event detection eklendi.
- MTF quality report eklendi.
- MTFPipeline eklendi.
- DataLake mtf/mtf_events feature set desteği aldı.
- MTF preview/batch/status scriptleri eklendi.
- Testler genişletildi.

### Phase 17: Makro Rejim Katmanı, Enflasyon Verileri, USDTRY Benchmark
- Macro profile sistemi eklendi.
- Macro series registry eklendi.
- EVDS/FRED provider güçlendirildi.
- MacroProvider eklendi.
- Inflation featureları eklendi.
- FX macro featureları eklendi.
- Benchmark builder eklendi.
- Macro regime ve macro events eklendi.
- MacroPipeline eklendi.
- Macro scripts ve testler eklendi.


### Phase 18: Asset Class Behavioral Profiles & Group Regimes
- AssetProfile config sistemi eklendi (`asset_profile_config.py`).
- Asset class registry eklendi (`asset_class_registry.py`).
- Asset behavior featureları eklendi (`asset_behavior_features.py`).
- Group feature builder eklendi (`group_features.py`).
- Relative strength featureları eklendi (`relative_strength.py`).
- Correlation ve dispersion featureları eklendi (`correlation_features.py`, `dispersion_features.py`).
- Asset class regime eklendi (`asset_class_regime.py`).
- Asset class event detection eklendi (`asset_class_events.py`).
- AssetProfilePipeline eklendi (`asset_profile_pipeline.py`).
- DataLake `asset_profiles` / `asset_profile_events` / `group_features` desteği aldı.
- Asset profile preview/batch/status scriptleri eklendi.
- Testler genişletildi.


Phase 19:
- Signal scoring profile sistemi eklendi.
- Signal taxonomy eklendi.
- Event normalizer eklendi.
- Event loader eklendi.
- Signal component skorları eklendi.
- SignalScorer eklendi.
- SignalCandidate dataclass eklendi.
- SignalCandidatePool eklendi.
- Signal filters ve quality report eklendi.
- SignalPipeline eklendi.
- DataLake signal_candidates/signal_pool desteği aldı.
- Signal preview/batch/status scriptleri eklendi.
- Testler genişletildi.


### Phase 20: Yönsel Ön Karar ve Bias Ayrıştırması
- Decision profile sistemi eklendi.
- Decision label registry eklendi.
- Directional bias modülü eklendi.
- Decision input loader eklendi.
- Decision component skorları eklendi.
- Conflict resolver eklendi.
- Neutral/no-trade filter eklendi.
- DecisionCandidate dataclass eklendi.
- DecisionEngine eklendi.
- DecisionCandidatePool eklendi.
- Decision quality report eklendi.
- DecisionPipeline eklendi.
- DataLake decision_candidates/decision_pool desteği aldı.
- Decision preview/batch/status scriptleri eklendi.
- Testler genişletildi.

### Phase 23: Risk Precheck Layer
- Risk precheck profile sistemi eklendi.
- Risk label registry eklendi.
- Risk component score modelleri eklendi.
- Volatility/gap/liquidity/data quality/regime/macro/asset risk modülleri eklendi.
- PreTradeRiskEvaluator eklendi.
- Risk filters eklendi.
- RiskPrecheckCandidate dataclass eklendi.
- RiskCandidatePool eklendi.
- Risk quality report eklendi.
- RiskPipeline eklendi.
- DataLake risk_candidates/risk_pool desteği aldı.
- Risk preview/batch/status scriptleri eklendi.
- Testler genişletildi.


## Phase 24: Pozisyon Boyutu Simülasyon Adayları, Volatiliteye Göre Teorik Risk Birimi ve Portföy Risk Bütçesi
- Sizing profile sistemi eklendi.
- Sizing label registry eklendi.
- Sizing models eklendi.
- Risk unit hesaplama eklendi.
- ATR tabanlı teorik sizing eklendi.
- Volatilite adjustment eklendi.
- Teorik budget model eklendi.
- Exposure limit proxy eklendi.
- Sizing filters eklendi.
- SizingCandidate dataclass eklendi.
- SizingCandidatePool eklendi.
- Sizing quality report eklendi.
- SizingPipeline eklendi.
- DataLake sizing_candidates/sizing_pool desteği aldı.
- Sizing preview/batch/status scriptleri eklendi.
- Testler genişletildi.

### Phase 25
- Level profile sistemi eklendi.
- Level label registry eklendi.
- Level models eklendi.
- ATR tabanlı teorik stop/target adayları eklendi.
- Structure/swing/breakout referans seviyeleri eklendi.
- Volatiliteye göre level adjustment eklendi.
- Target ladder eklendi.
- Invalidation zone candidate eklendi.
- Reward/risk hesaplama eklendi.
- Level filters eklendi.
- StopTargetLevelCandidate dataclass eklendi.
- StopTargetLevelCandidatePool eklendi.
- Level quality report eklendi.
- LevelPipeline eklendi.
- DataLake level_candidates/level_pool desteği aldı.
- Level preview/batch/status scriptleri eklendi.
- Testler genişletildi.


## Phase 26: Backtest Engine and Trade Lifecycle Simulation
- Backtest profile sistemi eklendi.
- Backtest label registry eklendi.
- SimulatedTrade ve BacktestRunSummary modelleri eklendi.
- BacktestDataAdapter eklendi.
- EventClock eklendi.
- LookaheadGuard eklendi.
- CandidateAdapter eklendi.
- ExecutionSimulator eklendi.
- TradeLifecycleEngine eklendi.
- TradeLedger eklendi.
- Equity curve ve performance summary eklendi.
- Backtest quality report eklendi.
- BacktestEngine ve BacktestPipeline eklendi.
- DataLake backtest trades/equity/runs/audits desteği aldı.
- Backtest preview/batch/status scriptleri eklendi.
- Testler genişletildi.

## Phase 27: Gelişmiş Backtest Performans Analizi ve Benchmark Kıyaslama
- Advanced metrics modülü eklendi.
- Drawdown metrics modülü eklendi.
- Rolling metrics modülü eklendi.
- Trade distribution analizi eklendi.
- Benchmark comparison eklendi.
- Inflation adjusted performance eklendi.
- Relative performance eklendi.
- Performance breakdown eklendi.
- Performance quality report eklendi.
- PerformanceAnalysisPipeline eklendi.
- DataLake performance/benchmark/rolling/drawdown kayıt desteği aldı.
- Performance preview/batch/status scriptleri eklendi.
- Testler genişletildi.


### Phase 28: Walk-Forward Validation & Optimizer Skeleton
- Validation profile sistemi eklendi (`validation_config.py`).
- Validation label registry eklendi (`validation_labels.py`).
- TimeSplit ve ParameterSet modelleri eklendi (`validation_models.py`).
- Train/test ve walk-forward split üretimi eklendi (`time_splits.py`).
- WalkForwardValidator eklendi (`walk_forward.py`).
- Parameter grid ve sensitivity modülleri eklendi (`parameter_grid.py`, `parameter_sensitivity.py`).
- OptimizerCandidateRunner eklendi (`optimizer_runner.py`).
- Robustness analysis eklendi (`robustness_analysis.py`).
- Overfitting checks eklendi (`overfitting_checks.py`).
- Validation quality report eklendi (`validation_quality.py`).
- ValidationPipeline eklendi (`validation_pipeline.py`).
- DataLake validation kayıt desteği aldı.
- Validation preview/batch/status scriptleri eklendi.
- Testler genişletildi.

### Phase 29: ML DATASET HAZIRLIĞI, SUPERVISED LEARNING TARGET ENGINEERING, FEATURE MATRIX BUILDER VE LEAKAGE-SAFE TRAIN/TEST SPLIT
- ML dataset profile sistemi eklendi.
- Dataset label registry eklendi.
- Target engineering modülü eklendi.
- FeatureMatrixBuilder eklendi.
- SupervisedDatasetBuilder eklendi.
- Leakage audit modülü eklendi.
- Chronological/purged/embargo split modülü eklendi.
- Dataset quality report eklendi.
- Dataset registry metadata eklendi.
- MLDatasetPipeline eklendi.
- DataLake ML feature/target/dataset/split/metadata kayıt desteği aldı.
- ML dataset preview/batch/status scriptleri eklendi.
- Testler genişletildi.

## Phase 30: İlk ML Model Training İskeleti
- ML training profile sistemi eklendi.
- Model label registry eklendi.
- Feature/target schema snapshot eklendi.
- BasicPreprocessor eklendi.
- Baseline model factory eklendi.
- Chronological CV modülü eklendi.
- MLModelTrainer eklendi.
- ModelEvaluator eklendi.
- Model artifact save/load eklendi.
- ModelRegistry taslağı eklendi.
- Model quality report eklendi.
- MLTrainingPipeline eklendi.
- DataLake model evaluation/CV/registry/artifact desteği aldı.
- ML training preview/batch/status scriptleri eklendi.
- Testler genişletildi.
