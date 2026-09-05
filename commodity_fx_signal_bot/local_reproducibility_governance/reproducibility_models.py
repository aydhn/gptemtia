"""Reproducibility models."""
from dataclasses import dataclass, asdict
import hashlib

@dataclass
class ReproducibilityDomain:
    domain_id: str
    domain_label: str
    domain_name: str
    description: str
    required_outputs: list[str]
    warnings: list[str]

@dataclass
class ReproducibilityDossierItem:
    dossier_id: str
    item_name: str
    source_ref: str
    output_ref: str
    status_label: str
    manual_review_required: bool
    warnings: list[str]

@dataclass
class EnvironmentReplayItem:
    replay_id: str
    replay_area: str
    replay_name: str
    replay_status: str
    boundary_note: str
    manual_review_required: bool
    warnings: list[str]

@dataclass
class DeterministicRunbookItem:
    runbook_id: str
    command_family: str
    command_ref: str
    expected_output_family: str
    determinism_label: str
    manual_review_required: bool
    warnings: list[str]

@dataclass
class BuildFreeReproductionItem:
    reproduction_id: str
    reproduction_area: str
    source_ref: str
    output_ref: str
    build_free_boundary: str
    warnings: list[str]

@dataclass
class ReproducibilityFinding:
    finding_id: str
    risk_label: str
    title: str
    description: str
    recommendation: str
    manual_review_required: bool
    warnings: list[str]

def build_reproducibility_domain_id(domain_label: str) -> str:
    h = hashlib.sha256(domain_label.encode()).hexdigest()[:8]
    return f"dom_{h}"

def build_reproducibility_dossier_item_id(item_name: str, source_ref: str) -> str:
    h = hashlib.sha256(f"{item_name}_{source_ref}".encode()).hexdigest()[:8]
    return f"dos_{h}"

def build_environment_replay_item_id(replay_area: str, replay_name: str) -> str:
    h = hashlib.sha256(f"{replay_area}_{replay_name}".encode()).hexdigest()[:8]
    return f"rep_{h}"

def build_deterministic_runbook_item_id(command_family: str, command_ref: str) -> str:
    h = hashlib.sha256(f"{command_family}_{command_ref}".encode()).hexdigest()[:8]
    return f"run_{h}"

def build_build_free_reproduction_item_id(reproduction_area: str, source_ref: str) -> str:
    h = hashlib.sha256(f"{reproduction_area}_{source_ref}".encode()).hexdigest()[:8]
    return f"bfr_{h}"

def build_reproducibility_finding_id(title: str) -> str:
    h = hashlib.sha256(title.encode()).hexdigest()[:8]
    return f"fnd_{h}"

def reproducibility_domain_to_dict(item: ReproducibilityDomain) -> dict:
    return asdict(item)

def reproducibility_dossier_item_to_dict(item: ReproducibilityDossierItem) -> dict:
    return asdict(item)

def environment_replay_item_to_dict(item: EnvironmentReplayItem) -> dict:
    return asdict(item)

def deterministic_runbook_item_to_dict(item: DeterministicRunbookItem) -> dict:
    return asdict(item)

def build_free_reproduction_item_to_dict(item: BuildFreeReproductionItem) -> dict:
    return asdict(item)

def reproducibility_finding_to_dict(item: ReproducibilityFinding) -> dict:
    return asdict(item)
