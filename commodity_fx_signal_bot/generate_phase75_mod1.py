import os
from pathlib import Path

base_dir = Path("c:/Users/immor/OneDrive/Belgeler/Projelerim/gptemtia/commodity_fx_signal_bot")
ls_dir = base_dir / "local_synthesis"
ls_dir.mkdir(parents=True, exist_ok=True)

(ls_dir / "__init__.py").touch(exist_ok=True)

# 1. synthesis_config.py
synthesis_config_content = """\
from dataclasses import dataclass
from typing import List

class ConfigError(Exception):
    pass

@dataclass(frozen=True)
class LocalSynthesisProfile:
    name: str
    description: str
    language: str = "tr"
    dry_run_default: bool = True
    allow_investment_advice: bool = False
    allow_live_trading_claim: bool = False
    allow_broker_readiness_claim: bool = False
    allow_production_release_claim: bool = False
    allow_model_deployment_claim: bool = False
    allow_official_completion_claim: bool = False
    allow_official_compliance_claim: bool = False
    allow_cloud_upload: bool = False
    allow_external_service: bool = False
    allow_external_llm: bool = False
    allow_file_modification: bool = False
    allow_file_deletion: bool = False
    allow_file_move: bool = False
    allow_overwrite: bool = False
    scan_docs: bool = True
    scan_reports: bool = True
    scan_data_lake: bool = True
    scan_scripts: bool = True
    scan_tests: bool = True
    scan_cross_layer_outputs: bool = True
    scan_safety_outputs: bool = True
    max_index_items: int = 500000
    max_sections: int = 10000
    min_quality_score: float = 0.40
    enabled: bool = True
    notes: str = ""

_profiles = {
    "balanced_local_synthesis": LocalSynthesisProfile(
        name="balanced_local_synthesis",
        description="Genel amaçlı local/offline final synthesis",
        language="tr",
        dry_run_default=True,
        max_index_items=500000,
        max_sections=10000,
        min_quality_score=0.40,
        notes="Genel amaçlı local/offline final synthesis, master index ve end-state documentation profili."
    ),
    "final_dossier_focus": LocalSynthesisProfile(
        name="final_dossier_focus",
        description="Dossier focus",
        language="tr",
        dry_run_default=True,
        max_sections=7000,
        notes="Project completion dossier, final binders ve end-state documentation odaklı profil."
    ),
    "master_index_focus": LocalSynthesisProfile(
        name="master_index_focus",
        description="Master index focus",
        language="tr",
        dry_run_default=True,
        max_index_items=500000,
        notes="Master artifact/report/DataLake/docs/scripts/tests index unification odaklı profil."
    ),
    "strict_final_safety": LocalSynthesisProfile(
        name="strict_final_safety",
        description="Strict safety",
        language="tr",
        dry_run_default=True,
        max_index_items=300000,
        max_sections=6000,
        min_quality_score=0.60,
        notes="Yatırım tavsiyesi, canlı trading, broker readiness, production release, official completion ve compliance overclaim denetimini sıkılaştıran profil."
    )
}

def get_local_synthesis_profile(name: str) -> LocalSynthesisProfile:
    if name not in _profiles:
        raise ConfigError(f"Bilinmeyen profil: {name}")
    return _profiles[name]

def list_local_synthesis_profiles(enabled_only: bool = True) -> List[LocalSynthesisProfile]:
    return [p for p in _profiles.values() if not enabled_only or p.enabled]

def validate_local_synthesis_profiles() -> None:
    for p in _profiles.values():
        if not p.language:
            raise ConfigError("language boş olmamalı.")
        if p.max_index_items <= 0 or p.max_sections <= 0:
            raise ConfigError("max_index_items ve max_sections pozitif olmalı.")
        if not (0.0 <= p.min_quality_score <= 1.0):
            raise ConfigError("min_quality_score 0-1 aralığında olmalı.")
        if not p.dry_run_default:
            raise ConfigError("Başlangıç profillerinde dry_run_default True olmalı.")
        if any([
            p.allow_investment_advice, p.allow_live_trading_claim, p.allow_broker_readiness_claim,
            p.allow_production_release_claim, p.allow_model_deployment_claim, p.allow_official_completion_claim,
            p.allow_official_compliance_claim, p.allow_cloud_upload, p.allow_external_service,
            p.allow_external_llm, p.allow_file_modification, p.allow_file_deletion, p.allow_file_move, p.allow_overwrite
        ]):
            raise ConfigError("Başlangıç profillerinde advice/live/broker vb. flagler False olmalı.")

def get_default_local_synthesis_profile() -> LocalSynthesisProfile:
    return _profiles["balanced_local_synthesis"]
"""
with open(ls_dir / "synthesis_config.py", "w", encoding="utf-8") as f: f.write(synthesis_config_content)

# 2. synthesis_labels.py
synthesis_labels_content = """\
from typing import List

_phase_family_labels = [
    "core_research_family", "data_storage_family", "reporting_family",
    "safety_governance_family", "metadata_evidence_family", "graph_timeline_family",
    "consistency_readiness_family", "maintenance_archive_dr_family",
    "training_briefing_family", "synthesis_family", "unknown_family"
]

_index_item_labels = [
    "artifact_index_item", "report_index_item", "datalake_index_item",
    "docs_index_item", "script_index_item", "test_index_item",
    "command_index_item", "generated_doc_index_item", "unknown_index_item"
]

_synthesis_status_labels = [
    "synthesis_ready", "synthesis_ready_with_warnings", "synthesis_missing",
    "synthesis_blocked_by_safety", "synthesis_needs_manual_review", "synthesis_unknown"
]

_closure_checklist_labels = [
    "closure_item_done", "closure_item_warning", "closure_item_missing",
    "closure_item_blocked", "closure_item_not_applicable", "closure_item_unknown"
]

_synthesis_risk_labels = [
    "synthesis_critical_risk", "synthesis_high_risk", "synthesis_medium_risk",
    "synthesis_low_risk", "synthesis_info", "synthesis_unknown_risk"
]

def list_phase_family_labels() -> List[str]: return _phase_family_labels.copy()
def list_index_item_labels() -> List[str]: return _index_item_labels.copy()
def list_synthesis_status_labels() -> List[str]: return _synthesis_status_labels.copy()
def list_closure_checklist_labels() -> List[str]: return _closure_checklist_labels.copy()
def list_synthesis_risk_labels() -> List[str]: return _synthesis_risk_labels.copy()

def validate_phase_family_label(label: str) -> None:
    if label not in _phase_family_labels: raise ValueError(f"Invalid {label}")
def validate_index_item_label(label: str) -> None:
    if label not in _index_item_labels: raise ValueError(f"Invalid {label}")
def validate_synthesis_status(label: str) -> None:
    if label not in _synthesis_status_labels: raise ValueError(f"Invalid {label}")
def validate_closure_checklist_label(label: str) -> None:
    if label not in _closure_checklist_labels: raise ValueError(f"Invalid {label}")
def validate_synthesis_risk(label: str) -> None:
    if label not in _synthesis_risk_labels: raise ValueError(f"Invalid {label}")
"""
with open(ls_dir / "synthesis_labels.py", "w", encoding="utf-8") as f: f.write(synthesis_labels_content)

# 3. synthesis_models.py
synthesis_models_content = """\
from dataclasses import dataclass, asdict
from typing import List, Optional

@dataclass
class PhaseFamily:
    family_id: str
    family_label: str
    family_name: str
    phase_range_hint: str
    description: str
    key_outputs: List[str]
    warnings: List[str]

@dataclass
class MasterIndexItem:
    item_id: str
    item_label: str
    relative_path: str
    family_label: str
    source_layer: str
    file_type: Optional[str]
    size_bytes: Optional[int]
    modified_at_utc: Optional[str]
    status: str
    warnings: List[str]

@dataclass
class FinalMapNode:
    node_id: str
    node_name: str
    family_label: str
    layer_name: str
    description: str
    related_outputs: List[str]
    warnings: List[str]

@dataclass
class FinalBinderSection:
    section_id: str
    section_title: str
    section_label: str
    summary: str
    references: List[str]
    warnings: List[str]

@dataclass
class SynthesisFinding:
    finding_id: str
    risk_label: str
    title: str
    description: str
    recommendation: str
    manual_review_required: bool
    warnings: List[str]

def build_phase_family_id(family_label: str) -> str: return f"fam_{family_label}"
def build_master_index_item_id(relative_path: str, item_label: str) -> str: return f"idx_{hash(relative_path)}_{item_label}"
def build_final_map_node_id(node_name: str, family_label: str) -> str: return f"node_{hash(node_name)}_{family_label}"
def build_final_binder_section_id(section_title: str) -> str: return f"sec_{hash(section_title)}"
def build_synthesis_finding_id(title: str) -> str: return f"fnd_{hash(title)}"

def phase_family_to_dict(item: PhaseFamily) -> dict: return asdict(item)
def master_index_item_to_dict(item: MasterIndexItem) -> dict: return asdict(item)
def final_map_node_to_dict(item: FinalMapNode) -> dict: return asdict(item)
def final_binder_section_to_dict(item: FinalBinderSection) -> dict: return asdict(item)
def synthesis_finding_to_dict(item: SynthesisFinding) -> dict: return asdict(item)
"""
with open(ls_dir / "synthesis_models.py", "w", encoding="utf-8") as f: f.write(synthesis_models_content)
