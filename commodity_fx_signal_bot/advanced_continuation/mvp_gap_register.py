import pandas as pd
from .continuation_config import AdvancedContinuationProfile
from .continuation_models import MvpAdvancedGapItem, build_mvp_gap_id

def build_default_mvp_advanced_gaps(profile: AdvancedContinuationProfile) -> list[MvpAdvancedGapItem]:
    areas = ["provider abstraction eksikleri", "FX provider eksikleri", "commodities provider eksikleri",
             "macro provider eksikleri", "economic calendar eksikleri", "news metadata eksikleri",
             "data quality eksikleri", "feature/indicator eksikleri", "regime engine eksikleri",
             "ML/GPU eksikleri", "backtest realism eksikleri", "slippage/cost eksikleri",
             "portfolio optimization eksikleri", "final integration eksikleri"]
    return [MvpAdvancedGapItem(build_mvp_gap_id(a, "101-160"), a, "MVP", "Advanced", "101-160", "High", "continuation_medium_risk", "Plan") for a in areas]

def build_mvp_to_advanced_gap_register(profile: AdvancedContinuationProfile) -> tuple[pd.DataFrame, dict]:
    items = build_default_mvp_advanced_gaps(profile)
    df = pd.DataFrame([vars(i) for i in items])
    return df, summarize_mvp_gap_register(df)

def summarize_mvp_gap_register(df: pd.DataFrame) -> dict:
    return {"total_gaps": len(df), "status": "continuation_ready"}
