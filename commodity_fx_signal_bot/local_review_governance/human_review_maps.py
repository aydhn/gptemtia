import pandas as pd
from local_review_governance.review_config import LocalReviewGovernanceProfile
from local_review_governance.review_models import HumanReviewItem, build_human_review_item_id, human_review_item_to_dict

def build_default_human_review_items(profile: LocalReviewGovernanceProfile) -> list[HumanReviewItem]:
    return [
        HumanReviewItem(
            review_id=build_human_review_item_id("Safety", "Safety Review"),
            review_area="Safety",
            review_title="Safety Review",
            review_status="review_rehearsal_needs_manual_review",
            reviewer_role="reviewer_operator",
            target_ref="docs/SAFE_USAGE_GUIDE.md",
            manual_review_required=True,
            warnings=["Not real safety approval"]
        )
    ]

def build_human_review_cockpit_route_map(profile: LocalReviewGovernanceProfile) -> tuple[pd.DataFrame, dict]:
    items = build_default_human_review_items(profile)
    df = pd.DataFrame([human_review_item_to_dict(i) for i in items])
    return df, summarize_human_review_map(df)

def build_human_review_cockpit_status_matrix(profile: LocalReviewGovernanceProfile) -> tuple[pd.DataFrame, dict]:
    items = build_default_human_review_items(profile)
    df = pd.DataFrame([human_review_item_to_dict(i) for i in items])
    return df, summarize_human_review_map(df)

def summarize_human_review_map(df: pd.DataFrame) -> dict:
    return {"total_items": len(df)}
