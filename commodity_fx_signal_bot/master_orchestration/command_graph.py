"""
Command graph and safe command registry.
"""

import pandas as pd
from pathlib import Path
from master_orchestration.master_config import MasterOrchestrationProfile
from master_orchestration.master_labels import validate_meta_runner_safety

_FORBIDDEN_TERMS = [
    "live order", "broker order", "real trade", "open position",
    "close position", "buy now", "sell now", "deploy model",
    "production deploy", "production scheduler", "background daemon",
    "while true", "run live", "external llm", "openai api",
    "real market download", "selenium", "playwright", "beautifulsoup"
]

def collect_safe_commands_from_existing_layers(project_root: Path) -> pd.DataFrame:
    # Collect mock commands to represent existing layers
    records = [
        {"command": "python -m scripts.run_system_healthcheck", "module": "observability"},
        {"command": "python -m scripts.run_report_summary_registry", "module": "report_summarization"},
        {"command": "python -m scripts.run_quality_gates", "module": "quality_gates"},
        {"command": "python -m scripts.run_master_orchestration_map", "module": "master_orchestration"},
    ]
    return pd.DataFrame(records)

def build_master_command_registry(project_root: Path, profile: MasterOrchestrationProfile) -> pd.DataFrame:
    df = collect_safe_commands_from_existing_layers(project_root)
    if df.empty:
        return pd.DataFrame(columns=["command_id", "command_name", "command", "module_name", "safety_label"])

    registry = []
    for _, row in df.iterrows():
        cmd = row["command"]
        module = row["module"]
        cmd_name = cmd.split(".")[-1] if "." in cmd else cmd
        safety = classify_master_command_safety(cmd, profile)

        registry.append({
            "command_id": f"cmd_{module}_{cmd_name}",
            "command_name": cmd_name,
            "command": cmd,
            "module_name": module,
            "safety_label": safety
        })
    return pd.DataFrame(registry)

def build_command_dependency_graph(commands_df: pd.DataFrame) -> pd.DataFrame:
    if commands_df.empty:
        return pd.DataFrame(columns=["source_command", "target_command"])

    # Mock dependencies
    records = []
    # For now just an empty map
    return pd.DataFrame(columns=["source_command", "target_command"])

def classify_master_command_safety(command: str, profile: MasterOrchestrationProfile) -> str:
    cmd_lower = command.lower()
    for term in _FORBIDDEN_TERMS:
        if term in cmd_lower:
            if "live order" in cmd_lower or "real trade" in cmd_lower: return "blocked_live"
            if "broker" in cmd_lower: return "blocked_broker"
            if "deploy" in cmd_lower: return "blocked_deploy"
            if "daemon" in cmd_lower or "while true" in cmd_lower: return "blocked_daemon"
            if "llm" in cmd_lower or "openai" in cmd_lower: return "blocked_external_llm"
            if "download" in cmd_lower: return "blocked_real_market_download"
            return "unsafe_unknown"

    return "safe_offline_executable_if_explicit" if profile.allow_execute else "safe_dry_run_only"

def validate_master_command_registry(commands_df: pd.DataFrame, profile: MasterOrchestrationProfile) -> dict:
    if commands_df.empty:
        return {"valid": True, "warnings": ["Empty command registry"]}

    warnings = []
    for _, row in commands_df.iterrows():
        safety = row["safety_label"]
        validate_meta_runner_safety(safety)
        if "blocked" in safety:
            warnings.append(f"Command {row['command_name']} is blocked: {safety}")

    return {"valid": len(warnings) == 0, "warnings": warnings}

def summarize_command_graph(commands_df: pd.DataFrame, graph_df: pd.DataFrame) -> dict:
    return {
        "total_commands": len(commands_df),
        "total_edges": len(graph_df),
        "blocked_commands": len(commands_df[commands_df["safety_label"].str.contains("blocked")]) if not commands_df.empty else 0
    }
