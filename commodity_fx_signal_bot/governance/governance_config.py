from dataclasses import dataclass


class ConfigError(Exception):
    pass

@dataclass(frozen=True)
class GovernanceProfile:
    name: str
    description: str
    scan_data_lake: bool = True
    scan_reports_output: bool = True
    capture_file_hashes: bool = True
    capture_schema_fingerprints: bool = True
    capture_row_counts: bool = True
    capture_modified_times: bool = True
    capture_artifact_sizes: bool = True
    max_file_hash_mb: int = 50
    lineage_max_depth: int = 8
    require_provenance_for_research_outputs: bool = True
    require_fingerprint_for_key_artifacts: bool = True
    require_audit_trail: bool = True
    min_quality_score: float = 0.40
    enabled: bool = True
    notes: str = ""

_GOVERNANCE_PROFILES = [
    GovernanceProfile(
        name="balanced_research_governance",
        description="Balanced research governance",
        scan_data_lake=True,
        scan_reports_output=True,
        capture_file_hashes=True,
        capture_schema_fingerprints=True,
        capture_row_counts=True,
        max_file_hash_mb=50,
        lineage_max_depth=8,
        require_provenance_for_research_outputs=True,
        require_fingerprint_for_key_artifacts=True,
        require_audit_trail=True,
        notes="Genel amaçlı offline research governance ve lineage profili."
    ),
    GovernanceProfile(
        name="strict_research_governance",
        description="Strict research governance",
        max_file_hash_mb=100,
        lineage_max_depth=12,
        require_provenance_for_research_outputs=True,
        require_fingerprint_for_key_artifacts=True,
        require_audit_trail=True,
        min_quality_score=0.60,
        notes="Daha sıkı provenance, fingerprint ve audit trail gereksinimleri olan profil."
    ),
    GovernanceProfile(
        name="light_research_governance",
        description="Light research governance",
        capture_file_hashes=False,
        capture_schema_fingerprints=True,
        capture_row_counts=True,
        max_file_hash_mb=10,
        lineage_max_depth=4,
        require_provenance_for_research_outputs=False,
        notes="Hızlı local tarama ve hafif governance raporu için."
    ),
    GovernanceProfile(
        name="experiment_lineage_governance",
        description="Experiment lineage governance",
        scan_data_lake=True,
        scan_reports_output=True,
        capture_file_hashes=True,
        lineage_max_depth=12,
        require_audit_trail=True,
        notes="Experiment tracking ve reproducibility manifestleriyle lineage bridge kurmaya odaklı profil."
    )
]

def get_governance_profile(name: str) -> GovernanceProfile:
    for profile in _GOVERNANCE_PROFILES:
        if profile.name == name:
            return profile
    raise ConfigError(f"Unknown governance profile: {name}")

def list_governance_profiles(enabled_only: bool = True) -> list[GovernanceProfile]:
    if enabled_only:
        return [p for p in _GOVERNANCE_PROFILES if p.enabled]
    return list(_GOVERNANCE_PROFILES)

def validate_governance_profiles() -> None:
    for profile in _GOVERNANCE_PROFILES:
        if profile.max_file_hash_mb <= 0:
            raise ValueError(f"Profile {profile.name} max_file_hash_mb must be > 0")
        if profile.lineage_max_depth <= 0:
            raise ValueError(f"Profile {profile.name} lineage_max_depth must be > 0")
        if not (0.0 <= profile.min_quality_score <= 1.0):
            raise ValueError(f"Profile {profile.name} min_quality_score must be between 0 and 1")
        if not (profile.scan_data_lake or profile.scan_reports_output):
            raise ValueError(f"Profile {profile.name} must have scan_data_lake or scan_reports_output set to True")

def get_default_governance_profile() -> GovernanceProfile:
    return get_governance_profile("balanced_research_governance")
