from dataclasses import dataclass, asdict

@dataclass
class FinalClosingDomain:
    domain_id: str
    domain_label: str
    domain_name: str
    description: str
    required_outputs: list[str]
    warnings: list[str]

@dataclass
class FinalTerminalLockItem:
    lock_id: str
    lock_area: str
    lock_title: str
    source_ref: str
    status_label: str
    manual_review_required: bool
    warnings: list[str]

@dataclass
class ProjectConstitutionItem:
    constitution_id: str
    constitution_area: str
    constitution_title: str
    constitution_status: str
    boundary_note: str
    manual_review_required: bool
    warnings: list[str]

@dataclass
class NonProductionSealItem:
    seal_id: str
    seal_area: str
    seal_title: str
    seal_status: str
    boundary_note: str
    manual_review_required: bool
    warnings: list[str]

@dataclass
class TerminalArchiveIndexItem:
    archive_index_id: str
    archive_area: str
    archive_title: str
    source_ref: str
    output_ref: str
    exclusion_reason: str
    warnings: list[str]

@dataclass
class ClosingGovernanceFinding:
    finding_id: str
    risk_label: str
    title: str
    description: str
    recommendation: str
    manual_review_required: bool
    warnings: list[str]

def build_final_closing_domain_id(domain_label: str) -> str:
    return f"FCD-{domain_label}"

def build_final_terminal_lock_item_id(lock_area: str, lock_title: str) -> str:
    return f"FTL-{lock_area}-{lock_title}".replace(" ", "_").lower()

def build_project_constitution_item_id(constitution_area: str, constitution_title: str) -> str:
    return f"UPC-{constitution_area}-{constitution_title}".replace(" ", "_").lower()

def build_non_production_seal_item_id(seal_area: str, seal_title: str) -> str:
    return f"NPS-{seal_area}-{seal_title}".replace(" ", "_").lower()

def build_terminal_archive_index_item_id(archive_area: str, archive_title: str) -> str:
    return f"TAI-{archive_area}-{archive_title}".replace(" ", "_").lower()

def build_closing_governance_finding_id(title: str) -> str:
    return f"CGF-{title}".replace(" ", "_").lower()

def final_closing_domain_to_dict(item: FinalClosingDomain) -> dict:
    return asdict(item)

def final_terminal_lock_item_to_dict(item: FinalTerminalLockItem) -> dict:
    return asdict(item)

def project_constitution_item_to_dict(item: ProjectConstitutionItem) -> dict:
    return asdict(item)

def non_production_seal_item_to_dict(item: NonProductionSealItem) -> dict:
    return asdict(item)

def terminal_archive_index_item_to_dict(item: TerminalArchiveIndexItem) -> dict:
    return asdict(item)

def closing_governance_finding_to_dict(item: ClosingGovernanceFinding) -> dict:
    return asdict(item)
