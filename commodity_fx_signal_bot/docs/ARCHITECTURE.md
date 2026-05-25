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

## Regime-Aware Portfolio Research

Portfolio Research / Returns / Baskets / Correlation
-> RegimeClassifier
-> RegimeConditionedReturns
-> RegimeCorrelation
-> MacroScenarios
-> ScenarioSensitivity
-> StressWindows
-> BasketStressTest
-> DrawdownClustering
-> RecoveryAnalysis
-> TailRisk
-> RiskRegimeExposure
-> RegimeQuality
-> Regime-Aware Portfolio Reports

### Synthetic Indices and Relative Strength Pipeline
Universe Prices / Returns -> IndexUniverse -> BenchmarkDefinitions -> WeightingSchemes -> CompositeIndexBuilder -> RelativeStrength -> RelativeMomentum -> RotationResearch -> LeadershipLaggard -> BenchmarkComparison -> IndexPerformance -> IndexQuality -> Synthetic Index Research Reports

### Factor Research Pipeline
Universe Prices / Returns / Synthetic Indices / Macro Proxies
-> FactorDefinitions
-> TrendFactor
-> MomentumFactor
-> VolatilityFactor
-> CarryProxyFactor
-> ValueProxyFactor
-> MacroSensitivityFactors
-> FactorScoring
-> FactorRanking
-> FactorBacktest
-> FactorIC
-> FactorStability
-> FactorExposure
-> FactorNeutralization
-> FactorQuality
-> Factor Research Reports


## Meta Research Pipeline (Phase 45)

Technical / Strategy / Risk-Level / Backtest / Validation / ML / Paper / Research Reports / Synthetic Index / Portfolio / Regime / Factor
-> EvidenceCollector
-> EvidenceNormalizer
-> SourceRegistry
-> ReliabilityScoring
-> ConsensusEngine
-> ConflictDetection
-> UncertaintyAggregation
-> EnsembleScoring
-> QualityAdjustment
-> MetaRanking
-> MetaSnapshot
-> MetaQuality
-> Meta Research Reports

## Experiment Tracking Layer
The Experiment Tracking layer standardizes how we record, compare, and version offline research experiments.
It interacts with existing meta, factor, portfolio, ML, and paper research outputs.
Workflow:
Research Outputs -> HypothesisRegistry -> ExperimentRegistry -> ExperimentRunner -> ResearchVersioning -> ArtifactManifest -> ReproducibilityManifest -> ExperimentMetrics -> AblationStudies -> ExperimentComparison -> Leaderboard -> ExperimentQuality -> Experiment Reports

### Data Provenance & Governance Flow
DataLake / Reports Output / Experiment Manifests / Research Artifacts
-> ArtifactInventory
-> Fingerprinting
-> ProvenanceRegistry
-> LineageGraph
-> DependencyTracing
-> AuditTrail
-> SourceAttribution
-> FreshnessGovernance
-> IntegrityGovernance
-> ExperimentLineageBridge
-> GovernanceChecklist
-> GovernanceQuality
-> Research Governance Reports

## Phase 48: Adaptive Research Planning

The architecture includes a comprehensive offline research planning pipeline:

Governance / Experiments / Meta / Factor / Synthetic Index / Portfolio / Regime / Validation / ML / Paper / Observability
→ `PlanningSignalCollector`
→ `BacklogBuilder`
→ `PriorityScoring`
→ `NextBestExperiment`
→ `ResearchDebt`
→ `ResearchOpportunities`
→ `RoadmapHealth`
→ `TaskDependencies`
→ `MilestoneTracking`
→ `OfflineTaskOrchestrationPlan`
→ `PlanningQuality`
→ Research Planning Reports


## Phase 49: Knowledge Base & Analyst Workspace

Docs / Reports Output / DataLake Research Artifacts / Experiments / Governance / Planning / Meta
→ `DocumentDiscovery`
→ `TextExtraction`
→ `Chunking`
→ `KnowledgeIndex`
→ `TFIDFRetrieval`
→ `FuzzyRetrieval`
→ `HybridRetrieval`
→ `MemoryCards`
→ `DecisionJournal`
→ `AnalystNotes`
→ `FindingsDigest`
→ `WorkspaceSummary`
→ `KBQuality`
→ Analyst Workspace Reports



## Phase 50: Offline Analyst Command Center

The Command Center provides guided orchestration and safe runbooks for offline research capabilities:

All Offline Modules / Scripts / Reports / DataLake / Knowledge Base
-> CommandRegistry
-> CommandSafety
-> WorkflowRegistry
-> RunbookRegistry
-> DryRunPlanner
-> InteractiveQueryFlows
-> ProjectStatus
-> ModuleHealth
-> ScriptDiscovery
-> PhaseCoverage
-> Consolidation
-> Onboarding
-> Troubleshooting
-> CommandQuality
-> Offline Analyst Command Center Reports


### Quality Gates Pipeline
Source Code / Tests / Scripts / DataLake / Reports / Docs
→ TestDiscovery
→ TestHealth
→ ImportGraph
→ StaticSafetyScan
→ RepoHygiene
→ DependencyAudit
→ SmokeTests
→ OutputContracts
→ DocumentationCoverage
→ LocalCIRunner
→ ReleaseChecklist
→ ReleaseManifest
→ ReleaseNotes
→ QualityGatePipeline

## Performance Profiling Flow
Offline Scripts / Command Registry / DataLake / Reports / Knowledge Index
→ RuntimeProfiler
→ MemoryProfiler
→ CPU/GPU Awareness
→ ResourceBudget
→ CacheRegistry
→ CacheStrategy
→ CacheInventory
→ BatchPlanner
→ Checkpointing
→ LargeRunStability
→ BottleneckDetection
→ OptimizationRecommendations
→ PerformanceQuality
→ Performance Reports
