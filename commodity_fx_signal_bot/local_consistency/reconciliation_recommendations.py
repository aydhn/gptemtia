import pandas as pd

from local_consistency.consistency_config import LocalConsistencyProfile
from local_consistency.consistency_models import ReconciliationRecommendation


def build_reconciliation_recommendations(findings_df: pd.DataFrame, stale_plan_df: pd.DataFrame | None, profile: LocalConsistencyProfile) -> tuple[pd.DataFrame, dict]:
    return pd.DataFrame(), {"warnings": []}

def map_consistency_finding_to_recommendation(row: pd.Series, profile: LocalConsistencyProfile) -> ReconciliationRecommendation:
    from local_consistency.consistency_models import ReconciliationRecommendation
    return ReconciliationRecommendation(
        recommendation_id="dummy",
        finding_id=None,
        title="Dummy",
        description="Dummy",
        safe_action="no_action_needed",
        destructive=False,
        requires_manual_review=False,
        warnings=[]
    )

def summarize_reconciliation_recommendations(recommendations_df: pd.DataFrame) -> dict:
    return {}
