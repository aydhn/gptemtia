"""Deprecation candidates."""
import pandas as pd
from .longterm_config import LocalLongTermOperationsProfile
from .longterm_models import DeprecationCandidate, build_deprecation_candidate_id, deprecation_candidate_to_dict

def build_default_deprecation_candidates(profile: LocalLongTermOperationsProfile) -> list[DeprecationCandidate]:
    return [
        DeprecationCandidate(
            candidate_id=build_deprecation_candidate_id("old_model", "ml"),
            candidate_name="old_model",
            candidate_area="ml",
            deprecation_status="deprecation_rehearsal_candidate",
            impact_note="low",
            manual_review_required=True,
            warnings=["Gerçek kaldırma kararı değildir."]
        )
    ]

def build_deprecation_candidate_registry(profile: LocalLongTermOperationsProfile) -> tuple[pd.DataFrame, dict]:
    items = build_default_deprecation_candidates(profile)
    df = pd.DataFrame([deprecation_candidate_to_dict(i) for i in items])
    return df, summarize_deprecation_candidates(df)

def summarize_deprecation_candidates(df: pd.DataFrame) -> dict:
    return {"total_items": len(df)}
