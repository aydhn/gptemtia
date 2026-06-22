import pandas as pd
from typing import Tuple, List, Dict, Any
from pathlib import Path
from datetime import datetime, timezone

from local_maintenance.maintenance_config import LocalMaintenanceProfile
from local_maintenance.maintenance_models import MaintenanceTask, build_maintenance_task_id, maintenance_task_to_dict

def build_tasks_for_domain(domain_label: str, profile: LocalMaintenanceProfile) -> List[MaintenanceTask]:
    tasks = []

    if domain_label == "documentation_maintenance":
        tasks.append(MaintenanceTask(
            task_id=build_maintenance_task_id(domain_label, "README and docs review"),
            domain_label=domain_label,
            task_name="README and docs review",
            description="Review main README and root documentation.",
            cadence="refresh_monthly_manual",
            status="maintenance_unknown",
            last_seen_utc=None,
            next_review_hint=None,
            safe_command=None,
            warnings=[]
        ))
        tasks.append(MaintenanceTask(
            task_id=build_maintenance_task_id(domain_label, "PHASE_LOG review"),
            domain_label=domain_label,
            task_name="PHASE_LOG review",
            description="Ensure PHASE_LOG is up to date with recent phases.",
            cadence="refresh_monthly_manual",
            status="maintenance_unknown",
            last_seen_utc=None,
            next_review_hint=None,
            safe_command=None,
            warnings=[]
        ))
        tasks.append(MaintenanceTask(
            task_id=build_maintenance_task_id(domain_label, "SAFE_USAGE_GUIDE review"),
            domain_label=domain_label,
            task_name="SAFE_USAGE_GUIDE review",
            description="Review SAFE_USAGE_GUIDE for compliance.",
            cadence="refresh_monthly_manual",
            status="maintenance_unknown",
            last_seen_utc=None,
            next_review_hint=None,
            safe_command=None,
            warnings=[]
        ))

    elif domain_label == "scripts_maintenance":
        tasks.append(MaintenanceTask(
            task_id=build_maintenance_task_id(domain_label, "status scripts review"),
            domain_label=domain_label,
            task_name="status scripts review",
            description="Run and review all status scripts.",
            cadence="refresh_before_handoff_manual",
            status="maintenance_unknown",
            last_seen_utc=None,
            next_review_hint=None,
            safe_command="python -m scripts.run_system_healthcheck",
            warnings=[]
        ))

    elif domain_label == "reports_maintenance":
        tasks.append(MaintenanceTask(
            task_id=build_maintenance_task_id(domain_label, "report outputs review"),
            domain_label=domain_label,
            task_name="report outputs review",
            description="Check generated report outputs for freshness.",
            cadence="refresh_monthly_manual",
            status="maintenance_unknown",
            last_seen_utc=None,
            next_review_hint=None,
            safe_command=None,
            warnings=[]
        ))

    elif domain_label == "datalake_maintenance":
        tasks.append(MaintenanceTask(
            task_id=build_maintenance_task_id(domain_label, "DataLake save/load pair review"),
            domain_label=domain_label,
            task_name="DataLake save/load pair review",
            description="Ensure save and load functions match in DataLake.",
            cadence="refresh_on_change_manual",
            status="maintenance_unknown",
            last_seen_utc=None,
            next_review_hint=None,
            safe_command=None,
            warnings=[]
        ))

    elif domain_label == "security_maintenance":
        tasks.append(MaintenanceTask(
            task_id=build_maintenance_task_id(domain_label, "secrets hygiene report refresh"),
            domain_label=domain_label,
            task_name="secrets hygiene report refresh",
            description="Refresh secrets hygiene reports.",
            cadence="refresh_monthly_manual",
            status="maintenance_unknown",
            last_seen_utc=None,
            next_review_hint=None,
            safe_command="python -m scripts.run_secrets_quality_report",
            warnings=[]
        ))

    elif domain_label == "backup_packaging_maintenance":
        tasks.append(MaintenanceTask(
            task_id=build_maintenance_task_id(domain_label, "backup recovery dry-run refresh"),
            domain_label=domain_label,
            task_name="backup recovery dry-run refresh",
            description="Perform a backup recovery dry run.",
            cadence="refresh_monthly_manual",
            status="maintenance_unknown",
            last_seen_utc=None,
            next_review_hint=None,
            safe_command=None,
            warnings=[]
        ))
        tasks.append(MaintenanceTask(
            task_id=build_maintenance_task_id(domain_label, "packaging manifest refresh"),
            domain_label=domain_label,
            task_name="packaging manifest refresh",
            description="Update portable packaging manifests.",
            cadence="refresh_before_handoff_manual",
            status="maintenance_unknown",
            last_seen_utc=None,
            next_review_hint=None,
            safe_command=None,
            warnings=[]
        ))

    elif domain_label == "evidence_metadata_graph_timeline_maintenance":
        tasks.append(MaintenanceTask(
            task_id=build_maintenance_task_id(domain_label, "evidence binder refresh"),
            domain_label=domain_label,
            task_name="evidence binder refresh",
            description="Refresh evidence governance binders.",
            cadence="refresh_monthly_manual",
            status="maintenance_unknown",
            last_seen_utc=None,
            next_review_hint=None,
            safe_command=None,
            warnings=[]
        ))
        tasks.append(MaintenanceTask(
            task_id=build_maintenance_task_id(domain_label, "metadata cards refresh"),
            domain_label=domain_label,
            task_name="metadata cards refresh",
            description="Update metadata cards.",
            cadence="refresh_monthly_manual",
            status="maintenance_unknown",
            last_seen_utc=None,
            next_review_hint=None,
            safe_command=None,
            warnings=[]
        ))
        tasks.append(MaintenanceTask(
            task_id=build_maintenance_task_id(domain_label, "graph index refresh"),
            domain_label=domain_label,
            task_name="graph index refresh",
            description="Update knowledge graph indexes.",
            cadence="refresh_monthly_manual",
            status="maintenance_unknown",
            last_seen_utc=None,
            next_review_hint=None,
            safe_command=None,
            warnings=[]
        ))
        tasks.append(MaintenanceTask(
            task_id=build_maintenance_task_id(domain_label, "timeline registry refresh"),
            domain_label=domain_label,
            task_name="timeline registry refresh",
            description="Update timeline event registries.",
            cadence="refresh_monthly_manual",
            status="maintenance_unknown",
            last_seen_utc=None,
            next_review_hint=None,
            safe_command=None,
            warnings=[]
        ))

    elif domain_label == "consistency_readiness_maintenance":
        tasks.append(MaintenanceTask(
            task_id=build_maintenance_task_id(domain_label, "consistency report refresh"),
            domain_label=domain_label,
            task_name="consistency report refresh",
            description="Run cross-layer consistency checks.",
            cadence="refresh_monthly_manual",
            status="maintenance_unknown",
            last_seen_utc=None,
            next_review_hint=None,
            safe_command="python -m scripts.run_consistency_status",
            warnings=[]
        ))
        tasks.append(MaintenanceTask(
            task_id=build_maintenance_task_id(domain_label, "readiness binder refresh"),
            domain_label=domain_label,
            task_name="readiness binder refresh",
            description="Refresh readiness binders.",
            cadence="refresh_monthly_manual",
            status="maintenance_unknown",
            last_seen_utc=None,
            next_review_hint=None,
            safe_command=None,
            warnings=[]
        ))

    elif domain_label == "dependency_maintenance":
        tasks.append(MaintenanceTask(
            task_id=build_maintenance_task_id(domain_label, "dependency review"),
            domain_label=domain_label,
            task_name="dependency review",
            description="Manually review dependencies for stale or unnecessary items.",
            cadence="refresh_quarterly_manual",
            status="maintenance_unknown",
            last_seen_utc=None,
            next_review_hint=None,
            safe_command=None,
            warnings=[]
        ))

    elif domain_label == "operator_maintenance":
        tasks.append(MaintenanceTask(
            task_id=build_maintenance_task_id(domain_label, "known gaps review"),
            domain_label=domain_label,
            task_name="known gaps review",
            description="Review documented gaps and limitations.",
            cadence="refresh_monthly_manual",
            status="maintenance_unknown",
            last_seen_utc=None,
            next_review_hint=None,
            safe_command=None,
            warnings=[]
        ))

    return tasks

def build_maintenance_task_registry(domain_df: pd.DataFrame, profile: LocalMaintenanceProfile) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    tasks = []
    if domain_df is not None and not domain_df.empty:
        for domain_label in domain_df["domain_label"]:
            tasks.extend(build_tasks_for_domain(domain_label, profile))

    df = pd.DataFrame([maintenance_task_to_dict(t) for t in tasks])
    summary = summarize_maintenance_tasks(df)
    return df, summary

def evaluate_maintenance_task_status(task_df: pd.DataFrame, project_root: Path, profile: LocalMaintenanceProfile) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    # In a real scenario, this would check mtime or presence of outputs.
    # For this offline/local implementation, we approximate it.

    df = task_df.copy()
    if not df.empty:
        df["status"] = "maintenance_due_soon"
        df["last_seen_utc"] = datetime.now(timezone.utc).isoformat()

    summary = summarize_maintenance_tasks(df)
    return df, summary

def summarize_maintenance_tasks(task_df: pd.DataFrame) -> Dict[str, Any]:
    if task_df is None or task_df.empty:
        return {"total_tasks": 0}

    summary = {
        "total_tasks": len(task_df),
        "tasks_by_domain": task_df["domain_label"].value_counts().to_dict(),
        "tasks_by_status": task_df["status"].value_counts().to_dict(),
        "disclaimer": "The maintenance task registry does not execute commands automatically."
    }
    return summary
