
from dataclasses import dataclass
from core.exceptions import ConfigError

@dataclass(frozen=True)
class SecretsHygieneProfile:
    name: str
    description: str
    language: str = "tr"
    dry_run_default: bool = True
    allow_secret_value_output: bool = False
    allow_file_modification: bool = False
    allow_secret_deletion: bool = False
    allow_cloud_vault: bool = False
    allow_external_scanner: bool = False
    allow_live_commands: bool = False
    allow_broker_commands: bool = False
    allow_deploy_commands: bool = False
    allow_background_daemons: bool = False
    allow_real_market_download: bool = False
    allow_external_llm: bool = False
    scan_source: bool = True
    scan_docs: bool = True
    scan_tests: bool = True
    scan_configs: bool = True
    scan_reports: bool = True
    scan_data_manifests: bool = True
    scan_generated_outputs: bool = True
    max_files: int = 150000
    max_file_mb: int = 20
    entropy_threshold: float = 4.2
    mask_keep_start: int = 4
    mask_keep_end: int = 4
    min_quality_score: float = 0.40
    enabled: bool = True
    notes: str = ""

_SECRETS_HYGIENE_PROFILES = {
    "balanced_local_secrets_hygiene": SecretsHygieneProfile(
        name="balanced_local_secrets_hygiene",
        description="General purpose local/offline secret hygiene and credential boundary profile",
    ),
    "strict_secret_boundary": SecretsHygieneProfile(
        name="strict_secret_boundary",
        description="Strict token, credential, and private data boundary profile",
        entropy_threshold=3.8,
        max_file_mb=10,
        min_quality_score=0.60,
    ),
    "config_env_focused_hygiene": SecretsHygieneProfile(
        name="config_env_focused_hygiene",
        description="Config, .env.example, settings and credential boundary profile",
        scan_reports=False,
        scan_generated_outputs=False,
    ),
    "report_leakage_hygiene": SecretsHygieneProfile(
        name="report_leakage_hygiene",
        description="Generated docs, reports/output and data/lake manifest secret leakage profile",
        scan_source=False,
        scan_tests=False,
    )
}

def get_secrets_hygiene_profile(name: str) -> SecretsHygieneProfile:
    if name not in _SECRETS_HYGIENE_PROFILES:
        raise ConfigError(f"Unknown SecretsHygieneProfile: {name}")
    return _SECRETS_HYGIENE_PROFILES[name]

def list_secrets_hygiene_profiles(enabled_only: bool = True) -> list[SecretsHygieneProfile]:
    if enabled_only:
        return [p for p in _SECRETS_HYGIENE_PROFILES.values() if p.enabled]
    return list(_SECRETS_HYGIENE_PROFILES.values())

def validate_secrets_hygiene_profiles() -> None:
    for name, profile in _SECRETS_HYGIENE_PROFILES.items():
        if not profile.language:
             raise ConfigError(f"Profile {name} must have a language")
        if profile.max_files <= 0:
             raise ConfigError(f"Profile {name} max_files must be positive")
        if profile.max_file_mb <= 0:
             raise ConfigError(f"Profile {name} max_file_mb must be positive")
        if profile.entropy_threshold <= 0:
             raise ConfigError(f"Profile {name} entropy_threshold must be positive")
        if profile.mask_keep_start < 0 or profile.mask_keep_end < 0:
             raise ConfigError(f"Profile {name} mask keep parameters cannot be negative")
        if not (0.0 <= profile.min_quality_score <= 1.0):
             raise ConfigError(f"Profile {name} min_quality_score must be between 0 and 1")
        if not profile.dry_run_default:
             raise ConfigError(f"Profile {name} dry_run_default must be True")
        if profile.allow_secret_value_output or profile.allow_file_modification or profile.allow_secret_deletion or profile.allow_cloud_vault or profile.allow_external_scanner:
             raise ConfigError(f"Profile {name} has unsafe allow flags enabled")

def get_default_secrets_hygiene_profile() -> SecretsHygieneProfile:
    return _SECRETS_HYGIENE_PROFILES["balanced_local_secrets_hygiene"]
