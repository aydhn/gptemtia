import pandas as pd
from local_review_governance.review_config import LocalReviewGovernanceProfile
from local_review_governance.review_models import ReviewerConsoleItem, build_reviewer_console_item_id, reviewer_console_item_to_dict

def build_default_reviewer_console_items(profile: LocalReviewGovernanceProfile) -> list[ReviewerConsoleItem]:
    return [
        ReviewerConsoleItem(
            console_id=build_reviewer_console_item_id("General", "Console Main"),
            console_area="General",
            console_title="Console Main",
            status_label="review_rehearsal_ready",
            target_ref="N/A",
            manual_action="Read offline",
            warnings=["No GUI"]
        )
    ]

def build_reviewer_console_status_board(profile: LocalReviewGovernanceProfile) -> tuple[pd.DataFrame, dict]:
    items = build_default_reviewer_console_items(profile)
    df = pd.DataFrame([reviewer_console_item_to_dict(i) for i in items])
    return df, summarize_reviewer_console_board(df)

def build_reviewer_console_warning_board(profile: LocalReviewGovernanceProfile) -> tuple[pd.DataFrame, dict]:
    df = pd.DataFrame([{"warning": "Not a dashboard"}])
    return df, summarize_reviewer_console_board(df)

def build_reviewer_console_manual_action_board(profile: LocalReviewGovernanceProfile) -> tuple[pd.DataFrame, dict]:
    df = pd.DataFrame([{"action": "manual review"}])
    return df, summarize_reviewer_console_board(df)

def summarize_reviewer_console_board(df: pd.DataFrame) -> dict:
    return {"total_items": len(df)}
