import pandas as pd
from pathlib import Path
from .runtime_config import AdvancedRuntimeProfile
from .runtime_models import RuntimeHealthFinding, build_runtime_health_finding_id

def build_default_runtime_health_findings(profile: AdvancedRuntimeProfile) -> pd.DataFrame:
    checks = [
        "settings importable", "paths importable", "DataLake importable",
        "FeatureStore importable", "report_builder importable",
        "advanced_continuation importable", "advanced_runtime importable",
        "scripts present", "tests present", "docs present",
        "no obvious forbidden command contract"
    ]
    items = []
    for c in checks:
        items.append(RuntimeHealthFinding(
            finding_id=build_runtime_health_finding_id(c),
            risk_label="runtime_info",
            title=c,
            description=f"Check if {c}",
            recommendation="Ensure available",
            manual_review_required=False
        ))
    return pd.DataFrame([i.to_dict() for i in items])

def build_runtime_health_check(project_root: Path, profile: AdvancedRuntimeProfile) -> tuple[pd.DataFrame, dict]:
    df = build_default_runtime_health_findings(profile)
    return df, summarize_runtime_health(df)

def summarize_runtime_health(df: pd.DataFrame) -> dict:
    if df.empty: return {"total": 0}
    return {"total_findings": len(df)}
