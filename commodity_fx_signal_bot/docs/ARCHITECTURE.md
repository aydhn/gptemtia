# Architecture

Processed Data Lake
-> Single Timeframe Feature Stores
-> MTFFeatureLoader
-> Timeframe Alignment
-> MTF Feature Joiner
-> MTF Context Scores
-> MTF Event Detection
-> MTF Feature Store
-> Future Strategy/Quality/Risk Engine


## Makro Akış (Phase 17)
```
Macro Providers
→ Raw Macro Data
→ Inflation Features
→ FX Macro Features
→ Benchmark Builder
→ Macro Regime
→ Macro Events
→ Macro Feature Store
→ Future Benchmark / Risk / Strategy Context
```


## Phase 18 Asset Profile Data Flow

Symbol Universe
→ AssetProfile Registry
→ Single Symbol Feature Stores
→ Group Feature Builder
→ Relative Strength
→ Correlation / Dispersion
→ Asset Class Regime
→ Asset Class Events
→ Asset Profile Feature Store
→ Future Strategy Selection / Risk Engine


Event Feature Stores
→ EventLoader
→ EventNormalizer
→ Signal Components
→ SignalScorer
→ SignalCandidatePool
→ Signal Quality
→ Future Strategy / Backtest / Paper Trade / Telegram


Signal Candidate Pool
→ DecisionInputLoader
→ Directional Bias Analysis
→ Decision Components
→ Conflict Resolver
→ Neutral / No-Trade Filter
→ DecisionEngine
→ DecisionCandidatePool
→ Future Strategy Engine / Backtest / Paper Trade

### Phase 23 Risk Precheck Flow
Strategy Rule Candidates
→ Risk Context Loader
→ Volatility / Gap / Liquidity / Data Quality / Regime / MTF / Macro / Asset Risk
→ PreTradeRiskEvaluator
→ RiskCandidatePool
→ Future Position Sizing / Backtest / Paper Trade


## Position Sizing Candidate Layer (Simülasyon Katmanı)

Risk Candidates
→ Sizing Context Loader
→ Risk Unit Calculator
→ ATR / Volatility Adjusted Sizing
→ Budget Model
→ Exposure Limits
→ SizingCandidatePool
→ Future Backtest / Paper Trade / Portfolio Simulation

## Sizing & Level Generation Flow
Sizing Candidates
→ Level Context Loader
→ ATR Levels
→ Structure Levels
→ Volatility Adjusted Levels
→ Target Ladder
→ Reward/Risk Evaluation
→ StopTargetLevelCandidatePool
→ Future Backtest / Paper Trade / Exit Simulation


### Simulation & Backtesting (Phase 26+)
Level Candidates
→ BacktestDataAdapter
→ CandidateAdapter
→ EventClock
→ LookaheadGuard
→ ExecutionSimulator
→ TradeLifecycleEngine
→ TradeLedger
→ EquityCurve
→ PerformanceSummary
→ BacktestQuality
→ Future Optimizer / Paper Trade / Research Reports

### Phase 27: Performance Analysis Pipeline
Backtest Trades / Equity Curve
-> Advanced Metrics
-> Drawdown Analysis
-> Rolling Metrics
-> Trade Distribution
-> Benchmark Comparison
-> Inflation Adjusted Performance
-> Performance Breakdown
-> Performance Quality
-> Future Walk-Forward / Optimizer / Research Reports


### Validation Katmanı (Phase 28)
Backtest ve Performance pipeline çıktıları üzerinden ilerleyerek;
`Backtest / Performance Outputs` -> `Time Splits` -> `Walk-Forward Validator` -> `Parameter Grid` -> `Sensitivity Analysis` -> `Robustness Analysis` -> `Overfitting Checks` -> `Optimizer Candidate Report` -> `Future Optimizer / Model Selection / Paper Trade Research`
şeklinde model performans dayanıklılığını (in-sample / out-of-sample) denetler.

### Phase 29: ML Dataset Hazırlık Katmanı
Feature Stores / Candidate Stores / Backtest Outputs
→ FeatureMatrixBuilder
→ TargetEngineering
→ LeakageChecks
→ Chronological / Purged / Embargo Split
→ SupervisedDatasetBuilder
→ DatasetRegistry
→ Future ML Training / Model Registry / Prediction Engine

## ML Baseline Training Pipeline Flow (Phase 30)
ML Supervised Dataset
-> Feature/Target Schema
-> BasicPreprocessor
-> BaselineModels
-> Chronological CV
-> MLModelTrainer
-> ModelEvaluator
-> ModelArtifacts
-> ModelRegistry
-> Future Prediction Engine / Model Monitoring / Paper Trade Research

## ML Context Integration Flow (Phase 32)
ML Prediction Context
→ MLContextIntegrationLoader
→ Model-Signal Alignment
→ Model-Decision Alignment
→ Model-Strategy Alignment
→ ML Conflict / Uncertainty Filters
→ Model-Aware Score Adjustment
→ Future Research Reports / Candidate Scoring / Paper Trade Research
