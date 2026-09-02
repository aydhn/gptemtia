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
