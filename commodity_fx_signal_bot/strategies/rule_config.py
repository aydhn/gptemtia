from dataclasses import dataclass, field
from config.settings import settings


class ConfigError(Exception):
    pass


@dataclass(frozen=True)
class StrategyRuleProfile:
    name: str
    description: str
    enabled_strategy_families: tuple[str, ...]
    enabled_rule_groups: tuple[str, ...]
    component_weights: dict[str, float]
    min_match_score: float = 0.45
    min_confidence: float = 0.50
    min_quality_score: float = 0.50
    max_conflict_score: float = 0.65
    min_readiness_score: float = 0.45
    require_strategy_candidate_passed: bool = True
    require_decision_candidate_passed: bool = False
    allow_wait_candidates: bool = True
    allow_invalidation_candidates: bool = True
    enabled: bool = True
    notes: str = ""


_BUILTIN_PROFILES: dict[str, StrategyRuleProfile] = {
    "balanced_rule_evaluation": StrategyRuleProfile(
        name="balanced_rule_evaluation",
        description="Balanced default profile for strategy rule evaluation.",
        enabled_strategy_families=(
            "trend_following",
            "mean_reversion",
            "breakout",
            "pullback",
            "divergence_reversal",
            "momentum_continuation",
            "range_reversion",
            "watchlist",
            "no_trade",
        ),
        enabled_rule_groups=(
            "entry_context",
            "exit_context",
            "invalidation",
            "continuation",
            "wait",
        ),
        component_weights={
            "strategy_fit": 0.15,
            "decision_quality": 0.15,
            "rule_condition_match": 0.25,
            "regime_fit": 0.10,
            "mtf_fit": 0.10,
            "volatility_context": 0.10,
            "asset_profile_fit": 0.05,
            "data_quality": 0.05,
            "conflict_penalty": 0.05,
        },
        min_match_score=0.45,
        min_confidence=0.50,
        min_quality_score=0.50,
        max_conflict_score=0.65,
        min_readiness_score=0.45,
    ),
    "trend_rule_evaluation": StrategyRuleProfile(
        name="trend_rule_evaluation",
        description="Emphasizes trend following and momentum rules.",
        enabled_strategy_families=(
            "trend_following",
            "momentum_continuation",
            "pullback",
            "watchlist",
            "no_trade",
        ),
        enabled_rule_groups=(
            "entry_context",
            "exit_context",
            "invalidation",
            "continuation",
            "wait",
        ),
        component_weights={
            "strategy_fit": 0.10,
            "decision_quality": 0.10,
            "rule_condition_match": 0.30,
            "regime_fit": 0.20,
            "mtf_fit": 0.15,
            "volatility_context": 0.05,
            "asset_profile_fit": 0.05,
            "data_quality": 0.05,
            "conflict_penalty": 0.00,
        },
        min_match_score=0.45,
    ),
    "mean_reversion_rule_evaluation": StrategyRuleProfile(
        name="mean_reversion_rule_evaluation",
        description="Emphasizes mean reversion and range reversion rules.",
        enabled_strategy_families=(
            "mean_reversion",
            "range_reversion",
            "divergence_reversal",
            "watchlist",
            "no_trade",
        ),
        enabled_rule_groups=(
            "entry_context",
            "exit_context",
            "invalidation",
            "continuation",
            "wait",
        ),
        component_weights={
            "strategy_fit": 0.10,
            "decision_quality": 0.10,
            "rule_condition_match": 0.30,
            "regime_fit": 0.10,
            "mtf_fit": 0.10,
            "volatility_context": 0.15,
            "asset_profile_fit": 0.05,
            "data_quality": 0.05,
            "conflict_penalty": 0.05,
        },
        min_match_score=0.45,
    ),
    "breakout_rule_evaluation": StrategyRuleProfile(
        name="breakout_rule_evaluation",
        description="Emphasizes breakout and volatility expansion rules.",
        enabled_strategy_families=(
            "breakout",
            "watchlist",
            "no_trade",
        ),
        enabled_rule_groups=(
            "entry_context",
            "exit_context",
            "invalidation",
            "continuation",
            "wait",
        ),
        component_weights={
            "strategy_fit": 0.10,
            "decision_quality": 0.10,
            "rule_condition_match": 0.30,
            "regime_fit": 0.10,
            "mtf_fit": 0.10,
            "volatility_context": 0.20,
            "asset_profile_fit": 0.05,
            "data_quality": 0.05,
            "conflict_penalty": 0.00,
        },
        min_match_score=0.45,
    ),
    "conservative_rule_evaluation": StrategyRuleProfile(
        name="conservative_rule_evaluation",
        description="Requires higher scores to generate entry/exit rules.",
        enabled_strategy_families=(
            "trend_following",
            "mean_reversion",
            "breakout",
            "pullback",
            "divergence_reversal",
            "momentum_continuation",
            "range_reversion",
            "watchlist",
            "no_trade",
        ),
        enabled_rule_groups=(
            "entry_context",
            "exit_context",
            "invalidation",
            "continuation",
            "wait",
        ),
        component_weights={
            "strategy_fit": 0.15,
            "decision_quality": 0.15,
            "rule_condition_match": 0.25,
            "regime_fit": 0.10,
            "mtf_fit": 0.10,
            "volatility_context": 0.10,
            "asset_profile_fit": 0.05,
            "data_quality": 0.05,
            "conflict_penalty": 0.05,
        },
        min_match_score=0.60,
        min_confidence=0.65,
        min_quality_score=0.65,
        max_conflict_score=0.40,
        min_readiness_score=0.60,
    ),
}


def normalize_rule_component_weights(weights: dict[str, float]) -> dict[str, float]:
    total = sum(weights.values())
    if total <= 0:
        return {k: 0.0 for k in weights}
    return {k: v / total for k, v in weights.items()}


def get_strategy_rule_profile(name: str) -> StrategyRuleProfile:
    if name not in _BUILTIN_PROFILES:
        raise ConfigError(f"StrategyRuleProfile '{name}' not found.")
    return _BUILTIN_PROFILES[name]


def list_strategy_rule_profiles(enabled_only: bool = True) -> list[StrategyRuleProfile]:
    if enabled_only:
        return [p for p in _BUILTIN_PROFILES.values() if p.enabled]
    return list(_BUILTIN_PROFILES.values())


def validate_strategy_rule_profiles() -> None:
    for name, profile in _BUILTIN_PROFILES.items():
        if not profile.enabled_strategy_families:
            raise ConfigError(f"Profile {name} has no enabled strategy families.")
        if not profile.enabled_rule_groups:
            raise ConfigError(f"Profile {name} has no enabled rule groups.")
        for field_name in [
            "min_match_score",
            "min_confidence",
            "min_quality_score",
            "max_conflict_score",
            "min_readiness_score",
        ]:
            val = getattr(profile, field_name)
            if not 0.0 <= val <= 1.0:
                raise ConfigError(
                    f"Profile {name} field {field_name} must be between 0.0 and 1.0."
                )


def get_default_strategy_rule_profile() -> StrategyRuleProfile:
    return get_strategy_rule_profile(settings.default_strategy_rule_profile)
