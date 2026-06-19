import pandas as pd
from pathlib import Path
from .readiness_config import LocalReadinessProfile
from .readiness_models import OperatorChecklistItem, build_operator_checklist_item_id

def build_final_operator_checklist(profile: LocalReadinessProfile) -> tuple[pd.DataFrame, dict]:
    items = [
        OperatorChecklistItem(
            item_id=build_operator_checklist_item_id("final_checklist", "Check local readiness status"),
            checklist_name="final_checklist",
            domain="readiness",
            instruction="Run local readiness status script",
            expected_output="Status CSV and text report generated",
            status="pending",
            safe_command="python -m scripts.run_readiness_status",
            warnings=[]
        )
    ]
    from .readiness_models import operator_checklist_item_to_dict
    df = pd.DataFrame([operator_checklist_item_to_dict(i) for i in items])
    return df, summarize_operator_checklist(df)

def build_operator_first_run_checklist(profile: LocalReadinessProfile) -> tuple[pd.DataFrame, dict]:
    items = [
        OperatorChecklistItem(
            item_id=build_operator_checklist_item_id("first_run", "Verify system health"),
            checklist_name="first_run",
            domain="system",
            instruction="Run system healthcheck",
            expected_output="Healthcheck report generated",
            status="pending",
            safe_command="python -m scripts.run_system_healthcheck",
            warnings=[]
        )
    ]
    from .readiness_models import operator_checklist_item_to_dict
    df = pd.DataFrame([operator_checklist_item_to_dict(i) for i in items])
    return df, summarize_operator_checklist(df)

def build_safe_operator_command_sequence(profile: LocalReadinessProfile) -> tuple[pd.DataFrame, dict]:
    commands = [
        "python -m scripts.run_quality_gate_status",
        "python -m scripts.run_final_review_status",
        "python -m scripts.run_scenario_regression_status",
        "python -m scripts.run_master_orchestration_status",
        "python -m scripts.run_secrets_hygiene_status",
        "python -m scripts.run_backup_recovery_status",
        "python -m scripts.run_packaging_status",
        "python -m scripts.run_evidence_status",
        "python -m scripts.run_metadata_status",
        "python -m scripts.run_graph_status",
        "python -m scripts.run_timeline_status",
        "python -m scripts.run_consistency_status",
        "python -m scripts.run_readiness_status"
    ]
    df = pd.DataFrame({"safe_command": commands})
    return df, {"total_commands": len(df)}

def summarize_operator_checklist(checklist_df: pd.DataFrame) -> dict:
    return {
        "total_items": len(checklist_df),
        "pending": len(checklist_df[checklist_df["status"] == "pending"])
    }
