from dataclasses import dataclass

from strategies.strategy_labels import validate_strategy_family


@dataclass(frozen=True)
class StrategyFamilySpec:
    family: str
    name: str
    description: str
    compatible_decision_labels: tuple[str, ...]
    compatible_candidate_types: tuple[str, ...]
    preferred_regimes: tuple[str, ...]
    avoided_regimes: tuple[str, ...]
    preferred_asset_profiles: tuple[str, ...]
    required_context_groups: tuple[str, ...]
    notes: str = ""


_FAMILY_SPECS = {
    "trend_following": StrategyFamilySpec(
        family="trend_following",
        name="Trend Following",
        description="Follows established trends.",
        compatible_decision_labels=("long_bias_candidate", "short_bias_candidate"),
        compatible_candidate_types=("trend_following", "momentum_continuation"),
        preferred_regimes=(
            "bullish_trend",
            "bearish_trend",
            "strong_bullish_trend",
            "strong_bearish_trend",
            "mtf_aligned_trend",
        ),
        avoided_regimes=("range_bound", "compressed_range", "conflicting_regime"),
        preferred_asset_profiles=("high_trend", "high_momentum"),
        required_context_groups=("trend", "regime"),
    ),
    "mean_reversion": StrategyFamilySpec(
        family="mean_reversion",
        name="Mean Reversion",
        description="Reverts to the mean after overextension.",
        compatible_decision_labels=(
            "long_bias_candidate",
            "short_bias_candidate",
            "watchlist_candidate",
        ),
        compatible_candidate_types=("mean_reversion", "pullback"),
        preferred_regimes=(
            "range_bound",
            "mean_reversion_friendly",
            "compressed_range",
        ),
        avoided_regimes=(
            "strong_bullish_trend",
            "strong_bearish_trend",
            "high_volatility",
        ),
        preferred_asset_profiles=("range_bound_profile",),
        required_context_groups=("mean_reversion", "regime"),
    ),
    "breakout": StrategyFamilySpec(
        family="breakout",
        name="Breakout",
        description="Trades breakouts from ranges or consolidation.",
        compatible_decision_labels=(
            "long_bias_candidate",
            "short_bias_candidate",
            "watchlist_candidate",
        ),
        compatible_candidate_types=("breakout", "volatility_expansion"),
        preferred_regimes=(
            "volatility_compression",
            "volatility_expansion",
            "breakout_candidate_regime",
        ),
        avoided_regimes=("conflicting_regime",),
        preferred_asset_profiles=("volatile_profile",),
        required_context_groups=("volatility", "regime"),
    ),
    "no_trade": StrategyFamilySpec(
        family="no_trade",
        name="No Trade",
        description="Conditions are unfavorable for trading.",
        compatible_decision_labels=(
            "no_trade_candidate",
            "conflict_candidate",
            "insufficient_quality_candidate",
            "risk_warning_candidate",
        ),
        compatible_candidate_types=("none", "unknown"),
        preferred_regimes=(),
        avoided_regimes=(),
        preferred_asset_profiles=(),
        required_context_groups=(),
    ),
    "watchlist": StrategyFamilySpec(
        family="watchlist",
        name="Watchlist",
        description="Conditions are forming but not ready.",
        compatible_decision_labels=("watchlist_candidate", "neutral_candidate"),
        compatible_candidate_types=("none", "unknown"),
        preferred_regimes=(),
        avoided_regimes=(),
        preferred_asset_profiles=(),
        required_context_groups=(),
    ),
}


def get_strategy_family_spec(family: str) -> StrategyFamilySpec:
    validate_strategy_family(family)
    if family not in _FAMILY_SPECS:
        return StrategyFamilySpec(
            family=family,
            name=family,
            description="",
            compatible_decision_labels=(),
            compatible_candidate_types=(),
            preferred_regimes=(),
            avoided_regimes=(),
            preferred_asset_profiles=(),
            required_context_groups=(),
        )
    return _FAMILY_SPECS[family]


def list_strategy_family_specs() -> list[StrategyFamilySpec]:
    return list(_FAMILY_SPECS.values())


def validate_strategy_family_specs() -> None:
    for family in _FAMILY_SPECS:
        validate_strategy_family(family)


def get_compatible_families_for_decision(
    decision_label: str, candidate_type: str
) -> list[str]:
    compatible_families = []

    if decision_label in (
        "no_trade_candidate",
        "conflict_candidate",
        "insufficient_quality_candidate",
        "risk_warning_candidate",
    ):
        return ["no_trade"]
    if decision_label in ("watchlist_candidate", "neutral_candidate"):
        return ["watchlist"]

    for spec in _FAMILY_SPECS.values():
        if decision_label in spec.compatible_decision_labels:
            if (
                candidate_type in spec.compatible_candidate_types
                or not spec.compatible_candidate_types
            ):
                compatible_families.append(spec.family)
            elif any(
                c_type in candidate_type for c_type in spec.compatible_candidate_types
            ):
                compatible_families.append(spec.family)

    if not compatible_families:
        return ["unknown"]

    return compatible_families
