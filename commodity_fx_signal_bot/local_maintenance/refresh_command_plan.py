import pandas as pd
from typing import Tuple, Dict, Any, List

from local_maintenance.maintenance_config import LocalMaintenanceProfile

def classify_refresh_command_safety(command: str) -> Dict[str, Any]:
    forbidden_terms = ["live", "broker", "deploy", "delete", "overwrite", "cloud", "external"]
    for term in forbidden_terms:
        if term in command.lower():
            return {"is_safe": False, "reason": f"Contains forbidden term: {term}"}

    if not command.startswith("python -m scripts.run_"):
        return {"is_safe": False, "reason": "Not a standard local run_ script command."}

    return {"is_safe": True, "reason": "Looks like a safe offline script."}

def build_refresh_command_groups(profile: LocalMaintenanceProfile) -> Dict[str, List[str]]:
    return {
        "status_refresh": [
            "python -m scripts.run_system_healthcheck",
            "python -m scripts.run_observability_status",
            "python -m scripts.run_maintenance_status"
        ],
        "safety_refresh": [
            "python -m scripts.run_secrets_quality_report",
            "python -m scripts.run_sensitive_file_scan"
        ],
        "backup_packaging_refresh": [
            "python -m scripts.run_portable_bundle_manifest",
            "python -m scripts.run_backup_recovery_status"
        ],
        "evidence_metadata_graph_timeline_refresh": [
            "python -m scripts.run_evidence_quality_report",
            "python -m scripts.run_metadata_report",
            "python -m scripts.run_timeline_report"
        ],
        "consistency_readiness_refresh": [
            "python -m scripts.run_consistency_status",
            "python -m scripts.run_readiness_report"
        ],
        "documentation_review": [
            "python -m scripts.run_documentation_pack_report"
        ],
        "maintenance_review": [
            "python -m scripts.run_maintenance_sustainability_report",
            "python -m scripts.run_maintenance_quality_report"
        ]
    }

def build_refresh_command_plan(profile: LocalMaintenanceProfile) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    groups = build_refresh_command_groups(profile)
    data = []

    for group, commands in groups.items():
        for cmd in commands:
            safety = classify_refresh_command_safety(cmd)
            if safety["is_safe"]:
                data.append({
                    "group": group,
                    "command": cmd,
                    "is_safe": safety["is_safe"]
                })

    df = pd.DataFrame(data)
    summary = summarize_refresh_command_plan(df)
    return df, summary

def summarize_refresh_command_plan(command_df: pd.DataFrame) -> Dict[str, Any]:
    if command_df is None or command_df.empty:
        return {"total_commands": 0}

    return {
        "total_commands": len(command_df),
        "groups": command_df["group"].unique().tolist() if "group" in command_df else [],
        "disclaimer": "These commands are NOT executed automatically. This plan is not a scheduler. Forbidden commands are omitted."
    }
