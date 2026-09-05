from dataclasses import dataclass, asdict
from typing import List

@dataclass
class TerminalCloseoutDomain:
    domain_id: str
    domain_label: str
    domain_name: str
    description: str
    required_outputs: List[str]
    warnings: List[str]

@dataclass
class TerminalCloseoutItem:
    closeout_id: str
    closeout_area: str
    closeout_title: str
    source_ref: str
    status_label: str
    manual_review_required: bool
    warnings: List[str]

@dataclass
class UltimateLedgerItem:
    ledger_id: str
    ledger_area: str
    ledger_title: str
    source_ref: str
    output_ref: str
    ledger_status: str
    warnings: List[str]

@dataclass
class GovernanceSealItem:
    seal_id: str
    seal_area: str
    seal_title: str
    seal_status: str
    boundary_note: str
    manual_review_required: bool
    warnings: List[str]

@dataclass
class ArchiveCatalogItem:
    archive_id: str
    archive_area: str
    archive_title: str
    source_ref: str
    catalog_status: str
    exclusion_reason: str
    warnings: List[str]

@dataclass
class HandoverConstitutionItem:
    constitution_id: str
    constitution_area: str
    constitution_title: str
    constitution_status: str
    boundary_note: str
    warnings: List[str]

@dataclass
class TerminalCloseoutFinding:
    finding_id: str
    risk_label: str
    title: str
    description: str
    recommendation: str
    manual_review_required: bool
    warnings: List[str]

def build_terminal_closeout_domain_id(domain_label: str) -> str:
    return f"dom_{domain_label}"

def build_terminal_closeout_item_id(closeout_area: str, closeout_title: str) -> str:
    return f"co_{closeout_area}_{closeout_title}".replace(" ", "_").lower()

def build_ultimate_ledger_item_id(ledger_area: str, ledger_title: str) -> str:
    return f"led_{ledger_area}_{ledger_title}".replace(" ", "_").lower()

def build_governance_seal_item_id(seal_area: str, seal_title: str) -> str:
    return f"seal_{seal_area}_{seal_title}".replace(" ", "_").lower()

def build_archive_catalog_item_id(archive_area: str, archive_title: str) -> str:
    return f"arc_{archive_area}_{archive_title}".replace(" ", "_").lower()

def build_handover_constitution_item_id(constitution_area: str, constitution_title: str) -> str:
    return f"hc_{constitution_area}_{constitution_title}".replace(" ", "_").lower()

def build_terminal_closeout_finding_id(title: str) -> str:
    return f"find_{title}".replace(" ", "_").lower()

def terminal_closeout_domain_to_dict(item: TerminalCloseoutDomain) -> dict:
    return asdict(item)

def terminal_closeout_item_to_dict(item: TerminalCloseoutItem) -> dict:
    return asdict(item)

def ultimate_ledger_item_to_dict(item: UltimateLedgerItem) -> dict:
    return asdict(item)

def governance_seal_item_to_dict(item: GovernanceSealItem) -> dict:
    return asdict(item)

def archive_catalog_item_to_dict(item: ArchiveCatalogItem) -> dict:
    return asdict(item)

def handover_constitution_item_to_dict(item: HandoverConstitutionItem) -> dict:
    return asdict(item)

def terminal_closeout_finding_to_dict(item: TerminalCloseoutFinding) -> dict:
    return asdict(item)
