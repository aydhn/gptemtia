import pandas as pd
from .governance_control_config import LocalGovernanceControlProfile

def build_default_governance_metrics(profile: LocalGovernanceControlProfile) -> pd.DataFrame:
    data = [
        {"metric_id": "M1", "metric_name": "Readiness Score", "is_real_kpi": False}
    ]
    return pd.DataFrame(data)

def build_governance_kpi_rehearsal_registry(profile: LocalGovernanceControlProfile) -> tuple[pd.DataFrame, dict]:
    data = [{"kpi": "Approval Rate Rehearsal", "target": "100%", "is_real_kpi": False}]
    df = pd.DataFrame(data)
    return df, {"total": len(df)}

def build_governance_metric_dictionary(profile: LocalGovernanceControlProfile) -> tuple[pd.DataFrame, dict]:
    df = build_default_governance_metrics(profile)
    return df, {"total": len(df)}

def summarize_governance_metrics(kpi_df: pd.DataFrame, metric_df: pd.DataFrame) -> dict:
    return {
        "kpi_count": len(kpi_df) if kpi_df is not None else 0,
        "metric_count": len(metric_df) if metric_df is not None else 0
    }
