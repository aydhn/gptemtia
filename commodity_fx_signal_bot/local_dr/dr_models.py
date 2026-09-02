
from dataclasses import dataclass

@dataclass
class DRDomain:
    domain_id: str
    domain_name: str
    domain_label: str
    description: str
    required_artifacts: list[str]
    warnings: list[str]

@dataclass
class TabletopScenario:
    scenario_id: str
    scenario_name: str
    domain_label: str
    description: str
    failure_mode: str
    expected_manual_response: str
    status: str
    warnings: list[str]

@dataclass
class RestoreDrillSimulation:
    drill_id: str
    drill_name: str
    domain_label: str
    source_manifest: str | None
    expected_artifacts: list[str]
    simulated_steps: list[str]
    status: str
    warnings: list[str]

@dataclass
class FailureMode:
    failure_id: str
    domain_label: str
    failure_name: str
    severity: str
    detection_hint: str
    manual_response: str
    prevention_hint: str
    warnings: list[str]

@dataclass
class DRFinding:
    finding_id: str
    domain_label: str
    risk_label: str
    title: str
    description: str
    recommendation: str
    manual_review_required: bool
    warnings: list[str]

def build_dr_domain_id(domain_name: str) -> str:
    return domain_name.lower().replace(" ", "_")

def build_tabletop_scenario_id(scenario_name: str, domain_label: str) -> str:
    return scenario_name.lower().replace(" ", "_")

def build_restore_drill_id(drill_name: str, domain_label: str) -> str:
    return drill_name.lower().replace(" ", "_")

def build_failure_mode_id(domain_label: str, failure_name: str) -> str:
    return failure_name.lower().replace(" ", "_")

def build_dr_finding_id(domain_label: str, title: str) -> str:
    return title.lower().replace(" ", "_")

def dr_domain_to_dict(item: DRDomain) -> dict:
    return item.__dict__
def tabletop_scenario_to_dict(item: TabletopScenario) -> dict:
    return item.__dict__
def restore_drill_simulation_to_dict(item: RestoreDrillSimulation) -> dict:
    return item.__dict__
def failure_mode_to_dict(item: FailureMode) -> dict:
    return item.__dict__
def dr_finding_to_dict(item: DRFinding) -> dict:
    return item.__dict__
