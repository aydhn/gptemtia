"""Atlas models module."""
from dataclasses import dataclass
import hashlib

@dataclass
class AtlasDomain:
    domain_id: str
    domain_label: str
    domain_name: str
    description: str
    required_outputs: list[str]
    warnings: list[str]

@dataclass
class MetaIndexItem:
    index_id: str
    title: str
    item_path: str
    item_family: str
    phase_ref: str
    lookup_family: str
    summary: str
    warnings: list[str]

@dataclass
class NavigationItem:
    nav_id: str
    route_label: str
    nav_title: str
    nav_area: str
    target_ref: str
    reading_priority: int
    manual_review_required: bool
    warnings: list[str]

@dataclass
class LookupItem:
    lookup_id: str
    lookup_key: str
    lookup_family: str
    source_ref: str
    target_ref: str
    relation_type: str
    warnings: list[str]

@dataclass
class AtlasCrosswalkItem:
    crosswalk_id: str
    crosswalk_area: str
    source_concept: str
    target_concept: str
    interpretation_note: str
    warnings: list[str]

@dataclass
class AtlasFinding:
    finding_id: str
    risk_label: str
    title: str
    description: str
    recommendation: str
    manual_review_required: bool
    warnings: list[str]

def _hash(*args) -> str:
    s = "|".join(str(a) for a in args)
    return hashlib.sha256(s.encode()).hexdigest()[:12]

def build_atlas_domain_id(domain_label: str) -> str:
    return f"dom_{_hash(domain_label)}"

def build_meta_index_item_id(item_path: str, item_family: str, phase_ref: str) -> str:
    return f"idx_{_hash(item_path, item_family, phase_ref)}"

def build_navigation_item_id(route_label: str, nav_title: str) -> str:
    return f"nav_{_hash(route_label, nav_title)}"

def build_lookup_item_id(lookup_key: str, lookup_family: str, target_ref: str) -> str:
    return f"lkp_{_hash(lookup_key, lookup_family, target_ref)}"

def build_atlas_crosswalk_item_id(crosswalk_area: str, source_concept: str, target_concept: str) -> str:
    return f"cw_{_hash(crosswalk_area, source_concept, target_concept)}"

def build_atlas_finding_id(title: str) -> str:
    return f"fnd_{_hash(title)}"

def atlas_domain_to_dict(item: AtlasDomain) -> dict:
    return {
        "domain_id": item.domain_id,
        "domain_label": item.domain_label,
        "domain_name": item.domain_name,
        "description": item.description,
        "required_outputs": ",".join(item.required_outputs),
        "warnings": ",".join(item.warnings)
    }

def meta_index_item_to_dict(item: MetaIndexItem) -> dict:
    return {
        "index_id": item.index_id,
        "title": item.title,
        "item_path": item.item_path,
        "item_family": item.item_family,
        "phase_ref": item.phase_ref,
        "lookup_family": item.lookup_family,
        "summary": item.summary,
        "warnings": ",".join(item.warnings)
    }

def navigation_item_to_dict(item: NavigationItem) -> dict:
    return {
        "nav_id": item.nav_id,
        "route_label": item.route_label,
        "nav_title": item.nav_title,
        "nav_area": item.nav_area,
        "target_ref": item.target_ref,
        "reading_priority": item.reading_priority,
        "manual_review_required": item.manual_review_required,
        "warnings": ",".join(item.warnings)
    }

def lookup_item_to_dict(item: LookupItem) -> dict:
    return {
        "lookup_id": item.lookup_id,
        "lookup_key": item.lookup_key,
        "lookup_family": item.lookup_family,
        "source_ref": item.source_ref,
        "target_ref": item.target_ref,
        "relation_type": item.relation_type,
        "warnings": ",".join(item.warnings)
    }

def atlas_crosswalk_item_to_dict(item: AtlasCrosswalkItem) -> dict:
    return {
        "crosswalk_id": item.crosswalk_id,
        "crosswalk_area": item.crosswalk_area,
        "source_concept": item.source_concept,
        "target_concept": item.target_concept,
        "interpretation_note": item.interpretation_note,
        "warnings": ",".join(item.warnings)
    }

def atlas_finding_to_dict(item: AtlasFinding) -> dict:
    return {
        "finding_id": item.finding_id,
        "risk_label": item.risk_label,
        "title": item.title,
        "description": item.description,
        "recommendation": item.recommendation,
        "manual_review_required": item.manual_review_required,
        "warnings": ",".join(item.warnings)
    }
