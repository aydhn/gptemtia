import pandas as pd
from local_final_closing.final_closing_config import LocalFinalClosingProfile
from local_final_closing.final_closing_models import NonProductionSealItem, build_non_production_seal_item_id, non_production_seal_item_to_dict

def build_default_non_production_seal_items(profile: LocalFinalClosingProfile) -> list[NonProductionSealItem]:
    return [
        NonProductionSealItem(
            seal_id=build_non_production_seal_item_id("core", "seal"),
            seal_area="core",
            seal_title="seal",
            seal_status="non_production_seal_documented_only",
            boundary_note="Not an official seal",
            manual_review_required=True,
            warnings=["no official seal", "no official production approval", "no legal sign-off", "no compliance approval", "no broker readiness", "no live trading approval", "no release approval", "no build attestation", "no investment advice", "no official acceptance"]
        )
    ]

def build_non_production_seal_criteria_registry(profile: LocalFinalClosingProfile) -> tuple[pd.DataFrame, dict]:
    items = build_default_non_production_seal_items(profile)
    df = pd.DataFrame([non_production_seal_item_to_dict(i) for i in items])
    return df, summarize_non_production_seal_map(df)

def build_non_production_seal_boundary_registry(profile: LocalFinalClosingProfile) -> tuple[pd.DataFrame, dict]:
    items = build_default_non_production_seal_items(profile)
    df = pd.DataFrame([non_production_seal_item_to_dict(i) for i in items])
    return df, summarize_non_production_seal_map(df)

def build_non_production_seal_non_seal_registry(profile: LocalFinalClosingProfile) -> tuple[pd.DataFrame, dict]:
    items = build_default_non_production_seal_items(profile)
    df = pd.DataFrame([non_production_seal_item_to_dict(i) for i in items])
    return df, summarize_non_production_seal_map(df)

def build_non_production_seal_limitation_register(profile: LocalFinalClosingProfile) -> tuple[pd.DataFrame, dict]:
    items = build_default_non_production_seal_items(profile)
    df = pd.DataFrame([non_production_seal_item_to_dict(i) for i in items])
    return df, summarize_non_production_seal_map(df)

def build_non_production_seal_manual_review_ledger(profile: LocalFinalClosingProfile) -> tuple[pd.DataFrame, dict]:
    items = build_default_non_production_seal_items(profile)
    df = pd.DataFrame([non_production_seal_item_to_dict(i) for i in items])
    return df, summarize_non_production_seal_map(df)

def summarize_non_production_seal_map(df: pd.DataFrame) -> dict:
    return {"total_items": len(df) if df is not None else 0}
