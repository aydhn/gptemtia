"""
Validation configuration module for walk-forward and parameter sensitivity.
"""

from dataclasses import dataclass


class ConfigError(Exception):
    """Exception raised for errors in validation configuration."""
    pass


@dataclass(frozen=True)
class ValidationProfile:
    """
    Profile definition for walk-forward validation and parameter sensitivity testing.
    """
    name: str
    description: str
    train_window_bars: int
    test_window_bars: int
    step_bars: int
    min_train_bars: int
    min_test_bars: int
    expanding_window: bool = False
    min_trades_per_split: int = 5
    max_parameter_combinations: int = 50
    primary_metric: str = "sharpe_ratio"
    secondary_metric: str = "max_drawdown_pct"
    overfitting_risk_threshold: float = 0.70
    min_robustness_score: float = 0.50
    enabled: bool = True
    notes: str = ""

    def __post_init__(self):
        if self.train_window_bars <= 0:
            raise ValueError(f"train_window_bars must be positive in profile {self.name}")
        if self.test_window_bars <= 0:
            raise ValueError(f"test_window_bars must be positive in profile {self.name}")
        if self.step_bars <= 0:
            raise ValueError(f"step_bars must be positive in profile {self.name}")
        if self.train_window_bars < self.min_train_bars:
            raise ValueError(f"train_window_bars must be >= min_train_bars in profile {self.name}")
        if self.test_window_bars < self.min_test_bars:
            raise ValueError(f"test_window_bars must be >= min_test_bars in profile {self.name}")
        if self.max_parameter_combinations <= 0:
            raise ValueError(f"max_parameter_combinations must be positive in profile {self.name}")
        if not (0 <= self.overfitting_risk_threshold <= 1):
            raise ValueError(f"overfitting_risk_threshold must be between 0 and 1 in profile {self.name}")
        if not (0 <= self.min_robustness_score <= 1):
            raise ValueError(f"min_robustness_score must be between 0 and 1 in profile {self.name}")


_VALIDATION_PROFILES = {
    "balanced_walk_forward_validation": ValidationProfile(
        name="balanced_walk_forward_validation",
        description="Balanced walk-forward validation profile for daily swing analysis.",
        train_window_bars=504,
        test_window_bars=126,
        step_bars=63,
        min_train_bars=252,
        min_test_bars=63,
        expanding_window=False,
        min_trades_per_split=5,
        max_parameter_combinations=50,
        primary_metric="sharpe_ratio",
        notes="Günlük swing analiz için dengeli walk-forward validasyon profili.",
    ),
    "expanding_walk_forward_validation": ValidationProfile(
        name="expanding_walk_forward_validation",
        description="Expanding window walk-forward validation profile.",
        train_window_bars=504,
        test_window_bars=126,
        step_bars=63,
        min_train_bars=252,
        min_test_bars=63,
        expanding_window=True,
        min_trades_per_split=5,
        max_parameter_combinations=50,
        primary_metric="sharpe_ratio",
        notes="Eğitim penceresi zamanla genişleyen validasyon profili.",
    ),
    "conservative_validation": ValidationProfile(
        name="conservative_validation",
        description="Conservative profile requiring more data and tighter robustness criteria.",
        train_window_bars=756,
        test_window_bars=126,
        step_bars=126,
        min_train_bars=504,
        min_test_bars=63,
        expanding_window=False,
        min_trades_per_split=10,
        max_parameter_combinations=50,
        primary_metric="sharpe_ratio",
        overfitting_risk_threshold=0.50,
        min_robustness_score=0.60,
        notes="Daha fazla veri ve daha sıkı robustness kriteri isteyen profil.",
    ),
    "fast_validation_debug": ValidationProfile(
        name="fast_validation_debug",
        description="Fast profile for debugging purposes.",
        train_window_bars=120,
        test_window_bars=30,
        step_bars=30,
        min_train_bars=90,
        min_test_bars=20,
        expanding_window=False,
        min_trades_per_split=2,
        max_parameter_combinations=10,
        primary_metric="sharpe_ratio",
        notes="Sadece hızlı debug için.",
    ),
}


def get_validation_profile(name: str) -> ValidationProfile:
    """Gets a validation profile by name."""
    if name not in _VALIDATION_PROFILES:
        raise ConfigError(f"Unknown validation profile: {name}")
    return _VALIDATION_PROFILES[name]


def list_validation_profiles(enabled_only: bool = True) -> list[ValidationProfile]:
    """Lists all available validation profiles."""
    profiles = list(_VALIDATION_PROFILES.values())
    if enabled_only:
        return [p for p in profiles if p.enabled]
    return profiles


def validate_validation_profiles() -> None:
    """Validates all configured validation profiles."""
    for profile in _VALIDATION_PROFILES.values():
        # Validation happens in __post_init__, so this just triggers it if not already
        pass


def get_default_validation_profile() -> ValidationProfile:
    """Gets the default validation profile."""
    return get_validation_profile("balanced_walk_forward_validation")
