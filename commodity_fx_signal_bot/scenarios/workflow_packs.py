"""
Workflow packs for composing scenario steps.
"""

import pandas as pd
from typing import Tuple, Dict

from scenarios.scenario_config import ScenarioProfile


def _build_workflow(workflow_name: str, s_type: str, objective: str, steps: list, commands: list) -> dict:
    clean_name = workflow_name.replace(" ", "_").lower()
    return {
        "workflow_id": f"wf_{clean_name}",
        "workflow_name": workflow_name,
        "scenario_type": s_type,
        "objective": objective,
        "steps": steps,
        "safe_commands": commands,
        "expected_outputs": ["markdown_report", "csv_output"],
        "limitations": ["Offline only.", "Synthetic data only."],
        "warnings": ["Workflow is an offline scenario. Do not run with live broker."]
    }


def build_symbol_research_workflow_pack(symbol: str, profile: ScenarioProfile) -> dict:
    return _build_workflow(
        f"symbol_research_{symbol}",
        "symbol_research_scenario",
        f"Evaluate offline signal candidates for {symbol}",
        [
            "Load synthetic OHLCV data",
            "Calculate offline indicators",
            "Generate pre-signal candidates",
            "Export candidate report"
        ],
        [
            f"python -m scripts.run_universe_preview --symbols {symbol}",
            f"python -m scripts.run_self_diagnostics"
        ]
    )


def build_governance_review_workflow_pack(profile: ScenarioProfile) -> dict:
    return _build_workflow(
        "governance_review",
        "governance_scenario",
        "Review offline governance status and provenance",
        [
            "Check dataset provenance",
            "Check code checksums",
            "Generate governance report"
        ],
        [
            "python -m scripts.run_governance_status"
        ]
    )


def build_experiment_review_workflow_pack(profile: ScenarioProfile) -> dict:
    return _build_workflow(
        "experiment_review",
        "experiment_tracking_scenario",
        "Review active offline experiments",
        [
            "List active experiments",
            "Check ablation results",
            "Generate experiment report"
        ],
        [
            "python -m scripts.run_experiment_status"
        ]
    )


def build_planning_review_workflow_pack(profile: ScenarioProfile) -> dict:
    return _build_workflow(
        "planning_review",
        "planning_scenario",
        "Review research planning backlog",
        [
            "List open backlog items",
            "Check next best action",
            "Generate planning report"
        ],
        [
            "python -m scripts.run_research_planning_status"
        ]
    )


def build_knowledge_query_workflow_pack(symbol: str, profile: ScenarioProfile) -> dict:
    return _build_workflow(
        f"knowledge_query_{symbol}",
        "knowledge_base_scenario",
        f"Query offline knowledge base for {symbol}",
        [
            "Build knowledge index",
            "Run query",
            "Export query report"
        ],
        [
            f"python -m scripts.run_research_query --query 'What do we know about {symbol}?'"
        ]
    )


def build_maintenance_dry_run_workflow_pack(profile: ScenarioProfile) -> dict:
    return _build_workflow(
        "maintenance_dry_run",
        "maintenance_scenario",
        "Dry-run maintenance operations",
        [
            "Check orphaned files",
            "Check stale caches",
            "Generate maintenance report"
        ],
        [
            "python -m scripts.run_maintenance_status"
        ]
    )


def build_final_review_workflow_pack(profile: ScenarioProfile) -> dict:
    return _build_workflow(
        "final_review_dry_run",
        "final_review_scenario",
        "Dry-run final safety review",
        [
            "Run security checks",
            "Run performance checks",
            "Run validation checks",
            "Generate final review report"
        ],
        [
            "python -m scripts.run_final_review_status"
        ]
    )


def build_default_workflow_packs(profile: ScenarioProfile) -> Tuple[pd.DataFrame, dict]:
    """Builds a set of default workflow packs based on the profile."""
    packs = []

    packs.append(build_symbol_research_workflow_pack("GC=F", profile))
    packs.append(build_governance_review_workflow_pack(profile))
    packs.append(build_experiment_review_workflow_pack(profile))
    packs.append(build_planning_review_workflow_pack(profile))
    packs.append(build_knowledge_query_workflow_pack("CL=F", profile))
    packs.append(build_maintenance_dry_run_workflow_pack(profile))
    packs.append(build_final_review_workflow_pack(profile))

    df = pd.DataFrame(packs)

    summary = {
        "total_packs": len(packs),
        "profile": profile.name,
        "warnings": ["All workflows are offline dry-runs."]
    }

    return df, summary
