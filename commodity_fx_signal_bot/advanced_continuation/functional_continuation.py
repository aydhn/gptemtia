import pandas as pd
from .continuation_config import AdvancedContinuationProfile
from .continuation_models import FunctionalContinuationItem, build_functional_continuation_id

def build_default_functional_continuation_items(profile: AdvancedContinuationProfile) -> list[FunctionalContinuationItem]:
    areas = [
        ("data/storage/data_lake.py", "Phase 106-115"),
        ("ml/feature_store.py", "Phase 116-125"),
        ("ML pipeline", "Phase 136-145"),
        ("backtest", "Phase 146-152"),
        ("portfolio_research / portfolio_regime", "Phase 153-157"),
        ("reports/report_builder.py", "tüm ileri fazlar"),
        ("docs/generated", "governance ve final delivery"),
        ("scripts", "operational dry-run commands")
    ]
    return [FunctionalContinuationItem(build_functional_continuation_id(a, t), a, a, t, "mapped", "") for a, t in areas]

def build_functional_continuation_layer(profile: AdvancedContinuationProfile) -> tuple[pd.DataFrame, dict]:
    items = build_default_functional_continuation_items(profile)
    df = pd.DataFrame([vars(i) for i in items])
    return df, summarize_functional_continuation(df)

def summarize_functional_continuation(df: pd.DataFrame) -> dict:
    return {"total_items": len(df), "status": "continuation_ready"}
