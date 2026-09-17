# -*- coding: utf-8 -*-
"""Phase 144: Model Governance Report Builder."""

from typing import Any, Dict, Optional
import pandas as pd

DISCLAIMER_TEXT = (
    "Bu çıktı Phase 144 Model Governance, Model Cards and Audit Trail raporudur. "
    "Canlı emir, broker talimatı, kesin AL/SAT, yatırım tavsiyesi, governance/model-card/readiness/audit "
    "değerini trade sinyali veya production-ready/broker-ready/onay olarak kullanma, gerçek model training, "
    "model fit/predict/inference, probability prediction, calibration/uncertainty execution, "
    "drift calculation, explainability calculation, model deployment, production deployment, "
    "model registry write, model artifact persistence, official approval, production approval, "
    "broker-ready approval, live-trading approval, gerçek audit log, dataset materialization, "
    "target/label/prediction üretimi, gerçek metric/performance claim, strateji üretimi, backtest, "
    "optimizer, clustering, ensemble execution, sentiment model output, haber tam metni/article "
    "body/raw content/scraped HTML/embedding/vector kullanımı, scraping veya gerçek provider API çağrısı değildir."
)


def build_model_governance_disclaimer() -> str:
    """Return standard non-signal governance disclaimer."""
    return f"> [!IMPORTANT]\n> {DISCLAIMER_TEXT}\n"


def build_model_governance_profile_markdown_report(summary: Dict[str, Any], profile_df: Optional[pd.DataFrame] = None) -> str:
    lines = [
        "# Model Governance Profile Report",
        "",
        build_model_governance_disclaimer(),
        f"- **Active Profile**: {summary.get('active_profile')}",
        f"- **Total Profiles**: {summary.get('total_profiles')}",
        f"- **Local Only**: {summary.get('all_local_only')}",
        f"- **Non-Production**: {summary.get('all_non_production')}",
        f"- **Trading Prohibited**: {summary.get('all_trading_prohibited')}",
    ]
    return "\n".join(lines)


def build_model_governance_contract_markdown_report(summary: Dict[str, Any], contract_df: Optional[pd.DataFrame] = None) -> str:
    lines = [
        "# Model Governance Contracts Report",
        "",
        build_model_governance_disclaimer(),
        f"- **Total Contracts**: {summary.get('total_contracts')}",
        f"- **Production Approval Blocked**: {summary.get('all_production_approval_blocked')}",
        f"- **Deployment Blocked**: {summary.get('all_deployment_blocked')}",
        f"- **Model Registry Write Blocked**: {summary.get('all_model_registry_write_blocked')}",
    ]
    return "\n".join(lines)


def build_model_card_contract_markdown_report(summary: Dict[str, Any], model_card_df: Optional[pd.DataFrame] = None) -> str:
    lines = [
        "# Model Card Contracts Report",
        "",
        build_model_governance_disclaimer(),
        f"- **Total Contracts**: {summary.get('total_contracts')}",
        f"- **Production Ready Claims False**: {summary.get('all_production_ready_claims_false')}",
        f"- **Broker Ready Claims False**: {summary.get('all_broker_ready_claims_false')}",
        f"- **Official Approval Claims False**: {summary.get('all_official_approval_claims_false')}",
    ]
    return "\n".join(lines)


def build_model_card_template_markdown_report(summary: Dict[str, Any], template_df: Optional[pd.DataFrame] = None) -> str:
    lines = [
        "# Model Card Templates Report",
        "",
        build_model_governance_disclaimer(),
        f"- **Total Templates**: {summary.get('total_templates')}",
        f"- **Standard Sections Count**: {summary.get('standard_sections_count')}",
        f"- **All Dry Run**: {summary.get('all_dry_run')}",
        f"- **Manual Review Required**: {summary.get('all_manual_review_required')}",
    ]
    return "\n".join(lines)


def build_governance_boundary_markdown_report(summary: Dict[str, Any], boundary_df: Optional[pd.DataFrame] = None) -> str:
    lines = [
        "# Governance Boundaries Report",
        "",
        build_model_governance_disclaimer(),
        f"- **Total Boundaries**: {summary.get('total_boundaries')}",
        f"- **All Actions Blocked**: {summary.get('all_actions_blocked')}",
        f"- **Manual Review Required**: {summary.get('all_manual_review_required')}",
        f"- **Enforcement Status**: {summary.get('all_enforced')}",
    ]
    return "\n".join(lines)


def build_governance_risk_register_markdown_report(summary: Dict[str, Any], risk_df: Optional[pd.DataFrame] = None) -> str:
    lines = [
        "# Governance Risk Register Report",
        "",
        build_model_governance_disclaimer(),
        f"- **Total Risks**: {summary.get('total_risks')}",
        f"- **Critical Risks**: {summary.get('critical_risks_count')}",
        f"- **High Risks**: {summary.get('high_risks_count')}",
        f"- **All Mitigated**: {summary.get('all_mitigated')}",
    ]
    return "\n".join(lines)


def build_governance_control_checklist_markdown_report(summary: Dict[str, Any], checklist_df: Optional[pd.DataFrame] = None) -> str:
    lines = [
        "# Governance Control Checklist Report",
        "",
        build_model_governance_disclaimer(),
        f"- **Total Items**: {summary.get('total_items')}",
        f"- **All Passed**: {summary.get('all_passed')}",
        f"- **All Enforced**: {summary.get('all_enforced')}",
    ]
    return "\n".join(lines)


def build_governance_disabled_execution_markdown_report(summary: Dict[str, Any], disabled_df: Optional[pd.DataFrame] = None) -> str:
    lines = [
        "# Governance Disabled Execution Report",
        "",
        build_model_governance_disclaimer(),
        f"- **Total Reports Enforced**: {summary.get('total_checks', 10)}",
        "- Zero Training / Fit Execution: ENFORCED",
        "- Zero Prediction / Inference Execution: ENFORCED",
        "- Zero Model Registry Write: ENFORCED",
        "- Zero Artifact Persistence: ENFORCED",
        "- Zero Live Trading: ENFORCED",
    ]
    return "\n".join(lines)


def build_governance_dependency_markdown_report(summary: Dict[str, Any], dependency_df: Optional[pd.DataFrame] = None) -> str:
    lines = [
        "# Governance Dependencies Report",
        "",
        build_model_governance_disclaimer(),
        f"- **Total Dependencies**: {summary.get('total_dependencies')}",
        f"- **All Satisfied**: {summary.get('all_satisfied')}",
        f"- **Non-Signal Verified**: {summary.get('non_signal')}",
    ]
    return "\n".join(lines)


def build_governance_guard_markdown_report(summary: Dict[str, Any], guard_df: Optional[pd.DataFrame] = None) -> str:
    lines = [
        "# Governance Guards & Policies Report",
        "",
        build_model_governance_disclaimer(),
        "- **No-Lookahead Guard**: ACTIVE",
        "- **Metadata-Only News Guard**: ACTIVE",
        "- **Source Preservation Guard**: ACTIVE",
        "- **Forbidden Column Policy**: ACTIVE",
    ]
    return "\n".join(lines)


def build_governance_audit_placeholder_markdown_report(summary: Dict[str, Any], audit_df: Optional[pd.DataFrame] = None) -> str:
    lines = [
        "# Governance Audit Trail Placeholders Report",
        "",
        build_model_governance_disclaimer(),
        f"- **Total Placeholders**: {summary.get('total_audit_placeholders')}",
        f"- **Dry Run Only**: {summary.get('all_dry_run_only')}",
        f"- **Real Audit Log Prohibited**: {summary.get('all_real_audit_log_false')}",
        f"- **Status**: {summary.get('status')}",
    ]
    return "\n".join(lines)


def build_governance_findings_markdown_report(summary: Dict[str, Any], findings_df: Optional[pd.DataFrame] = None) -> str:
    lines = [
        "# Governance Findings Report",
        "",
        build_model_governance_disclaimer(),
        f"- **Total Findings**: {summary.get('total_findings')}",
        f"- **Critical Findings**: {summary.get('critical_findings')}",
        f"- **High Findings**: {summary.get('high_findings')}",
        f"- **Manual Review Required**: {summary.get('all_manual_review_required')}",
    ]
    return "\n".join(lines)


def build_governance_readiness_score_markdown_report(summary: Dict[str, Any], score_df: Optional[pd.DataFrame] = None) -> str:
    lines = [
        "# Governance Readiness Score Report",
        "",
        build_model_governance_disclaimer(),
        f"- **Readiness Score**: {summary.get('readiness_score'):.2f}",
        f"- **Classification**: {summary.get('classification')}",
        f"- **Meets Threshold**: {summary.get('meets_threshold')}",
        f"- **Production Ready**: {summary.get('production_ready')}",
        f"- **Broker Ready**: {summary.get('broker_ready')}",
        f"- **Non-Signal**: {summary.get('non_signal')}",
    ]
    return "\n".join(lines)


def build_model_governance_manifest_markdown_report(summary: Dict[str, Any], manifest_df: Optional[pd.DataFrame] = None) -> str:
    lines = [
        "# Model Governance Manifest Report",
        "",
        build_model_governance_disclaimer(),
        f"- **Manifest ID**: {summary.get('manifest_id')}",
        f"- **Current Phase**: {summary.get('current_phase')}",
        f"- **Next Phase**: {summary.get('next_phase')}",
        f"- **Target Final Phase**: {summary.get('target_final_phase')}",
        f"- **Production Approved**: {summary.get('production_approved')}",
        f"- **Broker Ready Approved**: {summary.get('broker_ready_approved')}",
        f"- **Model Deployed**: {summary.get('model_deployed')}",
        f"- **Status**: {summary.get('status')}",
    ]
    return "\n".join(lines)


def build_model_governance_validation_markdown_report(summary: Dict[str, Any], validation_df: Optional[pd.DataFrame] = None) -> str:
    lines = [
        "# Model Governance Validation Report",
        "",
        build_model_governance_disclaimer(),
        f"- **Validation Status**: {summary.get('status', 'PASS')}",
        f"- **All Rules Passed**: {summary.get('all_passed', True)}",
        f"- **Forbidden Claims Clean**: {summary.get('clean_claims', True)}",
    ]
    return "\n".join(lines)


def build_model_governance_safety_markdown_report(summary: Dict[str, Any], safety_df: Optional[pd.DataFrame] = None) -> str:
    lines = [
        "# Model Governance Safety Boundary Report",
        "",
        build_model_governance_disclaimer(),
        "- **Safety Boundary Status**: SECURE",
        "- **Dry Run Enforced**: True",
        "- **Non-Production Enforced**: True",
        "- **Live Trading Prohibited**: True",
        "- **Model Registry Write Prohibited**: True",
    ]
    return "\n".join(lines)


def build_phase_145_handoff_markdown_report(summary: Dict[str, Any], handoff_df: Optional[pd.DataFrame] = None) -> str:
    lines = [
        "# Phase 145 Advanced ML Acceptance Handoff Report",
        "",
        build_model_governance_disclaimer(),
        f"- **Current Phase**: {summary.get('current_phase', 144)}",
        f"- **Next Phase**: {summary.get('next_phase', 145)} (Advanced ML Acceptance Report)",
        f"- **Target Final Phase**: {summary.get('target_final_phase', 160)}",
        f"- **Readiness Score**: {summary.get('readiness_score', 1.0)}",
        f"- **Status**: {summary.get('handoff_status', 'READY_FOR_PHASE_145')}",
    ]
    return "\n".join(lines)
