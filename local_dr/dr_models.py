from dataclasses import dataclass
from typing import Optional

@dataclass
class DRDomain:
    domain_id: str
    domain_label: str
    description: str
    criticality: str

@dataclass
class TabletopScenario:
    scenario_id: str
    domain_label: str
    scenario_name: str
    status: str
    details: str

@dataclass
class RestoreDrillSimulation:
    drill_id: str
    domain_label: str
    drill_name: str
    status: str
    paths_checked: list[str]

@dataclass
class FailureMode:
    failure_id: str
    domain_label: str
    failure_name: str
    severity: str

@dataclass
class DRFinding:
    finding_id: str
    domain_label: str
    title: str
    description: str

def build_dr_domain_id(domain_name: str) -> str:
    return f"dom_{domain_name.lower().replace(' ', '_')}"

def build_tabletop_scenario_id(scenario_name: str, domain_label: str) -> str:
    return f"scen_{domain_label}_{scenario_name.lower().replace(' ', '_')}"

def build_restore_drill_id(drill_name: str, domain_label: str) -> str:
    return f"drill_{domain_label}_{drill_name.lower().replace(' ', '_')}"

def build_failure_mode_id(domain_label: str, failure_name: str) -> str:
    return f"fail_{domain_label}_{failure_name.lower().replace(' ', '_')}"

def build_dr_finding_id(domain_label: str, title: str) -> str:
    return f"find_{domain_label}_{title.lower().replace(' ', '_')}"

def dr_domain_to_dict(item: DRDomain) -> dict:
    return {
        "domain_id": item.domain_id,
        "domain_label": item.domain_label,
        "description": item.description,
        "criticality": item.criticality,
    }

def tabletop_scenario_to_dict(item: TabletopScenario) -> dict:
    return {
        "scenario_id": item.scenario_id,
        "domain_label": item.domain_label,
        "scenario_name": item.scenario_name,
        "status": item.status,
        "details": item.details,
    }

def restore_drill_simulation_to_dict(item: RestoreDrillSimulation) -> dict:
    return {
        "drill_id": item.drill_id,
        "domain_label": item.domain_label,
        "drill_name": item.drill_name,
        "status": item.status,
        "paths_checked": item.paths_checked,
    }

def failure_mode_to_dict(item: FailureMode) -> dict:
    return {
        "failure_id": item.failure_id,
        "domain_label": item.domain_label,
        "failure_name": item.failure_name,
        "severity": item.severity,
    }

def dr_finding_to_dict(item: DRFinding) -> dict:
    return {
        "finding_id": item.finding_id,
        "domain_label": item.domain_label,
        "title": item.title,
        "description": item.description,
    }
