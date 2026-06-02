"""
Run order planner.
"""

import pandas as pd
from master_orchestration.master_config import MasterOrchestrationProfile

def build_recommended_run_order_for_mode(mode: str, commands_df: pd.DataFrame, profile: MasterOrchestrationProfile) -> pd.DataFrame:
    # A simple mock returning the commands for the mode with a sequence order
    if commands_df.empty:
        return pd.DataFrame()

    records = []
    order = 1
    for _, row in commands_df.iterrows():
        records.append({
            "run_order": order,
            "mode": mode,
            "command_name": row["command_name"],
            "command": row["command"],
            "safety_label": row["safety_label"]
        })
        order += 1

    return pd.DataFrame(records)

def build_daily_offline_operating_plan(commands_df: pd.DataFrame, profile: MasterOrchestrationProfile) -> tuple[pd.DataFrame, dict]:
    df = build_recommended_run_order_for_mode("daily_offline_review_mode", commands_df, profile)
    summary = {"plan": "daily", "total_steps": len(df)}
    return df, summary

def build_weekly_offline_operating_plan(commands_df: pd.DataFrame, profile: MasterOrchestrationProfile) -> tuple[pd.DataFrame, dict]:
    df = build_recommended_run_order_for_mode("weekly_offline_review_mode", commands_df, profile)
    summary = {"plan": "weekly", "total_steps": len(df)}
    return df, summary

def build_monthly_maintenance_plan(commands_df: pd.DataFrame, profile: MasterOrchestrationProfile) -> tuple[pd.DataFrame, dict]:
    df = build_recommended_run_order_for_mode("monthly_maintenance_mode", commands_df, profile)
    summary = {"plan": "monthly", "total_steps": len(df)}
    return df, summary

def build_full_audit_run_plan(commands_df: pd.DataFrame, profile: MasterOrchestrationProfile) -> tuple[pd.DataFrame, dict]:
    df = build_recommended_run_order_for_mode("full_audit_mode", commands_df, profile)
    summary = {"plan": "full_audit", "total_steps": len(df)}
    return df, summary

def build_specialized_run_plans(commands_df: pd.DataFrame, profile: MasterOrchestrationProfile) -> dict[str, pd.DataFrame]:
    plans = {}
    for mode in ["scenario_demo_mode", "regression_check_mode", "documentation_refresh_mode", "quality_performance_maintenance_mode", "final_review_mode", "summary_briefing_mode"]:
        plans[mode] = build_recommended_run_order_for_mode(mode, commands_df, profile)
    return plans

def summarize_run_order_plans(plans: dict[str, pd.DataFrame]) -> dict:
    summary = {}
    for k, v in plans.items():
        summary[k] = len(v)
    return summary
