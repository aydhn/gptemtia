from dataclasses import dataclass


class ConfigError(Exception):
    pass

@dataclass(frozen=True)
class LocalConsistencyProfile:
    name: str
    description: str
    language: str = "tr"
    dry_run_default: bool = True
    allow_auto_fix: bool = False
    allow_file_modification: bool = False
    allow_file_deletion: bool = False
    allow_overwrite: bool = False
    allow_cloud_upload: bool = False
    allow_external_service: bool = False
    allow_external_llm: bool = False
    allow_live_commands: bool = False
    allow_broker_commands: bool = False
    allow_deploy_commands: bool = False
    allow_background_daemons: bool = False
    allow_real_market_download: bool = False
    scan_config: bool = True
    scan_docs: bool = True
    scan_reports: bool = True
    scan_data_lake: bool = True
    scan_metadata: bool = True
    scan_evidence: bool = True
    scan_graph: bool = True
    scan_timeline: bool = True
    scan_security_layers: bool = True
    max_checks: int = 250000
    max_files: int = 200000
    stale_days_warning: int = 90
    min_coherence_score: float = 0.40
    min_quality_score: float = 0.40
    enabled: bool = True
    notes: str = ""

PROFILES = {
    "balanced_local_consistency": LocalConsistencyProfile(
        name="balanced_local_consistency",
        description="Balanced local consistency profile",
        notes="Genel amaçlı local/offline cross-layer consistency ve system coherence profili."
    ),
    "strict_consistency_boundary": LocalConsistencyProfile(
        name="strict_consistency_boundary",
        description="Strict consistency boundary profile",
        max_checks=150000,
        max_files=100000,
        stale_days_warning=60,
        min_coherence_score=0.60,
        min_quality_score=0.60,
        notes="Safety boundary, disclaimer, non-use policy, raw secret ve contradiction denetimini sıkılaştıran profil."
    ),
    "docs_reports_consistency_focus": LocalConsistencyProfile(
        name="docs_reports_consistency_focus",
        description="Docs and reports consistency focus",
        scan_metadata=False,
        scan_graph=False,
        notes="Docs, reports, phase log, DataLake ve generated output tutarlılığına odaklı profil."
    ),
    "metadata_graph_timeline_consistency": LocalConsistencyProfile(
        name="metadata_graph_timeline_consistency",
        description="Metadata, graph and timeline consistency focus",
        stale_days_warning=75,
        notes="Artifact metadata, local knowledge graph ve timeline tutarlılığına odaklı profil."
    )
}

def get_local_consistency_profile(name: str) -> LocalConsistencyProfile:
    if name not in PROFILES:
        raise ConfigError(f"Unknown profile: {name}")
    return PROFILES[name]

def list_local_consistency_profiles(enabled_only: bool = True) -> list[LocalConsistencyProfile]:
    return [p for p in PROFILES.values() if not enabled_only or p.enabled]

def validate_local_consistency_profiles() -> None:
    for name, p in PROFILES.items():
        if not p.language:
            raise ConfigError(f"Profile {name} has no language.")
        if p.max_checks <= 0 or p.max_files <= 0:
            raise ConfigError(f"Profile {name} has non-positive max checks or files.")
        if p.stale_days_warning <= 0:
            raise ConfigError(f"Profile {name} has non-positive stale_days_warning.")
        if not (0.0 <= p.min_coherence_score <= 1.0):
            raise ConfigError(f"Profile {name} has invalid min_coherence_score.")
        if not (0.0 <= p.min_quality_score <= 1.0):
            raise ConfigError(f"Profile {name} has invalid min_quality_score.")
        if not p.dry_run_default:
            raise ConfigError(f"Profile {name} must have dry_run_default=True.")
        if p.allow_auto_fix or p.allow_file_modification or p.allow_file_deletion or p.allow_overwrite or \
           p.allow_cloud_upload or p.allow_external_service or p.allow_live_commands or p.allow_broker_commands or \
           p.allow_deploy_commands or p.allow_background_daemons or p.allow_real_market_download or p.allow_external_llm:
            raise ConfigError(f"Profile {name} has unsafe allow flags enabled.")

def get_default_local_consistency_profile() -> LocalConsistencyProfile:
    return PROFILES["balanced_local_consistency"]
