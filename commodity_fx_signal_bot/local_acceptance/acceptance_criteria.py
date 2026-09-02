import pandas as pd
from local_acceptance.acceptance_config import LocalAcceptanceProfile

def build_default_acceptance_criteria(profile: LocalAcceptanceProfile) -> pd.DataFrame:
    criteria = [
        "local-only scope documented",
        "non-use policy documented",
        "final synthesis present",
        "hardening present",
        "quality reports present",
        "evidence trail present",
        "command catalog safe",
        "no raw secret output",
        "no live/broker/deploy claim",
        "no investment advice claim"
    ]
    return pd.DataFrame([{"criteria": c, "type": "mandatory"} for c in criteria])

def build_acceptance_criteria_registry(profile: LocalAcceptanceProfile) -> tuple[pd.DataFrame, dict]:
    df = build_default_acceptance_criteria(profile)
    return df, summarize_acceptance_criteria(df)

def summarize_acceptance_criteria(criteria_df: pd.DataFrame) -> dict:
    return {"total_criteria": len(criteria_df)}
