
import pandas as pd
from .macro_provider_config import MacroProviderProfile

def build_default_macro_revision_policy_requirements(profile: MacroProviderProfile) -> pd.DataFrame:
    reqs = [
        {"indicator_category": "macro_inflation", "revision_risk": "high", "vintage_data_needed": True, "previous_value_handling": "keep", "revised_value_handling": "append", "future_phase_owner": "Phase 113", "manual_review_required": True}
    ]
    return pd.DataFrame(reqs)

def build_macro_revision_policy_requirement_registry(profile: MacroProviderProfile) -> tuple[pd.DataFrame, dict]:
    df = build_default_macro_revision_policy_requirements(profile)
    return df, summarize_macro_revision_policy_requirements(df)

def summarize_macro_revision_policy_requirements(df: pd.DataFrame) -> dict:
    return {"total_requirements": len(df)}
