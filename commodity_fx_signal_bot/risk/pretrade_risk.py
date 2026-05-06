import pandas as pd
from typing import Tuple, List, Dict, Any
from risk.risk_config import RiskPrecheckProfile
from risk.risk_models import (
    RiskComponentScore,
    RiskContextSnapshot,
    aggregate_component_scores,
    invert_readiness_from_risk,
)
from risk.volatility_risk import calculate_volatility_risk_score
from risk.gap_risk import calculate_gap_risk_score
from risk.liquidity_risk import calculate_liquidity_risk_score
from risk.data_quality_risk import calculate_data_quality_risk_score
from risk.regime_risk import calculate_regime_risk_score
from risk.macro_risk import calculate_macro_risk_score
from risk.asset_risk import calculate_asset_profile_risk_score


class PreTradeRiskEvaluator:
    def __init__(self, profile: RiskPrecheckProfile):
        self.profile = profile

    def build_context_snapshot(
        self,
        symbol: str,
        timeframe: str,
        rule_row: pd.Series,
        context_frames: Dict[str, pd.DataFrame],
    ) -> Tuple[Dict[str, Any], Dict[str, Any]]:
        timestamp = (
            rule_row.name if isinstance(rule_row.name, (pd.Timestamp, str)) else None
        )
        if not timestamp and "timestamp" in rule_row:
            timestamp = rule_row["timestamp"]
        snapshot = {
            "symbol": symbol,
            "timeframe": timeframe,
            "timestamp": str(timestamp),
            "strategy_family": rule_row.get("strategy_family", ""),
            "condition_label": rule_row.get("condition_label", ""),
            "directional_bias": rule_row.get("directional_bias", "neutral"),
            "context_keys": list(context_frames.keys()),
        }
        for key, df in context_frames.items():
            if df is not None and not df.empty and timestamp in df.index:
                row = df.loc[timestamp]
                if isinstance(row, pd.DataFrame):
                    row = row.iloc[0]
                for col in row.index:
                    if col not in snapshot:
                        snapshot[col] = row[col]
        snapshot["context_available"] = len(context_frames) > 0
        return snapshot, {}

    def evaluate_rule_candidate(
        self,
        symbol: str,
        timeframe: str,
        rule_row: pd.Series,
        context_frames: Dict[str, pd.DataFrame],
    ) -> Tuple[Dict[str, Any], Dict[str, Any]]:
        snapshot, _ = self.build_context_snapshot(
            symbol, timeframe, rule_row, context_frames
        )
        component_scores = []
        if "volatility" in self.profile.enabled_risk_components:
            component_scores.append(
                calculate_volatility_risk_score(snapshot, self.profile)
            )
        if "gap" in self.profile.enabled_risk_components:
            component_scores.append(calculate_gap_risk_score(snapshot, self.profile))
        if "liquidity" in self.profile.enabled_risk_components:
            component_scores.append(
                calculate_liquidity_risk_score(snapshot, self.profile)
            )
        if "data_quality" in self.profile.enabled_risk_components:
            component_scores.append(
                calculate_data_quality_risk_score(snapshot, self.profile)
            )
        if "regime" in self.profile.enabled_risk_components:
            component_scores.append(calculate_regime_risk_score(snapshot, self.profile))
        if "macro" in self.profile.enabled_risk_components:
            component_scores.append(calculate_macro_risk_score(snapshot, self.profile))
        if "asset_profile" in self.profile.enabled_risk_components:
            component_scores.append(
                calculate_asset_profile_risk_score(snapshot, self.profile)
            )
        if "conflict" in self.profile.enabled_risk_components:
            conflict_risk = 0.5 if snapshot.get("event_conflict_high") else 0.1
            component_scores.append(
                RiskComponentScore(
                    "conflict",
                    conflict_risk,
                    "low" if conflict_risk < 0.4 else "high",
                    True,
                    [],
                    [],
                )
            )
        if "mtf" in self.profile.enabled_risk_components:
            mtf_risk = 0.5 if snapshot.get("event_mtf_conflict") else 0.1
            component_scores.append(
                RiskComponentScore(
                    "mtf", mtf_risk, "low" if mtf_risk < 0.4 else "high", True, [], []
                )
            )

        total_pretrade_risk_score, component_dict = aggregate_component_scores(
            component_scores, self.profile.component_weights
        )
        risk_readiness_score = invert_readiness_from_risk(total_pretrade_risk_score)

        blocking_reasons = []
        warnings = []
        for s in component_scores:
            if not s.passed:
                blocking_reasons.extend(s.reasons)
            warnings.extend(s.warnings)

        passed_risk_precheck = (
            total_pretrade_risk_score <= self.profile.max_total_pretrade_risk
            and risk_readiness_score >= self.profile.min_readiness_score
            and len(blocking_reasons) == 0
        )

        evaluation = {
            "component_scores": component_scores,
            "component_dict": component_dict,
            "total_pretrade_risk_score": total_pretrade_risk_score,
            "risk_readiness_score": risk_readiness_score,
            "blocking_reasons": blocking_reasons,
            "warnings": warnings,
            "passed_risk_precheck": passed_risk_precheck,
        }
        return evaluation, {}

    def evaluate_rule_frame(
        self,
        symbol: str,
        timeframe: str,
        rule_df: pd.DataFrame,
        context_frames: Dict[str, pd.DataFrame],
    ) -> Tuple[List[Dict[str, Any]], Dict[str, Any]]:
        evaluations = []
        for _, row in rule_df.iterrows():
            eval_dict, _ = self.evaluate_rule_candidate(
                symbol, timeframe, row, context_frames
            )
            eval_dict["_source_row"] = row
            evaluations.append(eval_dict)
        return evaluations, {}
