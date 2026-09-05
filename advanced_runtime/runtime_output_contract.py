import pandas as pd
from .runtime_config import AdvancedRuntimeProfile

def build_runtime_output_contract(profile: AdvancedRuntimeProfile) -> tuple[pd.DataFrame, dict]:
    areas = [
        "data/lake/advanced_continuation",
        "data/lake/advanced_runtime",
        "reports/output/advanced_continuation",
        "reports/output/advanced_runtime",
        "docs/generated/advanced_continuation",
        "docs/generated/advanced_runtime"
    ]
    data = []
    for a in areas:
        data.append({
            "output_area": a,
            "expected_format": "csv/json/md/txt",
            "persistence_scope": "local",
            "destructive_action_allowed": False,
            "manual_review_required": True,
            "warning": "Do not overwrite user data"
        })
    df = pd.DataFrame(data)
    return df, summarize_runtime_output_contract(df)

def summarize_runtime_output_contract(df: pd.DataFrame) -> dict:
    if df.empty: return {"total": 0}
    return {"total_outputs": len(df)}
