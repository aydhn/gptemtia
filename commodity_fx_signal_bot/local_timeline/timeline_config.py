"""
Local Timeline Configuration and Profiles.
"""

from dataclasses import dataclass
from typing import Dict, List


class ConfigError(Exception):
    pass


@dataclass(frozen=True)
class LocalTimelineProfile:
    name: str
    description: str
    language: str = "tr"
    dry_run_default: bool = True
    allow_external_event_service: bool = False
    allow_cloud_upload: bool = False
    allow_file_modification: bool = False
    allow_file_deletion: bool = False
    allow_live_commands: bool = False
    allow_broker_commands: bool = False
    allow_deploy_commands: bool = False
    allow_background_daemons: bool = False
    allow_real_market_download: bool = False
    allow_external_llm: bool = False
    scan_project_files: bool = True
    scan_reports: bool = True
    scan_data_lake: bool = True
    scan_docs: bool = True
    scan_generated_docs: bool = True
    scan_metadata_outputs: bool = True
    scan_evidence_outputs: bool = True
    scan_graph_outputs: bool = True
    max_events: int = 300000
    max_files: int = 200000
    freshness_days_warning: int = 45
    stale_days_warning: int = 90
    min_quality_score: float = 0.40
    enabled: bool = True
    notes: str = ""

    def __post_init__(self):
        if not self.language:
            raise ValueError("Language cannot be empty.")
        if self.max_events <= 0:
            raise ValueError("max_events must be positive.")
        if self.max_files <= 0:
            raise ValueError("max_files must be positive.")
        if self.freshness_days_warning <= 0:
            raise ValueError("freshness_days_warning must be positive.")
        if self.stale_days_warning < self.freshness_days_warning:
            raise ValueError("stale_days_warning cannot be less than freshness_days_warning.")
        if not 0.0 <= self.min_quality_score <= 1.0:
            raise ValueError("min_quality_score must be between 0 and 1.")


_PROFILES: Dict[str, LocalTimelineProfile] = {
    "balanced_local_timeline": LocalTimelineProfile(
        name="balanced_local_timeline",
        description="Balanced offline timeline.",
        language="tr",
        dry_run_default=True,
        allow_external_event_service=False,
        allow_cloud_upload=False,
        allow_file_modification=False,
        allow_file_deletion=False,
        allow_live_commands=False,
        allow_broker_commands=False,
        allow_deploy_commands=False,
        allow_background_daemons=False,
        allow_real_market_download=False,
        allow_external_llm=False,
        scan_project_files=True,
        scan_reports=True,
        scan_data_lake=True,
        scan_docs=True,
        scan_generated_docs=True,
        scan_metadata_outputs=True,
        scan_evidence_outputs=True,
        scan_graph_outputs=True,
        max_events=300000,
        max_files=200000,
        freshness_days_warning=45,
        stale_days_warning=90,
        notes="Genel amaçlı local/offline project timeline ve artifact evolution profili.",
    ),
    "phase_chronology_focus": LocalTimelineProfile(
        name="phase_chronology_focus",
        description="Phase chronology focus profile.",
        language="tr",
        dry_run_default=True,
        allow_external_event_service=False,
        allow_cloud_upload=False,
        allow_file_modification=False,
        allow_file_deletion=False,
        allow_live_commands=False,
        allow_broker_commands=False,
        allow_deploy_commands=False,
        allow_background_daemons=False,
        allow_real_market_download=False,
        allow_external_llm=False,
        scan_project_files=True,
        scan_reports=True,
        scan_data_lake=True,
        scan_docs=True,
        scan_generated_docs=True,
        scan_metadata_outputs=True,
        scan_evidence_outputs=True,
        scan_graph_outputs=True,
        freshness_days_warning=60,
        stale_days_warning=120,
        notes="Phase chronology, phase digest ve phase-based event timeline odaklı profil.",
    ),
    "artifact_evolution_focus": LocalTimelineProfile(
        name="artifact_evolution_focus",
        description="Artifact evolution focus profile.",
        language="tr",
        dry_run_default=True,
        allow_external_event_service=False,
        allow_cloud_upload=False,
        allow_file_modification=False,
        allow_file_deletion=False,
        allow_live_commands=False,
        allow_broker_commands=False,
        allow_deploy_commands=False,
        allow_background_daemons=False,
        allow_real_market_download=False,
        allow_external_llm=False,
        scan_project_files=True,
        scan_reports=True,
        scan_data_lake=True,
        scan_docs=True,
        scan_generated_docs=False,
        scan_metadata_outputs=True,
        scan_evidence_outputs=True,
        scan_graph_outputs=True,
        freshness_days_warning=30,
        stale_days_warning=90,
        notes="Artifact evolution, file/report/data lake değişim akışı ve temporal lineage odaklı profil.",
    ),
    "strict_timeline_safety": LocalTimelineProfile(
        name="strict_timeline_safety",
        description="Strict safety focus timeline.",
        language="tr",
        dry_run_default=True,
        allow_external_event_service=False,
        allow_cloud_upload=False,
        allow_file_modification=False,
        allow_file_deletion=False,
        allow_live_commands=False,
        allow_broker_commands=False,
        allow_deploy_commands=False,
        allow_background_daemons=False,
        allow_real_market_download=False,
        allow_external_llm=False,
        scan_project_files=True,
        scan_reports=True,
        scan_data_lake=True,
        scan_docs=True,
        scan_generated_docs=True,
        scan_metadata_outputs=True,
        scan_evidence_outputs=True,
        scan_graph_outputs=True,
        max_events=150000,
        max_files=100000,
        freshness_days_warning=30,
        stale_days_warning=60,
        min_quality_score=0.60,
        notes="Cloud event service, live/broker/deploy, raw secret ve yatırım tavsiyesi risklerini sıkı denetleyen profil.",
    ),
}

def get_local_timeline_profile(name: str) -> LocalTimelineProfile:
    if name not in _PROFILES:
        raise ConfigError(f"Unknown timeline profile: {name}")
    return _PROFILES[name]

def list_local_timeline_profiles(enabled_only: bool = True) -> List[LocalTimelineProfile]:
    if enabled_only:
        return [p for p in _PROFILES.values() if p.enabled]
    return list(_PROFILES.values())

def validate_local_timeline_profiles() -> None:
    for profile in _PROFILES.values():
        if not profile.dry_run_default:
            raise ConfigError(f"Profile {profile.name} must have dry_run_default=True")
        if profile.allow_external_event_service:
            raise ConfigError(f"Profile {profile.name} cannot allow external event service")
        if profile.allow_cloud_upload:
            raise ConfigError(f"Profile {profile.name} cannot allow cloud upload")
        if profile.allow_file_modification:
            raise ConfigError(f"Profile {profile.name} cannot allow file modification")
        if profile.allow_file_deletion:
            raise ConfigError(f"Profile {profile.name} cannot allow file deletion")
        if profile.allow_live_commands:
            raise ConfigError(f"Profile {profile.name} cannot allow live commands")
        if profile.allow_broker_commands:
            raise ConfigError(f"Profile {profile.name} cannot allow broker commands")
        if profile.allow_deploy_commands:
            raise ConfigError(f"Profile {profile.name} cannot allow deploy commands")
        if profile.allow_background_daemons:
            raise ConfigError(f"Profile {profile.name} cannot allow background daemons")
        if profile.allow_real_market_download:
            raise ConfigError(f"Profile {profile.name} cannot allow real market download")
        if profile.allow_external_llm:
            raise ConfigError(f"Profile {profile.name} cannot allow external llm")

def get_default_local_timeline_profile() -> LocalTimelineProfile:
    from config.settings import Settings
    settings = Settings()
    return get_local_timeline_profile(settings.default_local_timeline_profile)
