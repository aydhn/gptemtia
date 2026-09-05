from pathlib import Path
import pandas as pd
from local_completion_governance.completion_config import LocalCompletionGovernanceProfile
from local_completion_governance.completion_models import AcceptanceEvidenceItem, build_acceptance_evidence_item_id, acceptance_evidence_item_to_dict

def build_default_acceptance_evidence_items(profile: LocalCompletionGovernanceProfile) -> list[AcceptanceEvidenceItem]:
    return [
        AcceptanceEvidenceItem(
            evidence_id=build_acceptance_evidence_item_id("General", "Evidence"),
            evidence_area="General",
            evidence_title="Evidence",
            source_ref="Source",
            output_ref="Output",
            acceptance_status="acceptance_rehearsal_documented_only",
            warnings=["Not an official acceptance."]
        )
    ]

def build_acceptance_evidence_source_map(project_root: Path, profile: LocalCompletionGovernanceProfile) -> tuple[pd.DataFrame, dict]:
    items = build_default_acceptance_evidence_items(profile)
    df = pd.DataFrame([acceptance_evidence_item_to_dict(i) for i in items])
    return df, summarize_acceptance_evidence_map(df)

def build_acceptance_evidence_output_map(profile: LocalCompletionGovernanceProfile) -> tuple[pd.DataFrame, dict]:
    items = build_default_acceptance_evidence_items(profile)
    df = pd.DataFrame([acceptance_evidence_item_to_dict(i) for i in items])
    return df, summarize_acceptance_evidence_map(df)

def build_acceptance_evidence_command_map(profile: LocalCompletionGovernanceProfile) -> tuple[pd.DataFrame, dict]:
    items = build_default_acceptance_evidence_items(profile)
    df = pd.DataFrame([acceptance_evidence_item_to_dict(i) for i in items])
    return df, summarize_acceptance_evidence_map(df)

def build_acceptance_evidence_limitation_register(profile: LocalCompletionGovernanceProfile) -> tuple[pd.DataFrame, dict]:
    items = build_default_acceptance_evidence_items(profile)
    df = pd.DataFrame([acceptance_evidence_item_to_dict(i) for i in items])
    return df, summarize_acceptance_evidence_map(df)

def build_acceptance_evidence_non_approval_registry(profile: LocalCompletionGovernanceProfile) -> tuple[pd.DataFrame, dict]:
    items = build_default_acceptance_evidence_items(profile)
    df = pd.DataFrame([acceptance_evidence_item_to_dict(i) for i in items])
    return df, summarize_acceptance_evidence_map(df)

def summarize_acceptance_evidence_map(df: pd.DataFrame) -> dict:
    return {"total_items": len(df)}\n