"""
Configuration settings for Artifact Metadata Profiles.
"""

from dataclasses import dataclass
import logging

logger = logging.getLogger(__name__)

class ConfigError(Exception):
    pass

@dataclass(frozen=True)
class ArtifactMetadataProfile:
    name: str
    description: str
    language: str = "tr"
    dry_run_default: bool = True
    allow_model_deployment_claims: bool = False
    allow_official_certification_claims: bool = False
    allow_investment_advice_claims: bool = False
    allow_cloud_registry: bool = False
    allow_file_modification: bool = False
    allow_file_deletion: bool = False
    allow_live_commands: bool = False
    allow_broker_commands: bool = False
    allow_deploy_commands: bool = False
    allow_background_daemons: bool = False
    allow_real_market_download: bool = False
    allow_external_llm: bool = False
    scan_models: bool = True
    scan_datasets: bool = True
    scan_experiments: bool = True
    scan_backtests: bool = True
    scan_scenarios: bool = True
    scan_reports: bool = True
    scan_evidence: bool = True
    max_artifacts: int = 200000
    max_artifact_mb: int = 50
    freshness_days_warning: int = 45
    min_quality_score: float = 0.40
    enabled: bool = True
    notes: str = ""

_PROFILES = {
    "balanced_local_metadata": ArtifactMetadataProfile(
        name="balanced_local_metadata",
        description="Genel amacli local/offline model card, dataset card ve research artifact metadata profili.",
        language="tr",
        dry_run_default=True,
        allow_model_deployment_claims=False,
        allow_official_certification_claims=False,
        allow_investment_advice_claims=False,
        allow_cloud_registry=False,
        allow_file_modification=False,
        allow_file_deletion=False,
        allow_live_commands=False,
        allow_broker_commands=False,
        allow_deploy_commands=False,
        allow_background_daemons=False,
        allow_real_market_download=False,
        allow_external_llm=False,
        scan_models=True,
        scan_datasets=True,
        scan_experiments=True,
        scan_backtests=True,
        scan_scenarios=True,
        scan_reports=True,
        scan_evidence=True,
        max_artifacts=200000,
        max_artifact_mb=50,
        freshness_days_warning=45,
        min_quality_score=0.40,
        enabled=True,
        notes="Genel amacli local/offline model card, dataset card ve research artifact metadata profili."
    ),
    "model_dataset_focus_metadata": ArtifactMetadataProfile(
        name="model_dataset_focus_metadata",
        description="Model, dataset, feature ve backtest card’larina odakli profil.",
        language="tr",
        dry_run_default=True,
        allow_model_deployment_claims=False,
        allow_official_certification_claims=False,
        allow_investment_advice_claims=False,
        allow_cloud_registry=False,
        allow_file_modification=False,
        allow_file_deletion=False,
        allow_live_commands=False,
        allow_broker_commands=False,
        allow_deploy_commands=False,
        allow_background_daemons=False,
        allow_real_market_download=False,
        allow_external_llm=False,
        scan_models=True,
        scan_datasets=True,
        scan_experiments=True,
        scan_backtests=True,
        scan_scenarios=False,
        scan_reports=True,
        scan_evidence=False,
        max_artifacts=200000,
        max_artifact_mb=50,
        freshness_days_warning=60,
        min_quality_score=0.40,
        enabled=True,
        notes="Model, dataset, feature ve backtest card’larina odakli profil."
    ),
    "experiment_reproducibility_metadata": ArtifactMetadataProfile(
        name="experiment_reproducibility_metadata",
        description="Deney, replay, regression ve reproducibility card’larina odakli profil.",
        language="tr",
        dry_run_default=True,
        allow_model_deployment_claims=False,
        allow_official_certification_claims=False,
        allow_investment_advice_claims=False,
        allow_cloud_registry=False,
        allow_file_modification=False,
        allow_file_deletion=False,
        allow_live_commands=False,
        allow_broker_commands=False,
        allow_deploy_commands=False,
        allow_background_daemons=False,
        allow_real_market_download=False,
        allow_external_llm=False,
        scan_models=True,
        scan_datasets=True,
        scan_experiments=True,
        scan_backtests=True,
        scan_scenarios=True,
        scan_reports=True,
        scan_evidence=True,
        max_artifacts=200000,
        max_artifact_mb=50,
        freshness_days_warning=30,
        min_quality_score=0.40,
        enabled=True,
        notes="Deney, replay, regression ve reproducibility card’larina odakli profil."
    ),
    "strict_metadata_boundary": ArtifactMetadataProfile(
        name="strict_metadata_boundary",
        description="Deployment claim, certification claim, investment advice ve raw secret risklerini siki denetleyen profil.",
        language="tr",
        dry_run_default=True,
        allow_model_deployment_claims=False,
        allow_official_certification_claims=False,
        allow_investment_advice_claims=False,
        allow_cloud_registry=False,
        allow_file_modification=False,
        allow_file_deletion=False,
        allow_live_commands=False,
        allow_broker_commands=False,
        allow_deploy_commands=False,
        allow_background_daemons=False,
        allow_real_market_download=False,
        allow_external_llm=False,
        scan_models=True,
        scan_datasets=True,
        scan_experiments=True,
        scan_backtests=True,
        scan_scenarios=True,
        scan_reports=True,
        scan_evidence=True,
        max_artifacts=200000,
        max_artifact_mb=20,
        freshness_days_warning=30,
        min_quality_score=0.60,
        enabled=True,
        notes="Deployment claim, certification claim, investment advice ve raw secret risklerini siki denetleyen profil."
    )
}

def get_artifact_metadata_profile(name: str) -> ArtifactMetadataProfile:
    if name not in _PROFILES:
        raise ConfigError(f"Bilinmeyen profil: {name}")
    return _PROFILES[name]

def list_artifact_metadata_profiles(enabled_only: bool = True) -> list[ArtifactMetadataProfile]:
    if enabled_only:
        return [p for p in _PROFILES.values() if p.enabled]
    return list(_PROFILES.values())

def validate_artifact_metadata_profiles() -> None:
    for name, profile in _PROFILES.items():
        if not profile.language:
            raise ValueError(f"Profile {name} must have a language")
        if profile.max_artifacts <= 0:
            raise ValueError(f"Profile {name} must have positive max_artifacts")
        if profile.max_artifact_mb <= 0:
            raise ValueError(f"Profile {name} must have positive max_artifact_mb")
        if profile.freshness_days_warning <= 0:
            raise ValueError(f"Profile {name} must have positive freshness_days_warning")
        if not (0 <= profile.min_quality_score <= 1):
            raise ValueError(f"Profile {name} min_quality_score must be between 0 and 1")
        if not profile.dry_run_default:
            raise ValueError(f"Profile {name} must have dry_run_default=True")
        if profile.allow_model_deployment_claims:
            raise ValueError(f"Profile {name} allow_model_deployment_claims must be False")
        if profile.allow_official_certification_claims:
            raise ValueError(f"Profile {name} allow_official_certification_claims must be False")
        if profile.allow_investment_advice_claims:
            raise ValueError(f"Profile {name} allow_investment_advice_claims must be False")
        if profile.allow_cloud_registry:
            raise ValueError(f"Profile {name} allow_cloud_registry must be False")
        if profile.allow_file_modification:
            raise ValueError(f"Profile {name} allow_file_modification must be False")
        if profile.allow_file_deletion:
            raise ValueError(f"Profile {name} allow_file_deletion must be False")

def get_default_artifact_metadata_profile() -> ArtifactMetadataProfile:
    return get_artifact_metadata_profile("balanced_local_metadata")
