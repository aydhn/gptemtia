from pathlib import Path
import importlib
import pandas as pd

def list_project_packages(project_root: Path) -> list[str]:
    return [
        "config", "data", "features", "signals", "decisions", "strategies",
        "risk", "sizing", "levels", "backtesting", "validation", "ml",
        "ml_integration", "paper", "notifications", "orchestration",
        "observability", "security", "devtools", "reports"
    ]

def import_module_safely(module_name: str) -> dict:
    try:
        importlib.import_module(module_name)
        return {"module": module_name, "success": True, "error": None}
    except Exception as e:
        return {"module": module_name, "success": False, "error": str(e)}

def run_import_smoke_test(packages: list[str]) -> tuple[pd.DataFrame, dict]:
    results = [import_module_safely(p) for p in packages]
    df = pd.DataFrame(results)
    summary = {
        "total": len(packages),
        "success": sum(1 for r in results if r["success"]),
        "failed": sum(1 for r in results if not r["success"])
    }
    return df, summary

def build_import_smoke_report(import_df: pd.DataFrame) -> dict:
    if import_df.empty: return {"summary": "No data"}
    return {"summary": f"Tested {len(import_df)} packages"}
