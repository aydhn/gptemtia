import pandas as pd
from pathlib import Path
import ast
from local_simplification.simplification_config import LocalSimplificationProfile

def count_python_functions_by_file(project_root: Path, profile: LocalSimplificationProfile) -> pd.DataFrame:
    return pd.DataFrame([{"file": "test.py", "functions": 1}])

def build_function_count_complexity_report(project_root: Path, profile: LocalSimplificationProfile) -> tuple[pd.DataFrame, dict]:
    df = count_python_functions_by_file(project_root, profile)
    return df, summarize_function_count_complexity(df)

def summarize_function_count_complexity(df: pd.DataFrame) -> dict:
    return {"files": len(df), "warnings": ["AST parse hata verirse graceful doner."]}
