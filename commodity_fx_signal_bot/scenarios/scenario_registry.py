"""
Scenario registry for tracking and managing scenario definitions.
"""

from pathlib import Path
from typing import Dict, List, Optional
import pandas as pd
import json

from scenarios.scenario_config import ScenarioProfile
from scenarios.scenario_models import ScenarioDefinition, build_scenario_id, scenario_definition_to_dict
from scenarios.scenario_labels import validate_scenario_type, validate_scenario_status, validate_scenario_safety

class ScenarioRegistryError(Exception):
    pass


class ScenarioRegistry:
    def __init__(self, registry_dir: Path):
        self.registry_dir = registry_dir
        self.registry_dir.mkdir(parents=True, exist_ok=True)
        self.scenarios: Dict[str, ScenarioDefinition] = {}

    def add_scenario(self, scenario: ScenarioDefinition) -> Path:
        """Adds a scenario to the registry and returns the path where it would be saved (if we save it individually)."""
        validate_scenario_type(scenario.scenario_type)
        validate_scenario_status(scenario.status)
        validate_scenario_safety(scenario.safety_label)

        self.scenarios[scenario.scenario_id] = scenario
        return self.registry_dir / f"{scenario.scenario_id}.json"

    def load_scenarios(self) -> pd.DataFrame:
        """Returns the loaded scenarios as a DataFrame."""
        return scenario_definitions_to_dataframe(list(self.scenarios.values()))

    def get_scenario(self, scenario_id: str) -> Optional[dict]:
        """Returns a single scenario by ID as a dictionary."""
        scenario = self.scenarios.get(scenario_id)
        if scenario:
            return scenario_definition_to_dict(scenario)
        return None

    def list_by_type(self, scenario_type: str) -> pd.DataFrame:
        """Filters scenarios by type."""
        filtered = [s for s in self.scenarios.values() if s.scenario_type == scenario_type]
        return scenario_definitions_to_dataframe(filtered)

    def list_by_module(self, module_name: str) -> pd.DataFrame:
        """Filters scenarios by module involved."""
        filtered = [s for s in self.scenarios.values() if module_name in s.modules]
        return scenario_definitions_to_dataframe(filtered)

    def summarize(self) -> dict:
        """Summarizes the registry contents."""
        return {
            "total_scenarios": len(self.scenarios),
            "by_type": pd.Series([s.scenario_type for s in self.scenarios.values()]).value_counts().to_dict() if self.scenarios else {},
            "by_status": pd.Series([s.status for s in self.scenarios.values()]).value_counts().to_dict() if self.scenarios else {},
            "by_safety": pd.Series([s.safety_label for s in self.scenarios.values()]).value_counts().to_dict() if self.scenarios else {}
        }


def build_default_scenarios(profile: ScenarioProfile) -> List[ScenarioDefinition]:
    """Builds the default offline synthetic scenarios."""
    scenarios = []

    defaults = [
        ("GC=F synthetic trend research scenario", "symbol_research_scenario", ["GC=F"], ["signals", "indicators"]),
        ("USDTRY=X synthetic inflation comparison scenario", "symbol_research_scenario", ["USDTRY=X"], ["macro", "indicators"]),
        ("factor conflict synthetic scenario", "factor_research_scenario", ["GC=F", "CL=F"], ["factor_research", "signals"]),
        ("meta consensus disagreement scenario", "meta_research_scenario", ["SI=F", "HG=F"], ["meta_research"]),
        ("portfolio concentration synthetic scenario", "portfolio_research_scenario", ["GC=F", "SI=F", "CL=F"], ["portfolio_research"]),
        ("governance missing provenance scenario", "governance_scenario", ["GC=F"], ["governance"]),
        ("experiment ablation dry-run scenario", "experiment_tracking_scenario", ["CL=F"], ["experiments"]),
        ("planning backlog warning scenario", "planning_scenario", [], ["research_planning"]),
        ("knowledge query symbol memory scenario", "knowledge_base_scenario", ["GC=F"], ["knowledge_base"]),
        ("command center safe command query scenario", "command_center_scenario", [], ["command_center"]),
        ("maintenance cleanup dry-run scenario", "maintenance_scenario", [], ["maintenance"]),
        ("final review safety audit scenario", "final_review_scenario", [], ["final_review"]),
        ("end-to-end offline research scenario", "end_to_end_scenario", ["GC=F", "CL=F"], ["orchestration", "observability"])
    ]

    for name, s_type, symbols, modules in defaults:
        sid = build_scenario_id(name, s_type)
        scenarios.append(ScenarioDefinition(
            scenario_id=sid,
            scenario_name=name,
            scenario_type=s_type,
            status="scenario_planned",
            safety_label="synthetic_offline_only",
            description=f"Default synthetic offline scenario for {name}.",
            symbols=symbols,
            timeframe=profile.scenario_default_timeframe,
            modules=modules,
            fixture_paths=[],
            expected_output_paths=[],
            command_sequence_ids=[],
            warnings=["Offline synthetic scenario. Do not use for live trading."]
        ))

    return scenarios


def scenario_definitions_to_dataframe(scenarios: List[ScenarioDefinition]) -> pd.DataFrame:
    """Converts a list of scenarios to a Pandas DataFrame."""
    if not scenarios:
        return pd.DataFrame(columns=[
            "scenario_id", "scenario_name", "scenario_type", "status", "safety_label",
            "description", "symbols", "timeframe", "modules", "fixture_paths",
            "expected_output_paths", "command_sequence_ids", "warnings"
        ])
    return pd.DataFrame([scenario_definition_to_dict(s) for s in scenarios])
