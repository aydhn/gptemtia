import pandas as pd
from typing import Tuple, List, Dict, Any

from local_maintenance.maintenance_config import LocalMaintenanceProfile

def build_dependency_review_items(dep_df: pd.DataFrame, profile: LocalMaintenanceProfile) -> List[Dict[str, Any]]:
    items = [
        {
            "check_item": "dependency file exists",
            "description": "Ensure requirements.txt or pyproject.toml exists.",
            "status": "pending"
        },
        {
            "check_item": "pinned versions present",
            "description": "Verify all critical dependencies have pinned versions.",
            "status": "pending"
        },
        {
            "check_item": "optional deps documented",
            "description": "Ensure optional dependencies are properly documented.",
            "status": "pending"
        },
        {
            "check_item": "sklearn/networkx fallback documented",
            "description": "Check if fallbacks for heavy ML/graph libraries are documented.",
            "status": "pending"
        },
        {
            "check_item": "no unnecessary external services",
            "description": "Confirm no external cloud services are required.",
            "status": "pending"
        },
        {
            "check_item": "no OpenAI/external LLM requirement",
            "description": "Ensure no external LLMs are listed as hard requirements.",
            "status": "pending"
        },
        {
            "check_item": "no broker/live dependency required",
            "description": "Verify no live trading or broker libraries are required.",
            "status": "pending"
        },
        {
            "check_item": "update manually if needed",
            "description": "Dependencies should be updated manually, not via an auto-updater.",
            "status": "pending"
        },
        {
            "check_item": "run tests after manual update",
            "description": "Run the test suite manually after any dependency updates.",
            "status": "pending"
        }
    ]
    return items

def build_dependency_review_checklist(dep_df: pd.DataFrame, profile: LocalMaintenanceProfile) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    items = build_dependency_review_items(dep_df, profile)
    df = pd.DataFrame(items)
    summary = summarize_dependency_review(df)
    return df, summary

def summarize_dependency_review(review_df: pd.DataFrame) -> Dict[str, Any]:
    if review_df is None or review_df.empty:
        return {"total_checks": 0}

    return {
        "total_checks": len(review_df),
        "disclaimer": "This is a manual review checklist. It does not produce an upgrade command."
    }
