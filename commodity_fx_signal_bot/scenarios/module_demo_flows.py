"""
Module-specific demonstration flows for offline use.
"""

import pandas as pd
from typing import Tuple

from scenarios.scenario_config import ScenarioProfile


_DEMO_MODULES = [
    "research_reports", "report_exports", "portfolio_research",
    "portfolio_regime", "synthetic_indices", "factor_research",
    "meta_research", "experiments", "governance", "research_planning",
    "knowledge_base", "command_center", "quality_gates", "performance",
    "maintenance", "documentation", "final_review", "scenarios"
]


def build_module_demo_flow(module_name: str, profile: ScenarioProfile) -> dict:
    """Builds a dry-run demonstration flow for a single module."""
    clean_name = module_name.replace(" ", "_").lower()

    return {
        "module_name": module_name,
        "purpose": f"Demonstrate the offline capabilities of the {module_name} module.",
        "safe_commands": [
            f"python -m scripts.run_{clean_name}_status" if clean_name not in ["scenarios", "documentation"] else f"python -m scripts.run_{clean_name}_report"
        ],
        "expected_outputs": [f"{clean_name}_report.md"],
        "prerequisites": ["Synthetic sample data generated", "Data Lake structure initialized"],
        "synthetic_fixture_usage": True,
        "troubleshooting": f"If the flow fails, ensure that synthetic data is present in data/lake/{clean_name}.",
        "warnings": ["This is an offline demo. No live data or trading instructions are generated."]
    }


def build_all_module_demo_flows(profile: ScenarioProfile) -> Tuple[pd.DataFrame, dict]:
    """Builds demo flows for all configured modules."""
    flows = [build_module_demo_flow(mod, profile) for mod in _DEMO_MODULES]
    df = pd.DataFrame(flows)

    summary = {
        "total_modules": len(_DEMO_MODULES),
        "flows_generated": len(flows),
        "warnings": ["These flows are purely for demonstration and offline research."]
    }

    return df, summary


def validate_module_demo_flow(flow: dict) -> dict:
    """Validates a single demo flow."""
    validation = {
        "is_valid": True,
        "errors": [],
        "warnings": []
    }

    if not flow.get("synthetic_fixture_usage", False):
        validation["is_valid"] = False
        validation["errors"].append(f"Module flow {flow.get('module_name')} does not explicitly use synthetic fixtures.")

    for cmd in flow.get("safe_commands", []):
        if "live" in cmd or "broker" in cmd or "deploy" in cmd or "daemon" in cmd:
            validation["is_valid"] = False
            validation["errors"].append(f"Blocked term found in command: {cmd}")

    return validation


def summarize_module_demo_flows(flow_df: pd.DataFrame) -> dict:
    """Summarizes all module demo flows."""
    if flow_df.empty:
        return {"total_flows": 0}

    return {
        "total_flows": len(flow_df),
        "modules_covered": flow_df["module_name"].tolist(),
        "warnings": ["Demonstration flows are safe and offline."]
    }
