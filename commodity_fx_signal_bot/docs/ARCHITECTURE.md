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
