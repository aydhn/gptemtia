from dataclasses import dataclass
from typing import List, Dict


class ConfigError(Exception):
    """Raised when an invalid data lineage profile configuration is detected."""
    pass


@dataclass(frozen=True)
class DataLineageProfile:
    name: str
    description: str
    language: str = "tr"
    current_phase: int = 114
    target_final_phase: int = 160
    next_phase: int = 115
    dry_run_default: bool = True
    local_only: bool = True
    non_production: bool = True
    research_only: bool = True
    allow_live_trading: bool = False
    allow_broker_integration: bool = False
    allow_real_order: bool = False
    allow_investment_advice: bool = False
    allow_lineage_score_as_signal: bool = False
    allow_official_approval_claim: bool = False
    allow_model_deployment: bool = False
    allow_production_deployment: bool = False
    allow_web_server: bool = False
    allow_dashboard: bool = False
    allow_gui_tui: bool = False
    allow_external_llm: bool = False
    allow_vector_db: bool = False
    allow_embedding_api: bool = False
    allow_web_scraping: bool = False
    allow_html_scraping: bool = False
    allow_news_page_scraping: bool = False
    allow_browser_automation_scraping: bool = False
    allow_hidden_api_reverse_engineering: bool = False
    allow_paywall_bypass: bool = False
    allow_rate_limit_abuse: bool = False
    allow_required_network_call: bool = False
    allow_required_paid_api: bool = False
    allow_credential_output: bool = False
    allow_full_article_download: bool = False
    allow_copyrighted_article_copy: bool = False
    allow_source_overwrite: bool = False
    allow_auto_destructive_cleaning: bool = False
    allow_file_deletion: bool = False
    allow_file_move: bool = False
    allow_overwrite: bool = False
    allow_cloud_publish: bool = False
    allow_docker_push: bool = False
    allow_git_tag: bool = False
    allow_archive_creation: bool = False
    enable_source_registry: bool = True
    enable_provider_provenance: bool = True
    enable_dataset_provenance: bool = True
    enable_schema_provenance: bool = True
    enable_transformation_provenance: bool = True
    enable_normalization_lineage: bool = True
    enable_quality_lineage: bool = True
    enable_manual_review_lineage: bool = True
    enable_normalized_output_lineage: bool = True
    enable_domain_lineage: bool = True
    enable_license_provenance: bool = True
    enable_copyright_boundary: bool = True
    enable_metadata_only_provenance: bool = True
    enable_audit_trail: bool = True
    enable_scoring: bool = True
    enable_phase_115_handoff: bool = True
    min_traceability_score: float = 0.45
    enabled: bool = True
    notes: str = ""


DATA_LINEAGE_PROFILES: Dict[str, DataLineageProfile] = {
    "balanced_local_lineage_provenance": DataLineageProfile(
        name="balanced_local_lineage_provenance",
        description="Phase 114 local/offline data lineage and provenance layer için dengeli profil.",
        current_phase=114,
        target_final_phase=160,
        next_phase=115,
        dry_run_default=True,
        local_only=True,
        non_production=True,
        research_only=True,
        min_traceability_score=0.45,
        notes="Phase 114 local/offline data lineage and provenance layer için dengeli profil.",
    ),
    "strict_lineage_provenance_safety": DataLineageProfile(
        name="strict_lineage_provenance_safety",
        description="Lineage score’un sinyal/official approval gibi sunulmasını, scraping’i, source overwrite’ı, credential output’u ve deployment’ı sıkı engelleyen lineage profili.",
        current_phase=114,
        target_final_phase=160,
        next_phase=115,
        dry_run_default=True,
        local_only=True,
        non_production=True,
        research_only=True,
        min_traceability_score=0.65,
        notes="Lineage score’un sinyal/official approval gibi sunulmasını, scraping’i, source overwrite’ı, credential output’u ve deployment’ı sıkı engelleyen lineage profili.",
    ),
    "dry_run_lineage_contract_focus": DataLineageProfile(
        name="dry_run_lineage_contract_focus",
        description="Gerçek veri indirmeden fixture/contract dataframe’ler üzerinde lineage/provenance contract testlerine odaklı profil.",
        current_phase=114,
        target_final_phase=160,
        next_phase=115,
        dry_run_default=True,
        local_only=True,
        non_production=True,
        research_only=True,
        min_traceability_score=0.45,
        notes="Gerçek veri indirmeden fixture/contract dataframe’ler üzerinde lineage/provenance contract testlerine odaklı profil.",
    ),
}


def get_data_lineage_profile(name: str) -> DataLineageProfile:
    if name not in DATA_LINEAGE_PROFILES:
        raise ConfigError(f"Unknown data lineage profile: '{name}'. Available: {list(DATA_LINEAGE_PROFILES.keys())}")
    return DATA_LINEAGE_PROFILES[name]


def list_data_lineage_profiles(enabled_only: bool = True) -> List[DataLineageProfile]:
    if enabled_only:
        return [p for p in DATA_LINEAGE_PROFILES.values() if p.enabled]
    return list(DATA_LINEAGE_PROFILES.values())


def validate_data_lineage_profiles() -> None:
    for name, p in DATA_LINEAGE_PROFILES.items():
        if p.current_phase != 114:
            raise ConfigError(f"Profile {name}: current_phase must be 114, got {p.current_phase}")
        if p.target_final_phase != 160:
            raise ConfigError(f"Profile {name}: target_final_phase must be 160, got {p.target_final_phase}")
        if p.next_phase != 115:
            raise ConfigError(f"Profile {name}: next_phase must be 115, got {p.next_phase}")
        if not p.dry_run_default:
            raise ConfigError(f"Profile {name}: dry_run_default must be True")
        if not (p.local_only and p.non_production and p.research_only):
            raise ConfigError(f"Profile {name}: local_only, non_production, and research_only must be True")
        
        forbidden_flags = [
            ("allow_live_trading", p.allow_live_trading),
            ("allow_broker_integration", p.allow_broker_integration),
            ("allow_real_order", p.allow_real_order),
            ("allow_investment_advice", p.allow_investment_advice),
            ("allow_lineage_score_as_signal", p.allow_lineage_score_as_signal),
            ("allow_official_approval_claim", p.allow_official_approval_claim),
            ("allow_model_deployment", p.allow_model_deployment),
            ("allow_production_deployment", p.allow_production_deployment),
            ("allow_web_server", p.allow_web_server),
            ("allow_dashboard", p.allow_dashboard),
            ("allow_gui_tui", p.allow_gui_tui),
            ("allow_external_llm", p.allow_external_llm),
            ("allow_vector_db", p.allow_vector_db),
            ("allow_embedding_api", p.allow_embedding_api),
            ("allow_web_scraping", p.allow_web_scraping),
            ("allow_html_scraping", p.allow_html_scraping),
            ("allow_news_page_scraping", p.allow_news_page_scraping),
            ("allow_browser_automation_scraping", p.allow_browser_automation_scraping),
            ("allow_hidden_api_reverse_engineering", p.allow_hidden_api_reverse_engineering),
            ("allow_paywall_bypass", p.allow_paywall_bypass),
            ("allow_rate_limit_abuse", p.allow_rate_limit_abuse),
            ("allow_required_network_call", p.allow_required_network_call),
            ("allow_required_paid_api", p.allow_required_paid_api),
            ("allow_credential_output", p.allow_credential_output),
            ("allow_full_article_download", p.allow_full_article_download),
            ("allow_copyrighted_article_copy", p.allow_copyrighted_article_copy),
            ("allow_source_overwrite", p.allow_source_overwrite),
            ("allow_auto_destructive_cleaning", p.allow_auto_destructive_cleaning),
            ("allow_file_deletion", p.allow_file_deletion),
            ("allow_file_move", p.allow_file_move),
            ("allow_overwrite", p.allow_overwrite),
            ("allow_cloud_publish", p.allow_cloud_publish),
            ("allow_docker_push", p.allow_docker_push),
            ("allow_git_tag", p.allow_git_tag),
            ("allow_archive_creation", p.allow_archive_creation),
        ]
        for flag_name, val in forbidden_flags:
            if val:
                raise ConfigError(f"Profile {name}: {flag_name} must be False, got True")
        
        if not (0.0 <= p.min_traceability_score <= 1.0):
            raise ConfigError(f"Profile {name}: min_traceability_score must be between 0.0 and 1.0, got {p.min_traceability_score}")


def get_default_data_lineage_profile() -> DataLineageProfile:
    return get_data_lineage_profile("balanced_local_lineage_provenance")
