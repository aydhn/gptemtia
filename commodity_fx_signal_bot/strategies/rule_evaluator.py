import pandas as pd
from typing import Any
from .rule_config import StrategyRuleProfile
from .rule_engine import RuleEngine
from .rule_templates import list_builtin_rule_templates
from .entry_exit_candidates import (
    EntryExitConditionCandidate,
    build_condition_id,
    infer_rule_status_from_result,
)


class StrategyRuleEvaluator:
    def __init__(
        self, profile: StrategyRuleProfile, rule_engine: RuleEngine | None = None
    ):
        self.profile = profile
        if rule_engine is None:
            all_templates = list_builtin_rule_templates(enabled_only=True)
            enabled_templates = [
                t
                for t in all_templates
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
            t
            for t in self.rule_engine.templates
            if t.strategy_family
            in (strategy_family, "generic", "no_trade", "watchlist")
        ]

        results = self.rule_engine.evaluate_templates(
            applicable_templates, strategy_row, context_snapshot
        )

        for res in results:
            rule_status = infer_rule_status_from_result(
                res,
                self.profile,
                base_confidence=base_confidence,
                base_quality=base_quality,
                base_readiness=base_readiness,
                conflict=conflict_score,
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

            cond_id = build_condition_id(
                symbol, timeframe, timestamp, res["rule_id"], source_strategy_id
            )

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
                    required_failures=[
                        c
                        for c in res["failed_conditions"]
                        if c
                        in [
                            c2.name
                            for t in self.rule_engine.templates
                            if t.rule_id == res["rule_id"]
                            for c2 in t.conditions
                            if c2.required
                        ]
                    ],
                    block_reasons=block_reasons,
                    warnings=res["warnings"],
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
            timestamp = (
                row.name if isinstance(row.name, pd.Timestamp) else row.get("timestamp")
            )

            context_snapshot = {}
            for name, df in context_frames.items():
                if df is not None and not df.empty and timestamp in df.index:
                    context_snapshot.update(df.loc[timestamp].to_dict())

            try:
                candidates = self.evaluate_strategy_candidate(
                    symbol, timeframe, row, context_snapshot
                )
                all_candidates.extend(candidates)
            except Exception as e:
                warnings.append(
                    f"Error evaluating rules for {symbol} at {timestamp}: {e}"
                )

        summary = {
            "input_strategy_rows": len(strategies_df),
            "evaluated_rules": len(self.rule_engine.templates),
            "produced_condition_candidates": len(all_candidates),
            "by_rule_group": {},
            "by_strategy_family": {},
            "by_condition_label": {},
            "average_match_score": 0.0,
            "warnings": warnings,
        }

        if all_candidates:
            match_scores = []
            for c in all_candidates:
                summary["by_rule_group"][c.rule_group] = (
                    summary["by_rule_group"].get(c.rule_group, 0) + 1
                )
                summary["by_strategy_family"][c.strategy_family] = (
                    summary["by_strategy_family"].get(c.strategy_family, 0) + 1
                )
                summary["by_condition_label"][c.condition_label] = (
                    summary["by_condition_label"].get(c.condition_label, 0) + 1
                )
                match_scores.append(c.match_score)
            summary["average_match_score"] = sum(match_scores) / len(match_scores)

        return all_candidates, summary
