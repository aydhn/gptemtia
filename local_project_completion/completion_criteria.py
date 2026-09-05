import pandas as pd
from .completion_models import CompletionCriterion, build_completion_criterion_id, completion_criterion_to_dict
from .completion_config import LocalProjectCompletionProfile

def build_default_completion_criteria(profile: LocalProjectCompletionProfile) -> list[CompletionCriterion]:
    return [
        CompletionCriterion(
            criterion_id=build_completion_criterion_id("live_trading_disabled", "safety"),
            criterion_name="live_trading_disabled",
            criterion_area="safety",
            audit_status="last_mile_audit_pass_rehearsal",
            evidence_refs=[],
            manual_review_required=True,
            warnings=["No live trading allowed."]
        )
    ]

def build_project_completion_criteria_matrix(profile: LocalProjectCompletionProfile) -> tuple[pd.DataFrame, dict]:
    crits = build_default_completion_criteria(profile)
    df = pd.DataFrame([completion_criterion_to_dict(c) for c in crits])
    return df, summarize_project_completion_criteria(df)

def summarize_project_completion_criteria(df: pd.DataFrame) -> dict:
    return {"criteria": len(df), "note": "Criteria is not official acceptance."}
