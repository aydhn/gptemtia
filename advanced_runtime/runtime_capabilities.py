import pandas as pd
from .runtime_config import AdvancedRuntimeProfile
from .runtime_models import RuntimeCapabilityItem, build_runtime_capability_id

def build_default_runtime_capabilities(profile: AdvancedRuntimeProfile) -> list[RuntimeCapabilityItem]:
    caps = [
        ("capability_settings", "settings"),
        ("capability_paths", "paths"),
        ("capability_datalake", "datalake"),
        ("capability_featurestore", "featurestore"),
        ("capability_reporting", "reporting"),
        ("capability_scripts", "scripts"),
        ("capability_tests", "tests"),
        ("capability_docs", "docs"),
        ("capability_advanced_continuation", "advanced_continuation"),
        ("capability_provider_future", "future data providers"),
        ("capability_feature_future", "future feature engine"),
        ("capability_regime_future", "future regime engine"),
        ("capability_ml_gpu_future", "future ML/GPU"),
        ("capability_backtest_future", "future backtest"),
        ("capability_portfolio_future", "future portfolio"),
        ("capability_final_integration_future", "future final integration")
    ]
    items = []
    for label, name in caps:
        items.append(RuntimeCapabilityItem(
            capability_id=build_runtime_capability_id(label),
            capability_label=label,
            capability_name=name,
            current_status="ready" if "future" not in name else "planned",
            future_phase_range="103-160",
            required_by=[],
            warnings=[]
        ))
    return items

def build_runtime_capability_registry(profile: AdvancedRuntimeProfile) -> tuple[pd.DataFrame, dict]:
    items = build_default_runtime_capabilities(profile)
    df = pd.DataFrame([i.to_dict() for i in items])
    return df, summarize_runtime_capabilities(df)

def summarize_runtime_capabilities(df: pd.DataFrame) -> dict:
    if df.empty: return {"total": 0}
    return {"total": len(df), "planned": len(df[df["current_status"] == "planned"])}
