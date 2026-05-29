"""
Data models for scenarios and case studies.
"""

from dataclasses import dataclass, asdict
from typing import List, Dict, Optional
import hashlib
import json


@dataclass
class ScenarioDefinition:
    scenario_id: str
    scenario_name: str
    scenario_type: str
    status: str
    safety_label: str
    description: str
    symbols: List[str]
    timeframe: str
    modules: List[str]
    fixture_paths: List[str]
    expected_output_paths: List[str]
    command_sequence_ids: List[str]
    warnings: List[str]


@dataclass
class ScenarioFixture:
    fixture_id: str
    scenario_id: str
    fixture_name: str
    fixture_type: str
    path: str
    row_count: Optional[int]
    symbols: List[str]
    generated_at_utc: str
    synthetic: bool
    warnings: List[str]


@dataclass
class ScenarioExpectedOutput:
    expected_output_id: str
    scenario_id: str
    output_name: str
    output_type: str
    required: bool
    path_pattern: str
    validation_rule: str
    warnings: List[str]


@dataclass
class ScenarioDryRunResult:
    dry_run_id: str
    scenario_id: str
    scenario_name: str
    started_at_utc: str
    finished_at_utc: Optional[str]
    status: str
    executed_commands: List[str]
    blocked_commands: List[str]
    produced_outputs: List[str]
    validation_passed: bool
    warnings: List[str]


@dataclass
class CaseStudy:
    case_study_id: str
    title: str
    case_study_label: str
    scenario_ids: List[str]
    objective: str
    steps: List[Dict]
    expected_learning: str
    warnings: List[str]


def _hash_string(val: str) -> str:
    """Helper to generate deterministic hash."""
    return hashlib.sha256(val.encode("utf-8")).hexdigest()[:12]


def build_scenario_id(scenario_name: str, scenario_type: str) -> str:
    """Builds a deterministic scenario ID."""
    clean_name = scenario_name.replace(" ", "_").lower()
    clean_type = scenario_type.replace(" ", "_").lower()
    return f"scn_{clean_type}_{clean_name}_{_hash_string(clean_name)}"


def build_fixture_id(scenario_id: str, fixture_name: str) -> str:
    """Builds a deterministic fixture ID."""
    clean_name = fixture_name.replace(" ", "_").lower()
    return f"fix_{scenario_id}_{clean_name}_{_hash_string(clean_name)}"


def build_expected_output_id(scenario_id: str, output_name: str) -> str:
    """Builds a deterministic expected output ID."""
    clean_name = output_name.replace(" ", "_").lower()
    return f"out_{scenario_id}_{clean_name}_{_hash_string(clean_name)}"


def build_dry_run_id(scenario_id: str, started_at_utc: str) -> str:
    """Builds a deterministic dry run ID."""
    return f"run_{scenario_id}_{_hash_string(started_at_utc)}"


def build_case_study_id(title: str, case_study_label: str) -> str:
    """Builds a deterministic case study ID."""
    clean_title = title.replace(" ", "_").lower()
    clean_label = case_study_label.replace(" ", "_").lower()
    return f"cst_{clean_label}_{_hash_string(clean_title)}"


def scenario_definition_to_dict(definition: ScenarioDefinition) -> dict:
    """Converts a ScenarioDefinition to a dictionary."""
    return asdict(definition)


def scenario_fixture_to_dict(fixture: ScenarioFixture) -> dict:
    """Converts a ScenarioFixture to a dictionary."""
    return asdict(fixture)


def scenario_expected_output_to_dict(output: ScenarioExpectedOutput) -> dict:
    """Converts a ScenarioExpectedOutput to a dictionary."""
    return asdict(output)


def scenario_dry_run_result_to_dict(result: ScenarioDryRunResult) -> dict:
    """Converts a ScenarioDryRunResult to a dictionary."""
    return asdict(result)


def case_study_to_dict(case_study: CaseStudy) -> dict:
    """Converts a CaseStudy to a dictionary."""
    return asdict(case_study)
