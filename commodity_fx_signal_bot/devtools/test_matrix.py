from pathlib import Path
import pandas as pd

def discover_tests(tests_dir: Path) -> pd.DataFrame:
    if not tests_dir.exists():
        return pd.DataFrame()
    files = [f.name for f in tests_dir.glob("test_*.py") if f.is_file()]
    data = []
    for f in files:
        data.append({
            "test_file": f,
            "related_module": infer_related_module(f),
            "category": infer_test_category(f),
            "phase_hint": "phase_X",
            "exists": True,
            "test_count_estimate": 1,
            "warnings": []
        })
    return pd.DataFrame(data)

def infer_test_category(test_file: str) -> str:
    name = test_file.replace("test_", "").replace(".py", "")
    categories = [
        "config", "data", "features", "candidates", "risk", "sizing", "levels",
        "backtest", "performance", "validation", "ml", "paper", "notifications",
        "orchestration", "observability", "security", "devtools"
    ]
    for c in categories:
        if c in name: return c
    return "unknown"

def infer_related_module(test_file: str) -> str:
    return test_file.replace("test_", "").replace(".py", "")

def build_test_matrix(project_root: Path) -> tuple[pd.DataFrame, dict]:
    tests_dir = project_root / "tests"
    df = discover_tests(tests_dir)
    summary = {"total_test_files": len(df)} if not df.empty else {"total_test_files": 0}
    return df, summary

def export_test_matrix_markdown(test_df: pd.DataFrame) -> str:
    if test_df.empty: return "No tests found."
    return test_df.to_markdown(index=False)
