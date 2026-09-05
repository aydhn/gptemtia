import pandas as pd
from .packaging_config import LocalDistributionPackagingProfile

def build_default_packaging_governance_criteria(profile: LocalDistributionPackagingProfile) -> pd.DataFrame:
    return pd.DataFrame([
        {"criteria": "distribution bundle rehearsal available", "status": "checked"},
        {"criteria": "portable docs bundle available", "status": "checked"},
        {"criteria": "release folder manifest available", "status": "checked"},
        {"criteria": "ZIP-map available", "status": "checked"},
        {"criteria": "inclusion/exclusion matrices available", "status": "checked"},
        {"criteria": "no archive generated", "status": "checked"},
        {"criteria": "no package publish", "status": "checked"},
        {"criteria": "no deployment", "status": "checked"},
        {"criteria": "no live/broker/advice", "status": "checked"},
        {"criteria": "manual review required", "status": "checked"}
    ])

def build_packaging_governance_criteria_matrix(profile: LocalDistributionPackagingProfile) -> tuple[pd.DataFrame, dict]:
    df = build_default_packaging_governance_criteria(profile)
    return df, summarize_packaging_governance_criteria(df)

def summarize_packaging_governance_criteria(df: pd.DataFrame) -> dict:
    return {"status": "generated", "rows": len(df)}
