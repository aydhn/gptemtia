from .condition_models import RuleTemplate
from .condition_library import (
    condition_column_gt, condition_column_gte, condition_column_lt,
    condition_column_lte, condition_column_between, condition_bool_true,
    condition_bool_false, condition_label_contains, trend_context_conditions,
    mean_reversion_context_conditions, breakout_context_conditions,
    pullback_context_conditions, divergence_context_conditions,
    no_trade_context_conditions
)

def build_trend_following_rule_templates() -> list[RuleTemplate]:
    return [
        RuleTemplate(
            rule_id="trend_following_alignment_entry_context",
            name="Trend Following Alignment Entry Context",
            strategy_family="trend_following",
            rule_group="entry_context",
            condition_label="entry_condition_candidate",
            description="Entry candidate for strong aligned trend.",
            conditions=tuple([
                condition_label_contains("strategy_family", "trend_following", required=True),
                condition_label_contains("strategy_status", "candidate", required=True),
                condition_column_gt("decision_quality_score", 0.5, weight=1.0),
                condition_column_lt("conflict_score", 0.5, weight=1.0)
            ] + trend_context_conditions()),
            min_required_conditions=1
        )
    ]

def build_momentum_continuation_rule_templates() -> list[RuleTemplate]:
    return [
        RuleTemplate(
            rule_id="momentum_continuation_entry_context",
            name="Momentum Continuation Entry Context",
            strategy_family="momentum_continuation",
            rule_group="entry_context",
            condition_label="entry_condition_candidate",
            description="Entry candidate for momentum continuation.",
            conditions=tuple([
                condition_label_contains("strategy_family", "momentum_continuation", required=True),
                condition_column_gt("momentum_strength", 0.6, weight=1.5),
                condition_column_lt("volatility_shock", 0.7, weight=1.0)
            ]),
            min_required_conditions=1
        )
    ]

def build_mean_reversion_rule_templates() -> list[RuleTemplate]:
    return [
        RuleTemplate(
            rule_id="mean_reversion_snapback_entry_context",
            name="Mean Reversion Snapback Entry Context",
            strategy_family="mean_reversion",
            rule_group="entry_context",
            condition_label="entry_condition_candidate",
            description="Entry candidate for mean reversion setups.",
            conditions=tuple([
                condition_label_contains("strategy_family", "mean_reversion", required=True),
                condition_column_lt("volatility_shock", 0.8, weight=1.0)
            ] + mean_reversion_context_conditions()),
            min_required_conditions=1
        )
    ]

def build_breakout_rule_templates() -> list[RuleTemplate]:
    return [
        RuleTemplate(
            rule_id="breakout_setup_entry_context",
            name="Breakout Setup Entry Context",
            strategy_family="breakout",
            rule_group="entry_context",
            condition_label="entry_condition_candidate",
            description="Entry candidate for breakout setups.",
            conditions=tuple([
                condition_label_contains("strategy_family", "breakout", required=True),
                condition_column_gt("asset_breakout_suitability", 0.4, weight=1.0)
            ] + breakout_context_conditions()),
            min_required_conditions=1
        )
    ]

def build_pullback_rule_templates() -> list[RuleTemplate]:
    return [
        RuleTemplate(
            rule_id="trend_pullback_entry_context",
            name="Trend Pullback Entry Context",
            strategy_family="pullback",
            rule_group="entry_context",
            condition_label="entry_condition_candidate",
            description="Entry candidate for trend pullbacks.",
            conditions=tuple([
                condition_label_contains("strategy_family", "pullback", required=True),
                condition_column_lt("conflict_score", 0.5, weight=1.0)
            ] + pullback_context_conditions()),
            min_required_conditions=1
        )
    ]

def build_divergence_reversal_rule_templates() -> list[RuleTemplate]:
    return [
        RuleTemplate(
            rule_id="divergence_reversal_entry_context",
            name="Divergence Reversal Entry Context",
            strategy_family="divergence_reversal",
            rule_group="entry_context",
            condition_label="entry_condition_candidate",
            description="Entry candidate for divergence reversal.",
            conditions=tuple([
                condition_label_contains("strategy_family", "divergence_reversal", required=True),
                condition_column_lt("conflict_score", 0.6, weight=1.0)
            ] + divergence_context_conditions()),
            min_required_conditions=1
        )
    ]

def build_range_reversion_rule_templates() -> list[RuleTemplate]:
    return [
         RuleTemplate(
            rule_id="range_reversion_entry_context",
            name="Range Reversion Entry Context",
            strategy_family="range_reversion",
            rule_group="entry_context",
            condition_label="entry_condition_candidate",
            description="Entry candidate for range reversion.",
            conditions=tuple([
                condition_label_contains("strategy_family", "range_reversion", required=True),
                condition_column_lt("regime_trend_score", 0.4, weight=1.0)
            ]),
            min_required_conditions=1
        )
    ]

def build_generic_exit_rule_templates() -> list[RuleTemplate]:
    return [
        RuleTemplate(
            rule_id="generic_exit_context_candidate",
            name="Generic Exit Context Candidate",
            strategy_family="generic",
            rule_group="exit_context",
            condition_label="exit_condition_candidate",
            description="Generic exit condition candidate based on context.",
            conditions=tuple([
                condition_column_gt("conflict_score", 0.6, weight=1.0),
                condition_column_lt("strategy_readiness", 0.4, weight=1.0)
            ]),
            min_required_conditions=1
        )
    ]

def build_generic_invalidation_rule_templates() -> list[RuleTemplate]:
    return [
        RuleTemplate(
            rule_id="generic_invalidation_context_candidate",
            name="Generic Invalidation Context Candidate",
            strategy_family="generic",
            rule_group="invalidation",
            condition_label="invalidation_condition_candidate",
            description="Generic invalidation candidate.",
            conditions=tuple([
                condition_column_gt("conflict_score", 0.7, required=True),
                condition_column_lt("quality_score", 0.3, weight=1.0)
            ]),
            min_required_conditions=1
        )
    ]

def build_generic_wait_rule_templates() -> list[RuleTemplate]:
    return [
        RuleTemplate(
            rule_id="generic_wait_context_candidate",
            name="Generic Wait Context Candidate",
            strategy_family="generic",
            rule_group="wait",
            condition_label="wait_condition_candidate",
            description="Generic wait candidate.",
            conditions=tuple([
                condition_column_between("conflict_score", 0.4, 0.7, weight=1.0),
                condition_column_lt("strategy_readiness", 0.5, weight=1.0)
            ]),
            min_required_conditions=0
        )
    ]

def build_no_trade_rule_templates() -> list[RuleTemplate]:
    return [
        RuleTemplate(
            rule_id="generic_no_trade_context",
            name="Generic No Trade Context",
            strategy_family="no_trade",
            rule_group="no_trade_context",
            condition_label="no_trade_condition_candidate",
            description="Generic no trade condition.",
            conditions=tuple(no_trade_context_conditions()),
            min_required_conditions=1
        )
    ]

def build_watchlist_rule_templates() -> list[RuleTemplate]:
    return [
        RuleTemplate(
            rule_id="generic_watchlist_context",
            name="Generic Watchlist Context",
            strategy_family="watchlist",
            rule_group="wait",
            condition_label="wait_condition_candidate",
            description="Watchlist evaluation context.",
            conditions=tuple([
                condition_label_contains("strategy_family", "watchlist", required=True)
            ]),
            min_required_conditions=1
        )
    ]


def list_builtin_rule_templates(enabled_only: bool = True) -> list[RuleTemplate]:
    templates = []
    templates.extend(build_trend_following_rule_templates())
    templates.extend(build_momentum_continuation_rule_templates())
    templates.extend(build_mean_reversion_rule_templates())
    templates.extend(build_breakout_rule_templates())
    templates.extend(build_pullback_rule_templates())
    templates.extend(build_divergence_reversal_rule_templates())
    templates.extend(build_range_reversion_rule_templates())
    templates.extend(build_generic_exit_rule_templates())
    templates.extend(build_generic_invalidation_rule_templates())
    templates.extend(build_generic_wait_rule_templates())
    templates.extend(build_no_trade_rule_templates())
    templates.extend(build_watchlist_rule_templates())

    if enabled_only:
        return [t for t in templates if t.enabled]
    return templates

def validate_builtin_rule_templates() -> None:
    templates = list_builtin_rule_templates(enabled_only=False)
    seen_ids = set()
    for t in templates:
        if t.rule_id in seen_ids:
            raise ValueError(f"Duplicate rule_id found: {t.rule_id}")
        seen_ids.add(t.rule_id)
        from .condition_models import validate_rule_template
        validate_rule_template(t)

def get_rule_template(rule_id: str) -> RuleTemplate:
    for t in list_builtin_rule_templates(enabled_only=False):
        if t.rule_id == rule_id:
            return t
    raise ValueError(f"Rule template '{rule_id}' not found.")
