import pandas as pd
from pathlib import Path
from .runtime_config import AdvancedRuntimeProfile
from .runtime_models import RuntimeModuleItem, build_runtime_module_id

def build_default_runtime_modules(profile: AdvancedRuntimeProfile) -> list[RuntimeModuleItem]:
    modules = [
        "config/settings.py", "config/paths.py", "data/storage/data_lake.py",
        "ml/feature_store.py", "reports/report_builder.py", "scripts", "tests", "docs",
        "advanced_continuation", "future data_provider layer", "future feature_engine layer",
        "future regime_engine layer", "future ml_gpu layer", "future backtest_v2 layer",
        "future portfolio_engine layer", "future full integration layer"
    ]
    items = []
    for m in modules:
        items.append(RuntimeModuleItem(
            module_id=build_runtime_module_id("core", m.replace("/", "_").replace(" ", "_")),
            module_area="core",
            module_ref=m,
            runtime_role="infrastructure" if "future" not in m else "placeholder",
            contract_required=True,
            status_label="runtime_ready" if "future" not in m else "planned",
            warnings=[]
        ))
    return items

def build_runtime_module_registry(project_root: Path, profile: AdvancedRuntimeProfile) -> tuple[pd.DataFrame, dict]:
    items = build_default_runtime_modules(profile)
    df = pd.DataFrame([i.to_dict() for i in items])
    return df, summarize_runtime_module_registry(df)

def summarize_runtime_module_registry(df: pd.DataFrame) -> dict:
    if df.empty: return {"total": 0}
    return {"total": len(df)}
