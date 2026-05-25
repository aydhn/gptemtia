"""
Quality validation for the Command Center.
"""

import pandas as pd
from typing import Dict
from command_center.command_config import CommandCenterProfile
from command_center.command_safety import detect_forbidden_command_terms

def check_for_forbidden_command_terms_in_command_center(text: str | None = None, df: pd.DataFrame | None = None, summary: dict | None = None) -> dict:
    all_terms = []

    if text:
        res = detect_forbidden_command_terms(text)
        if res["forbidden_terms_found"]:
            all_terms.extend(res["found_terms"])

    if df is not None and not df.empty:
        for col in df.columns:
            if df[col].dtype == object:
                for val in df[col].dropna():
                    if isinstance(val, str):
                        res = detect_forbidden_command_terms(val)
                        if res["forbidden_terms_found"]:
                            all_terms.extend(res["found_terms"])

    # simple summary check
    if summary:
        for k, v in summary.items():
            if isinstance(v, str):
                res = detect_forbidden_command_terms(v)
                if res["forbidden_terms_found"]:
                    all_terms.extend(res["found_terms"])

    return {
        "forbidden_terms_found": len(all_terms) > 0,
        "found_terms": list(set(all_terms))
    }

def check_command_registry_quality(commands_df: pd.DataFrame, profile: CommandCenterProfile) -> dict:
    if commands_df is None or commands_df.empty:
        return {"valid": False, "warnings": ["Command registry is empty."]}

    res = check_for_forbidden_command_terms_in_command_center(df=commands_df)
    if res["forbidden_terms_found"]:
        return {"valid": False, "warnings": [f"Forbidden terms found: {res['found_terms']}"]}

    return {"valid": True, "warnings": []}

def check_workflow_quality(workflows_df: pd.DataFrame) -> dict:
    if workflows_df is None or workflows_df.empty:
        return {"valid": False, "warnings": ["Workflows registry is empty."]}

    res = check_for_forbidden_command_terms_in_command_center(df=workflows_df)
    if res["forbidden_terms_found"]:
        return {"valid": False, "warnings": [f"Forbidden terms found: {res['found_terms']}"]}

    return {"valid": True, "warnings": []}

def check_runbook_quality(runbooks_df: pd.DataFrame) -> dict:
    if runbooks_df is None or runbooks_df.empty:
        return {"valid": False, "warnings": ["Runbooks registry is empty."]}

    res = check_for_forbidden_command_terms_in_command_center(df=runbooks_df)
    if res["forbidden_terms_found"]:
        return {"valid": False, "warnings": [f"Forbidden terms found: {res['found_terms']}"]}

    return {"valid": True, "warnings": []}

def check_dry_run_plan_quality(plan_df: pd.DataFrame) -> dict:
    if plan_df is None or plan_df.empty:
        return {"valid": False, "warnings": ["Dry run plan is empty."]}

    # Check for blocked commands specifically
    if "safety_label" in plan_df.columns:
        blocked = plan_df[plan_df["safety_label"] == "blocked"]
        if not blocked.empty:
            return {"valid": False, "warnings": [f"Plan contains {len(blocked)} blocked commands."]}

    res = check_for_forbidden_command_terms_in_command_center(df=plan_df)
    if res["forbidden_terms_found"]:
        return {"valid": False, "warnings": [f"Forbidden terms found: {res['found_terms']}"]}

    return {"valid": True, "warnings": []}

def check_project_status_quality(status_df: pd.DataFrame) -> dict:
    if status_df is None or status_df.empty:
        return {"valid": False, "warnings": ["Project status is empty."]}
    return {"valid": True, "warnings": []}

def build_command_center_quality_report(summary: dict, commands_df: pd.DataFrame | None = None, workflows_df: pd.DataFrame | None = None, runbooks_df: pd.DataFrame | None = None) -> dict:
    profile = summary.get("profile") # We assume the caller might pass the profile or we just mock

    cmd_qual = check_command_registry_quality(commands_df, profile) if commands_df is not None else {"valid": True, "warnings": []}
    wf_qual = check_workflow_quality(workflows_df) if workflows_df is not None else {"valid": True, "warnings": []}
    rb_qual = check_runbook_quality(runbooks_df) if runbooks_df is not None else {"valid": True, "warnings": []}

    warnings = cmd_qual["warnings"] + wf_qual["warnings"] + rb_qual["warnings"]

    return {
        "command_registry_valid": cmd_qual["valid"],
        "workflows_valid": wf_qual["valid"],
        "runbooks_valid": rb_qual["valid"],
        "dry_run_plan_valid": True, # Hardcoded for now unless passed
        "project_status_valid": True, # Hardcoded
        "forbidden_command_terms_found": len(warnings) > 0,
        "warning_count": len(warnings),
        "passed": len(warnings) == 0,
        "warnings": warnings
    }
