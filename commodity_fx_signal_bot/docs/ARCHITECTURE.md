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

## Local Knowledge Graph Data Flow

Artifact Metadata / Evidence Governance / Report Summaries / Docs / Commands / Scenarios / Regression / DataLake / Reports
→ NodeRegistry
→ EdgeRegistry
→ RelationshipExtractors
→ ArtifactRelationshipGraph
→ ModuleGraph
→ ReportGraph
→ EvidenceGraph
→ CardGraph
→ ScenarioRegressionGraph
→ CommandReportGraph
→ LocalSemanticKeywordIndex
→ LocalTFIDFIndex
→ RelationshipQuery
→ GraphTraversal
→ GraphAnalysis
→ GraphGapDetection
→ GraphExport
→ GraphValidation
→ GraphQuality
→ Local Knowledge Graph Outputs

## Local Timeline Data Flow
Project Files / Reports / DataLake / Docs / Metadata / Evidence / Graph / Quality / Safety
→ EventRegistry
→ PhaseChronology
→ ArtifactEvolution
→ FileTimeline
→ ReportTimeline
→ DataLakeTimeline
→ DocumentationTimeline
→ CommandTimeline
→ EvidenceTimeline
→ MetadataTimeline
→ GraphTimeline
→ ScenarioRegressionTimeline
→ QualitySafetyTimeline
→ BackupPackagingSecretsTimeline
→ TemporalLineage
→ EventClustering
→ FreshnessAnalysis
→ EventGapDetection
→ ChangeDigest
→ TimelineQuery
→ TimelineExport
→ TimelineValidation
→ TimelineQuality
→ Local Timeline Outputs

### Local Consistency Engine Flow
Config / Env Template / Paths / DataLake / Scripts / Reports / Docs / Evidence / Metadata / Graph / Timeline / Backup / Packaging / Secrets
-> ConsistencyCheckRegistry
-> CrossLayerConsistencyMatrix
-> ConfigEnvConsistency
-> SettingsDocsConsistency
-> PathsDataLakeConsistency
-> ScriptReportConsistency
-> ReportDataLakeConsistency
-> DocsPhaseLogConsistency
-> EvidenceControlConsistency
-> MetadataArtifactConsistency
-> GraphMetadataConsistency
-> TimelineArtifactConsistency
-> BackupPackagingSecretsConsistency
-> NonUsePolicyConsistency
-> DisclaimerConsistency
-> SafetyBoundaryConsistency
-> ContradictionDetector
-> ReferenceChecker
-> StaleReconciliation
-> CoherenceScoring
-> ReconciliationRecommendations
-> ConsistencyValidation
-> ConsistencyQuality
-> Local Consistency Outputs

## Local Readiness Pipeline

Docs / Tests / Scripts / Reports / DataLake / Security / Backup / Packaging / Metadata / Evidence / Graph / Timeline / Consistency
-> ReadinessGateRegistry
-> MilestoneAcceptanceCriteria
-> PhaseEvidenceBinder
-> OperatorChecklist
-> StabilizationChecklist
-> DryRunCommands
-> CommandCoverage
-> DocsReadiness
-> TestsReadiness
-> DataLakeReadiness
-> ReportsReadiness
-> SecurityBoundaryReadiness
-> BackupPackagingReadiness
-> CrossLayerReadiness
-> LimitationsRegister
-> GapsRegister
-> ManualReviewRegister
-> GoNoGoRegistry
-> HandoffManifest
-> ReadinessScoring
-> RiskSummary
-> ReadinessValidation
-> ReadinessQuality
-> Local Readiness Outputs

## Local Maintenance Data Flow

Docs / Tests / Scripts / Reports / DataLake / Config / Requirements / Security / Backup / Packaging / Evidence / Metadata / Graph / Timeline / Consistency / Readiness
-> MaintenanceDomainRegistry
-> MaintenanceTaskRegistry
-> PeriodicReviewCalendar
-> RefreshCadence
-> DependencyAgingWatch
-> DependencyReviewChecklist
-> StaleArtifactWatch
-> StaleReportWatch
-> StaleDocumentationWatch
-> StaleTestWatch
-> ManualReviewQueue
-> MaintenanceGapRegister
-> MaintenanceRiskSummary
-> SustainabilityScoring
-> OperatorPeriodicReviewChecklist
-> ReviewTemplates
-> RefreshCommandPlan
-> MaintenanceRunbook
-> LongTermSustainabilityBinder
-> MaintenanceValidation
-> MaintenanceQuality
-> Local Maintenance Outputs

### Phase 71: Local Archival Strategy & Preservation Layer
Docs / Reports / DataLake / Config / Scripts / Tests / Security / Backup / Packaging / Evidence / Metadata / Graph / Timeline / Consistency / Readiness / Maintenance
→ ArchiveDomainRegistry
→ ArchiveItemRegistry
→ ArchiveCandidateInventory
→ ArchiveExclusionRegistry
→ ProjectSnapshotCatalog
→ ColdStorageManifest
→ RetentionPolicy
→ RetentionReview
→ ArchiveHashManifest
→ IntegrityVerification
→ RestoreReadiness
→ ProvenanceRegistry
→ DependencySnapshot
→ DocumentationArchiveIndex
→ ReportArchiveIndex
→ DataLakeArchiveIndex
→ CrossLayerArchiveIndex
→ SecurityArchiveBoundary
→ SecretExclusionVerification
→ ArchiveGapRegister
→ ArchiveRiskSummary
→ LongHorizonPreservationBinder
→ ArchiveValidation
→ ArchiveQuality
→ Local Archive Outputs
\n\n
## Local Disaster-Recovery Architecture (Phase 72)

Archive / Backup / Docs / Reports / DataLake / Config / Scripts / Tests / Security / Evidence / Metadata / Graph / Timeline / Consistency / Readiness / Maintenance
→ DRDomainRegistry
→ TabletopScenarios
→ RestoreDrillSimulation
→ FailureModeRegistry
→ FailurePlaybooks
→ IncidentRehearsalBinder
→ ResilienceCalendar
→ RestoreReadinessChecklist
→ ArchiveRestoreTraceability
→ BackupRestoreTraceability
→ DataLakeRestoreSimulation
→ DocsRestoreSimulation
→ ReportsRestoreSimulation
→ ConfigEnvRestoreSimulation
→ ScriptsTestsRestoreSimulation
→ CrossLayerRestoreSimulation
→ SecretBoundaryRehearsal
→ RecoveryCommandPlan
→ DRGaps
→ DRRisks
→ ResilienceScoring
→ DRValidation
→ DRQuality
→ Local DR Outputs

## Phase 73: Local Training Layer
Docs / Reports / Scripts / Tests / DataLake / Safety Docs / Evidence / Metadata / Graph / Timeline / Consistency / Readiness / Maintenance / Archive / DR
-> TrainingDomainRegistry
-> RoleBasedOnboardingPaths
-> OperatorTrainingPack
-> AnalystTrainingPack
-> DeveloperTrainingPack
-> SafeUsageTraining
-> NonUsePolicyTraining
-> GuidedWalkthroughRegistry
-> LocalWalkthroughLessons
-> CommandLessons
-> ReportLessons
-> DataLakeLessons
-> CrossLayerLessons
-> TroubleshootingLessons
-> Glossary
-> ConceptMap
-> FAQ
-> FirstWeekCurriculum
-> KnowledgeTransferChecklist
-> HandoverEducationBinder
-> TrainingAssessment
-> TrainingGaps
-> TrainingRisks
-> TrainingValidation
-> TrainingQuality
-> Local Training Outputs

Docs / Reports / DataLake / Evidence / Metadata / Graph / Timeline / Consistency / Readiness / Maintenance / Archive / DR / Training
-> CommunicationProfileRegistry
-> StakeholderAudienceRegistry
-> ExecutiveSummaryPack
-> ProjectOnePager
-> NonTechnicalBriefingDeckSource
-> ProjectNarrativeReport
-> DecisionContextBinder
-> CapabilityMap
-> BoundaryNonUseSummary
-> RiskLimitationNarrative
-> MilestoneNarrative
-> PhaseEvolutionNarrative
-> ArchitectureNarrative
-> StakeholderFAQ
-> ExecutiveGlossary
-> SafeCommunicationGuide
-> CommunicationDoDont
-> StakeholderTemplates
-> CommunicationGaps
-> CommunicationRisks
-> BriefingValidation
-> BriefingQuality
-> Local Briefing Outputs

### Phase 75: Local Synthesis Layer
Docs / Reports / DataLake / Scripts / Tests / Evidence / Metadata / Graph / Timeline / Consistency / Readiness / Maintenance / Archive / DR / Training / Briefing
→ SynthesisProfileRegistry
→ PhaseFamilyRegistry
→ MasterArtifactIndex
→ MasterReportIndex
→ MasterDataLakeIndex
→ MasterDocsIndex
→ MasterScriptIndex
→ MasterTestIndex
→ CrossPhaseFinalMap
→ EndStateCapabilityMap
→ EndStateBoundaryMap
→ EndStateModuleDependencyMap
→ EndStateOutputCatalog
→ FinalCatalogs
→ FinalNonUsePolicyBinder
→ FinalSafetyBoundaryBinder
→ FinalLocalOnlyStatement
→ FinalLimitationRegister
→ FinalManualReviewRegister
→ FinalNoGoSafeGoSummary
→ NavigationGuides
→ ProjectCompletionDossier
→ ProjectClosureChecklist
→ FinalSynthesisValidation
→ FinalSynthesisQuality
→ Local Synthesis Outputs

## Local Hardening Architecture

Source / Docs / Reports / DataLake / Scripts / Tests / Contracts / Safety / Synthesis
→ HardeningProfileRegistry
→ HardeningDomainRegistry
→ DeadCodeCandidateReview
→ UnusedModuleReview
→ OrphanScriptReview
→ OrphanTestReview
→ DuplicateUtilityReview
→ ContractSurfaceRegistry
→ PublicFunctionContracts
→ DataLakeContracts
→ FeatureStoreContracts
→ ScriptCLIContracts
→ ReportBuilderContracts
→ ConfigContracts
→ PathContracts
→ TestContractFreeze
→ DocumentationFreezeSnapshot
→ GeneratedDocsFreezeCatalog
→ RCDryRunFreezeManifest
→ RCCommandPlan
→ RCBoundaryChecklist
→ Import/Path/Output/Naming/Dependency/SafetyHealth
→ HardeningGaps
→ HardeningRisks
→ FreezeValidation
→ FreezeQuality
→ Local Hardening Outputs

Synthesis / Hardening / Docs / Reports / DataLake / Scripts / Tests / Safety / Evidence
→ AcceptanceProfileRegistry
→ AcceptanceDomainRegistry
→ AcceptanceCriteriaRegistry
→ FinalAcceptanceSimulationChecklist
→ ReviewerQuestionBank
→ ReviewerEvidenceRequestMatrix
→ AuditStyleLocalEvidenceTrail
→ EvidenceOutputTrace
→ EvidenceTestTrace
→ EvidenceDocTrace
→ EvidenceSafetyBoundaryTrace
→ IndependentReviewerPack
→ SignoffRehearsalChecklist
→ VerificationScenarioRegistry
→ VerificationRehearsalPlan
→ FinalVerificationEvidenceBinder
→ AcceptanceNoGoSafeGo
→ AcceptanceGaps
→ AcceptanceRisks
→ AcceptanceReadinessScoring
→ AcceptanceValidation
→ AcceptanceQuality
→ Local Acceptance Outputs

### Local Delivery Rehearsal
- Final delivery bundle manifest nasıl okunur? It is a JSON/CSV manifest, no real files are packaged.
- Handoff package index ne yapar/ne yapmaz? Indexes available files for review. Does not move them.
- Portable reviewer archive guide nasıl kullanılır? Provides a sequence for local code review.
- Final local transfer checklist neden resmi teslim onayı değildir? Because it operates strictly locally in dry-run mode.
- Delivery rehearsal binder nasıl yorumlanır? A summary text document of the rehearsal.
- Delivery readiness score neden production handoff değildir? Because no real transfer or deployment is made.
Gerçek transfer, package publish, cloud upload, deployment, canlı emir, broker execution ve yatırım tavsiyesi yoktur.
\n\n### Phase 79: Local Archival

Delivery / Acceptance / Hardening / Synthesis / Docs / Reports / DataLake / Scripts / Tests / Safety
-> ArchivalProfileRegistry
-> ArchivalDomainRegistry
-> HashPolicyRegistry
-> SensitiveFileExclusionRegistry
-> ArchiveCandidateInventory
-> FinalHashCatalog
-> FinalHashOfHashesCatalog
-> FinalArchivalSealRehearsalManifest
-> ImmutableManifestRehearsalCatalog
-> LocalProvenanceLockfile
-> HashRehearsalReports
-> CustodyChainSimulation
-> LongTermCustodyGuide
-> RetentionNotes
-> TamperEvidenceDryRun
-> ReproducibilityPointers
-> ProvenanceTraceMatrices
-> ArchivalNoGoSafeGo
-> ArchivalExceptions
-> ArchivalGaps
-> ArchivalRisks
-> ArchivalReadinessScoring
-> ArchivalValidation
-> ArchivalQuality
-> Local Archival Outputs

## Phase 80: Local Closure Flow
Archival / Delivery / Acceptance / Hardening / Synthesis / Briefing / Training / Docs / Reports / DataLake / Scripts / Tests / Safety
→ ClosureProfileRegistry
→ ClosureDomainRegistry
→ FinalProjectMetaReview
→ LessonsLearnedCompendium
→ FutureRoadmapBacklog
→ FuturePhaseCandidateRegistry
→ PostProjectGovernanceRehearsal
→ ClosureRecaps
→ UnresolvedItems
→ OpenQuestions
→ ImprovementBacklog
→ MaintenanceCalendar
→ OwnershipMatrix
→ DecisionLog
→ AssumptionsRegister
→ LimitationsRegister
→ ClosureNoGoSafeGo
→ HandoffAftercare
→ ClosureFAQ
→ ClosureExceptions
→ ClosureGaps
→ ClosureRisks
→ ClosureReadinessScoring
→ V1LocalClosureDossier
→ ClosureValidation
→ ClosureQuality
→ Local Closure Outputs

Closure / Archival / Delivery / Acceptance / Hardening / Synthesis / Briefing / Training / Docs / Reports / DataLake / Scripts / Tests / Safety
→ ReuseProfileRegistry
→ ReuseDomainRegistry
→ FinalAuditMemoryPack
→ PhaseMemoryCapsules
→ ReusableTemplateCatalog
→ PromptTemplateLibrary
→ ModuleBlueprints
→ ScriptPatterns
→ TestPatterns
→ DataLakeContractPatterns
→ ReportPatterns
→ SafetyBoundaryPatterns
→ DocumentationPatterns
→ PatternExtractionReports
→ LocalKnowledgeReuseKit
→ V11PlanningSeed
→ V11BacklogSeed
→ V11SafetyBoundarySeed
→ FutureProjectStarter
→ ReuseNoGoSafeGo
→ ReuseExceptions
→ ReuseGaps
→ ReuseRisks
→ ReuseReadinessScoring
→ ReuseValidation
→ ReuseQuality
→ Local Reuse Outputs

### Local Simplification Flow (Phase 82)
Reuse / Closure / Archival / Delivery / Acceptance / Hardening / Synthesis / Docs / Reports / DataLake / Scripts / Tests / Safety
→ SimplificationProfileRegistry
→ SimplificationDomainRegistry
→ FinalModularComplexityMap
→ ModuleFamilyComplexity
→ FolderDepthComplexity
→ FileCountComplexity
→ FunctionCountComplexity
→ Script/Test/Output/DocsSprawlReports
→ ConsolidationCandidates
→ SpecificSimplificationCandidates
→ OptionalSlimmingPlan
→ RepoErgonomicsGuide
→ MaintainerOnboardingGuide
→ MaintainabilityImprovementSeed
→ ComplexityNoGoSafeGo
→ SimplificationExceptions
→ SimplificationGaps
→ SimplificationRisks
→ MaintainabilityReadinessScoring
→ SimplificationValidation
→ SimplificationQuality
→ Local Simplification Outputs
\n\n-> PerformanceProfileRegistry -> PerformanceDomainRegistry -> FinalLocalPerformanceBudget -> LightweightRuntimeProfile -> ResourceFootprintRehearsal -> CPU/Memory/DiskEstimates -> GrowthEstimates -> Script/Test/PipelineRuntimeEstimates -> MaintenanceCostEstimate -> MaintenanceEffortMatrix -> OperatorTimeBudget -> LocalMachineSuitability -> OfflineEfficiencyPlanning -> EfficiencyCandidates -> LightweightModeRecommendations -> HeavyOutputWarnings -> RetentionRehearsal -> PerformanceNoGoSafeGo -> PerformanceExceptions -> PerformanceGaps -> PerformanceRisks -> PerformanceReadinessScoring -> PerformanceValidation -> PerformanceQuality -> Local Performance Outputs
## Local Usability Review and Operator Navigation
Phase 84:
- Final local usability review gerçek kullanıcı testi değildir.
- Operator friction map telemetry veya analytics değildir.
- Command discoverability guide komut çalıştırmaz.
- Documentation navigation assistant pack harici LLM/API değildir.
- Operator paths canlı operasyon prosedürü değildir.
- Human-in-the-loop checkpoint otomatik onay üretmez.
- Usability readiness score production usability approval değildir.
- Çıktılar data/lake/local_usability ve reports/output/local_usability altında oluşur.

Komutlar:
```bash
python -m scripts.run_usability_domain_registry
python -m scripts.run_final_local_usability_review
python -m scripts.run_command_discoverability_guide
python -m scripts.run_documentation_navigation_assistant
python -m scripts.run_operator_paths
python -m scripts.run_usability_quality_report
python -m scripts.run_usability_status
```
\n### Local Red-Team Rehearsal Flow
Governance Control / Usability / Performance / Simplification / Reuse / Closure / Archival / Delivery / Acceptance / Hardening / Synthesis / Docs / Reports / DataLake / Scripts / Tests / Safety
→ RedTeamProfileRegistry
→ RedTeamDomainRegistry
→ FinalLocalRedTeamRehearsalPacket
→ MisuseScenarioLibrary
→ AbuseCaseSimulationRegistry
→ AdversarialPromptSafetyChecklist
→ PromptInjectionRiskPatterns
→ UnsafeOutputPatterns
→ ForbiddenCapabilityRequests
→ BoundaryViolationScenarios
→ SpecificMisuseRegistries
→ SafetyResponseExpectations
→ SafeRefusalTemplates
→ SafeRedirectPatterns
→ ManualEscalation
→ HumanReviewAbuseCases
→ RedTeamReadingOrder
→ SafetyAssuranceSummary
→ SafetyCoverageMatrix
→ SafetyBlindspots
→ SafetyNonGoals
→ RedTeamNoGoSafeGo
→ RedTeamExceptions
→ RedTeamGaps
→ RedTeamRisks
→ RedTeamReadinessScoring
→ RedTeamValidation
→ RedTeamQuality
→ Local Red-Team Outputs
\n
### Phase 87 Pipeline
RedTeam / Governance Control / Usability / Performance / Simplification / Reuse / Closure / Archival / Delivery / Acceptance / Hardening / Synthesis / Docs / Reports / DataLake / Scripts / Tests / Safety
→ IncidentResponseProfileRegistry
→ IncidentDomainRegistry
→ FinalLocalIncidentResponseRehearsalPacket
→ SafetyEventRegister
→ SafetyEventTaxonomy
→ SeverityTriageClassification
→ SpecificEventRegistries
→ RollbackDecisionPlaybook
→ RollbackBoundaries
→ ContainmentRehearsal
→ DegradedModeRehearsal
→ RecoveryRehearsal
→ ResilienceSupervision
→ EvidenceSnapshotIndex
→ IncidentReadingOrder
→ TimelineTemplates
→ PostIncidentReviewTemplates
→ RootCauseCategories
→ CorrectiveActionRehearsal
→ CommunicationTemplates
→ EscalationDecisions
→ IncidentNoGoSafeGo
→ IncidentExceptions
→ IncidentGaps
→ IncidentRisks
→ IncidentReadinessScoring
→ IncidentValidation
→ IncidentQuality
→ Local Incident Response Outputs

Release Candidate / Incident Response / RedTeam / Governance Control / Usability / Performance / Simplification / Reuse / Closure / Archival / Delivery / Acceptance / Hardening / Synthesis / Docs / Reports / DataLake / Scripts / Tests / Safety
→ LongTermOperationsProfileRegistry
→ LongTermDomainRegistry
→ FinalLocalLongTermOperationsBinder
→ ReviewCalendars
→ LifecycleMaintenanceWorkbook
→ MaintenanceCadence
→ MaintenanceOwnership
→ MaintenanceEvidence
→ RetentionDataLakeGeneratedDocsReview
→ QualitySafetyIncidentRedTeamGovernanceReview
→ DeprecationRehearsal
→ DeprecationCandidates
→ NonDeprecationBoundaries
→ MigrationReadiness
→ V1xRoadmapGovernance
→ RoadmapCandidates
→ RoadmapPriority
→ FeatureIntake
→ ChangeControl
→ RiskBenefitReview
→ RoadmapNoGoSafeGo
→ LifecycleExceptions
→ LifecycleGaps
→ LifecycleRisks
→ LifecycleReadinessScoring
→ LifecycleValidation
→ LifecycleQuality
→ Local Long-Term Operations Outputs

## Project Completion Pipeline
LongTerm Operations / Release Candidate / Incident Response / RedTeam / Governance Control / Usability / Performance / Simplification / Reuse / Closure / Archival / Delivery / Acceptance / Hardening / Synthesis / Docs / Reports / DataLake / Scripts / Tests / Safety
→ ProjectCompletionProfileRegistry
→ CompletionDomainRegistry
→ FinalLocalSystemClosureDossier
→ TerminalHandoffPack
→ KnowledgeFreezeRehearsal
→ KnowledgeFreezeBoundaries
→ LastMileAuditBinder
→ CompletionEvidenceMap
→ CompletionCriteriaMatrix
→ CompletionReadinessPacket
→ CompletionUnresolvedLimitationsFinalRisk
→ FinalInventories
→ FinalCommandOutputMaps
→ FinalRecaps
→ FinalHandoffChecklists
→ TerminalMaps
→ CompletionNoGoSafeGo
→ CompletionExceptions
→ CompletionGaps
→ CompletionRisks
→ CompletionReadinessScoring
→ CompletionValidation
→ CompletionQuality
→ Local Project Completion Outputs


## Preservation Flow
Project Completion / LongTerm Operations / Release Candidate / Incident Response / RedTeam / Governance Control / Usability / Performance / Simplification / Reuse / Closure / Archival / Delivery / Acceptance / Hardening / Synthesis / Docs / Reports / DataLake / Scripts / Tests / Safety
→ PreservationProfileRegistry
→ PreservationDomainRegistry
→ FinalLocalArchiveSealRehearsalPacket
→ ArchiveSealChecklist
→ ArchiveSealBoundaries
→ ImmutableReadmeRehearsal
→ EvidenceVaultIndex
→ EvidenceVaultIntegrity
→ FinalKnowledgeCapsule
→ KnowledgeCapsuleMaps
→ PreservationBinder
→ PreservationInventories
→ PreservationFingerprints
→ PreservationRestoreNotes
→ PreservationNonGoals
→ PreservationAccessNotes
→ PreservationHandoff
→ PreservationNoGoSafeGo
→ PreservationExceptions
→ PreservationGaps
→ PreservationRisks
→ PreservationReadinessScoring
→ PreservationValidation
→ PreservationQuality
→ Local Post-Completion Preservation Outputs


## Local Project Atlas Katmanı

Continuity Intelligence / Post-Completion Preservation / Project Completion / LongTerm Operations / Release Candidate / Incident Response / RedTeam / Governance Control / Usability / Performance / Simplification / Reuse / Closure / Archival / Delivery / Acceptance / Hardening / Synthesis / Docs / Reports / DataLake / Scripts / Tests / Safety
→ ProjectAtlasProfileRegistry
→ AtlasDomainRegistry
→ FinalLocalMetaIndex
→ UniversalNavigationMap
→ CrossPhaseLookupEngine
→ CrossPhaseLookupTables
→ OfflineSemanticTableOfContents
→ TerminalProjectAtlas
→ AtlasFamilyMaps
→ AtlasPhaseMaps
→ AtlasRouteMaps
→ AtlasGlossary
→ AtlasCrosswalks
→ AtlasNoGoSafeGo
→ AtlasExceptions
→ AtlasGaps
→ AtlasRisks
→ AtlasReadinessScoring
→ AtlasValidation
→ AtlasQuality
→ Local Project Atlas Outputs

### Local Review Governance (Phase 94)
Project Atlas -> Local Review Governance:
- ReviewGovernanceProfileRegistry
- ReviewGovernanceDomainRegistry
- FinalLocalHumanReviewCockpit
- HumanReviewCockpitMaps
- ManualApprovalLedgerRehearsal
- ApprovalBoundaries
- ExpertReviewWorkbook
- ExpertReviewMaps
- OfflineReviewerConsole
- ReviewerConsoleBoards
- TerminalReviewGovernanceBinder
- ReviewCriteria
- ReviewEvidence
- ReviewIssues
- ReviewEscalation
- ReviewNonGoals
- ReviewNoGoSafeGo
- ReviewExceptions
- ReviewGaps
- ReviewRisks
- ReviewReadinessScoring
- ReviewValidation
- ReviewQuality

-> DistributionPackagingProfileRegistry
-> DistributionPackagingDomainRegistry
-> FinalLocalDistributionBundleRehearsal
-> DistributionBundleManifest
-> DistributionBundleFolderSourceOutputMaps
-> InclusionExclusionMatrices
-> PortableDocsBundle
-> OfflineReleaseFolderManifest
-> TerminalHandoverZipMap
-> FinalPackagingGovernanceBinder
-> PackagingCriteria
-> PackagingEvidence
-> PackagingIssues
-> PackagingHandoff
-> PackagingSourceOutputCommandMaps
-> PackagingNoGoSafeGo
-> PackagingExceptions
-> PackagingGaps
-> PackagingRisks
-> PackagingReadinessScoring
-> PackagingValidation
-> PackagingQuality
-> Local Distribution Packaging Outputs
