import pandas as pd
from local_review_governance.review_config import LocalReviewGovernanceProfile
from local_review_governance.review_models import ExpertReviewItem, build_expert_review_item_id, expert_review_item_to_dict

def build_default_expert_review_items(profile: LocalReviewGovernanceProfile) -> list[ExpertReviewItem]:
    areas = [
        "architecture review",
        "data/reports review",
        "safety boundary review",
        "governance review",
        "redteam/incident review",
        "quality/testing review",
        "release-candidate review",
        "longterm/review lifecycle",
        "completion/preservation/continuity/atlas review",
        "manual review only"
    ]
    items = []
    for a in areas:
        items.append(
            ExpertReviewItem(
                expert_review_id=build_expert_review_item_id(a, f"{a} ok?"),
                expert_area=a,
                reviewer_role="reviewer_external_expert_rehearsal",
                review_question=f"Is {a} aligned?",
                evidence_refs=[],
                manual_review_required=True,
                warnings=["Not official expert sign-off"]
            )
        )
    return items

def build_expert_review_workbook(profile: LocalReviewGovernanceProfile) -> tuple[pd.DataFrame, dict]:
    items = build_default_expert_review_items(profile)
    df = pd.DataFrame([expert_review_item_to_dict(i) for i in items])
    return df, summarize_expert_review_workbook(df)

def summarize_expert_review_workbook(df: pd.DataFrame) -> dict:
    return {"total_items": len(df)}
