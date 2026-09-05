import pandas as pd
from local_completion_governance.completion_config import LocalCompletionGovernanceProfile
from local_completion_governance.completion_models import CertificationRehearsalItem, build_certification_rehearsal_item_id, certification_rehearsal_item_to_dict

def build_default_certification_rehearsal_items(profile: LocalCompletionGovernanceProfile) -> list[CertificationRehearsalItem]:
    return [
        CertificationRehearsalItem(
            certification_id=build_certification_rehearsal_item_id("General", "Criteria"),
            criteria_area="General",
            criteria_title="Criteria",
            rehearsal_status="certification_rehearsal_documented_only",
            boundary_note="No real certification.",
            evidence_refs=["None"],
            warnings=["Not a real certification."]
        )
    ]

def build_end_state_certification_criteria_registry(profile: LocalCompletionGovernanceProfile) -> tuple[pd.DataFrame, dict]:
    items = build_default_certification_rehearsal_items(profile)
    df = pd.DataFrame([certification_rehearsal_item_to_dict(i) for i in items])
    return df, summarize_end_state_certification_map(df)

def build_end_state_certification_boundary_registry(profile: LocalCompletionGovernanceProfile) -> tuple[pd.DataFrame, dict]:
    items = build_default_certification_rehearsal_items(profile)
    df = pd.DataFrame([certification_rehearsal_item_to_dict(i) for i in items])
    return df, summarize_end_state_certification_map(df)

def build_end_state_non_certification_registry(profile: LocalCompletionGovernanceProfile) -> tuple[pd.DataFrame, dict]:
    data = [
        {"claim": "no official certification"},
        {"claim": "no official acceptance"},
        {"claim": "no legal sign-off"},
        {"claim": "no compliance approval"},
        {"claim": "no production approval"},
        {"claim": "no broker readiness"},
        {"claim": "no live trading approval"},
        {"claim": "no investment advice"},
        {"claim": "no release approval"},
        {"claim": "no build attestation"}
    ]
    df = pd.DataFrame(data)
    return df, summarize_end_state_certification_map(df)

def build_end_state_certification_evidence_map(profile: LocalCompletionGovernanceProfile) -> tuple[pd.DataFrame, dict]:
    items = build_default_certification_rehearsal_items(profile)
    df = pd.DataFrame([certification_rehearsal_item_to_dict(i) for i in items])
    return df, summarize_end_state_certification_map(df)

def build_end_state_certification_limitation_register(profile: LocalCompletionGovernanceProfile) -> tuple[pd.DataFrame, dict]:
    items = build_default_certification_rehearsal_items(profile)
    df = pd.DataFrame([certification_rehearsal_item_to_dict(i) for i in items])
    return df, summarize_end_state_certification_map(df)

def summarize_end_state_certification_map(df: pd.DataFrame) -> dict:
    return {"total_items": len(df)}\n