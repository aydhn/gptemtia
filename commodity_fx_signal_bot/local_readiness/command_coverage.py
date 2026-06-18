import pandas as pd
from pathlib import Path
from .readiness_config import LocalReadinessProfile

def discover_status_scripts(project_root: Path) -> pd.DataFrame:
    scripts_dir = project_root / "scripts"
    status_scripts = []
    if scripts_dir.exists():
        for p in scripts_dir.glob("run_*_status.py"):
            status_scripts.append(p.name)
    return pd.DataFrame({"script_name": status_scripts})

def discover_report_scripts(project_root: Path) -> pd.DataFrame:
    scripts_dir = project_root / "scripts"
    report_scripts = []
    if scripts_dir.exists():
        for p in scripts_dir.glob("run_*_report*.py"):
            report_scripts.append(p.name)
    return pd.DataFrame({"script_name": report_scripts})

def build_safe_command_coverage_report(project_root: Path, command_df: pd.DataFrame, profile: LocalReadinessProfile) -> tuple[pd.DataFrame, dict]:
    status_df = discover_status_scripts(project_root)
    report_df = discover_report_scripts(project_root)

    all_scripts = set(status_df["script_name"].tolist() + report_df["script_name"].tolist())
    df = pd.DataFrame({"script_name": list(all_scripts)})
    df["covered"] = True
    return df, summarize_command_coverage(df)

def detect_missing_status_scripts(project_root: Path, expected_domains: list[str]) -> pd.DataFrame:
    existing = discover_status_scripts(project_root)["script_name"].tolist()
    missing = []
    for domain in expected_domains:
        expected_name = f"run_{domain}_status.py"
        if expected_name not in existing:
            missing.append(expected_name)
    return pd.DataFrame({"missing_script": missing})

def summarize_command_coverage(coverage_df: pd.DataFrame) -> dict:
    return {
        "total_covered": len(coverage_df)
    }
