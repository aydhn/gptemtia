import pandas as pd
from typing import Tuple, Dict
from .archive_config import LocalArchiveProfile

def build_archive_risk_summary(gap_df: pd.DataFrame, boundary_df: pd.DataFrame, verification_df: pd.DataFrame, profile: LocalArchiveProfile) -> Tuple[pd.DataFrame, Dict]:
    risks = []
    if not verification_df.empty:
        for _, row in verification_df.iterrows():
            risks.append({"risk_type": "secret_mismatch", "risk_level": "archive_critical_risk"})
    if not gap_df.empty:
        for _, row in gap_df.iterrows():
            risks.append({"risk_type": row.get('gap_type', 'unknown_gap'), "risk_level": "archive_medium_risk"})
    df = pd.DataFrame(risks)
    return df, {"total_risks_identified": len(df)}
