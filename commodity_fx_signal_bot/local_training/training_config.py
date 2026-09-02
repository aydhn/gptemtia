from dataclasses import dataclass

class ConfigError(Exception):
    pass

@dataclass(frozen=True)
class LocalTrainingProfile:
    name: str
    description: str
    language: str = "tr"
    dry_run_default: bool = True
    allow_cloud_upload: bool = False
    allow_external_training_service: bool = False
    allow_external_llm: bool = False
    allow_file_modification: bool = False
    allow_file_deletion: bool = False
    allow_file_move: bool = False
    allow_overwrite: bool = False
    allow_live_commands: bool = False
    allow_broker_commands: bool = False
    allow_deploy_commands: bool = False
    allow_background_daemons: bool = False
    allow_real_market_download: bool = False
    allow_certification_claim: bool = False
    allow_investment_advice_training: bool = False
    scan_docs: bool = True
    scan_reports: bool = True
    scan_scripts: bool = True
    scan_tests: bool = True
    scan_data_lake: bool = True
    scan_cross_layer_outputs: bool = True
    scan_safety_docs: bool = True
    max_lessons: int = 10000
    max_walkthrough_steps: int = 5000
    min_training_quality_score: float = 0.40
    enabled: bool = True
    notes: str = ""

PROFILES = {
    "balanced_local_training": LocalTrainingProfile(
        name="balanced_local_training",
        description="Genel amaçlı local/offline knowledge-transfer, onboarding ve handover education profili.",
        language="tr",
        dry_run_default=True,
        allow_cloud_upload=False,
        allow_external_training_service=False,
        allow_external_llm=False,
        allow_file_modification=False,
        allow_file_deletion=False,
        allow_file_move=False,
        allow_overwrite=False,
        allow_live_commands=False,
        allow_broker_commands=False,
        allow_deploy_commands=False,
        allow_background_daemons=False,
        allow_real_market_download=False,
        allow_certification_claim=False,
        allow_investment_advice_training=False,
        scan_docs=True,
        scan_reports=True,
        scan_scripts=True,
        scan_tests=True,
        scan_data_lake=True,
        scan_cross_layer_outputs=True,
        scan_safety_docs=True,
        max_lessons=10000,
        max_walkthrough_steps=5000,
        min_training_quality_score=0.40,
        enabled=True,
        notes="Genel amaçlı local/offline knowledge-transfer, onboarding ve handover education profili."
    ),
    "operator_onboarding_focus": LocalTrainingProfile(
        name="operator_onboarding_focus",
        description="Operatör onboarding odaklı profil.",
        language="tr",
        dry_run_default=True,
        scan_docs=True,
        scan_reports=True,
        scan_scripts=True,
        scan_tests=False,
        scan_data_lake=True,
        scan_cross_layer_outputs=True,
        scan_safety_docs=True,
        notes="Operatör onboarding, first-week curriculum ve safe command lessons odaklı profil."
    ),
    "developer_onboarding_focus": LocalTrainingProfile(
        name="developer_onboarding_focus",
        description="Geliştirici onboarding odaklı profil.",
        language="tr",
        dry_run_default=True,
        scan_docs=True,
        scan_reports=True,
        scan_scripts=True,
        scan_tests=True,
        scan_data_lake=True,
        scan_cross_layer_outputs=True,
        scan_safety_docs=True,
        notes="Geliştirici onboarding, repo yapısı, test contract ve modül mimarisi odaklı profil."
    ),
    "strict_training_safety": LocalTrainingProfile(
        name="strict_training_safety",
        description="Strict safety training profil.",
        language="tr",
        dry_run_default=True,
        max_lessons=7000,
        max_walkthrough_steps=3000,
        min_training_quality_score=0.60,
        notes="Non-use policy, canlı/broker/deploy yasakları ve eğitim güvenlik sınırlarını sıkılaştıran profil."
    )
}

def get_local_training_profile(name: str) -> LocalTrainingProfile:
    if name not in PROFILES:
        raise ConfigError(f"Bilinmeyen profil: {name}")
    return PROFILES[name]

def list_local_training_profiles(enabled_only: bool = True) -> list[LocalTrainingProfile]:
    if enabled_only:
        return [p for p in PROFILES.values() if p.enabled]
    return list(PROFILES.values())

def validate_local_training_profiles() -> None:
    for name, p in PROFILES.items():
        if not p.language:
            raise ConfigError(f"Profile {name} must have a language.")
        if p.max_lessons <= 0:
            raise ConfigError(f"Profile {name} max_lessons must be positive.")
        if p.max_walkthrough_steps <= 0:
            raise ConfigError(f"Profile {name} max_walkthrough_steps must be positive.")
        if not (0 <= p.min_training_quality_score <= 1):
            raise ConfigError(f"Profile {name} min_training_quality_score must be between 0 and 1.")
        
        # Initial profiles checks
        if name in ["balanced_local_training", "operator_onboarding_focus", "developer_onboarding_focus", "strict_training_safety"]:
            if not p.dry_run_default:
                raise ConfigError(f"Profile {name} dry_run_default must be True.")
            if any([
                p.allow_cloud_upload, p.allow_external_training_service, p.allow_external_llm,
                p.allow_file_modification, p.allow_file_deletion, p.allow_file_move, p.allow_overwrite,
                p.allow_live_commands, p.allow_broker_commands, p.allow_deploy_commands,
                p.allow_background_daemons, p.allow_real_market_download, p.allow_certification_claim,
                p.allow_investment_advice_training
            ]):
                raise ConfigError(f"Profile {name} must have all allow flags as False.")

def get_default_local_training_profile() -> LocalTrainingProfile:
    return PROFILES["balanced_local_training"]
