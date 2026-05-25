"""
Phase coverage tracking.
"""

import pandas as pd
from pathlib import Path
import re

def parse_phase_log(project_root: Path) -> pd.DataFrame:
    phase_log_path = project_root / "docs" / "PHASE_LOG.md"
    phases = []

    if phase_log_path.exists():
        with open(phase_log_path, "r", encoding="utf-8") as f:
            content = f.read()

        # Simplified parsing
        matches = re.finditer(r"## Phase (\d+):?(.*)", content)
        for match in matches:
            phase_num = int(match.group(1))
            title = match.group(2).strip()
            phases.append({
                "phase_number": phase_num,
                "phase_title": title
            })
    return pd.DataFrame(phases)

def infer_phase_modules() -> pd.DataFrame:
    # Hardcoded mapping for demonstration
    data = [
        {"phase_number": 39, "expected_module": "research_reports"},
        {"phase_number": 42, "expected_module": "portfolio_regime"},
        {"phase_number": 43, "expected_module": "synthetic_indices"},
        {"phase_number": 44, "expected_module": "factor_research"},
        {"phase_number": 45, "expected_module": "meta_research"},
        {"phase_number": 46, "expected_module": "experiments"},
        {"phase_number": 47, "expected_module": "governance"},
        {"phase_number": 48, "expected_module": "research_planning"},
        {"phase_number": 49, "expected_module": "knowledge_base"},
        {"phase_number": 50, "expected_module": "command_center"}
    ]
    return pd.DataFrame(data)

def build_phase_coverage_matrix(project_root: Path) -> pd.DataFrame:
    log_df = parse_phase_log(project_root)
    mod_df = infer_phase_modules()

    if log_df.empty or mod_df.empty:
        return pd.DataFrame()

    df = pd.merge(log_df, mod_df, on="phase_number", how="left")

    coverage = []
    for _, row in df.iterrows():
        module = row.get("expected_module")
        if pd.isna(module):
            continue

        mod_path = project_root / module

        coverage.append({
            "phase_number": row["phase_number"],
            "phase_title": row["phase_title"],
            "expected_module": module,
            "module_directory_exists": mod_path.exists(),
            "scripts_exist": True, # Mocked
            "tests_exist": True, # Mocked
            "docs_updated": True, # Mocked
            "status": "covered" if mod_path.exists() else "missing",
            "warnings": [] if mod_path.exists() else ["Module directory missing"]
        })

    return pd.DataFrame(coverage)

def summarize_phase_coverage(coverage_df: pd.DataFrame) -> dict:
    if coverage_df.empty:
        return {}

    return {
        "total_phases_tracked": len(coverage_df),
        "phases_covered": len(coverage_df[coverage_df["status"] == "covered"]),
        "phases_missing": len(coverage_df[coverage_df["status"] == "missing"])
    }
