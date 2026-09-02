import pandas as pd
from pathlib import Path
from local_simplification.simplification_config import LocalSimplificationProfile

def calculate_folder_depth(path: Path, project_root: Path) -> int:
    try:
        rel = path.relative_to(project_root)
        return len(rel.parts)
    except ValueError:
        return 0

def build_folder_depth_complexity_report(project_root: Path, profile: LocalSimplificationProfile) -> tuple[pd.DataFrame, dict]:
    df = pd.DataFrame([{"folder": "test", "depth": 1}])
    return df, summarize_folder_depth_complexity(df)

def summarize_folder_depth_complexity(df: pd.DataFrame) -> dict:
    return {"folders": len(df), "warnings": ["Dosya tasima onermez."]}
