import pandas as pd
from .continuation_config import AdvancedContinuationProfile

def build_advanced_module_dependency_map(profile: AdvancedContinuationProfile) -> tuple[pd.DataFrame, dict]:
    deps = [
        {"source": "data provider", "target": "data quality -> normalization -> lineage"},
        {"source": "normalized data", "target": "feature engine -> feature store"},
        {"source": "feature store", "target": "regime engine -> strategy router"},
        {"source": "feature store + regime", "target": "ML pipeline"},
        {"source": "ML outputs + strategy outputs", "target": "backtest"},
        {"source": "backtest outputs", "target": "portfolio risk engine"},
        {"source": "portfolio outputs", "target": "final reports"},
        {"source": "final reports", "target": "governance/quality"}
    ]
    df = pd.DataFrame(deps)
    return df, summarize_dependency_map(df)

def summarize_dependency_map(df: pd.DataFrame) -> dict:
    return {"total_deps": len(df), "status": "continuation_ready"}
