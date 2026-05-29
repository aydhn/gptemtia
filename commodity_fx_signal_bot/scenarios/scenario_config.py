"""
Scenario configuration and profiles for controlled offline research scenarios.
"""

from dataclasses import dataclass
from typing import Dict, List


class ConfigError(Exception):
    pass


@dataclass(frozen=True)
class ScenarioProfile:
    name: str
    description: str
    use_synthetic_data_only: bool = True
    allow_real_market_download: bool = False
    allow_live_commands: bool = False
    allow_broker_commands: bool = False
    allow_deploy_commands: bool = False
    allow_background_daemons: bool = False
    scenario_default_timeframe: str = "1d"
    generate_sample_data: bool = True
    generate_fixtures: bool = True
    generate_expected_outputs: bool = True
    run_dry_run_validation: bool = True
    max_symbols: int = 20
    max_rows_per_symbol: int = 500
    random_seed: int = 42
    min_quality_score: float = 0.40
    enabled: bool = True
    notes: str = ""


# Default built-in profiles
_SCENARIO_PROFILES = {
    "balanced_offline_scenarios": ScenarioProfile(
        name="balanced_offline_scenarios",
        description="General-purpose balanced offline profile.",
        use_synthetic_data_only=True,
        allow_real_market_download=False,
        allow_live_commands=False,
        allow_broker_commands=False,
        allow_deploy_commands=False,
        allow_background_daemons=False,
        max_symbols=20,
        max_rows_per_symbol=500,
        random_seed=42,
        notes="Genel amaçlı offline synthetic scenario ve demo workflow profili."
    ),
    "small_demo_scenarios": ScenarioProfile(
        name="small_demo_scenarios",
        description="Small profile for lightweight demos.",
        max_symbols=8,
        max_rows_per_symbol=120,
        random_seed=42,
        use_synthetic_data_only=True,
        allow_real_market_download=False,
        allow_live_commands=False,
        allow_broker_commands=False,
        allow_deploy_commands=False,
        allow_background_daemons=False,
        notes="Hızlı demo ve lightweight case study profili."
    ),
    "full_demo_scenarios": ScenarioProfile(
        name="full_demo_scenarios",
        description="Full profile for deep demos.",
        max_symbols=25,
        max_rows_per_symbol=1000,
        random_seed=42,
        use_synthetic_data_only=True,
        allow_real_market_download=False,
        allow_live_commands=False,
        allow_broker_commands=False,
        allow_deploy_commands=False,
        allow_background_daemons=False,
        notes="Daha geniş sentetik fixture ve end-to-end demo profili."
    ),
    "documentation_demo_scenarios": ScenarioProfile(
        name="documentation_demo_scenarios",
        description="Profile for documentation generation.",
        max_symbols=10,
        max_rows_per_symbol=200,
        generate_sample_data=True,
        generate_fixtures=True,
        generate_expected_outputs=True,
        run_dry_run_validation=True,
        use_synthetic_data_only=True,
        allow_real_market_download=False,
        allow_live_commands=False,
        allow_broker_commands=False,
        allow_deploy_commands=False,
        allow_background_daemons=False,
        notes="Dokümantasyon ve kullanıcı rehberi örnekleri için demo senaryo profili."
    )
}


def get_scenario_profile(name: str) -> ScenarioProfile:
    """Returns the requested scenario profile or raises ConfigError."""
    if name not in _SCENARIO_PROFILES:
        raise ConfigError(f"Unknown scenario profile: {name}")
    return _SCENARIO_PROFILES[name]


def list_scenario_profiles(enabled_only: bool = True) -> List[ScenarioProfile]:
    """Returns a list of scenario profiles."""
    profiles = list(_SCENARIO_PROFILES.values())
    if enabled_only:
        return [p for p in profiles if p.enabled]
    return profiles


def validate_scenario_profiles() -> None:
    """Validates the configuration of all profiles."""
    for name, profile in _SCENARIO_PROFILES.items():
        if profile.max_symbols <= 0:
            raise ConfigError(f"Profile {name}: max_symbols must be positive")
        if profile.max_rows_per_symbol <= 0:
            raise ConfigError(f"Profile {name}: max_rows_per_symbol must be positive")
        if not (0.0 <= profile.min_quality_score <= 1.0):
            raise ConfigError(f"Profile {name}: min_quality_score must be between 0.0 and 1.0")

        # Security constraints
        if not profile.use_synthetic_data_only:
            raise ConfigError(f"Profile {name}: use_synthetic_data_only MUST be True for scenarios")
        if profile.allow_real_market_download:
            raise ConfigError(f"Profile {name}: allow_real_market_download MUST be False for scenarios")
        if profile.allow_live_commands or profile.allow_broker_commands or profile.allow_deploy_commands or profile.allow_background_daemons:
            raise ConfigError(f"Profile {name}: Live, broker, deploy, or daemon commands MUST be False")


def get_default_scenario_profile() -> ScenarioProfile:
    """Returns the default balanced scenario profile."""
    return get_scenario_profile("balanced_offline_scenarios")
