import os
from pathlib import Path

base_dir = Path("commodity_fx_signal_bot/local_project_atlas")
base_dir.mkdir(parents=True, exist_ok=True)

with open(base_dir / "atlas_labels.py", "w", encoding="utf-8") as f:
    f.write('''"""Atlas labels module."""

_ATLAS_DOMAIN_LABELS = [
    "meta_index_domain", "universal_navigation_domain", "cross_phase_lookup_domain",
    "semantic_toc_domain", "terminal_project_atlas_domain", "family_map_domain",
    "phase_map_domain", "route_map_domain", "glossary_domain", "crosswalk_domain",
    "quality_validation_domain", "unknown_atlas_domain"
]

_ATLAS_STATUS_LABELS = [
    "atlas_rehearsal_ready", "atlas_rehearsal_ready_with_warnings", "atlas_rehearsal_missing",
    "atlas_rehearsal_blocked_by_safety", "atlas_rehearsal_needs_manual_review", "atlas_rehearsal_unknown"
]

_LOOKUP_FAMILY_LABELS = [
    "lookup_docs", "lookup_scripts", "lookup_reports", "lookup_datalake",
    "lookup_generated_docs", "lookup_tests", "lookup_safety_boundary", "lookup_unknown"
]

_ATLAS_ROUTE_LABELS = [
    "route_operator", "route_analyst", "route_maintainer", "route_codex_agent",
    "route_future_reader", "route_unknown"
]

_ATLAS_RISK_LABELS = [
    "atlas_critical_risk", "atlas_high_risk", "atlas_medium_risk", "atlas_low_risk",
    "atlas_info", "atlas_unknown_risk"
]

def list_atlas_domain_labels() -> list[str]:
    return _ATLAS_DOMAIN_LABELS

def list_atlas_status_labels() -> list[str]:
    return _ATLAS_STATUS_LABELS

def list_lookup_family_labels() -> list[str]:
    return _LOOKUP_FAMILY_LABELS

def list_atlas_route_labels() -> list[str]:
    return _ATLAS_ROUTE_LABELS

def list_atlas_risk_labels() -> list[str]:
    return _ATLAS_RISK_LABELS

def validate_atlas_domain_label(label: str) -> None:
    if label not in _ATLAS_DOMAIN_LABELS:
        raise ValueError(f"Invalid atlas domain label: {label}")

def validate_atlas_status(label: str) -> None:
    if label not in _ATLAS_STATUS_LABELS:
        raise ValueError(f"Invalid atlas status label: {label}")

def validate_lookup_family(label: str) -> None:
    if label not in _LOOKUP_FAMILY_LABELS:
        raise ValueError(f"Invalid lookup family label: {label}")

def validate_atlas_route(label: str) -> None:
    if label not in _ATLAS_ROUTE_LABELS:
        raise ValueError(f"Invalid atlas route label: {label}")

def validate_atlas_risk(label: str) -> None:
    if label not in _ATLAS_RISK_LABELS:
        raise ValueError(f"Invalid atlas risk label: {label}")
''')

with open(base_dir / "atlas_models.py", "w", encoding="utf-8") as f:
    f.write('''"""Atlas models module."""
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
''')

with open(base_dir / "atlas_domain_registry.py", "w", encoding="utf-8") as f:
    f.write('''"""Atlas domain registry module."""
import pandas as pd
from .atlas_config import LocalProjectAtlasProfile
from .atlas_models import AtlasDomain, build_atlas_domain_id, atlas_domain_to_dict

def build_default_atlas_domains(profile: LocalProjectAtlasProfile) -> list[AtlasDomain]:
    domains = []
    labels = [
        "meta_index_domain", "universal_navigation_domain", "cross_phase_lookup_domain",
        "semantic_toc_domain", "terminal_project_atlas_domain", "family_map_domain",
        "phase_map_domain", "route_map_domain", "glossary_domain", "crosswalk_domain",
        "quality_validation_domain"
    ]
    for lbl in labels:
        domains.append(AtlasDomain(
            domain_id=build_atlas_domain_id(lbl),
            domain_label=lbl,
            domain_name=lbl.replace("_", " ").title(),
            description=f"{lbl} domain for offline project atlas. Not enterprise search or official index.",
            required_outputs=["none"],
            warnings=["Offline context only."]
        ))
    return domains

def build_atlas_domain_registry(profile: LocalProjectAtlasProfile) -> tuple[pd.DataFrame, dict]:
    domains = build_default_atlas_domains(profile)
    df = pd.DataFrame([atlas_domain_to_dict(d) for d in domains])
    summary = summarize_atlas_domains(df)
    return df, summary

def summarize_atlas_domains(domain_df: pd.DataFrame) -> dict:
    return {
        "total_domains": len(domain_df),
        "domain_labels": domain_df["domain_label"].unique().tolist() if not domain_df.empty else []
    }
''')

with open(base_dir / "meta_index.py", "w", encoding="utf-8") as f:
    f.write('''"""Final local meta-index module."""
import os
from pathlib import Path
import pandas as pd
from .atlas_config import LocalProjectAtlasProfile
from .atlas_models import MetaIndexItem, build_meta_index_item_id, meta_index_item_to_dict

def classify_meta_index_item(path: Path, project_root: Path, profile: LocalProjectAtlasProfile) -> dict:
    try:
        rel_path = str(path.relative_to(project_root)).replace("\\\\", "/")
    except ValueError:
        rel_path = str(path).replace("\\\\", "/")
        
    item_family = "unknown"
    lookup_family = "lookup_unknown"
    
    if "docs/" in rel_path:
        item_family = "docs"
        lookup_family = "lookup_docs"
    elif "scripts/" in rel_path:
        item_family = "scripts"
        lookup_family = "lookup_scripts"
    elif "reports/" in rel_path:
        item_family = "reports"
        lookup_family = "lookup_reports"
    elif "data/lake/" in rel_path:
        item_family = "datalake"
        lookup_family = "lookup_datalake"
    elif "tests/" in rel_path:
        item_family = "tests"
        lookup_family = "lookup_tests"

    return {
        "title": path.name,
        "item_path": rel_path,
        "item_family": item_family,
        "phase_ref": "various",
        "lookup_family": lookup_family,
        "summary": f"Offline file: {path.name}",
        "exists": path.exists(),
        "size_bytes": path.stat().st_size if path.exists() else 0,
        "manual_review_required": False,
        "warnings": ["Not official knowledge index."]
    }

def discover_meta_index_items(project_root: Path, profile: LocalProjectAtlasProfile) -> pd.DataFrame:
    items = []
    
    for root, dirs, files in os.walk(project_root):
        if ".git" in root or "__pycache__" in root or "venv" in root:
            continue
            
        for file in files:
            p = Path(root) / file
            if not p.is_file():
                continue
            
            info = classify_meta_index_item(p, project_root, profile)
            
            if info["item_family"] == "unknown":
                continue

            item = MetaIndexItem(
                index_id=build_meta_index_item_id(info["item_path"], info["item_family"], info["phase_ref"]),
                title=info["title"],
                item_path=info["item_path"],
                item_family=info["item_family"],
                phase_ref=info["phase_ref"],
                lookup_family=info["lookup_family"],
                summary=info["summary"],
                warnings=info["warnings"]
            )
            
            d = meta_index_item_to_dict(item)
            d["exists"] = info["exists"]
            d["size_bytes"] = info["size_bytes"]
            d["manual_review_required"] = info["manual_review_required"]
            items.append(d)
            
            if len(items) >= profile.max_items:
                break
        if len(items) >= profile.max_items:
            break
            
    return pd.DataFrame(items)

def build_final_local_meta_index(project_root: Path, profile: LocalProjectAtlasProfile) -> tuple[pd.DataFrame, dict]:
    df = discover_meta_index_items(project_root, profile)
    summary = summarize_meta_index(df)
    return df, summary

def summarize_meta_index(df: pd.DataFrame) -> dict:
    return {
        "total_items": len(df),
        "total_size_bytes": int(df["size_bytes"].sum()) if not df.empty else 0,
        "families": df["item_family"].unique().tolist() if not df.empty else []
    }

def save_meta_index(df: pd.DataFrame, output_path: Path) -> Path:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(output_path, index=False)
    return output_path
''')

with open(base_dir / "universal_navigation.py", "w", encoding="utf-8") as f:
    f.write('''"""Universal navigation map module."""
import pandas as pd
from .atlas_config import LocalProjectAtlasProfile
from .atlas_models import NavigationItem, build_navigation_item_id, navigation_item_to_dict

def build_default_navigation_items(profile: LocalProjectAtlasProfile) -> list[NavigationItem]:
    items = []
    routes = ["route_operator", "route_analyst", "route_maintainer", "route_codex_agent", "route_future_reader", "route_quality", "route_safety"]
    for r in routes:
        items.append(NavigationItem(
            nav_id=build_navigation_item_id(r, f"Start for {r}"),
            route_label=r,
            nav_title=f"{r} entry point",
            nav_area="general",
            target_ref="README.md",
            reading_priority=1,
            manual_review_required=True,
            warnings=["Not official SOP."]
        ))
    return items

def build_universal_navigation_map(profile: LocalProjectAtlasProfile) -> tuple[pd.DataFrame, dict]:
    items = build_default_navigation_items(profile)
    df = pd.DataFrame([navigation_item_to_dict(i) for i in items])
    return df, summarize_universal_navigation(df)

def summarize_universal_navigation(df: pd.DataFrame) -> dict:
    return {
        "total_routes": len(df["route_label"].unique()) if not df.empty else 0,
        "total_items": len(df)
    }
''')

print("Created core1")
