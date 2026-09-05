
import pandas as pd
from .macro_provider_config import MacroProviderProfile

def build_default_macro_frequency_unit_requirements(profile: MacroProviderProfile) -> pd.DataFrame:
    reqs = [
        {"indicator_category": "macro_inflation", "expected_frequency": "monthly", "allowed_frequency_variants": ["quarterly"], "expected_unit": "percent", "allowed_unit_variants": ["index"], "normalization_note": "", "future_phase_owner": "Phase 113", "manual_review_required": True}
    ]
    return pd.DataFrame(reqs)

def build_macro_frequency_unit_normalization_requirement_registry(profile: MacroProviderProfile) -> tuple[pd.DataFrame, dict]:
    df = build_default_macro_frequency_unit_requirements(profile)
    return df, summarize_macro_frequency_unit_requirements(df)

def summarize_macro_frequency_unit_requirements(df: pd.DataFrame) -> dict:
    return {"total_requirements": len(df)}
