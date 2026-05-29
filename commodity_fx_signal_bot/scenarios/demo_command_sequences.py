"""
Safe command sequences for offline demo execution.
"""

import pandas as pd
from typing import Tuple, List

from scenarios.scenario_config import ScenarioProfile
from scenarios.scenario_models import ScenarioDefinition


BLOCKED_COMMAND_PATTERNS = [
    "live", "broker", "order", "buy", "sell", "open_position", "close_position",
    "deploy", "daemon", "server", "selenium", "playwright", "scraping", "trade"
]


def _is_safe(command: str) -> bool:
    """Checks if a command contains blocked patterns."""
    cmd_lower = command.lower()
    for pattern in BLOCKED_COMMAND_PATTERNS:
        # Check whole words to avoid blocking e.g., 'delivery'
        import re
        # Underscores are word characters in regex, so  broker  doesn't match send_broker_order
        # We can split by non-alphanumeric or just do a simple string check if it's safe enough,
        # but let's just do a simple substring check for the demo patterns
        if pattern in cmd_lower:
            return False
    return True


def build_safe_demo_command_sequence(scenario: ScenarioDefinition, profile: ScenarioProfile) -> pd.DataFrame:
    """Builds a sequence of safe commands for a scenario."""
    commands = []

    # Base command: check status
    commands.append("python -m scripts.run_observability_status")

    if "research_planning" in scenario.modules:
        commands.append("python -m scripts.run_research_planning_status")
    if "governance" in scenario.modules:
        commands.append("python -m scripts.run_governance_status")
    if "knowledge_base" in scenario.modules:
        commands.append("python -m scripts.run_knowledge_index_report")
    if "experiments" in scenario.modules:
        commands.append("python -m scripts.run_experiment_status")

    records = []
    for i, cmd in enumerate(commands):
        safe = _is_safe(cmd)
        records.append({
            "scenario_id": scenario.scenario_id,
            "step_number": i + 1,
            "command": cmd,
            "is_safe": safe,
            "blocked_reason": "Contains blocked pattern." if not safe else None
        })

    return pd.DataFrame(records)


def build_all_demo_command_sequences(scenarios: List[ScenarioDefinition], profile: ScenarioProfile) -> Tuple[pd.DataFrame, dict]:
    """Builds command sequences for all scenarios."""
    all_records = []

    for scenario in scenarios:
        seq_df = build_safe_demo_command_sequence(scenario, profile)
        if not seq_df.empty:
            all_records.extend(seq_df.to_dict(orient="records"))

    if all_records:
        df = pd.DataFrame(all_records)
    else:
        df = pd.DataFrame(columns=["scenario_id", "step_number", "command", "is_safe", "blocked_reason"])

    summary = {
        "total_commands": len(df),
        "safe_commands": int(df["is_safe"].sum()) if not df.empty else 0,
        "blocked_commands": int((~df["is_safe"]).sum()) if not df.empty else 0,
        "warnings": ["Commands are for offline demonstration only."]
    }

    return df, summary


def validate_demo_command_sequence(command_df: pd.DataFrame) -> dict:
    """Validates that all commands in a sequence are safe."""
    validation = {
        "is_valid": True,
        "errors": [],
        "warnings": []
    }

    if command_df.empty:
        validation["warnings"].append("Command sequence is empty.")
        return validation

    blocked = command_df[~command_df["is_safe"]]
    if not blocked.empty:
        validation["is_valid"] = False
        validation["errors"].append(f"Found {len(blocked)} blocked commands.")

    if validation["is_valid"]:
        validation["warnings"].append("All commands passed safety filter.")

    return validation


def summarize_demo_command_sequences(command_df: pd.DataFrame) -> dict:
    """Summarizes the command sequences."""
    if command_df.empty:
        return {"total": 0}

    return {
        "total_commands": len(command_df),
        "unique_scenarios": int(command_df["scenario_id"].nunique()),
        "safe_count": int(command_df["is_safe"].sum()),
        "blocked_count": int((~command_df["is_safe"]).sum()),
        "warnings": ["These are safe offline commands."]
    }
