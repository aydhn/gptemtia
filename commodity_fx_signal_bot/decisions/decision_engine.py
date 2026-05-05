import pandas as pd
from typing import Dict, List, Tuple
from .decision_config import DecisionProfile
from .decision_candidate import DecisionCandidate, build_decision_id
from .directional_bias import (
    infer_dominant_direction,
    calculate_bullish_bearish_balance,
)
from .decision_components import (
    calculate_signal_score_component,
    calculate_directional_consensus_component,
    calculate_regime_confirmation_component,
    calculate_mtf_confirmation_component,
    calculate_macro_context_component,
    calculate_asset_profile_fit_component,
    calculate_quality_component,
    calculate_risk_precheck_component,
    calculate_strategy_readiness_score,
)
from .conflict_resolver import (
    detect_signal_direction_conflict,
    detect_regime_decision_conflict,
    detect_mtf_decision_conflict,
    detect_macro_decision_conflict,
    detect_asset_profile_conflict,
    aggregate_decision_conflicts,
)
from .neutral_filter import (
    should_mark_neutral,
    should_mark_no_trade,
    should_mark_watchlist,
    build_no_trade_reasons,
)


class DecisionEngine:
    def __init__(self, profile: DecisionProfile):
        self.profile = profile

    def build_decision_for_timestamp(
        self,
        symbol: str,
        timeframe: str,
        timestamp: pd.Timestamp,
        candidates_at_time: pd.DataFrame,
        context_frames: Dict[str, pd.DataFrame],
    ) -> DecisionCandidate:

        dominant_bias = infer_dominant_direction(candidates_at_time)

        # Determine candidate type (simplified)
        candidate_type = "mixed"
        if (
            not candidates_at_time.empty
            and "candidate_type" in candidates_at_time.columns
        ):
            counts = candidates_at_time["candidate_type"].value_counts()
            if not counts.empty:
                candidate_type = counts.index[0]

        source_count = len(candidates_at_time)
        top_score = (
            candidates_at_time["signal_score"].max()
            if not candidates_at_time.empty
            and "signal_score" in candidates_at_time.columns
            else 0.0
        )

        sig_comp = calculate_signal_score_component(candidates_at_time)
        dir_comp = calculate_directional_consensus_component(
            candidates_at_time, dominant_bias
        )
        reg_comp = calculate_regime_confirmation_component(
            context_frames, timestamp, dominant_bias, candidate_type
        )
        mtf_comp = calculate_mtf_confirmation_component(
            context_frames, timestamp, dominant_bias
        )
        mac_comp = calculate_macro_context_component(
            context_frames, timestamp, dominant_bias
        )
        ast_comp = calculate_asset_profile_fit_component(
            context_frames, timestamp, candidate_type
        )
        qual_comp = calculate_quality_component(
            candidates_at_time, context_frames, timestamp
        )
        risk_comp = calculate_risk_precheck_component(
            candidates_at_time, context_frames, timestamp
        )

        components = {
            "signal_score": sig_comp,
            "directional_consensus": dir_comp,
            "regime_confirmation": reg_comp,
            "mtf_confirmation": mtf_comp,
            "macro_context": mac_comp,
            "asset_profile_fit": ast_comp,
            "quality_score": qual_comp,
            "risk_precheck": risk_comp,
        }

        w = self.profile.component_weights
        decision_score = sum(w.get(k, 0) * v for k, v in components.items())

        conflicts = [
            detect_signal_direction_conflict(candidates_at_time),
            detect_regime_decision_conflict(context_frames, timestamp, dominant_bias),
            detect_mtf_decision_conflict(context_frames, timestamp, dominant_bias),
            detect_macro_decision_conflict(context_frames, timestamp, dominant_bias),
            detect_asset_profile_conflict(context_frames, timestamp, candidate_type),
        ]

        conflict_summary = aggregate_decision_conflicts(conflicts)
        conflict_score = conflict_summary["conflict_score"]

        strategy_readiness = calculate_strategy_readiness_score(components)

        balance = calculate_bullish_bearish_balance(candidates_at_time)
        is_neutral = should_mark_neutral(
            dir_comp, balance, self.profile.neutral_zone_threshold
        )

        is_no_trade, nt_reasons = should_mark_no_trade(
            qual_comp, conflict_score, strategy_readiness, self.profile
        )
        is_watchlist, wl_reasons = should_mark_watchlist(
            decision_score, qual_comp, conflict_score, self.profile
        )

        nt_reasons.extend(
            build_no_trade_reasons(components, conflict_summary, self.profile)
        )

        if is_no_trade or conflict_summary["blocking_conflict"]:
            decision_label = "no_trade_candidate"
        elif is_neutral:
            decision_label = "neutral_candidate"
        elif is_watchlist:
            decision_label = "watchlist_candidate"
        elif dominant_bias == "bullish":
            decision_label = "long_bias_candidate"
        elif dominant_bias == "bearish":
            decision_label = "short_bias_candidate"
        else:
            decision_label = "conflict_candidate"

        passed = not is_no_trade and decision_score >= self.profile.min_signal_score

        ts_str = (
            timestamp.isoformat() if hasattr(timestamp, "isoformat") else str(timestamp)
        )
        decision_id = build_decision_id(
            symbol, timeframe, ts_str, decision_label, candidate_type
        )

        return DecisionCandidate(
            symbol=symbol,
            timeframe=timeframe,
            timestamp=ts_str,
            decision_id=decision_id,
            decision_label=decision_label,
            directional_bias=dominant_bias,
            candidate_type=candidate_type,
            source_candidate_count=source_count,
            top_source_candidate_score=top_score,
            signal_score_component=sig_comp,
            directional_consensus_component=dir_comp,
            regime_confirmation_component=reg_comp,
            mtf_confirmation_component=mtf_comp,
            macro_context_component=mac_comp,
            asset_profile_fit_component=ast_comp,
            quality_component=qual_comp,
            risk_precheck_component=risk_comp,
            conflict_score=conflict_score,
            decision_score=decision_score,
            decision_confidence=dir_comp,
            decision_quality_score=qual_comp,
            strategy_readiness_score=strategy_readiness,
            passed_decision_filters=passed,
            no_trade_reasons=list(set(nt_reasons)),
            conflict_reasons=conflict_summary["conflict_reasons"],
            warnings=conflict_summary["warnings"],
            notes=f"Generated via {self.profile.name}",
        )

    def build_decisions(
        self,
        symbol: str,
        timeframe: str,
        signal_candidates_df: pd.DataFrame,
        context_frames: Dict[str, pd.DataFrame],
    ) -> Tuple[List[DecisionCandidate], Dict]:
        decisions = []
        if signal_candidates_df is None or signal_candidates_df.empty:
            return decisions, {"count": 0}

        # Group candidates by index (timestamp)
        for timestamp, group in signal_candidates_df.groupby(level=0):
            cand = self.build_decision_for_timestamp(
                symbol, timeframe, pd.Timestamp(timestamp), group, context_frames
            )
            decisions.append(cand)

        return decisions, {"count": len(decisions)}
