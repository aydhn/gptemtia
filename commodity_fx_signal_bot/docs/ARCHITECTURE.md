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

### Maintenance Architecture
DataLake / Reports Output / Logs / Cache / Checkpoints / Archives
→ StorageInventory
→ RetentionPolicies
→ ArchiveStrategy
→ CleanupPlanner
→ RotationPlanner
→ DuplicateDetection
→ StaleDetection
→ LargeArtifactReview
→ StorageGrowth
→ SafeFileOps
→ MaintenanceChecklist
→ LifecycleHealth
→ MaintenanceQuality
→ Maintenance Reports

## Phase 55: Final System Review

The system executes a comprehensive final system review and offline acceptance workflow.

All Modules / Scripts / Reports / DataLake / Docs / Quality Gates / Maintenance / Performance
→ SystemInventory
→ ArchitectureAudit
→ SafetyAudit
→ IntegrationAudit
→ CommandAudit
→ DataLakeAudit
→ ReportOutputAudit
→ DocumentationAudit
→ QualityGateAudit
→ ReadinessAudit
→ RiskRegister
→ GapRegister
→ AcceptanceChecklist
→ ReleaseReadinessDryRun
→ ConsolidationAudit
→ FinalReviewQuality
→ Final Review Reports



## Scenario Pipeline Architecture (Phase 56)

ScenarioProfile
→ ScenarioRegistry
→ SampleDataBuilder
→ FixtureGenerator
→ ExpectedOutputs
→ WorkflowPacks
→ DemoCommandSequences
→ ScenarioDryRunExecutor
→ ScenarioValidation
→ CaseStudies
→ ModuleDemoFlows
→ EndToEndDemo
→ ScenarioQuality
→ Scenario Reports


## Scenario Regression Flow (Phase 57)
Scenario Registry / Synthetic Fixtures / Expected Outputs / Demo Workflows
-> RegressionRegistry
-> GoldenOutputs
-> SnapshotCapture
-> SnapshotCompare
-> DeterministicReplay
-> FixtureReproducibility
-> OutputContractValidation
-> DemoWorkflowRegression
-> EndToEndAcceptance
-> DriftDetection
-> FailureRegister
-> AcceptanceChecklist
-> RegressionQuality
-> Scenario Regression Reports


## Analyst UX and Operator Productivity Flow (Phase 58)

Command Center / Documentation / Scenario Regression / Quality Gates / Final Review
-> CommandAliases
-> IntentClassifier
-> SafeCommandMapper
-> PromptPacks
-> WorkflowShortcuts
-> QueryMapping
-> AnalystTaskBoard
-> CheatSheets
-> ProductivityChecklist
-> UXValidation
-> UXQuality
-> Analyst UX Reports


### Report Summarization Pipeline
Reports Output / DataLake Reports / Docs / Status Outputs
→ ReportInventory
→ TextSummarizer
→ FindingExtractor
→ WarningExtractor
→ RiskGapExtractor
→ ModuleSummaries
→ SymbolBriefs
→ DigestCards
→ SafetyQualityBriefs
→ ExecutiveSummary
→ AnalystBrief
→ WeeklyReviewPack
→ FollowUpTasks
→ SummaryValidation
→ SummaryQuality
→ Report Summarization Outputs

### Phase 61: Portable Packaging
Project Source / Config / Docs / Tests / Reports / DataLake
→ EnvironmentSnapshot
→ DependencyInventory
→ RequirementsExport
→ InstallVerification
→ ImportVerification
→ ScriptVerification
→ ConfigVerification
→ SourcePolicy
→ BundleManifest
→ ArchiveManifest
→ ReproducibleSetupGuide
→ EnvironmentDrift
→ PackagingSafety
→ PackagingQuality
→ Portable Packaging Outputs

### Phase 62: Backup/Restore Dry-Run and Disaster Recovery

Project Source / Config / Docs / Tests / DataLake / Reports / Manifests
→ ProjectStateInventory
→ ScopeClassifier
→ BackupPolicies
→ CriticalArtifacts
→ BackupManifest
→ BackupDryRunPlan
→ RestoreDryRunPlan
→ RestoreVerification
→ DisasterRecoveryManifest
→ RecoveryRunbook
→ IntegrityManifest
→ RecoveryGapAnalysis
→ BackupSafety
→ BackupQuality
→ Backup Recovery Outputs

### Phase 64: Evidence Governance
Reports / DataLake / Docs / Generated Evidence / Quality / Safety / Secrets / Backup / Packaging / Master Outputs
→ EvidenceArtifactInventory
→ PolicyRegistry
→ ControlRegistry
→ PolicyToControlMapping
→ ControlToEvidenceMapping
→ TraceabilityMatrix
→ EvidenceScoring
→ EvidenceGapRegister
→ EvidencePacks
→ AuditEvidenceBinder
→ GovernanceEvidenceExport
→ EvidenceDigest
→ EvidenceValidation
→ EvidenceQuality
→ Evidence Governance Outputs

### Artifact Metadata Flow
Research Artifacts -> ResearchArtifactInventory -> ModelCards/DatasetCards/ExperimentCards/ReproducibilityCards -> BacktestCards/ScenarioCards/RegressionCards/FeatureSetCards/SyntheticDataCards/ResearchReportCards -> LineageCards/LimitationCards/IntendedUseCards/NonUsePolicyCards -> MetadataScoring/MetadataValidation/MetadataQuality/MetadataExport -> Artifact Metadata Outputs
