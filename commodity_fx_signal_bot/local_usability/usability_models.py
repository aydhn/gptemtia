from dataclasses import dataclass
from typing import Any

@dataclass
class UsabilityDomain:
    domain_id: str
    domain_label: str
    domain_name: str
    description: str
    required_outputs: list[str]
    warnings: list[str]

@dataclass
class OperatorFrictionItem:
    friction_id: str
    friction_area: str
    source_layer: str
    friction_label: str
    description: str
    recommended_manual_action: str
    warnings: list[str]

@dataclass
class OperatorTaskJourney:
    journey_id: str
    journey_name: str
    path_label: str
    steps: list[str]
    expected_outputs: list[str]
    manual_review_required: bool
    warnings: list[str]

@dataclass
class CommandGuideItem:
    command_id: str
    command_name: str
    command_family: str
    purpose: str
    when_to_run: str
    when_not_to_run: str
    safety_notes: list[str]
    warnings: list[str]

@dataclass
class UsabilityFinding:
    finding_id: str
    risk_label: str
    title: str
    description: str
    recommendation: str
    manual_review_required: bool
    warnings: list[str]

import hashlib

def _hash(s: str) -> str:
    return hashlib.md5(s.encode("utf-8")).hexdigest()[:8]

def build_usability_domain_id(domain_label: str) -> str:
    return f"dom_{domain_label}_{_hash(domain_label)}"

def build_operator_friction_id(friction_area: str, source_layer: str) -> str:
    return f"fric_{_hash(friction_area + source_layer)}"

def build_operator_task_journey_id(journey_name: str) -> str:
    return f"jour_{_hash(journey_name)}"

def build_command_guide_item_id(command_name: str) -> str:
    return f"cmd_{_hash(command_name)}"

def build_usability_finding_id(title: str) -> str:
    return f"find_{_hash(title)}"

def usability_domain_to_dict(item: UsabilityDomain) -> dict:
    return item.__dict__

def operator_friction_item_to_dict(item: OperatorFrictionItem) -> dict:
    return item.__dict__

def operator_task_journey_to_dict(item: OperatorTaskJourney) -> dict:
    return item.__dict__

def command_guide_item_to_dict(item: CommandGuideItem) -> dict:
    return item.__dict__

def usability_finding_to_dict(item: UsabilityFinding) -> dict:
    return item.__dict__
