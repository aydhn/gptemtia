"""
Operating modes registry and logic.
"""

import pandas as pd
from master_orchestration.master_config import MasterOrchestrationProfile

_MODES = [
    {
        "mode_id": "daily_offline_review_mode",
        "purpose": "Daily review of offline signals and performance",
        "recommended_commands": ["run_system_healthcheck", "run_report_summary_registry", "run_quality_gates"],
        "run_frequency_suggestion": "Daily",
        "safety_notes": "Dry run only. Generates offline summaries."
    },
    {
        "mode_id": "weekly_offline_review_mode",
        "purpose": "Weekly deep dive into performance and reports",
        "recommended_commands": ["run_weekly_offline_review_pack", "run_performance"],
        "run_frequency_suggestion": "Weekly",
        "safety_notes": "Heavy computation."
    },
    {
        "mode_id": "monthly_maintenance_mode",
        "purpose": "Monthly maintenance and data cleaning",
        "recommended_commands": ["run_maintenance_checks"],
        "run_frequency_suggestion": "Monthly",
        "safety_notes": "Destructive cleanup not allowed. Read only."
    },
    {
        "mode_id": "full_audit_mode",
        "purpose": "Full system audit",
        "recommended_commands": ["run_quality_gates", "run_performance", "run_documentation_pack_report"],
        "run_frequency_suggestion": "Quarterly or on demand",
        "safety_notes": "Long running time."
    },
    {
        "mode_id": "scenario_demo_mode",
        "purpose": "Scenario tests and demo generation",
        "recommended_commands": ["run_scenarios"],
        "run_frequency_suggestion": "On demand",
        "safety_notes": "No real market data download in demo mode."
    },
    {
        "mode_id": "regression_check_mode",
        "purpose": "Check for system regressions",
        "recommended_commands": ["run_scenario_regression"],
        "run_frequency_suggestion": "Post code changes",
        "safety_notes": "Must pass before finalizing changes."
    },
    {
        "mode_id": "documentation_refresh_mode",
        "purpose": "Refresh all documentation",
        "recommended_commands": ["run_documentation_pack_report"],
        "run_frequency_suggestion": "Post documentation changes",
        "safety_notes": "Offline text generation."
    },
    {
        "mode_id": "quality_performance_maintenance_mode",
        "purpose": "Run QPM checks",
        "recommended_commands": ["run_quality_gates", "run_performance", "run_maintenance_checks"],
        "run_frequency_suggestion": "On demand",
        "safety_notes": "Comprehensive checks."
    },
    {
        "mode_id": "final_review_mode",
        "purpose": "Final pipeline review",
        "recommended_commands": ["run_final_review"],
        "run_frequency_suggestion": "Pre phase completion",
        "safety_notes": "Generates final phase outputs."
    },
    {
        "mode_id": "summary_briefing_mode",
        "purpose": "Generate executive and analyst briefs",
        "recommended_commands": ["run_analyst_brief_report", "run_executive_summary_report"],
        "run_frequency_suggestion": "Daily",
        "safety_notes": "No external LLMs."
    }
]

def build_operating_mode_registry(profile: MasterOrchestrationProfile) -> pd.DataFrame:
    return pd.DataFrame(_MODES)

def get_commands_for_operating_mode(mode: str, commands_df: pd.DataFrame, profile: MasterOrchestrationProfile) -> pd.DataFrame:
    if commands_df.empty:
        return pd.DataFrame()

    mode_info = next((m for m in _MODES if m["mode_id"] == mode), None)
    if not mode_info:
        return pd.DataFrame()

    recommended = mode_info["recommended_commands"]
    mask = commands_df["command_name"].apply(lambda x: any(cmd in x for cmd in recommended))
    return commands_df[mask]

def build_operating_mode_description(mode: str) -> dict:
    mode_info = next((m for m in _MODES if m["mode_id"] == mode), None)
    if not mode_info:
        return {"mode_id": mode, "purpose": "Unknown mode"}
    return mode_info

def validate_operating_modes(mode_df: pd.DataFrame, commands_df: pd.DataFrame) -> dict:
    if mode_df.empty:
        return {"valid": False, "warnings": ["Empty mode registry"]}
    return {"valid": True, "warnings": []}

def summarize_operating_modes(mode_df: pd.DataFrame) -> dict:
    if mode_df.empty:
        return {"total_modes": 0}
    return {
        "total_modes": len(mode_df),
        "modes": mode_df["mode_id"].tolist()
    }
