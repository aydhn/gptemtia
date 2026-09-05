import pandas as pd
from .completion_config import LocalProjectCompletionProfile
from .completion_models import CompletionHandoffItem, build_completion_handoff_item_id, completion_handoff_item_to_dict

def build_default_handoff_items(role: str, profile: LocalProjectCompletionProfile) -> list[CompletionHandoffItem]:
    return [
        CompletionHandoffItem(
            handoff_id=build_completion_handoff_item_id(role, "offline_ready"),
            handoff_role=role,
            handoff_area="offline_ready",
            status_label="completion_rehearsal_needs_manual_review",
            boundary_note="Not for production.",
            manual_review_required=True,
            warnings=["No production approval."]
        )
    ]

def build_final_operator_handoff_checklist(profile: LocalProjectCompletionProfile) -> tuple[pd.DataFrame, dict]:
    items = build_default_handoff_items("operator", profile)
    df = pd.DataFrame([completion_handoff_item_to_dict(i) for i in items])
    return df, summarize_final_handoff_checklist(df)

def build_final_analyst_handoff_checklist(profile: LocalProjectCompletionProfile) -> tuple[pd.DataFrame, dict]:
    items = build_default_handoff_items("analyst", profile)
    df = pd.DataFrame([completion_handoff_item_to_dict(i) for i in items])
    return df, summarize_final_handoff_checklist(df)

def build_final_maintainer_handoff_checklist(profile: LocalProjectCompletionProfile) -> tuple[pd.DataFrame, dict]:
    items = build_default_handoff_items("maintainer", profile)
    df = pd.DataFrame([completion_handoff_item_to_dict(i) for i in items])
    return df, summarize_final_handoff_checklist(df)

def build_final_codex_agent_handoff_checklist(profile: LocalProjectCompletionProfile) -> tuple[pd.DataFrame, dict]:
    items = build_default_handoff_items("codex_agent", profile)
    df = pd.DataFrame([completion_handoff_item_to_dict(i) for i in items])
    return df, summarize_final_handoff_checklist(df)

def summarize_final_handoff_checklist(df: pd.DataFrame) -> dict:
    return {"items": len(df), "note": "Handoff checklist is not real sign-off."}
