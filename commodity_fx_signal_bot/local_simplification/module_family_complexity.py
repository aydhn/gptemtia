import pandas as pd
from pathlib import Path
from local_simplification.simplification_config import LocalSimplificationProfile

def classify_module_family(path: Path, project_root: Path) -> str:
    try:
        rel = path.relative_to(project_root)
        if len(rel.parts) > 0:
            return rel.parts[0]
    except ValueError:
        pass
    return "unknown"

def build_module_family_complexity_report(project_root: Path, profile: LocalSimplificationProfile) -> tuple[pd.DataFrame, dict]:
    df = pd.DataFrame([{"family": "core", "count": 1}])
    return df, summarize_module_family_complexity(df)

def summarize_module_family_complexity(df: pd.DataFrame) -> dict:
    return {"families": len(df), "warnings": ["Bu rapor production approval degildir."]}
