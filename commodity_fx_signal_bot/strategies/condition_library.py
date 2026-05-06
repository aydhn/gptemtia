from .condition_models import RuleCondition


def condition_column_gt(
    column: str,
    threshold: float,
    name: str | None = None,
    weight: float = 1.0,
    required: bool = False,
) -> RuleCondition:
    return RuleCondition(
        name=name or f"{column}_gt_{threshold}",
        left=column,
        operator="gt",
        right=threshold,
        weight=weight,
        required=required,
    )


def condition_column_gte(
    column: str,
    threshold: float,
    name: str | None = None,
    weight: float = 1.0,
    required: bool = False,
) -> RuleCondition:
    return RuleCondition(
        name=name or f"{column}_gte_{threshold}",
        left=column,
        operator="gte",
        right=threshold,
        weight=weight,
        required=required,
    )


def condition_column_lt(
    column: str,
    threshold: float,
    name: str | None = None,
    weight: float = 1.0,
    required: bool = False,
) -> RuleCondition:
    return RuleCondition(
        name=name or f"{column}_lt_{threshold}",
        left=column,
        operator="lt",
        right=threshold,
        weight=weight,
        required=required,
    )


def condition_column_lte(
    column: str,
    threshold: float,
    name: str | None = None,
    weight: float = 1.0,
    required: bool = False,
) -> RuleCondition:
    return RuleCondition(
        name=name or f"{column}_lte_{threshold}",
        left=column,
        operator="lte",
        right=threshold,
        weight=weight,
        required=required,
    )


def condition_column_between(
    column: str,
    low: float,
    high: float,
    name: str | None = None,
    weight: float = 1.0,
    required: bool = False,
) -> RuleCondition:
    return RuleCondition(
        name=name or f"{column}_between_{low}_{high}",
        left=column,
        operator="between",
        right=(low, high),
        weight=weight,
        required=required,
    )


def condition_bool_true(
    column: str, name: str | None = None, weight: float = 1.0, required: bool = False
) -> RuleCondition:
    return RuleCondition(
        name=name or f"{column}_is_true",
        left=column,
        operator="is_true",
        right=True,
        weight=weight,
        required=required,
    )


def condition_bool_false(
    column: str, name: str | None = None, weight: float = 1.0, required: bool = False
) -> RuleCondition:
    return RuleCondition(
        name=name or f"{column}_is_false",
        left=column,
        operator="is_false",
        right=False,
        weight=weight,
        required=required,
    )


def condition_label_contains(
    column: str,
    value: str,
    name: str | None = None,
    weight: float = 1.0,
    required: bool = False,
) -> RuleCondition:
    return RuleCondition(
        name=name or f"{column}_contains_{value}",
        left=column,
        operator="contains",
        right=value,
        weight=weight,
        required=required,
    )


def trend_context_conditions() -> list[RuleCondition]:
    return [
        condition_column_gt(
            "regime_trend_score", 0.5, name="strong_trend_regime", weight=1.5
        ),
        condition_column_gt(
            "mtf_trend_alignment_score", 0.6, name="mtf_trend_alignment", weight=1.0
        ),
    ]


def mean_reversion_context_conditions() -> list[RuleCondition]:
    return [
        condition_column_lt(
            "regime_trend_score", 0.3, name="weak_trend_regime", weight=1.0
        ),
        condition_column_lt(
            "strong_trend_conflict", 0.4, name="low_trend_conflict", weight=1.0
        ),
    ]


def breakout_context_conditions() -> list[RuleCondition]:
    return [
        condition_column_gt(
            "volatility_expansion_score", 0.6, name="volatility_expansion", weight=1.5
        ),
        condition_column_between(
            "regime_trend_score", 0.2, 0.8, name="breakout_friendly_trend", weight=1.0
        ),
    ]


def pullback_context_conditions() -> list[RuleCondition]:
    return [
        condition_column_gt(
            "regime_trend_score", 0.5, name="established_trend", weight=1.5
        ),
        condition_column_gt(
            "mean_reversion_pullback_score",
            0.5,
            name="pullback_event_active",
            weight=1.5,
        ),
    ]


def divergence_context_conditions() -> list[RuleCondition]:
    return [
        condition_bool_true(
            "has_divergence_event",
            name="divergence_detected",
            weight=2.0,
            required=True,
        ),
        condition_column_lt(
            "momentum_strength", 0.4, name="weakening_momentum", weight=1.0
        ),
    ]


def no_trade_context_conditions() -> list[RuleCondition]:
    return [
        condition_label_contains(
            "decision_label", "no_trade", name="no_trade_decision", required=True
        ),
        condition_column_lt("quality_score", 0.3, name="low_quality_score"),
    ]


def quality_block_conditions() -> list[RuleCondition]:
    return [
        condition_column_lt(
            "decision_quality_score", 0.4, name="decision_quality_too_low", weight=2.0
        )
    ]


def conflict_block_conditions() -> list[RuleCondition]:
    return [
        condition_column_gt(
            "conflict_score", 0.7, name="unacceptable_conflict_score", weight=2.0
        )
    ]
