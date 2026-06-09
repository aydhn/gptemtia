import pandas as pd
from evidence_governance.evidence_config import EvidenceGovernanceProfile
from evidence_governance.evidence_models import ControlItem, build_control_id

def build_default_control_registry(profile: EvidenceGovernanceProfile) -> list[ControlItem]:
    controls = [
        ("live_order_absence_control", "safety_controls", "Canlı emir kodlarının bulunmaması", ["safety_evidence"]),
        ("broker_execution_absence_control", "safety_controls", "Broker bağlantısının bulunmaması", ["safety_evidence"]),
        ("investment_advice_absence_control", "safety_controls", "Yatırım tavsiyesi disclaimer'ı", ["documentation_evidence", "report_evidence"]),
        ("external_llm_absence_control", "safety_controls", "Harici LLM isteğinin olmaması", ["safety_evidence", "quality_evidence"]),
        ("web_scraping_absence_control", "operational_controls", "Scraping tool eksikliği", ["quality_evidence"]),
        ("secrets_redaction_control", "secrets_controls", "Secret maskeleme doğrulama raporları", ["secrets_hygiene_evidence"]),
        ("env_template_placeholder_control", "secrets_controls", ".env.example doğrulama", ["secrets_hygiene_evidence"]),
        ("gitignore_secret_exclusion_control", "secrets_controls", ".gitignore kontrolü", ["secrets_hygiene_evidence"]),
        ("backup_manifest_secret_exclusion_control", "backup_recovery_controls", "Backup'ta secret olmaması", ["backup_recovery_evidence", "secrets_hygiene_evidence"]),
        ("packaging_manifest_secret_exclusion_control", "packaging_controls", "Packaging'de secret olmaması", ["packaging_evidence", "secrets_hygiene_evidence"]),
        ("data_report_manifest_only_control", "packaging_controls", "Sadece manifest çıkması", ["packaging_evidence"]),
        ("quality_gate_report_presence_control", "quality_controls", "Quality gate raporlarının mevcudiyeti", ["quality_evidence"]),
        ("scenario_regression_report_presence_control", "scenario_regression_controls", "Regression rapor mevcudiyeti", ["scenario_regression_evidence"]),
        ("final_review_report_presence_control", "final_review_controls", "Final review rapor mevcudiyeti", ["final_review_evidence"]),
        ("documentation_index_presence_control", "documentation_controls", "Dokümantasyon indexinin olması", ["documentation_evidence"]),
        ("master_dry_run_plan_presence_control", "master_orchestration_controls", "Dry run planın olması", ["master_orchestration_evidence"]),
        ("recovery_runbook_presence_control", "backup_recovery_controls", "Recovery runbook mevcudiyeti", ["backup_recovery_evidence"]),
        ("reproducible_setup_guide_presence_control", "operational_controls", "Setup guide mevcudiyeti", ["packaging_evidence", "documentation_evidence"])
    ]

    registry = []
    for name, domain, desc, req_labels in controls:
        ctrl_id = build_control_id(name, domain)
        registry.append(ControlItem(
            control_id=ctrl_id,
            control_name=name,
            control_domain=domain,
            description=desc,
            required_evidence_labels=req_labels,
            optional_evidence_labels=[],
            status="control_unknown",
            warnings=[]
        ))

    return registry

def control_registry_to_dataframe(controls: list[ControlItem]) -> pd.DataFrame:
    from evidence_governance.evidence_models import control_item_to_dict
    if not controls:
        return pd.DataFrame()
    return pd.DataFrame([control_item_to_dict(c) for c in controls])

def validate_control_registry(control_df: pd.DataFrame, profile: EvidenceGovernanceProfile) -> dict:
    if control_df is None or control_df.empty:
        return {"passed": False, "warnings": ["Empty control registry"]}

    warnings = []

    # ensure required_evidence_labels exist
    if "required_evidence_labels" not in control_df.columns:
        warnings.append("Missing required_evidence_labels")

    return {"passed": len(warnings) == 0, "warnings": warnings}

def summarize_control_registry(control_df: pd.DataFrame) -> dict:
    if control_df is None or control_df.empty:
        return {"total_controls": 0}

    return {
        "total_controls": len(control_df),
        "domains": control_df["control_domain"].value_counts().to_dict() if "control_domain" in control_df.columns else {}
    }
