"""
End-to-End offline demo composer.
"""

import pandas as pd
from typing import Tuple

from scenarios.scenario_config import ScenarioProfile


def build_end_to_end_offline_demo_plan(profile: ScenarioProfile) -> pd.DataFrame:
    """Builds the execution plan for the E2E offline demo."""
    steps = [
        {"step": 1, "action": "scenario registry oluştur", "command": "python -m scripts.run_scenario_registry_report"},
        {"step": 2, "action": "synthetic sample data oluştur", "command": "python -m scripts.run_sample_data_builder"},
        {"step": 3, "action": "scenario fixtures oluştur", "command": "[Internal Pipeline Step]"},
        {"step": 4, "action": "knowledge index oluştur", "command": "python -m scripts.run_knowledge_index_report"},
        {"step": 5, "action": "governance status kontrol et", "command": "python -m scripts.run_governance_status"},
        {"step": 6, "action": "experiment status kontrol et", "command": "python -m scripts.run_experiment_status"},
        {"step": 7, "action": "planning status kontrol et", "command": "python -m scripts.run_research_planning_status"},
        {"step": 8, "action": "command catalog kontrol et", "command": "python -m scripts.run_command_catalog_report"},
        {"step": 9, "action": "quality gate status kontrol et", "command": "python -m scripts.run_quality_gate_status"},
        {"step": 10, "action": "performance status kontrol et", "command": "python -m scripts.run_performance_status"},
        {"step": 11, "action": "maintenance status kontrol et", "command": "python -m scripts.run_maintenance_status"},
        {"step": 12, "action": "documentation status kontrol et", "command": "python -m scripts.run_documentation_pack_report"},
        {"step": 13, "action": "final review status kontrol et", "command": "python -m scripts.run_final_review_status"},
        {"step": 14, "action": "scenario validation raporu üret", "command": "python -m scripts.run_scenario_dry_run"}
    ]
    return pd.DataFrame(steps)


def build_end_to_end_demo_expected_outputs(profile: ScenarioProfile) -> pd.DataFrame:
    """Defines the expected outputs for the E2E demo."""
    outputs = [
        {"output_name": "scenario_registry.csv", "required": True},
        {"output_name": "sample_data_manifest.csv", "required": True},
        {"output_name": "scenario_validation.csv", "required": True},
        {"output_name": "end_to_end_demo_report.json", "required": True}
    ]
    return pd.DataFrame(outputs)


def build_end_to_end_demo_report(
    plan_df: pd.DataFrame,
    expected_df: pd.DataFrame,
    validation_summary: dict = None
) -> Tuple[str, dict]:
    """Builds the final E2E demo JSON/Dict report."""
    report = {
        "title": "End-to-End Offline Demo Report",
        "description": "Comprehensive offline demonstration of the research system.",
        "plan_steps": plan_df.to_dict(orient="records") if not plan_df.empty else [],
        "expected_outputs": expected_df.to_dict(orient="records") if not expected_df.empty else [],
        "validation_summary": validation_summary or {},
        "warnings": ["This is an offline demonstration. It does not evaluate live market conditions or produce live trades."]
    }

    # We return JSON string and dict summary
    import json
    return json.dumps(report, indent=4), report


def summarize_end_to_end_demo(plan_df: pd.DataFrame) -> dict:
    """Summarizes the E2E demo plan."""
    if plan_df.empty:
        return {"total_steps": 0}

    return {
        "total_steps": len(plan_df),
        "commands_to_run": len([c for c in plan_df["command"] if c != "[Internal Pipeline Step]"]),
        "warnings": ["End-to-end demo is not for production acceptance."]
    }
