import pandas as pd
from .runtime_config import AdvancedRuntimeProfile

def build_runtime_dependency_graph(profile: AdvancedRuntimeProfile) -> tuple[pd.DataFrame, dict]:
    data = [
        {"source": "settings", "target": "paths", "type": "config_dep"},
        {"source": "paths", "target": "DataLake", "type": "storage_dep"},
        {"source": "paths", "target": "reports", "type": "output_dep"},
        {"source": "DataLake", "target": "FeatureStore", "type": "data_dep"},
        {"source": "DataLake", "target": "reports", "type": "data_dep"},
        {"source": "FeatureStore", "target": "feature engine future", "type": "future_dep"},
        {"source": "feature engine future", "target": "regime engine future", "type": "future_dep"},
        {"source": "feature engine future", "target": "ML/GPU future", "type": "future_dep"},
        {"source": "regime engine future", "target": "strategy router future", "type": "future_dep"},
        {"source": "ML/GPU future", "target": "backtest future", "type": "future_dep"},
        {"source": "backtest future", "target": "portfolio future", "type": "future_dep"},
        {"source": "portfolio future", "target": "final reports", "type": "future_dep"},
        {"source": "final reports", "target": "governance/quality", "type": "review_dep"}
    ]
    df = pd.DataFrame(data)
    return df, summarize_runtime_dependency_graph(df)

def summarize_runtime_dependency_graph(df: pd.DataFrame) -> dict:
    if df.empty: return {"total": 0}
    return {"total_edges": len(df)}
