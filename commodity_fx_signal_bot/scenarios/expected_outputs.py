"""
Expected outputs contracts for scenario dry runs.
"""

import pandas as pd
from pathlib import Path
from typing import List, Tuple

from scenarios.scenario_models import ScenarioDefinition, ScenarioExpectedOutput, build_expected_output_id


def build_expected_outputs_for_scenario(scenario: ScenarioDefinition) -> List[ScenarioExpectedOutput]:
    """Defines the expected output contracts for a given scenario."""
    outputs = []

    # Generic status report expected for all scenarios
    out_id = build_expected_output_id(scenario.scenario_id, "status_report")
    outputs.append(ScenarioExpectedOutput(
        expected_output_id=out_id,
        scenario_id=scenario.scenario_id,
        output_name="status_report",
        output_type="status_report",
        required=False,
        path_pattern=f"*{scenario.scenario_id}_status.txt",
        validation_rule="file_exists_optional",
        warnings=["Status report is optional."]
    ))

    # Module-specific expected outputs
    if "governance" in scenario.modules:
        out_id = build_expected_output_id(scenario.scenario_id, "governance_manifest")
        outputs.append(ScenarioExpectedOutput(
            expected_output_id=out_id,
            scenario_id=scenario.scenario_id,
            output_name="governance_manifest",
            output_type="json_manifest",
            required=True,
            path_pattern="*governance*.json",
            validation_rule="file_exists_required",
            warnings=["Governance manifest required."]
        ))

    if "signals" in scenario.modules:
        out_id = build_expected_output_id(scenario.scenario_id, "signal_candidates")
        outputs.append(ScenarioExpectedOutput(
            expected_output_id=out_id,
            scenario_id=scenario.scenario_id,
            output_name="signal_candidates",
            output_type="csv_output",
            required=True,
            path_pattern="*signal_candidates*.csv",
            validation_rule="expected_columns_present",
            warnings=["Signal candidates must not contain LIVE orders."]
        ))

    return outputs


def build_expected_output_contracts(scenarios: List[ScenarioDefinition]) -> pd.DataFrame:
    """Builds a DataFrame of all expected output contracts."""
    all_outputs = []
    for scenario in scenarios:
        outputs = build_expected_outputs_for_scenario(scenario)
        all_outputs.extend([out.__dict__ for out in outputs])

    if all_outputs:
        return pd.DataFrame(all_outputs)
    else:
        return pd.DataFrame(columns=[
            "expected_output_id", "scenario_id", "output_name", "output_type",
            "required", "path_pattern", "validation_rule", "warnings"
        ])


def validate_expected_outputs(scenario_id: str, expected_df: pd.DataFrame, project_root: Path) -> Tuple[pd.DataFrame, dict]:
    """Validates if expected outputs for a scenario actually exist."""
    if expected_df.empty:
        return pd.DataFrame(), {"warnings": ["No expected outputs to validate."]}

    scenario_outputs = expected_df[expected_df["scenario_id"] == scenario_id].copy()
    if scenario_outputs.empty:
        return pd.DataFrame(), {"warnings": [f"No expected outputs defined for scenario {scenario_id}."]}

    validation_results = []

    # In a real validation, we would use project_root.rglob(path_pattern)
    # Here we just simulate validation
    for _, row in scenario_outputs.iterrows():
        is_valid = True
        warnings = list(row["warnings"])

        if row["validation_rule"] == "file_exists_required":
            warnings.append(f"Simulated validation passed for {row['output_name']}.")

        validation_results.append({
            "expected_output_id": row["expected_output_id"],
            "is_valid": is_valid,
            "validation_details": "Simulated check.",
            "warnings": warnings
        })

    results_df = pd.DataFrame(validation_results)

    summary = {
        "scenario_id": scenario_id,
        "total_checked": len(results_df),
        "total_valid": int(results_df["is_valid"].sum()),
        "warnings": ["Expected outputs validation is a simulated dry-run check."]
    }

    return results_df, summary


def summarize_expected_outputs(expected_df: pd.DataFrame) -> dict:
    """Summarizes the expected outputs DataFrame."""
    if expected_df.empty:
        return {"total_contracts": 0}

    return {
        "total_contracts": len(expected_df),
        "required_contracts": int(expected_df["required"].sum()),
        "by_type": expected_df["output_type"].value_counts().to_dict(),
        "warnings": ["These are expected outputs for offline scenarios, not live trading artifacts."]
    }
