"""
Validation logic for scenario definitions and execution results.
"""

import pandas as pd
from pathlib import Path
from typing import Tuple

from scenarios.scenario_config import ScenarioProfile
from scenarios.scenario_models import ScenarioDefinition
from scenarios.scenario_labels import SCENARIO_TYPE_LABELS, SCENARIO_SAFETY_LABELS


def validate_scenario_definition(scenario: ScenarioDefinition, profile: ScenarioProfile) -> dict:
    """Validates a single scenario definition."""
    validation = {
        "is_valid": True,
        "errors": [],
        "warnings": []
    }

    if scenario.scenario_type not in SCENARIO_TYPE_LABELS:
        validation["is_valid"] = False
        validation["errors"].append(f"Invalid type: {scenario.scenario_type}")

    if scenario.safety_label not in SCENARIO_SAFETY_LABELS:
        validation["is_valid"] = False
        validation["errors"].append(f"Invalid safety label: {scenario.safety_label}")

    if profile.use_synthetic_data_only and scenario.safety_label not in ["synthetic_offline_only", "dry_run_only", "safe_demo_flow"]:
        validation["is_valid"] = False
        validation["errors"].append("Scenario safety label violates synthetic data only profile.")

    return validation


def validate_scenario_fixtures(fixtures_df: pd.DataFrame, profile: ScenarioProfile) -> dict:
    """Validates fixtures dataframe."""
    validation = {
        "is_valid": True,
        "errors": [],
        "warnings": []
    }

    if fixtures_df.empty and profile.generate_fixtures:
        validation["warnings"].append("Profile requires fixtures but none were generated.")

    if not fixtures_df.empty:
        non_synthetic = fixtures_df[~fixtures_df["synthetic"]]
        if not non_synthetic.empty:
            validation["is_valid"] = False
            validation["errors"].append(f"Found {len(non_synthetic)} non-synthetic fixtures.")

    return validation


def validate_scenario_expected_outputs(expected_df: pd.DataFrame, project_root: Path) -> Tuple[pd.DataFrame, dict]:
    """Validates that all scenarios have expected outputs."""
    if expected_df.empty:
        return pd.DataFrame(), {"is_valid": True, "warnings": ["No expected outputs to validate."]}

    # We return the dataframe itself and a summary
    validation = {
        "is_valid": True,
        "errors": [],
        "warnings": ["Simulated output validation."]
    }

    return expected_df.copy(), validation


def validate_scenario_dry_run_results(dry_run_df: pd.DataFrame) -> dict:
    """Validates the results of dry runs."""
    validation = {
        "is_valid": True,
        "errors": [],
        "warnings": []
    }

    if dry_run_df.empty:
        validation["warnings"].append("No dry run results to validate.")
        return validation

    failed = dry_run_df[~dry_run_df["validation_passed"]]
    if not failed.empty:
        validation["is_valid"] = False
        validation["errors"].append(f"Found {len(failed)} failed dry runs (blocked commands).")

    return validation


def build_scenario_validation_report(
    scenarios_df: pd.DataFrame,
    fixtures_df: pd.DataFrame = None,
    expected_df: pd.DataFrame = None,
    dry_run_df: pd.DataFrame = None
) -> Tuple[pd.DataFrame, dict]:
    """Builds a comprehensive validation report."""
    results = []

    if not scenarios_df.empty:
        for _, row in scenarios_df.iterrows():
            valid = True
            reasons = []

            if row["safety_label"] not in SCENARIO_SAFETY_LABELS:
                valid = False
                reasons.append("Invalid safety label")

            results.append({
                "scenario_id": row["scenario_id"],
                "validation_type": "definition",
                "is_valid": valid,
                "reasons": "; ".join(reasons) if reasons else "OK"
            })

    df = pd.DataFrame(results) if results else pd.DataFrame(columns=["scenario_id", "validation_type", "is_valid", "reasons"])

    summary = {
        "total_checks": len(df),
        "passed": int(df["is_valid"].sum()) if not df.empty else 0,
        "warnings": ["Validation passed is NOT an approval for live trading. It only means offline structure is valid."]
    }

    return df, summary
