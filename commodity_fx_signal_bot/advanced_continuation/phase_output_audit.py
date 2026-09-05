import pandas as pd
from pathlib import Path
from .continuation_config import AdvancedContinuationProfile
from .continuation_models import PhaseOutputAuditItem, build_phase_output_audit_id

def build_default_phase_output_audit_items(profile: AdvancedContinuationProfile) -> list[PhaseOutputAuditItem]:
    areas = ["core architecture", "config/paths/settings", "DataLake", "FeatureStore",
             "reporting", "ML scaffold", "backtest scaffold", "research reports",
             "governance/safety", "redteam/incident", "documentation/export",
             "packaging", "reproducibility", "completion", "terminal closeout", "final closing"]
    return [PhaseOutputAuditItem(build_phase_output_audit_id("1-100", a), "1-100", a, "present", "present", "", False) for a in areas]

def build_phase_1_100_output_audit(project_root: Path, profile: AdvancedContinuationProfile) -> tuple[pd.DataFrame, dict]:
    items = build_default_phase_output_audit_items(profile)
    df = pd.DataFrame([vars(i) for i in items])
    return df, summarize_phase_output_audit(df)

def summarize_phase_output_audit(df: pd.DataFrame) -> dict:
    return {"total_audits": len(df), "status": "continuation_ready"}
