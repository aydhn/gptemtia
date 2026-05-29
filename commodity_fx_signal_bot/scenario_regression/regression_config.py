from dataclasses import dataclass

class ConfigError(Exception):
    pass

@dataclass(frozen=True)
class ScenarioRegressionProfile:
    name: str
    description: str
    use_synthetic_only: bool = True
    allow_real_market_download: bool = False
    allow_live_commands: bool = False
    allow_broker_commands: bool = False
    allow_deploy_commands: bool = False
    allow_background_daemons: bool = False
    generate_golden_outputs: bool = True
    capture_snapshots: bool = True
    compare_snapshots: bool = True
    run_deterministic_replay: bool = True
    validate_output_contracts: bool = True
    max_scenarios: int = 50
    max_snapshot_rows: int = 1000
    numeric_tolerance: float = 1e-8
    text_similarity_threshold: float = 0.95
    acceptance_threshold: float = 0.85
    random_seed: int = 42
    min_quality_score: float = 0.40
    enabled: bool = True
    notes: str = ""

_profiles = {
    "balanced_scenario_regression": ScenarioRegressionProfile(
        name="balanced_scenario_regression",
        description="Genel amaçlı offline scenario regression ve deterministic replay profili.",
        use_synthetic_only=True,
        allow_real_market_download=False,
        allow_live_commands=False,
        allow_broker_commands=False,
        allow_deploy_commands=False,
        allow_background_daemons=False,
        generate_golden_outputs=True,
        capture_snapshots=True,
        compare_snapshots=True,
        run_deterministic_replay=True,
        validate_output_contracts=True,
        max_scenarios=50,
        max_snapshot_rows=1000,
        numeric_tolerance=1e-8,
        text_similarity_threshold=0.95,
        acceptance_threshold=0.85,
        random_seed=42,
        min_quality_score=0.40,
        notes="Genel amaçlı offline scenario regression ve deterministic replay profili.",
    ),
    "strict_scenario_regression": ScenarioRegressionProfile(
        name="strict_scenario_regression",
        description="Daha sıkı snapshot, replay ve acceptance eşiği kullanan regression profili.",
        use_synthetic_only=True,
        allow_real_market_download=False,
        allow_live_commands=False,
        allow_broker_commands=False,
        allow_deploy_commands=False,
        allow_background_daemons=False,
        max_scenarios=100,
        max_snapshot_rows=2000,
        numeric_tolerance=1e-10,
        text_similarity_threshold=0.98,
        acceptance_threshold=0.95,
        min_quality_score=0.60,
        notes="Daha sıkı snapshot, replay ve acceptance eşiği kullanan regression profili.",
    ),
    "fast_scenario_regression": ScenarioRegressionProfile(
        name="fast_scenario_regression",
        description="Hızlı smoke-style scenario regression profili.",
        use_synthetic_only=True,
        allow_real_market_download=False,
        allow_live_commands=False,
        allow_broker_commands=False,
        allow_deploy_commands=False,
        allow_background_daemons=False,
        max_scenarios=15,
        max_snapshot_rows=300,
        numeric_tolerance=1e-6,
        text_similarity_threshold=0.90,
        acceptance_threshold=0.75,
        notes="Hızlı smoke-style scenario regression profili.",
    ),
    "demo_acceptance_regression": ScenarioRegressionProfile(
        name="demo_acceptance_regression",
        description="Demo workflow ve end-to-end acceptance doğrulamasına odaklı profil.",
        use_synthetic_only=True,
        allow_real_market_download=False,
        allow_live_commands=False,
        allow_broker_commands=False,
        allow_deploy_commands=False,
        allow_background_daemons=False,
        max_scenarios=30,
        max_snapshot_rows=1000,
        compare_snapshots=True,
        run_deterministic_replay=True,
        validate_output_contracts=True,
        acceptance_threshold=0.90,
        notes="Demo workflow ve end-to-end acceptance doğrulamasına odaklı profil.",
    ),
}

def get_scenario_regression_profile(name: str) -> ScenarioRegressionProfile:
    if name not in _profiles:
        raise ConfigError(f"Unknown scenario regression profile: {name}")
    return _profiles[name]

def list_scenario_regression_profiles(enabled_only: bool = True) -> list[ScenarioRegressionProfile]:
    return [p for p in _profiles.values() if not enabled_only or p.enabled]

def validate_scenario_regression_profiles() -> None:
    for name, p in _profiles.items():
        if p.max_scenarios <= 0:
            raise ConfigError(f"Profile {name} max_scenarios must be positive.")
        if p.max_snapshot_rows <= 0:
            raise ConfigError(f"Profile {name} max_snapshot_rows must be positive.")
        if p.numeric_tolerance < 0:
            raise ConfigError(f"Profile {name} numeric_tolerance must be >= 0.")
        if not (0 <= p.text_similarity_threshold <= 1):
            raise ConfigError(f"Profile {name} text_similarity_threshold must be between 0 and 1.")
        if not (0 <= p.acceptance_threshold <= 1):
            raise ConfigError(f"Profile {name} acceptance_threshold must be between 0 and 1.")
        if not (0 <= p.min_quality_score <= 1):
            raise ConfigError(f"Profile {name} min_quality_score must be between 0 and 1.")
        if not p.use_synthetic_only:
            raise ConfigError(f"Profile {name} use_synthetic_only must be True.")
        if p.allow_real_market_download or p.allow_live_commands or p.allow_broker_commands or p.allow_deploy_commands or p.allow_background_daemons:
            raise ConfigError(f"Profile {name} cannot allow live/real commands.")

def get_default_scenario_regression_profile() -> ScenarioRegressionProfile:
    from config.settings import settings
    return get_scenario_regression_profile(settings.default_scenario_regression_profile)
