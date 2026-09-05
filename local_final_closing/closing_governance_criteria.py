import pandas as pd
from local_final_closing.final_closing_config import LocalFinalClosingProfile

def build_default_closing_governance_criteria(profile: LocalFinalClosingProfile) -> pd.DataFrame:
    return pd.DataFrame([
        {"criterion": "final master terminal lock rehearsal available", "met": True},
        {"criterion": "project constitution available", "met": True},
        {"criterion": "non-production seal rehearsal available", "met": True},
        {"criterion": "terminal archive index available", "met": True},
        {"criterion": "closing super-binder available", "met": True},
        {"criterion": "no official lock/constitution/seal/archive/handover", "met": True},
        {"criterion": "no production approval", "met": True},
        {"criterion": "no live/broker/advice", "met": True},
        {"criterion": "no build/deploy/release/archive", "met": True},
        {"criterion": "manual review required", "met": True}
    ])

def build_closing_governance_final_criteria_matrix(profile: LocalFinalClosingProfile) -> tuple[pd.DataFrame, dict]:
    df = build_default_closing_governance_criteria(profile)
    return df, summarize_closing_governance_criteria(df)

def summarize_closing_governance_criteria(df: pd.DataFrame) -> dict:
    return {"total_criteria": len(df)}
