from dataclasses import dataclass
import hashlib

@dataclass
class RedTeamDomain:
    domain_id: str
    domain_label: str
    domain_name: str
    description: str
    required_outputs: list[str]
    warnings: list[str]

@dataclass
class MisuseScenario:
    scenario_id: str
    scenario_name: str
    misuse_category: str
    abstract_description: str
    unsafe_request_pattern: str
    expected_safe_response: str
    manual_review_required: bool
    warnings: list[str]

@dataclass
class AbuseCaseSimulation:
    simulation_id: str
    simulation_name: str
    misuse_category: str
    simulated_condition: str
    expected_boundary: str
    expected_response_label: str
    dry_run_only: bool
    warnings: list[str]

@dataclass
class SafetyChecklistItem:
    checklist_id: str
    checklist_area: str
    check_name: str
    expected_result: str
    blocking_if_failed: bool
    warnings: list[str]

@dataclass
class RedTeamFinding:
    finding_id: str
    risk_label: str
    title: str
    description: str
    recommendation: str
    manual_review_required: bool
    warnings: list[str]

def build_redteam_domain_id(domain_label: str) -> str:
    s = f"redteam_domain_{domain_label}"
    return hashlib.md5(s.encode()).hexdigest()[:12]

def build_misuse_scenario_id(scenario_name: str, misuse_category: str) -> str:
    s = f"misuse_scenario_{scenario_name}_{misuse_category}"
    return hashlib.md5(s.encode()).hexdigest()[:12]

def build_abuse_case_simulation_id(simulation_name: str, misuse_category: str) -> str:
    s = f"abuse_case_simulation_{simulation_name}_{misuse_category}"
    return hashlib.md5(s.encode()).hexdigest()[:12]

def build_safety_checklist_item_id(checklist_area: str, check_name: str) -> str:
    s = f"safety_checklist_{checklist_area}_{check_name}"
    return hashlib.md5(s.encode()).hexdigest()[:12]

def build_redteam_finding_id(title: str) -> str:
    s = f"redteam_finding_{title}"
    return hashlib.md5(s.encode()).hexdigest()[:12]

def redteam_domain_to_dict(item: RedTeamDomain) -> dict:
    return {
        "domain_id": item.domain_id,
        "domain_label": item.domain_label,
        "domain_name": item.domain_name,
        "description": item.description,
        "required_outputs": "|".join(item.required_outputs),
        "warnings": "|".join(item.warnings)
    }

def misuse_scenario_to_dict(item: MisuseScenario) -> dict:
    return {
        "scenario_id": item.scenario_id,
        "scenario_name": item.scenario_name,
        "misuse_category": item.misuse_category,
        "abstract_description": item.abstract_description,
        "unsafe_request_pattern": item.unsafe_request_pattern,
        "expected_safe_response": item.expected_safe_response,
        "manual_review_required": item.manual_review_required,
        "warnings": "|".join(item.warnings)
    }

def abuse_case_simulation_to_dict(item: AbuseCaseSimulation) -> dict:
    return {
        "simulation_id": item.simulation_id,
        "simulation_name": item.simulation_name,
        "misuse_category": item.misuse_category,
        "simulated_condition": item.simulated_condition,
        "expected_boundary": item.expected_boundary,
        "expected_response_label": item.expected_response_label,
        "dry_run_only": item.dry_run_only,
        "warnings": "|".join(item.warnings)
    }

def safety_checklist_item_to_dict(item: SafetyChecklistItem) -> dict:
    return {
        "checklist_id": item.checklist_id,
        "checklist_area": item.checklist_area,
        "check_name": item.check_name,
        "expected_result": item.expected_result,
        "blocking_if_failed": item.blocking_if_failed,
        "warnings": "|".join(item.warnings)
    }

def redteam_finding_to_dict(item: RedTeamFinding) -> dict:
    return {
        "finding_id": item.finding_id,
        "risk_label": item.risk_label,
        "title": item.title,
        "description": item.description,
        "recommendation": item.recommendation,
        "manual_review_required": item.manual_review_required,
        "warnings": "|".join(item.warnings)
    }
