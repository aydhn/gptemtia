import pandas as pd
from typing import Tuple, Dict, Any, Optional

from local_maintenance.maintenance_config import LocalMaintenanceProfile

def validate_maintenance_domains(domain_df: pd.DataFrame, profile: LocalMaintenanceProfile) -> Dict[str, Any]:
    if domain_df is None or domain_df.empty:
        return {"valid": False, "warnings": ["Domain registry is empty."]}

    warnings = []
    if not "domain_id" in domain_df.columns:
        warnings.append("Missing domain_id in domain registry.")

    return {"valid": len(warnings) == 0, "warnings": warnings}

def validate_maintenance_tasks(task_df: pd.DataFrame, profile: LocalMaintenanceProfile) -> Dict[str, Any]:
    if task_df is None or task_df.empty:
        return {"valid": False, "warnings": ["Task registry is empty."]}

    warnings = []
    if not "task_id" in task_df.columns:
        warnings.append("Missing task_id in task registry.")

    return {"valid": len(warnings) == 0, "warnings": warnings}

def validate_refresh_cadence(cadence_df: pd.DataFrame, profile: LocalMaintenanceProfile) -> Dict[str, Any]:
    if cadence_df is None or cadence_df.empty:
        return {"valid": False, "warnings": ["Cadence registry is empty."]}

    warnings = []
    if not "suggested_cadence" in cadence_df.columns:
        warnings.append("Missing suggested_cadence in cadence registry.")

    return {"valid": len(warnings) == 0, "warnings": warnings}

def validate_dependency_watch(dep_df: pd.DataFrame, profile: LocalMaintenanceProfile) -> Dict[str, Any]:
    if dep_df is None or dep_df.empty:
        return {"valid": True, "warnings": ["Dependency watch is empty (maybe skipped)."]}
    return {"valid": True, "warnings": []}

def validate_refresh_commands(command_df: pd.DataFrame, profile: LocalMaintenanceProfile) -> Dict[str, Any]:
    if command_df is None or command_df.empty:
        return {"valid": False, "warnings": ["Refresh command plan is empty."]}
    return {"valid": True, "warnings": []}

def validate_no_scheduler_or_auto_upgrade_claims(
    text: Optional[str] = None,
    df: Optional[pd.DataFrame] = None,
    summary: Optional[Dict] = None
) -> Dict[str, Any]:

    warnings = []

    def check_str(s: str):
        s_low = s.lower()
        if "production scheduler" in s_low and "not" not in s_low and "değildir" not in s_low:
            warnings.append("Found claim about production scheduler.")
        if "auto upgrade" in s_low and "not" not in s_low and "değildir" not in s_low:
            warnings.append("Found claim about auto upgrade.")

    if text:
        check_str(text)

    return {"valid": len(warnings) == 0, "warnings": warnings}

def build_maintenance_validation_report(tables: Dict[str, pd.DataFrame], profile: LocalMaintenanceProfile) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    results = []

    r1 = validate_maintenance_domains(tables.get("domains"), profile)
    results.append({"check": "domain_validation", "passed": r1["valid"], "warnings": "; ".join(r1["warnings"])})

    r2 = validate_maintenance_tasks(tables.get("tasks"), profile)
    results.append({"check": "task_validation", "passed": r2["valid"], "warnings": "; ".join(r2["warnings"])})

    r3 = validate_refresh_commands(tables.get("commands"), profile)
    results.append({"check": "commands_validation", "passed": r3["valid"], "warnings": "; ".join(r3["warnings"])})

    df = pd.DataFrame(results)

    summary = {
        "total_checks": len(df),
        "passed_checks": len(df[df["passed"] == True]),
        "disclaimer": "Validation passed does not constitute a maintenance SLA."
    }
    return df, summary
