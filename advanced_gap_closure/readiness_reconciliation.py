import pandas as pd
from .gap_closure_config import FunctionalGapClosureProfile
from .gap_closure_models import ReadinessReconciliationItem, build_readiness_reconciliation_id, to_dict

def build_default_readiness_reconciliation_items(profile: FunctionalGapClosureProfile) -> list[ReadinessReconciliationItem]:
    areas = ["Phase 101 roadmap readiness", "Phase 102 runtime readiness", "Phase 103 research engine interface readiness", "Phase 104 config profile readiness", "DataLake readiness", "FeatureStore readiness", "report builder readiness", "script command readiness", "safety/no-go readiness", "Phase 106 data foundation readiness"]
    items = []
    for area in areas:
        items.append(ReadinessReconciliationItem(
            reconciliation_id=build_readiness_reconciliation_id(area, "101-104"),
            foundation_area=area,
            source_phase_range="101-104",
            current_state="ready",
            target_state="ready",
            reconciliation_status="gap_closed",
            warnings=[],
            manual_review_required=False
        ))
    return items

def build_advanced_readiness_reconciliation_registry(profile: FunctionalGapClosureProfile) -> tuple[pd.DataFrame, dict]:
    items = build_default_readiness_reconciliation_items(profile)
    df = pd.DataFrame([to_dict(i) for i in items])
    summary = summarize_readiness_reconciliation(df)
    return df, summary

def summarize_readiness_reconciliation(df: pd.DataFrame) -> dict:
    return {"total_items": len(df)}
