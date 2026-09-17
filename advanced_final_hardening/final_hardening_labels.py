# -*- coding: utf-8 -*-
"""Phase 159: Final Hardening Labels.

Defines standardized domain, status, and execution labels for Phase 159.
Enforces contract-only semantics and blocks all live trading/execution claims.
"""

# Domain Labels
FINAL_HARDENING_PROFILE_DOMAIN: str = "final_hardening_profile_domain"
FINAL_HARDENING_DOMAIN: str = "final_hardening_domain"
FINAL_HARDENING_SCOPE_DOMAIN: str = "final_hardening_scope_domain"
FINAL_HARDENING_CONTRACT_DOMAIN: str = "final_hardening_contract_domain"
OPERATOR_RUNBOOK_DOMAIN: str = "operator_runbook_domain"
RELEASE_CANDIDATE_DOMAIN: str = "release_candidate_domain"
CONFIGURATION_FREEZE_DOMAIN: str = "configuration_freeze_domain"
DOCUMENTATION_FREEZE_DOMAIN: str = "documentation_freeze_domain"
SAFETY_FREEZE_DOMAIN: str = "safety_freeze_domain"
VALIDATION_FREEZE_DOMAIN: str = "validation_freeze_domain"
DEPENDENCY_FREEZE_DOMAIN: str = "dependency_freeze_domain"
MANIFEST_FREEZE_DOMAIN: str = "manifest_freeze_domain"
REPORT_FREEZE_DOMAIN: str = "report_freeze_domain"
SETTINGS_AUDIT_DOMAIN: str = "settings_audit_domain"
ENV_TEMPLATE_AUDIT_DOMAIN: str = "env_template_audit_domain"
PATHS_AUDIT_DOMAIN: str = "paths_audit_domain"
INVENTORY_DOMAIN: str = "inventory_domain"
OPERATOR_PROTOCOL_DOMAIN: str = "operator_protocol_domain"
TROUBLESHOOTING_DOMAIN: str = "troubleshooting_domain"
RECOVERY_DOMAIN: str = "recovery_domain"
NO_GO_PROTOCOL_DOMAIN: str = "no_go_protocol_domain"
SAFE_USAGE_PROTOCOL_DOMAIN: str = "safe_usage_protocol_domain"
RELEASE_CANDIDATE_CHECKPOINT_DOMAIN: str = "release_candidate_checkpoint_domain"
RELEASE_CANDIDATE_BOUNDARY_DOMAIN: str = "release_candidate_boundary_domain"
BLOCKER_DOMAIN: str = "blocker_domain"
GAP_DOMAIN: str = "gap_domain"
WARNING_DOMAIN: str = "warning_domain"
FINDING_DOMAIN: str = "finding_domain"
READINESS_SCORE_DOMAIN: str = "readiness_score_domain"
MANIFEST_DOMAIN: str = "manifest_domain"
HEALTH_DOMAIN: str = "health_domain"
VALIDATION_DOMAIN: str = "validation_domain"
SAFETY_DOMAIN: str = "safety_domain"
PHASE_160_HANDOFF_DOMAIN: str = "phase_160_handoff_domain"

# Status Labels
FINAL_HARDENING_CONTRACT_READY: str = "final_hardening_contract_ready"
FINAL_HARDENING_READY_WITH_WARNINGS: str = "final_hardening_ready_with_warnings"
FINAL_HARDENING_MANUAL_REVIEW_REQUIRED: str = "final_hardening_manual_review_required"
FINAL_HARDENING_BLOCKED_BY_SAFETY: str = "final_hardening_blocked_by_safety"
RELEASE_CANDIDATE_CONTRACT_READY: str = "release_candidate_contract_ready"
OPERATOR_RUNBOOK_CONTRACT_READY: str = "operator_runbook_contract_ready"
FINAL_HARDENING_CONTRACT_ONLY: str = "final_hardening_contract_only"
FINAL_HARDENING_UNKNOWN: str = "final_hardening_unknown"

# Execution Labels (Always Blocked / Contract Only)
EXECUTION_BLOCKED_NO_SYSTEM_EXECUTION: str = "execution_blocked_no_system_execution"
EXECUTION_BLOCKED_NO_END_TO_END_RUN: str = "execution_blocked_no_end_to_end_run"
EXECUTION_BLOCKED_NO_RELEASE_DEPLOYMENT: str = "execution_blocked_no_release_deployment"
EXECUTION_BLOCKED_NO_PRODUCTION_DEPLOYMENT: str = "execution_blocked_no_production_deployment"
EXECUTION_BLOCKED_NO_LIVE_TRADING: str = "execution_blocked_no_live_trading"
EXECUTION_BLOCKED_NO_BROKER: str = "execution_blocked_no_broker"
EXECUTION_BLOCKED_NO_ORDER_GENERATION: str = "execution_blocked_no_order_generation"
EXECUTION_BLOCKED_NO_SIGNAL_GENERATION: str = "execution_blocked_no_signal_generation"
EXECUTION_BLOCKED_NO_MODEL_TRAINING: str = "execution_blocked_no_model_training"
EXECUTION_BLOCKED_NO_PREDICTION: str = "execution_blocked_no_prediction"
EXECUTION_BLOCKED_NO_MODEL_REGISTRY_WRITE: str = "execution_blocked_no_model_registry_write"
EXECUTION_BLOCKED_NO_ARTIFACT_PERSISTENCE: str = "execution_blocked_no_artifact_persistence"
EXECUTION_CONTRACT_ONLY: str = "execution_contract_only"

# Standard Collections
ALL_FINAL_HARDENING_DOMAINS = [
    FINAL_HARDENING_PROFILE_DOMAIN,
    FINAL_HARDENING_DOMAIN,
    FINAL_HARDENING_SCOPE_DOMAIN,
    FINAL_HARDENING_CONTRACT_DOMAIN,
    OPERATOR_RUNBOOK_DOMAIN,
    RELEASE_CANDIDATE_DOMAIN,
    CONFIGURATION_FREEZE_DOMAIN,
    DOCUMENTATION_FREEZE_DOMAIN,
    SAFETY_FREEZE_DOMAIN,
    VALIDATION_FREEZE_DOMAIN,
    DEPENDENCY_FREEZE_DOMAIN,
    MANIFEST_FREEZE_DOMAIN,
]

ALL_FINAL_HARDENING_PROFILES = [
    "balanced_final_hardening_operator_runbook_contracts",
    "strict_non_production_hardening_and_freeze_safety",
    "offline_release_candidate_readiness_audit",
]

ALL_FINAL_HARDENING_METRICS = [
    "readiness_score",
    "checkpoint_pass_rate",
    "boundary_enforcement_rate",
    "freeze_compliance_rate",
    "inventory_coverage_rate",
    "audit_success_rate",
    "validation_pass_rate",
    "health_check_rate",
    "blocker_resolution_rate",
    "gap_reconciliation_rate",
    "warning_acknowledgement_rate",
]

ALL_FINAL_HARDENING_STATUSES = [
    FINAL_HARDENING_CONTRACT_READY,
    FINAL_HARDENING_READY_WITH_WARNINGS,
    FINAL_HARDENING_MANUAL_REVIEW_REQUIRED,
    FINAL_HARDENING_BLOCKED_BY_SAFETY,
    RELEASE_CANDIDATE_CONTRACT_READY,
    OPERATOR_RUNBOOK_CONTRACT_READY,
]

ALL_OPERATOR_RUNBOOK_NAMES = [
    "system_startup_verification",
    "graceful_offline_shutdown",
    "offline_configuration_audit",
    "local_data_integrity_check",
    "offline_report_inspection",
    "subsystem_health_audit",
    "hardening_contract_validation",
    "diagnostic_and_troubleshooting",
    "safe_state_recovery",
    "no_go_violation_handling",
    "manual_review_sign_off",
    "safe_offline_usage_rules",
    "incident_response_isolation",
    "scheduled_offline_maintenance",
    "local_data_backup_snapshot",
    "local_state_recovery_rehearsal",
]

ALL_OPERATOR_RUNBOOK_DOMAINS = [
    "startup",
    "shutdown",
    "config_check",
    "data_check",
    "report_check",
    "health_check",
    "validation",
    "troubleshooting",
]

ALL_RELEASE_CANDIDATE_CHECKLIST_NAMES = [
    "component_freeze_verification",
    "dependency_lock_verification",
    "pipeline_contract_readiness",
    "safety_boundary_enforcement",
    "documentation_freeze_integrity",
    "cli_scripts_dry_run_validation",
    "test_suite_offline_compliance",
    "report_disclaimer_audit",
    "no_go_protocols_strict_enforcement",
    "go_boundaries_controlled_allowance",
    "critical_blockers_resolution",
    "functional_gaps_reconciliation",
    "operational_warnings_acknowledgement",
    "audit_findings_closure",
    "readiness_score_threshold_check",
    "final_manifest_verification",
]

ALL_RELEASE_CANDIDATE_GATES = [
    "freeze_gate",
    "dependency_gate",
    "contract_gate",
    "safety_gate",
    "documentation_gate",
    "script_gate",
    "test_gate",
    "manifest_gate",
]

ALL_RELEASE_CANDIDATE_NO_GO_BOUNDARIES = [
    "no_live_trading",
    "no_broker_api",
    "no_order_generation",
    "no_signal_generation",
    "no_investment_advice",
    "no_system_execution",
    "no_end_to_end_run",
    "no_release_deployment",
    "no_production_deployment",
    "no_model_training",
    "no_model_inference",
    "no_prediction_generation",
    "no_model_registry_write",
    "no_artifact_persistence",
    "no_web_scraping",
    "no_destructive_file_actions",
]

ALL_RELEASE_CANDIDATE_GO_BOUNDARIES = [
    "allow_offline_contract_inspection",
    "allow_local_profile_validation",
    "allow_runbook_documentation_reading",
    "allow_checklist_verification",
    "allow_freeze_audit_execution",
    "allow_script_inventory_inspection",
    "allow_test_inventory_inspection",
    "allow_docs_inventory_inspection",
    "allow_report_inventory_inspection",
    "allow_boundary_enforcement_check",
    "allow_dry_run_pipeline_check",
    "allow_health_check_inspection",
    "allow_validation_report_generation",
    "allow_readiness_scoring_calculation",
    "allow_release_candidate_manifest_generation",
    "allow_phase_160_handoff_preparation",
]

FINAL_HARDENING_DISCLAIMER: str = (
    "> [!WARNING]\n"
    "> **YASAL VE GÜVENLİK FERAGATNAMESİ (PHASE 159)**:\n"
    "> Bu çıktı Phase 159 Final Hardening, Operator Runbook and Release Candidate çıktısıdır. "
    "> Canlı emir, broker talimatı, kesin AL/SAT, yatırım tavsiyesi, final-hardening/release-candidate/readiness/runbook "
    "> değerini trade sinyali veya production-ready/broker-ready/onay olarak kullanma, gerçek full-system execution, "
    "> end-to-end bot run, live trading, broker execution, order generation, signal generation, model training, "
    "> model fit/predict/inference, target/label/prediction üretimi, backtest, benchmark, optimizer, portfolio construction, "
    "> risk reporting, scenario execution, metric calculation, release deployment, production deployment, model deployment, "
    "> model registry write, model artifact persistence, scraping, haber tam metni/article body/raw content/scraped HTML/"
    "> embedding/vector kullanımı veya gerçek provider API çağrısı değildir.\n"
)

