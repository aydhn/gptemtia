# Architecture Document

Sistem aşağıdaki katmanlardan oluşur:
- Data (Data fetching and caching)
- Features (Technical indicators)
- Asset Profiles (Context evaluation)
- Regimes (Macro classification)
- Signals (Signal candidate generation)
- Decisions (Decision bias generation)
- Strategies (Trade sizing and strategy alignment)
- Backtesting / Paper (Simulating trades safely without real exchange connections)
- ML Integration (Optional predictions as context)
- Observability (Logging and metrics)
- Security (Secret masking)
- Notifications (Telegram alerts)
- Orchestration (Pipelines)
- DevTools (Developer experience and repo hygiene)

Bu sistem hiçbir koşulda canlı broker emri GÖNDERMEZ.

## Research Reports (Phase 39)

The Research Reports component extracts offline analysis, backtesting, and ML metadata to assemble human-readable reports without emitting real signals.
The flow works as follows:

DataLake Outputs / FeatureStore / Backtest / Validation / ML / Paper / Quality
-> ResearchDataCollector
-> Section Summaries
-> SymbolResearchSnapshot
-> NarrativeBuilder
-> RankingBuilder
-> MarkdownRenderer
-> CSVExporter
-> ResearchQuality
-> User-Readable Research Reports (Markdown, TXT, CSV)
