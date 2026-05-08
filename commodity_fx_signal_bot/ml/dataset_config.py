from dataclasses import dataclass

@dataclass(frozen=True)
class MLDatasetProfile:
    name: str
    description: str
    feature_sets: tuple[str, ...]
    target_types: tuple[str, ...]
    forward_return_horizons: tuple[int, ...]
    forward_volatility_horizons: tuple[int, ...]
    future_drawdown_horizons: tuple[int, ...]
    direction_threshold: float = 0.002
    positive_return_threshold: float = 0.005
    negative_return_threshold: float = -0.005
    min_rows: int = 200
    max_feature_nan_ratio: float = 0.35
    max_target_nan_ratio: float = 0.20
    use_purged_split: bool = True
    embargo_bars: int = 5
    test_size_ratio: float = 0.20
    validation_size_ratio: float = 0.20
    enabled: bool = True
    notes: str = ""

_PROFILES = {
    "balanced_supervised_dataset": MLDatasetProfile(
        name="balanced_supervised_dataset",
        description="General purpose supervised ML dataset preparation profile",
        feature_sets=(
            "technical", "momentum", "trend", "volatility", "volume",
            "mean_reversion", "price_action", "divergence", "mtf",
            "regime", "macro", "asset_profiles", "signal_candidates",
            "decision_candidates", "strategy_candidates", "strategy_rule_candidates",
            "risk_candidates", "sizing_candidates", "level_candidates"
        ),
        target_types=("forward_return", "direction_class", "future_volatility", "future_drawdown", "candidate_outcome"),
        forward_return_horizons=(1, 3, 5, 10, 20),
        forward_volatility_horizons=(5, 10, 20),
        future_drawdown_horizons=(5, 10, 20),
        notes="Genel amaçlı supervised ML dataset hazırlık profili."
    ),
    "price_action_light_dataset": MLDatasetProfile(
        name="price_action_light_dataset",
        description="Lighter profile focusing on price action with fewer dependencies",
        feature_sets=("technical", "momentum", "trend", "volatility", "price_action", "regime"),
        target_types=("forward_return", "direction_class", "future_drawdown"),
        forward_return_horizons=(1, 3, 5),
        forward_volatility_horizons=(5,),
        future_drawdown_horizons=(5, 10),
        min_rows=300,
        notes="Daha sade ve daha az candidate bağımlı dataset profili."
    ),
    "candidate_outcome_dataset": MLDatasetProfile(
        name="candidate_outcome_dataset",
        description="Profile focusing on candidate outcome classification",
        feature_sets=(
            "signal_candidates", "decision_candidates", "strategy_candidates",
            "strategy_rule_candidates", "risk_candidates", "sizing_candidates",
            "level_candidates", "backtest"
        ),
        target_types=("candidate_outcome", "trade_result", "reward_risk_outcome"),
        forward_return_horizons=(),
        forward_volatility_horizons=(),
        future_drawdown_horizons=(),
        notes="Candidate outcome sınıflandırmasına odaklı dataset profili."
    ),
    "regime_macro_dataset": MLDatasetProfile(
        name="regime_macro_dataset",
        description="Profile focusing on regimes and macro contexts",
        feature_sets=("trend", "volatility", "mtf", "regime", "macro", "asset_profiles", "benchmarks"),
        target_types=("forward_return", "direction_class", "future_volatility"),
        forward_return_horizons=(5, 10, 20),
        forward_volatility_horizons=(10, 20),
        future_drawdown_horizons=(20,),
        notes="Rejim ve makro bağlam ağırlıklı dataset profili."
    )
}

class ConfigError(Exception):
    pass

def get_ml_dataset_profile(name: str) -> MLDatasetProfile:
    if name not in _PROFILES:
        raise ConfigError(f"Unknown ML dataset profile: {name}")
    return _PROFILES[name]

def list_ml_dataset_profiles(enabled_only: bool = True) -> list[MLDatasetProfile]:
    profiles = list(_PROFILES.values())
    if enabled_only:
        profiles = [p for p in profiles if p.enabled]
    return profiles

def validate_ml_dataset_profiles() -> None:
    for name, profile in _PROFILES.items():
        if not profile.feature_sets:
            raise ConfigError(f"Profile {name} has no feature_sets")
        if not profile.target_types:
            raise ConfigError(f"Profile {name} has no target_types")

        for horizon in profile.forward_return_horizons + profile.forward_volatility_horizons + profile.future_drawdown_horizons:
            if horizon <= 0:
                raise ConfigError(f"Profile {name} has invalid horizon <= 0")

        if not (0 <= profile.test_size_ratio <= 1):
             raise ConfigError(f"Profile {name} has invalid test_size_ratio")
        if not (0 <= profile.validation_size_ratio <= 1):
             raise ConfigError(f"Profile {name} has invalid validation_size_ratio")

        if profile.test_size_ratio + profile.validation_size_ratio >= 0.8:
            raise ConfigError(f"Profile {name} splits leave too little for training")

        if not (0 <= profile.max_feature_nan_ratio <= 1):
             raise ConfigError(f"Profile {name} has invalid max_feature_nan_ratio")
        if not (0 <= profile.max_target_nan_ratio <= 1):
             raise ConfigError(f"Profile {name} has invalid max_target_nan_ratio")

def get_default_ml_dataset_profile() -> MLDatasetProfile:
    from config.settings import settings
    return get_ml_dataset_profile(settings.default_ml_dataset_profile)
