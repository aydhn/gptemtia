import pandas as pd
from local_completion_governance.completion_config import LocalCompletionGovernanceProfile
from local_completion_governance.completion_models import ClosureSynthesisItem, build_closure_synthesis_item_id, closure_synthesis_item_to_dict

def build_default_closure_synthesis_items(profile: LocalCompletionGovernanceProfile) -> list[ClosureSynthesisItem]:
    return [
        ClosureSynthesisItem(
            closure_id=build_closure_synthesis_item_id("Phase", "Phase Recap"),
            recap_area="Phase",
            recap_title="Phase Recap",
            source_ref="Phase Log",
            status_label="completion_rehearsal_ready",
            manual_review_required=True,
            warnings=["Not official project closure."]
        )
    ]

def build_closure_synthesis_phase_recap_map(profile: LocalCompletionGovernanceProfile) -> tuple[pd.DataFrame, dict]:
    items = build_default_closure_synthesis_items(profile)
    df = pd.DataFrame([closure_synthesis_item_to_dict(i) for i in items])
    return df, summarize_closure_synthesis_map(df)

def build_closure_synthesis_module_recap_map(profile: LocalCompletionGovernanceProfile) -> tuple[pd.DataFrame, dict]:
    items = build_default_closure_synthesis_items(profile)
    df = pd.DataFrame([closure_synthesis_item_to_dict(i) for i in items])
    return df, summarize_closure_synthesis_map(df)

def build_closure_synthesis_output_recap_map(profile: LocalCompletionGovernanceProfile) -> tuple[pd.DataFrame, dict]:
    items = build_default_closure_synthesis_items(profile)
    df = pd.DataFrame([closure_synthesis_item_to_dict(i) for i in items])
    return df, summarize_closure_synthesis_map(df)

def build_closure_synthesis_safety_recap_map(profile: LocalCompletionGovernanceProfile) -> tuple[pd.DataFrame, dict]:
    items = build_default_closure_synthesis_items(profile)
    df = pd.DataFrame([closure_synthesis_item_to_dict(i) for i in items])
    return df, summarize_closure_synthesis_map(df)

def summarize_closure_synthesis_map(df: pd.DataFrame) -> dict:
    return {"total_items": len(df)}
