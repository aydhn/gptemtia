"""
Master orchestration status.
"""

import pandas as pd
from pathlib import Path
from config.paths import (
    LAKE_MASTER_ORCHESTRATION_LAYER_MAPS,
    LAKE_MASTER_ORCHESTRATION_DEPENDENCIES,
    LAKE_MASTER_ORCHESTRATION_COMMAND_GRAPHS,
    LAKE_MASTER_ORCHESTRATION_MASTER_PLANS,
    LAKE_MASTER_ORCHESTRATION_META_RUNNER,
    LAKE_MASTER_ORCHESTRATION_OPERATING_MODES,
    LAKE_MASTER_ORCHESTRATION_PLAYBOOKS,
    LAKE_MASTER_ORCHESTRATION_RUN_ORDERS,
    LAKE_MASTER_ORCHESTRATION_HANDOFFS,
    LAKE_MASTER_ORCHESTRATION_CONSOLIDATION,
    LAKE_MASTER_ORCHESTRATION_SAFETY,
    LAKE_MASTER_ORCHESTRATION_STATUS,
    LAKE_MASTER_ORCHESTRATION_QUALITY
)

def build_master_orchestration_status(project_root: Path) -> pd.DataFrame:
    directories = [
        ("Layer Maps", LAKE_MASTER_ORCHESTRATION_LAYER_MAPS),
        ("Dependencies", LAKE_MASTER_ORCHESTRATION_DEPENDENCIES),
        ("Command Graphs", LAKE_MASTER_ORCHESTRATION_COMMAND_GRAPHS),
        ("Master Plans", LAKE_MASTER_ORCHESTRATION_MASTER_PLANS),
        ("Meta Runner", LAKE_MASTER_ORCHESTRATION_META_RUNNER),
        ("Operating Modes", LAKE_MASTER_ORCHESTRATION_OPERATING_MODES),
        ("Playbooks", LAKE_MASTER_ORCHESTRATION_PLAYBOOKS),
        ("Run Orders", LAKE_MASTER_ORCHESTRATION_RUN_ORDERS),
        ("Handoffs", LAKE_MASTER_ORCHESTRATION_HANDOFFS),
        ("Consolidation", LAKE_MASTER_ORCHESTRATION_CONSOLIDATION),
        ("Safety", LAKE_MASTER_ORCHESTRATION_SAFETY),
        ("Status", LAKE_MASTER_ORCHESTRATION_STATUS),
        ("Quality", LAKE_MASTER_ORCHESTRATION_QUALITY)
    ]

    records = []
    for name, path in directories:
        exists = path.exists()
        count = len(list(path.glob("*.*"))) if exists else 0
        records.append({
            "category": name,
            "directory_exists": exists,
            "artifact_count": count
        })

    return pd.DataFrame(records)

def collect_master_output_status(project_root: Path) -> pd.DataFrame:
    # Just a mock to be similar to datalake status but for outputs
    return build_master_orchestration_status(project_root)

def collect_cross_layer_status(project_root: Path) -> pd.DataFrame:
    return build_master_orchestration_status(project_root)

def summarize_master_status(status_df: pd.DataFrame) -> dict:
    if status_df.empty:
        return {"total_categories": 0}

    return {
        "total_categories": len(status_df),
        "total_artifacts": status_df["artifact_count"].sum(),
        "missing_directories": len(status_df[~status_df["directory_exists"]])
    }
