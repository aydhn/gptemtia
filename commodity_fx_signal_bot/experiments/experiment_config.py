from dataclasses import dataclass

class ConfigError(Exception):
    pass

@dataclass(frozen=True)
class ExperimentProfile:
    name: str
    description: str
    max_runs_in_leaderboard: int = 500
    min_quality_score: float = 0.40
    default_baseline_name: str = "baseline_research_run"
    enable_ablation_studies: bool = True
    enable_comparison: bool = True
    enable_leaderboard: bool = True
    require_hypothesis: bool = False
    require_reproducibility_manifest: bool = True
    capture_environment: bool = True
    capture_config_snapshot: bool = True
    capture_artifact_snapshot: bool = True
    allow_rerun_candidates: bool = True
    dry_run: bool = True
    enabled: bool = True
    notes: str = ""

def get_experiment_profile(name: str) -> ExperimentProfile:
    profiles = {p.name: p for p in list_experiment_profiles(enabled_only=False)}
    if name not in profiles:
        raise ConfigError(f"Experiment profile '{name}' not found.")
    return profiles[name]

def list_experiment_profiles(enabled_only: bool = True) -> list[ExperimentProfile]:
    profiles = [
        ExperimentProfile(
            name="balanced_experiment_tracking",
            description="Genel amaçlı offline experiment tracking ve research versioning profili.",
            max_runs_in_leaderboard=500,
            min_quality_score=0.40,
            enable_ablation_studies=True,
            enable_comparison=True,
            enable_leaderboard=True,
            require_hypothesis=False,
            require_reproducibility_manifest=True,
            dry_run=True,
            notes="Genel amaçlı offline experiment tracking ve research versioning profili.",
            enabled=True
        ),
        ExperimentProfile(
            name="strict_experiment_tracking",
            description="Daha sıkı hipotez, kalite ve reproducibility gereksinimleri olan profil.",
            max_runs_in_leaderboard=1000,
            min_quality_score=0.55,
            require_hypothesis=True,
            require_reproducibility_manifest=True,
            capture_environment=True,
            capture_config_snapshot=True,
            capture_artifact_snapshot=True,
            dry_run=True,
            notes="Daha sıkı hipotez, kalite ve reproducibility gereksinimleri olan profil.",
            enabled=True
        ),
        ExperimentProfile(
            name="ablation_focused_experiment_tracking",
            description="Ablation study ve bileşen etkisi araştırmasına odaklı profil.",
            enable_ablation_studies=True,
            enable_comparison=True,
            enable_leaderboard=False,
            require_hypothesis=True,
            dry_run=True,
            notes="Ablation study ve bileşen etkisi araştırmasına odaklı profil.",
            enabled=True
        ),
        ExperimentProfile(
            name="light_experiment_tracking",
            description="Hafif deney kayıt ve hızlı karşılaştırma profili.",
            max_runs_in_leaderboard=100,
            require_hypothesis=False,
            require_reproducibility_manifest=False,
            capture_artifact_snapshot=False,
            dry_run=True,
            notes="Hafif deney kayıt ve hızlı karşılaştırma profili.",
            enabled=True
        )
    ]
    if enabled_only:
        return [p for p in profiles if p.enabled]
    return profiles

def validate_experiment_profiles() -> None:
    for profile in list_experiment_profiles(enabled_only=False):
        if profile.max_runs_in_leaderboard <= 0:
            raise ConfigError(f"Profile '{profile.name}' has non-positive max_runs_in_leaderboard.")
        if not (0.0 <= profile.min_quality_score <= 1.0):
            raise ConfigError(f"Profile '{profile.name}' has min_quality_score outside [0,1].")
        if not profile.default_baseline_name:
            raise ConfigError(f"Profile '{profile.name}' has empty default_baseline_name.")
        if not profile.dry_run:
            raise ConfigError(f"Profile '{profile.name}' dry_run must be True.")

def get_default_experiment_profile() -> ExperimentProfile:
    from config.settings import settings
    return get_experiment_profile(settings.default_experiment_profile)
