"""
Dependency mapping logic.
"""

import pandas as pd
from pathlib import Path

from master_orchestration.layer_map import infer_layer_for_module

def build_module_dependency_map(project_root: Path, layer_df: pd.DataFrame) -> pd.DataFrame:
    # A simple mock module dependency graph for mapping purposes
    records = []

    # Just generating some dummy dependencies for core modules
    core_deps = {
        "features": ["data"],
        "feature_store": ["data_lake"],
        "ml": ["features", "feature_store"],
        "backtest": ["data_lake", "feature_store"],
        "research_reports": ["data_lake"],
        "reports": ["data_lake", "research_reports", "ml", "backtest"],
        "master_orchestration": ["reports", "analyst_ux", "documentation", "final_review"]
    }

    for module, deps in core_deps.items():
        source_layer = infer_layer_for_module(module)
        for dep in deps:
            target_layer = infer_layer_for_module(dep)
            records.append({
                "source_module": module,
                "target_module": dep,
                "source_layer": source_layer,
                "target_layer": target_layer
            })

    return pd.DataFrame(records)

def build_report_dependency_map(project_root: Path) -> pd.DataFrame:
    # Mock report dependency
    records = [
        {"report": "report_summarization", "depends_on": "research_reports"},
        {"report": "final_review", "depends_on": "quality_gates"},
        {"report": "master_orchestration", "depends_on": "final_review"}
    ]
    return pd.DataFrame(records)

def build_datalake_dependency_map(project_root: Path) -> pd.DataFrame:
    # Mock datalake dependency
    records = [
        {"artifact": "master_command_plan", "producer": "master_orchestration", "consumer": "playbook"},
        {"artifact": "features", "producer": "feature_store", "consumer": "ml"}
    ]
    return pd.DataFrame(records)

def build_cross_layer_dependency_summary(module_dep_df: pd.DataFrame, report_dep_df: pd.DataFrame, datalake_dep_df: pd.DataFrame) -> dict:
    return {
        "total_module_dependencies": len(module_dep_df),
        "total_report_dependencies": len(report_dep_df),
        "total_datalake_dependencies": len(datalake_dep_df)
    }

def detect_dependency_warnings(module_dep_df: pd.DataFrame) -> pd.DataFrame:
    warnings = []
    if not module_dep_df.empty:
        for _, row in module_dep_df.iterrows():
            if row["target_layer"] == "unknown_layer":
                warnings.append({
                    "module": row["source_module"],
                    "dependency": row["target_module"],
                    "warning": "Unknown target layer"
                })
    return pd.DataFrame(warnings) if warnings else pd.DataFrame(columns=["module", "dependency", "warning"])
