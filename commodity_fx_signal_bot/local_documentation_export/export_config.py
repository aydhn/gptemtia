"""Export config."""
from dataclasses import dataclass
from typing import List

class ConfigError(Exception):
    pass

@dataclass(frozen=True)
class LocalDocumentationExportProfile:
    name: str
    description: str
    language: str = "tr"
    dry_run_default: bool = True
    allow_real_static_site_deploy: bool = False
    allow_web_server: bool = False
    allow_web_dashboard: bool = False
    allow_gui_creation: bool = False
    allow_tui_creation: bool = False
    allow_pdf_binary_export: bool = False
    allow_browser_automation: bool = False
    allow_presentation_deck: bool = False
    allow_slides_generation: bool = False
    allow_cloud_docs_service: bool = False
    allow_cloud_hosting: bool = False
    allow_cdn_publish: bool = False
    allow_package_publish: bool = False
    allow_docker_build_push: bool = False
    allow_git_tag: bool = False
    allow_cloud_upload: bool = False
    allow_deployment: bool = False
    allow_official_documentation_release: bool = False
    allow_legal_signoff: bool = False
    allow_compliance_approval: bool = False
    allow_production_approval_claim: bool = False
    allow_official_acceptance_claim: bool = False
    allow_broker_readiness_claim: bool = False
    allow_live_trading_claim: bool = False
    allow_investment_advice: bool = False
    allow_model_deployment_claim: bool = False
    allow_telemetry: bool = False
    allow_external_service: bool = False
    allow_external_llm: bool = False
    allow_vector_db: bool = False
    allow_embedding_api: bool = False
    allow_file_modification: bool = False
    allow_file_deletion: bool = False
    allow_file_move: bool = False
    allow_overwrite: bool = False
    scan_docs: bool = True
    scan_reports: bool = True
    scan_data_lake: bool = True
    scan_scripts: bool = True
    scan_tests: bool = True
    scan_generated_docs: bool = True
    scan_review_outputs: bool = True
    scan_atlas_outputs: bool = True
    scan_continuity_outputs: bool = True
    scan_preservation_outputs: bool = True
    scan_completion_outputs: bool = True
    scan_safety_outputs: bool = True
    max_items: int = 750000
    max_rows: int = 300000
    min_readiness_score: float = 0.40
    min_quality_score: float = 0.40
    enabled: bool = True
    notes: str = ""

_PROFILES = {
    "balanced_local_documentation_export": LocalDocumentationExportProfile(
        name="balanced_local_documentation_export",
        description="Genel amaçlı local/offline static site export rehearsal, printable binder ve PDF-ready documentation profili.",
        notes="Genel amaçlı local/offline static site export rehearsal, printable binder ve PDF-ready documentation profili."
    ),
    "static_html_focus": LocalDocumentationExportProfile(
        name="static_html_focus",
        description="Offline HTML documentation pack, static site manifest, navigation tree ve link map odaklı profil.",
        max_rows=200000,
        scan_data_lake=False,
        scan_scripts=False,
        scan_tests=False,
        scan_continuity_outputs=False,
        scan_preservation_outputs=False,
        scan_completion_outputs=False,
        scan_safety_outputs=False,
        notes="Offline HTML documentation pack, static site manifest, navigation tree ve link map odaklı profil."
    ),
    "printable_binder_focus": LocalDocumentationExportProfile(
        name="printable_binder_focus",
        description="Printable binder, PDF-ready markdown/html, reading order ve appendix registry odaklı profil.",
        max_rows=250000,
        scan_scripts=False,
        scan_tests=False,
        scan_review_outputs=False,
        scan_atlas_outputs=False,
        scan_completion_outputs=False,
        scan_safety_outputs=False,
        notes="Printable binder, PDF-ready markdown/html, reading order ve appendix registry odaklı profil."
    ),
    "strict_documentation_export_safety": LocalDocumentationExportProfile(
        name="strict_documentation_export_safety",
        description="Hosting/dashboard/PDF/slides/deployment/publish/live/broker/advice overclaim denetimini sıkılaştıran profil.",
        max_items=300000,
        max_rows=120000,
        min_readiness_score=0.60,
        min_quality_score=0.60,
        notes="Hosting/dashboard/PDF/slides/deployment/publish/live/broker/advice overclaim denetimini sıkılaştıran profil."
    ),
}

def get_local_documentation_export_profile(name: str) -> LocalDocumentationExportProfile:
    if name not in _PROFILES:
        raise ConfigError(f"Profile {name} not found.")
    return _PROFILES[name]

def list_local_documentation_export_profiles(enabled_only: bool = True) -> list[LocalDocumentationExportProfile]:
    return [p for p in _PROFILES.values() if (not enabled_only or p.enabled)]

def validate_local_documentation_export_profiles() -> None:
    for p in _PROFILES.values():
        if not p.language:
            raise ConfigError("language bos olamaz.")
        if p.max_items <= 0 or p.max_rows <= 0:
            raise ConfigError("max_items/rows pozitif olmali.")
        if not (0 <= p.min_readiness_score <= 1) or not (0 <= p.min_quality_score <= 1):
            raise ConfigError("score 0-1 arasinda olmali.")
        if not p.dry_run_default:
            raise ConfigError("dry_run_default True olmali.")
        if p.allow_real_static_site_deploy or p.allow_pdf_binary_export or p.allow_presentation_deck or p.allow_investment_advice:
            raise ConfigError("Yasakli flagler var.")

def get_default_local_documentation_export_profile() -> LocalDocumentationExportProfile:
    return _PROFILES["balanced_local_documentation_export"]
