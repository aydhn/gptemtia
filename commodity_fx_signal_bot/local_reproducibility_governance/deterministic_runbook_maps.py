"""Deterministic runbook maps."""
import pandas as pd
from .reproducibility_config import LocalReproducibilityGovernanceProfile
from .reproducibility_models import DeterministicRunbookItem, build_deterministic_runbook_item_id, deterministic_runbook_item_to_dict

def build_deterministic_command_sequence_registry(profile: LocalReproducibilityGovernanceProfile) -> tuple[pd.DataFrame, dict]:
    items = build_default_deterministic_runbook_items(profile)
    df = pd.DataFrame([deterministic_runbook_item_to_dict(i) for i in items])
    return df, summarize_deterministic_runbook_map(df)

def build_deterministic_output_expectation_registry(profile: LocalReproducibilityGovernanceProfile) -> tuple[pd.DataFrame, dict]:
    items = build_default_deterministic_runbook_items(profile)
    df = pd.DataFrame([deterministic_runbook_item_to_dict(i) for i in items])
    return df, summarize_deterministic_runbook_map(df)

def build_deterministic_rerun_checklist(profile: LocalReproducibilityGovernanceProfile) -> tuple[pd.DataFrame, dict]:
    items = build_default_deterministic_runbook_items(profile)
    df = pd.DataFrame([deterministic_runbook_item_to_dict(i) for i in items])
    return df, summarize_deterministic_runbook_map(df)

def build_deterministic_rerun_boundary_registry(profile: LocalReproducibilityGovernanceProfile) -> tuple[pd.DataFrame, dict]:
    items = build_default_deterministic_runbook_items(profile)
    df = pd.DataFrame([deterministic_runbook_item_to_dict(i) for i in items])
    return df, summarize_deterministic_runbook_map(df)

def build_default_deterministic_runbook_items(profile: LocalReproducibilityGovernanceProfile) -> list[DeterministicRunbookItem]:
    return [
        DeterministicRunbookItem(
            runbook_id=build_deterministic_runbook_item_id("cmd", "ref"),
            command_family="cmd",
            command_ref="ref",
            expected_output_family="out",
            determinism_label="deterministic_rehearsal_available",
            manual_review_required=True,
            warnings=["Determinism guarantee degildir.", "Komut calistirmaz."]
        )
    ]

def summarize_deterministic_runbook_map(df: pd.DataFrame) -> dict:
    return {"items": len(df)}
