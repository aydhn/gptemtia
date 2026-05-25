"""
Script discovery and availability matrix.
"""

import pandas as pd
from pathlib import Path

def classify_script(script_path: Path) -> str:
    name = script_path.name.lower()
    if "status" in name:
        return "status_script"
    if "report" in name:
        return "report_script"
    if "query" in name:
        return "query_script"
    if "diagnostic" in name or "health" in name:
        return "diagnostic_script"
    if "run" in name:
        return "pipeline_script"
    return "unknown_script"

def infer_script_module(script_path: Path) -> str:
    # A simplified inference based on file name prefix
    name = script_path.name.replace("run_", "").replace("_report.py", "").replace("_status.py", "")
    return name.split("_")[0]

def discover_scripts(project_root: Path) -> pd.DataFrame:
    script_dir = project_root / "scripts"
    data = []
    if script_dir.exists():
        for file in script_dir.glob("*.py"):
            if file.name == "__init__.py":
                continue

            script_class = classify_script(file)
            module = infer_script_module(file)
            warnings = []

            with open(file, "r", encoding="utf-8") as f:
                content = f.read().lower()
                if "live" in content or "broker" in content or "deploy" in content:
                    warnings.append("potentially_unsafe_content")

            data.append({
                "script_name": file.name,
                "script_class": script_class,
                "inferred_module": module,
                "warnings": warnings
            })
    return pd.DataFrame(data)

def build_script_availability_matrix(project_root: Path) -> pd.DataFrame:
    df = discover_scripts(project_root)
    if df.empty:
        return pd.DataFrame()

    matrix = df.groupby(["inferred_module", "script_class"]).size().unstack(fill_value=0).reset_index()
    return matrix

def summarize_script_discovery(script_df: pd.DataFrame) -> dict:
    if script_df.empty:
        return {}

    return {
        "total_scripts": len(script_df),
        "status_scripts": len(script_df[script_df["script_class"] == "status_script"]),
        "report_scripts": len(script_df[script_df["script_class"] == "report_script"]),
        "scripts_with_warnings": len(script_df[script_df["warnings"].apply(lambda x: len(x) > 0)])
    }
