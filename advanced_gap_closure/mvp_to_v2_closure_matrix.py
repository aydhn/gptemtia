import pandas as pd
from .gap_closure_config import FunctionalGapClosureProfile
from .gap_closure_models import ClosureMatrixItem, build_closure_matrix_id, to_dict

def build_default_closure_matrix_items(profile: FunctionalGapClosureProfile) -> list[ClosureMatrixItem]:
    areas = [
        ("MVP governance layer", "advanced safety boundary", 106),
        ("MVP DataLake", "v2 provider/data quality foundation", 106),
        ("MVP FeatureStore", "v2 feature engine", 116),
        ("MVP ML scaffold", "v2 ML/GPU pipeline", 136),
        ("MVP backtest scaffold", "v2 realistic backtest", 146),
        ("MVP portfolio research", "v2 portfolio optimization", 153),
        ("MVP reports", "v2 advanced report profiles", 158),
        ("MVP docs", "v2 analyst/operator handoff", 159),
        ("MVP closure docs", "v2 advanced delivery governance", 160)
    ]
    items = []
    for mvp, adv, phase in areas:
        items.append(ClosureMatrixItem(
            closure_id=build_closure_matrix_id(mvp, adv),
            mvp_area=mvp,
            advanced_target_area=adv,
            current_phase_support="partial",
            required_future_phase=str(phase),
            closure_status="gap_partially_closed",
            gap_note="",
            manual_review_required=False
        ))
    return items

def build_mvp_to_v2_closure_matrix(profile: FunctionalGapClosureProfile) -> tuple[pd.DataFrame, dict]:
    items = build_default_closure_matrix_items(profile)
    df = pd.DataFrame([to_dict(i) for i in items])
    return df, summarize_mvp_to_v2_closure_matrix(df)

def summarize_mvp_to_v2_closure_matrix(df: pd.DataFrame) -> dict:
    return {"total_items": len(df)}
