import pandas as pd
from .gap_closure_config import FunctionalGapClosureProfile
from .gap_closure_models import MissingFunctionalityItem, build_missing_functionality_id, to_dict

def build_default_missing_functionality_items(profile: FunctionalGapClosureProfile) -> list[MissingFunctionalityItem]:
    areas = ["provider", "feature", "regime", "ML", "backtest", "portfolio"]
    return [MissingFunctionalityItem(
        missing_id=build_missing_functionality_id(area, 106),
        functionality_area=area,
        current_gap="Missing implementation",
        required_for_phase=106,
        priority_label="priority_high",
        risk_label="functional_gap_medium_risk",
        recommendation="Implement in future phase",
        manual_review_required=False
    ) for area in areas]

def build_missing_functionality_register(profile: FunctionalGapClosureProfile) -> tuple[pd.DataFrame, dict]:
    df = pd.DataFrame([to_dict(i) for i in build_default_missing_functionality_items(profile)])
    return df, summarize_missing_functionality_register(df)

def summarize_missing_functionality_register(df: pd.DataFrame) -> dict: return {"total": len(df)}
