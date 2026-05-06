with open("commodity_fx_signal_bot/strategies/condition_models.py", "w") as f:
    f.write("""from dataclasses import dataclass

@dataclass(frozen=True)
class RuleCondition:
    name: str
    left: str
    operator: str
    right: float | int | str | bool | tuple | list
    weight: float = 1.0
    required: bool = False
    description: str = ""

@dataclass(frozen=True)
class RuleTemplate:
    rule_id: str
    name: str
    strategy_family: str
    rule_group: str
    condition_label: str
    description: str
    conditions: tuple[RuleCondition, ...]
    preferred_regimes: tuple[str, ...] = ()
    avoided_regimes: tuple[str, ...] = ()
    preferred_asset_classes: tuple[str, ...] = ()
    min_required_conditions: int = 1
    enabled: bool = True
    notes: str = ""

_SUPPORTED_OPERATORS = [
    "gt", "gte", "lt", "lte", "eq", "neq", "between",
    "abs_gt", "abs_lt", "is_true", "is_false", "contains", "not_contains"
]

def list_supported_operators() -> list[str]:
    return list(_SUPPORTED_OPERATORS)

def validate_rule_condition(condition: RuleCondition) -> None:
    if condition.operator not in _SUPPORTED_OPERATORS:
        raise ValueError(f"Unsupported operator '{condition.operator}' in rule condition '{condition.name}'")
    if condition.operator == "between":
        if not isinstance(condition.right, (tuple, list)) or len(condition.right) != 2:
            raise ValueError(f"Operator 'between' requires 'right' to be a tuple/list of length 2 in '{condition.name}'")
    if condition.weight < 0.0:
        raise ValueError(f"Weight must be non-negative in '{condition.name}'")

def validate_rule_template(template: RuleTemplate) -> None:
    if not template.rule_id:
        raise ValueError("rule_id cannot be empty")
    if template.min_required_conditions < 0:
        raise ValueError(f"min_required_conditions must be >= 0 in template '{template.rule_id}'")
    for condition in template.conditions:
        validate_rule_condition(condition)
""")

with open("commodity_fx_signal_bot/strategies/condition_library.py", "w") as f:
    f.write("""from .condition_models import RuleCondition

def condition_column_gt(column: str, threshold: float, name: str | None = None, weight: float = 1.0, required: bool = False) -> RuleCondition:
    return RuleCondition(name=name or f"{column}_gt_{threshold}", left=column, operator="gt", right=threshold, weight=weight, required=required)

def condition_column_gte(column: str, threshold: float, name: str | None = None, weight: float = 1.0, required: bool = False) -> RuleCondition:
    return RuleCondition(name=name or f"{column}_gte_{threshold}", left=column, operator="gte", right=threshold, weight=weight, required=required)

def condition_column_lt(column: str, threshold: float, name: str | None = None, weight: float = 1.0, required: bool = False) -> RuleCondition:
    return RuleCondition(name=name or f"{column}_lt_{threshold}", left=column, operator="lt", right=threshold, weight=weight, required=required)

def condition_column_lte(column: str, threshold: float, name: str | None = None, weight: float = 1.0, required: bool = False) -> RuleCondition:
    return RuleCondition(name=name or f"{column}_lte_{threshold}", left=column, operator="lte", right=threshold, weight=weight, required=required)

def condition_column_between(column: str, low: float, high: float, name: str | None = None, weight: float = 1.0, required: bool = False) -> RuleCondition:
    return RuleCondition(name=name or f"{column}_between_{low}_{high}", left=column, operator="between", right=(low, high), weight=weight, required=required)

def condition_bool_true(column: str, name: str | None = None, weight: float = 1.0, required: bool = False) -> RuleCondition:
    return RuleCondition(name=name or f"{column}_is_true", left=column, operator="is_true", right=True, weight=weight, required=required)

def condition_bool_false(column: str, name: str | None = None, weight: float = 1.0, required: bool = False) -> RuleCondition:
    return RuleCondition(name=name or f"{column}_is_false", left=column, operator="is_false", right=False, weight=weight, required=required)

def condition_label_contains(column: str, value: str, name: str | None = None, weight: float = 1.0, required: bool = False) -> RuleCondition:
    return RuleCondition(name=name or f"{column}_contains_{value}", left=column, operator="contains", right=value, weight=weight, required=required)

def trend_context_conditions() -> list[RuleCondition]:
    return [
        condition_column_gt("regime_trend_score", 0.5, name="strong_trend_regime", weight=1.5),
        condition_column_gt("mtf_trend_alignment_score", 0.6, name="mtf_trend_alignment", weight=1.0)
    ]

def mean_reversion_context_conditions() -> list[RuleCondition]:
    return [
        condition_column_lt("regime_trend_score", 0.3, name="weak_trend_regime", weight=1.0),
        condition_column_lt("strong_trend_conflict", 0.4, name="low_trend_conflict", weight=1.0)
    ]

def breakout_context_conditions() -> list[RuleCondition]:
    return [
        condition_column_gt("volatility_expansion_score", 0.6, name="volatility_expansion", weight=1.5),
        condition_column_between("regime_trend_score", 0.2, 0.8, name="breakout_friendly_trend", weight=1.0)
    ]

def pullback_context_conditions() -> list[RuleCondition]:
    return [
        condition_column_gt("regime_trend_score", 0.5, name="established_trend", weight=1.5),
        condition_column_gt("mean_reversion_pullback_score", 0.5, name="pullback_event_active", weight=1.5)
    ]

def divergence_context_conditions() -> list[RuleCondition]:
    return [
        condition_bool_true("has_divergence_event", name="divergence_detected", weight=2.0, required=True),
        condition_column_lt("momentum_strength", 0.4, name="weakening_momentum", weight=1.0)
    ]

def no_trade_context_conditions() -> list[RuleCondition]:
    return [
        condition_label_contains("decision_label", "no_trade", name="no_trade_decision", required=True),
        condition_column_lt("quality_score", 0.3, name="low_quality_score")
    ]

def quality_block_conditions() -> list[RuleCondition]:
    return [
        condition_column_lt("decision_quality_score", 0.4, name="decision_quality_too_low", weight=2.0)
    ]

def conflict_block_conditions() -> list[RuleCondition]:
    return [
        condition_column_gt("conflict_score", 0.7, name="unacceptable_conflict_score", weight=2.0)
    ]
""")

with open("commodity_fx_signal_bot/strategies/rule_templates.py", "w") as f:
    f.write("""from .condition_models import RuleTemplate
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
""")

with open("commodity_fx_signal_bot/strategies/rule_engine.py", "w") as f:
    f.write("""import pandas as pd
from typing import Any
from .condition_models import RuleCondition, RuleTemplate

class RuleEngine:
    def __init__(self, templates: list[RuleTemplate] | None = None):
        self.templates = templates or []

    def evaluate_condition(
        self,
        condition: RuleCondition,
        row: pd.Series,
        context_snapshot: dict | None = None,
    ) -> dict:
        context_snapshot = context_snapshot or {}

        val: Any = None
        warning = ""

        if condition.left in row:
            val = row[condition.left]
        elif condition.left in context_snapshot:
            val = context_snapshot[condition.left]
        else:
            warning = f"Column/key '{condition.left}' not found in row or context"

        passed = False
        if val is not None and not pd.isna(val):
            try:
                op = condition.operator
                right = condition.right

                if op == "gt": passed = float(val) > float(right)
                elif op == "gte": passed = float(val) >= float(right)
                elif op == "lt": passed = float(val) < float(right)
                elif op == "lte": passed = float(val) <= float(right)
                elif op == "eq": passed = val == right
                elif op == "neq": passed = val != right
                elif op == "between": passed = float(right[0]) <= float(val) <= float(right[1])
                elif op == "abs_gt": passed = abs(float(val)) > float(right)
                elif op == "abs_lt": passed = abs(float(val)) < float(right)
                elif op == "is_true": passed = bool(val) is True
                elif op == "is_false": passed = bool(val) is False
                elif op == "contains": passed = str(right) in str(val)
                elif op == "not_contains": passed = str(right) not in str(val)
            except (ValueError, TypeError) as e:
                warning = f"Evaluation error: {e}"
                passed = False

        return {
            "condition_name": condition.name,
            "passed": passed,
            "required": condition.required,
            "weight": condition.weight,
            "left": condition.left,
            "operator": condition.operator,
            "right": condition.right,
            "observed_value": val,
            "warning": warning
        }

    def evaluate_template(
        self,
        template: RuleTemplate,
        row: pd.Series,
        context_snapshot: dict | None = None,
    ) -> dict:
        required_passed = 0
        required_failed = 0
        passed_conds = []
        failed_conds = []
        warnings = []

        total_weight = 0.0
        passed_weight = 0.0

        for cond in template.conditions:
            res = self.evaluate_condition(cond, row, context_snapshot)
            if res["warning"]:
                warnings.append(res["warning"])

            total_weight += cond.weight
            if res["passed"]:
                passed_weight += cond.weight
                passed_conds.append(cond.name)
                if cond.required:
                    required_passed += 1
            else:
                failed_conds.append(cond.name)
                if cond.required:
                    required_failed += 1

        match_score = (passed_weight / total_weight) if total_weight > 0 else 0.0

        matched = required_failed == 0 and len(passed_conds) >= template.min_required_conditions
        partial_match = required_failed == 0 and len(passed_conds) > 0 and not matched

        return {
            "rule_id": template.rule_id,
            "strategy_family": template.strategy_family,
            "rule_group": template.rule_group,
            "condition_label": template.condition_label,
            "matched": matched,
            "partial_match": partial_match,
            "match_score": match_score,
            "required_conditions_passed": required_passed,
            "required_conditions_failed": required_failed,
            "passed_conditions": passed_conds,
            "failed_conditions": failed_conds,
            "warnings": warnings
        }

    def evaluate_templates(
        self,
        templates: list[RuleTemplate],
        row: pd.Series,
        context_snapshot: dict | None = None,
    ) -> list[dict]:
        return [self.evaluate_template(t, row, context_snapshot) for t in templates]
""")

with open("commodity_fx_signal_bot/strategies/entry_exit_candidates.py", "w") as f:
    f.write("""from dataclasses import dataclass, asdict
from typing import Any
import hashlib
import json
from .rule_config import StrategyRuleProfile

@dataclass
class EntryExitConditionCandidate:
    symbol: str
    timeframe: str
    timestamp: str
    condition_id: str
    source_strategy_id: str
    source_decision_id: str
    strategy_family: str
    rule_id: str
    rule_group: str
    condition_label: str
    rule_status: str
    directional_bias: str
    candidate_type: str
    match_score: float
    confidence_score: float
    quality_score: float
    readiness_score: float
    conflict_score: float
    passed_rule_filters: bool
    passed_conditions: list[str]
    failed_conditions: list[str]
    required_failures: list[str]
    block_reasons: list[str]
    warnings: list[str]
    notes: str = ""

def build_condition_id(symbol: str, timeframe: str, timestamp: str, rule_id: str, source_strategy_id: str) -> str:
    raw = f"{symbol}_{timeframe}_{timestamp}_{rule_id}_{source_strategy_id}"
    return hashlib.sha256(raw.encode("utf-8")).hexdigest()[:16]

def entry_exit_candidate_to_dict(candidate: EntryExitConditionCandidate) -> dict[str, Any]:
    return asdict(candidate)

def infer_rule_status_from_result(result: dict, profile: StrategyRuleProfile, base_confidence: float = 0.5, base_quality: float = 0.5, base_readiness: float = 0.5, conflict: float = 0.0) -> str:

    if result.get("required_conditions_failed", 0) > 0:
        return "blocked_candidate"

    match_score = result.get("match_score", 0.0)

    if match_score < profile.min_match_score:
        return "partial_match_candidate"

    if conflict > profile.max_conflict_score:
        return "conflict_blocked"

    if base_confidence < profile.min_confidence:
        return "insufficient_context"

    if base_quality < profile.min_quality_score:
        return "insufficient_quality"

    if base_readiness < profile.min_readiness_score:
        return "wait_candidate"

    if result.get("matched", False):
        return "matched_candidate"

    return "unknown"
""")

with open("commodity_fx_signal_bot/strategies/rule_evaluator.py", "w") as f:
    f.write("""import pandas as pd
from typing import Any
from .rule_config import StrategyRuleProfile
from .rule_engine import RuleEngine
from .rule_templates import list_builtin_rule_templates
from .entry_exit_candidates import EntryExitConditionCandidate, build_condition_id, infer_rule_status_from_result

class StrategyRuleEvaluator:
    def __init__(self, profile: StrategyRuleProfile, rule_engine: RuleEngine | None = None):
        self.profile = profile
        if rule_engine is None:
            all_templates = list_builtin_rule_templates(enabled_only=True)
            enabled_templates = [
                t for t in all_templates
                if t.strategy_family in profile.enabled_strategy_families
                and t.rule_group in profile.enabled_rule_groups
            ]
            self.rule_engine = RuleEngine(templates=enabled_templates)
        else:
            self.rule_engine = rule_engine

    def evaluate_strategy_candidate(
        self,
        symbol: str,
        timeframe: str,
        strategy_row: pd.Series,
        context_snapshot: dict | None = None,
    ) -> list[EntryExitConditionCandidate]:
        candidates = []
        if context_snapshot is None:
            context_snapshot = {}

        timestamp = str(strategy_row.get("timestamp", ""))
        source_strategy_id = str(strategy_row.get("strategy_id", ""))
        source_decision_id = str(strategy_row.get("decision_id", ""))
        strategy_family = str(strategy_row.get("strategy_family", ""))
        directional_bias = str(strategy_row.get("directional_bias", ""))
        candidate_type = str(strategy_row.get("candidate_type", ""))

        base_confidence = float(strategy_row.get("decision_confidence_score", 0.5))
        base_quality = float(strategy_row.get("decision_quality_score", 0.5))
        base_readiness = float(strategy_row.get("strategy_readiness", 0.5))
        conflict_score = float(strategy_row.get("conflict_score", 0.0))

        applicable_templates = [
            t for t in self.rule_engine.templates
            if t.strategy_family in (strategy_family, "generic", "no_trade", "watchlist")
        ]

        results = self.rule_engine.evaluate_templates(applicable_templates, strategy_row, context_snapshot)

        for res in results:
            rule_status = infer_rule_status_from_result(
                res,
                self.profile,
                base_confidence=base_confidence,
                base_quality=base_quality,
                base_readiness=base_readiness,
                conflict=conflict_score
            )

            passed_filters = rule_status == "matched_candidate"

            block_reasons = []
            if rule_status == "blocked_candidate":
                block_reasons.append("Required conditions failed")
            elif rule_status == "conflict_blocked":
                block_reasons.append("High conflict score")
            elif rule_status == "insufficient_context":
                block_reasons.append("Low confidence score")
            elif rule_status == "insufficient_quality":
                block_reasons.append("Low quality score")

            cond_id = build_condition_id(symbol, timeframe, timestamp, res["rule_id"], source_strategy_id)

            candidates.append(
                EntryExitConditionCandidate(
                    symbol=symbol,
                    timeframe=timeframe,
                    timestamp=timestamp,
                    condition_id=cond_id,
                    source_strategy_id=source_strategy_id,
                    source_decision_id=source_decision_id,
                    strategy_family=strategy_family,
                    rule_id=res["rule_id"],
                    rule_group=res["rule_group"],
                    condition_label=res["condition_label"],
                    rule_status=rule_status,
                    directional_bias=directional_bias,
                    candidate_type=candidate_type,
                    match_score=res["match_score"],
                    confidence_score=base_confidence,
                    quality_score=base_quality,
                    readiness_score=base_readiness,
                    conflict_score=conflict_score,
                    passed_rule_filters=passed_filters,
                    passed_conditions=res["passed_conditions"],
                    failed_conditions=res["failed_conditions"],
                    required_failures=[c for c in res["failed_conditions"] if c in [c2.name for t in self.rule_engine.templates if t.rule_id == res["rule_id"] for c2 in t.conditions if c2.required]],
                    block_reasons=block_reasons,
                    warnings=res["warnings"]
                )
            )

        return candidates

    def evaluate_strategy_frame(
        self,
        symbol: str,
        timeframe: str,
        strategies_df: pd.DataFrame,
        context_frames: dict[str, pd.DataFrame],
    ) -> tuple[list[EntryExitConditionCandidate], dict]:

        all_candidates = []
        warnings = []

        for _, row in strategies_df.iterrows():
            timestamp = row.name if isinstance(row.name, pd.Timestamp) else row.get("timestamp")

            context_snapshot = {}
            for name, df in context_frames.items():
                if df is not None and not df.empty and timestamp in df.index:
                    context_snapshot.update(df.loc[timestamp].to_dict())

            try:
                candidates = self.evaluate_strategy_candidate(symbol, timeframe, row, context_snapshot)
                all_candidates.extend(candidates)
            except Exception as e:
                warnings.append(f"Error evaluating rules for {symbol} at {timestamp}: {e}")

        summary = {
            "input_strategy_rows": len(strategies_df),
            "evaluated_rules": len(self.rule_engine.templates),
            "produced_condition_candidates": len(all_candidates),
            "by_rule_group": {},
            "by_strategy_family": {},
            "by_condition_label": {},
            "average_match_score": 0.0,
            "warnings": warnings
        }

        if all_candidates:
            match_scores = []
            for c in all_candidates:
                summary["by_rule_group"][c.rule_group] = summary["by_rule_group"].get(c.rule_group, 0) + 1
                summary["by_strategy_family"][c.strategy_family] = summary["by_strategy_family"].get(c.strategy_family, 0) + 1
                summary["by_condition_label"][c.condition_label] = summary["by_condition_label"].get(c.condition_label, 0) + 1
                match_scores.append(c.match_score)
            summary["average_match_score"] = sum(match_scores) / len(match_scores)

        return all_candidates, summary
""")

with open("commodity_fx_signal_bot/strategies/rule_labels.py", "w") as f:
    f.write("""_RULE_GROUPS = [
    "entry_context",
    "exit_context",
    "invalidation",
    "continuation",
    "wait",
    "risk_warning",
    "quality_warning",
    "no_trade_context"
]

_CONDITION_CANDIDATE_LABELS = [
    "entry_condition_candidate",
    "exit_condition_candidate",
    "invalidation_condition_candidate",
    "continuation_condition_candidate",
    "wait_condition_candidate",
    "no_trade_condition_candidate",
    "insufficient_quality_condition_candidate",
    "conflict_condition_candidate",
    "unknown_condition_candidate"
]

_RULE_STATUS_LABELS = [
    "matched_candidate",
    "partial_match_candidate",
    "blocked_candidate",
    "watchlist_candidate",
    "wait_candidate",
    "invalidated_candidate",
    "insufficient_context",
    "insufficient_quality",
    "conflict_blocked",
    "unknown"
]

def list_rule_groups() -> list[str]:
    return list(_RULE_GROUPS)

def list_condition_candidate_labels() -> list[str]:
    return list(_CONDITION_CANDIDATE_LABELS)

def list_rule_status_labels() -> list[str]:
    return list(_RULE_STATUS_LABELS)

def validate_rule_group(label: str) -> None:
    if label not in _RULE_GROUPS:
        raise ValueError(f"Invalid rule group label: {label}")

def validate_condition_candidate_label(label: str) -> None:
    if label not in _CONDITION_CANDIDATE_LABELS:
        raise ValueError(f"Invalid condition candidate label: {label}")

def validate_rule_status(label: str) -> None:
    if label not in _RULE_STATUS_LABELS:
        raise ValueError(f"Invalid rule status label: {label}")

def is_entry_condition(label: str) -> bool:
    return label == "entry_condition_candidate"

def is_exit_condition(label: str) -> bool:
    return label == "exit_condition_candidate"

def is_wait_condition(label: str) -> bool:
    return label == "wait_condition_candidate"

def is_blocked_status(label: str) -> bool:
    return label in ("blocked_candidate", "conflict_blocked", "insufficient_quality", "insufficient_context")
""")

with open("commodity_fx_signal_bot/strategies/rule_config.py", "w") as f:
    f.write("""from dataclasses import dataclass, field
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
        for field_name in ["min_match_score", "min_confidence", "min_quality_score", "max_conflict_score", "min_readiness_score"]:
            val = getattr(profile, field_name)
            if not 0.0 <= val <= 1.0:
                raise ConfigError(f"Profile {name} field {field_name} must be between 0.0 and 1.0.")

def get_default_strategy_rule_profile() -> StrategyRuleProfile:
    return get_strategy_rule_profile(settings.default_strategy_rule_profile)
""")

with open("commodity_fx_signal_bot/strategies/rule_pipeline.py", "w") as f:
    f.write("""import pandas as pd
import logging
from config.settings import Settings
from config.symbols import SymbolSpec
from data.storage.data_lake import DataLake
from .rule_config import StrategyRuleProfile, get_default_strategy_rule_profile
from .rule_evaluator import StrategyRuleEvaluator
from .rule_pool import StrategyRuleCandidatePool
from .rule_quality import build_rule_quality_report

logger = logging.getLogger(__name__)

class StrategyRulePipeline:
    def __init__(
        self,
        data_lake: DataLake,
        settings: Settings,
        profile: StrategyRuleProfile | None = None,
    ):
        self.data_lake = data_lake
        self.settings = settings
        self.profile = profile or get_default_strategy_rule_profile()
        self.evaluator = StrategyRuleEvaluator(self.profile)

    def load_strategy_candidates(
        self,
        spec: SymbolSpec,
        timeframe: str,
    ) -> tuple[pd.DataFrame, dict]:
        df = pd.DataFrame()
        warnings = []
        try:
            from ml.feature_store import FeatureStore
            store = FeatureStore(self.data_lake)
            df = store.load_strategy_candidates(spec, timeframe)
            if df.empty:
                warnings.append("Strategy candidates dataframe is empty")
        except Exception as e:
            warnings.append(f"Failed to load strategy candidates: {e}")
        return df, {"warnings": warnings}

    def load_rule_context_frames(
        self,
        spec: SymbolSpec,
        timeframe: str,
    ) -> tuple[dict[str, pd.DataFrame], dict]:

        frames = {}
        missing = []

        from ml.feature_store import FeatureStore
        store = FeatureStore(self.data_lake)

        loaders = {
            "decision_candidates": store.load_decision_candidates,
            "signal_candidates": store.load_signal_candidates,
            "regime": store.load_regime_features,
            "regime_events": store.load_regime_events,
            "mtf": lambda s, t: store.load_mtf_features(s, t),
            "mtf_events": lambda s, t: store.load_mtf_events(s, t),
            "macro": lambda s, t: store.load_macro_features(),
            "macro_events": lambda s, t: store.load_macro_events(),
            "asset_profiles": store.load_asset_profile_features,
            "asset_profile_events": store.load_asset_profile_events,
        }

        for name, loader in loaders.items():
            try:
                df = loader(spec, timeframe)
                if df is not None and not df.empty:
                    frames[name] = df
                else:
                    missing.append(name)
            except Exception:
                missing.append(name)

        return frames, {"missing_context_frames": missing}

    def build_for_symbol_timeframe(
        self,
        spec: SymbolSpec,
        timeframe: str = "1d",
        profile: StrategyRuleProfile | None = None,
        save: bool = True,
    ) -> tuple[pd.DataFrame, dict]:

        prof = profile or self.profile

        if spec.asset_class in ["benchmark", "synthetic", "macro"]:
            return pd.DataFrame(), {"warnings": [f"Skipped {spec.symbol} (asset_class: {spec.asset_class})"]}

        strat_df, strat_meta = self.load_strategy_candidates(spec, timeframe)
        if strat_df.empty:
            return pd.DataFrame(), {"warnings": strat_meta["warnings"]}

        ctx_frames, ctx_meta = self.load_rule_context_frames(spec, timeframe)

        evaluator = StrategyRuleEvaluator(prof)
        candidates, eval_summary = evaluator.evaluate_strategy_frame(
            spec.symbol, timeframe, strat_df, ctx_frames
        )

        pool = StrategyRuleCandidatePool()
        pool.extend(candidates)
        df = pool.to_dataframe()

        pool_summary = pool.summarize()
        quality_report = build_rule_quality_report(df, eval_summary)

        if save and not df.empty and self.settings.save_strategy_rule_candidates:
            try:
                self.data_lake.save_features(spec, "strategy_rule_candidates", timeframe, df)
                if self.settings.save_entry_exit_candidates:
                    self.data_lake.save_features(spec, "entry_exit_candidates", timeframe, df)
            except Exception as e:
                logger.error(f"Failed to save rule candidates for {spec.symbol}: {e}")

        summary = {
            "symbol": spec.symbol,
            "timeframe": timeframe,
            "profile": prof.name,
            "loaded_strategy_candidates": len(strat_df),
            "missing_context_frames": ctx_meta["missing_context_frames"],
            "rule_candidate_count": pool_summary["total_rule_candidates"],
            "passed_rule_candidate_count": pool_summary["passed_rule_candidates"],
            "quality_report": quality_report,
            "warnings": strat_meta["warnings"] + eval_summary["warnings"],
            "latest_rule_candidates": pool_summary["top_rule_candidates"]
        }

        return df, summary

    def build_for_universe(
        self,
        specs: list[SymbolSpec],
        timeframe: str = "1d",
        profile: StrategyRuleProfile | None = None,
        limit: int | None = None,
        save: bool = True,
    ) -> dict:

        prof = profile or self.profile
        universe_pool = StrategyRuleCandidatePool()

        processed = 0
        failed = 0

        target_specs = specs[:limit] if limit else specs

        for spec in target_specs:
            try:
                df, _ = self.build_for_symbol_timeframe(spec, timeframe, prof, save)
                if not df.empty:
                    pool = StrategyRuleCandidatePool.from_dataframe(df)
                    universe_pool.extend(pool.candidates)
                    processed += 1
            except Exception as e:
                logger.error(f"Error building rule candidates for {spec.symbol}: {e}")
                failed += 1

        summary = universe_pool.summarize()
        summary["processed_symbols"] = processed
        summary["failed_symbols"] = failed

        if save and self.settings.save_strategy_rule_pool:
            try:
                df_pool = universe_pool.to_dataframe()
                if not df_pool.empty:
                    if hasattr(self.data_lake, 'save_strategy_rule_pool'):
                        self.data_lake.save_strategy_rule_pool(timeframe, df_pool, prof.name)
            except Exception as e:
                logger.error(f"Failed to save strategy rule pool: {e}")

        return summary
""")

with open("commodity_fx_signal_bot/strategies/rule_pool.py", "w") as f:
    f.write("""import pandas as pd
from typing import Any
from .entry_exit_candidates import EntryExitConditionCandidate, entry_exit_candidate_to_dict
import ast

class StrategyRuleCandidatePool:
    def __init__(self):
        self.candidates: list[EntryExitConditionCandidate] = []

    def add(self, candidate: EntryExitConditionCandidate) -> None:
        self.candidates.append(candidate)

    def extend(self, candidates: list[EntryExitConditionCandidate]) -> None:
        self.candidates.extend(candidates)

    def to_dataframe(self) -> pd.DataFrame:
        if not self.candidates:
            return pd.DataFrame()

        dicts = [entry_exit_candidate_to_dict(c) for c in self.candidates]
        df = pd.DataFrame(dicts)

        for col in ["passed_conditions", "failed_conditions", "required_failures", "block_reasons", "warnings"]:
            if col in df.columns:
                df[col] = df[col].apply(lambda x: str(x) if isinstance(x, list) else x)

        if "timestamp" in df.columns:
            df["timestamp"] = pd.to_datetime(df["timestamp"])
            df.set_index("timestamp", inplace=True)

        return df

    @staticmethod
    def from_dataframe(df: pd.DataFrame) -> "StrategyRuleCandidatePool":
        pool = StrategyRuleCandidatePool()
        if df.empty:
            return pool

        df_copy = df.copy()
        if df_copy.index.name == "timestamp":
            df_copy.reset_index(inplace=True)

        for col in ["passed_conditions", "failed_conditions", "required_failures", "block_reasons", "warnings"]:
            if col in df_copy.columns:
                df_copy[col] = df_copy[col].apply(lambda x: ast.literal_eval(x) if isinstance(x, str) and x.startswith("[") else [])

        for _, row in df_copy.iterrows():
            d = row.to_dict()
            d["timestamp"] = str(d["timestamp"])
            pool.add(EntryExitConditionCandidate(**d))

        return pool

    def rank(self, top_n: int | None = None) -> list[EntryExitConditionCandidate]:
        sorted_candidates = sorted(
            self.candidates,
            key=lambda x: (x.passed_rule_filters, x.match_score, x.confidence_score, x.quality_score),
            reverse=True
        )
        if top_n is not None:
            return sorted_candidates[:top_n]
        return sorted_candidates

    def summarize(self) -> dict[str, Any]:
        passed = [c for c in self.candidates if c.passed_rule_filters]

        summary = {
            "total_rule_candidates": len(self.candidates),
            "passed_rule_candidates": len(passed),
            "by_symbol": {},
            "by_timeframe": {},
            "by_strategy_family": {},
            "by_rule_group": {},
            "by_condition_label": {},
            "by_rule_status": {},
            "average_match_score": 0.0,
            "average_confidence_score": 0.0,
            "top_rule_candidates": []
        }

        if self.candidates:
            match_scores = []
            conf_scores = []

            for c in self.candidates:
                summary["by_symbol"][c.symbol] = summary["by_symbol"].get(c.symbol, 0) + 1
                summary["by_timeframe"][c.timeframe] = summary["by_timeframe"].get(c.timeframe, 0) + 1
                summary["by_strategy_family"][c.strategy_family] = summary["by_strategy_family"].get(c.strategy_family, 0) + 1
                summary["by_rule_group"][c.rule_group] = summary["by_rule_group"].get(c.rule_group, 0) + 1
                summary["by_condition_label"][c.condition_label] = summary["by_condition_label"].get(c.condition_label, 0) + 1
                summary["by_rule_status"][c.rule_status] = summary["by_rule_status"].get(c.rule_status, 0) + 1
                match_scores.append(c.match_score)
                conf_scores.append(c.confidence_score)

            summary["average_match_score"] = sum(match_scores) / len(match_scores)
            summary["average_confidence_score"] = sum(conf_scores) / len(conf_scores)

            top_ranked = self.rank(top_n=5)
            summary["top_rule_candidates"] = [
                f"{c.symbol} | {c.rule_id} | {c.rule_status} | match: {c.match_score:.2f}"
                for c in top_ranked
            ]

        return summary
""")

with open("commodity_fx_signal_bot/strategies/rule_quality.py", "w") as f:
    f.write("""import pandas as pd

_FORBIDDEN_TERMS = [
    "BUY",
    "SELL",
    "OPEN_LONG",
    "OPEN_SHORT",
    "CLOSE_POSITION",
    "MARKET_ORDER",
    "LIMIT_ORDER",
    "STOP_LOSS_ORDER",
    "TAKE_PROFIT_ORDER",
    "SEND_ORDER",
    "EXECUTE_TRADE"
]

def check_rule_candidate_dataframe(df: pd.DataFrame) -> dict:
    if df.empty:
        return {"passed": True, "reason": "empty_dataframe"}

    res_ranges = check_rule_score_ranges(df)
    res_dup = check_rule_candidate_duplicates(df)
    res_miss = check_missing_rule_fields(df)
    res_forb = check_for_forbidden_order_terms_in_rules(df)

    passed = res_ranges["passed"] and res_dup["passed"] and res_miss["passed"] and res_forb["passed"]

    return {
        "passed": passed,
        "score_ranges": res_ranges,
        "duplicates": res_dup,
        "missing_fields": res_miss,
        "forbidden_terms": res_forb
    }

def check_rule_score_ranges(df: pd.DataFrame) -> dict:
    invalid_count = 0
    cols_to_check = ["match_score", "confidence_score", "quality_score", "readiness_score", "conflict_score"]

    for col in cols_to_check:
        if col in df.columns:
            invalid = df[(df[col] < 0.0) | (df[col] > 1.0)]
            invalid_count += len(invalid)

    return {
        "passed": invalid_count == 0,
        "invalid_score_count": invalid_count
    }

def check_rule_candidate_duplicates(df: pd.DataFrame) -> dict:
    dup_count = 0
    if "condition_id" in df.columns:
        dup_count = df.duplicated(subset=["condition_id"]).sum()

    return {
        "passed": dup_count == 0,
        "duplicate_condition_count": int(dup_count)
    }

def check_missing_rule_fields(df: pd.DataFrame) -> dict:
    required_cols = ["symbol", "timeframe", "condition_id", "rule_id", "rule_group", "condition_label", "rule_status", "match_score"]
    missing = [col for col in required_cols if col not in df.columns]

    return {
        "passed": len(missing) == 0,
        "missing_required_fields": missing
    }

def check_for_forbidden_order_terms_in_rules(df: pd.DataFrame) -> dict:
    forbidden_found = []

    for col in df.columns:
        if df[col].dtype == object or pd.api.types.is_string_dtype(df[col]):
            text_series = df[col].astype(str).str.upper()
            for term in _FORBIDDEN_TERMS:
                if text_series.str.contains(term).any():
                    forbidden_found.append(f"{col}:{term}")

    return {
        "passed": len(forbidden_found) == 0,
        "forbidden_order_terms_found": forbidden_found
    }

def build_rule_quality_report(df: pd.DataFrame, summary: dict) -> dict:
    quality_res = check_rule_candidate_dataframe(df)

    passed_ratio = 0.0
    if not df.empty and "passed_rule_filters" in df.columns:
        passed_ratio = df["passed_rule_filters"].mean()

    return {
        "rows": len(df),
        "passed": quality_res["passed"],
        "duplicate_condition_count": quality_res["duplicates"]["duplicate_condition_count"],
        "invalid_score_count": quality_res["score_ranges"]["invalid_score_count"],
        "missing_required_fields": quality_res["missing_fields"]["missing_required_fields"],
        "forbidden_order_terms_found": quality_res["forbidden_terms"]["forbidden_order_terms_found"],
        "passed_rule_ratio": float(passed_ratio),
        "warning_count": len(summary.get("warnings", []))
    }
""")
