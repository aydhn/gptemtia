import pandas as pd
import numpy as np
import logging
from signals.signal_config import SignalScoringProfile
from signals.signal_candidate import SignalCandidate, build_candidate_id
import signals.signal_components as comp

logger = logging.getLogger(__name__)


class SignalScorer:
    def __init__(self, profile: SignalScoringProfile):
        self.profile = profile

    def score_candidate(
        self,
        symbol: str,
        timeframe: str,
        timestamp: pd.Timestamp,
        candidate_type: str,
        directional_bias: str,
        events_df: pd.DataFrame,
        context_frames: dict[str, pd.DataFrame],
    ) -> SignalCandidate:

        # Calculate components
        event_strength = comp.calculate_event_strength_score(
            events_df,
            timestamp,
            self.profile.event_lookback_bars,
            self.profile.decay_half_life_bars,
        )
        category_confluence = comp.calculate_category_confluence_score(
            events_df, timestamp, self.profile.event_lookback_bars
        )

        trend_context = comp.calculate_trend_context_score(
            context_frames, timestamp, directional_bias
        )
        regime_context = comp.calculate_regime_context_score(
            context_frames, timestamp, candidate_type, directional_bias
        )
        mtf_context = comp.calculate_mtf_context_score(
            context_frames, timestamp, directional_bias
        )
        macro_context = comp.calculate_macro_context_score(
            context_frames, timestamp, directional_bias
        )
        asset_profile_context = comp.calculate_asset_profile_context_score(
            context_frames, timestamp, candidate_type
        )
        data_quality = comp.calculate_data_quality_score(context_frames, timestamp)

        conflict_score = comp.calculate_conflict_score(
            events_df, context_frames, timestamp, directional_bias
        )
        risk_precheck = comp.calculate_risk_precheck_score(context_frames, timestamp)

        w = self.profile.component_weights

        # Calculate base score
        candidate_score = (
            event_strength * w.get("event_strength", 0)
            + category_confluence * w.get("category_confluence", 0)
            + trend_context * w.get("trend_context", 0)
            + regime_context * w.get("regime_context", 0)
            + mtf_context * w.get("mtf_context", 0)
            + macro_context * w.get("macro_context", 0)
            + asset_profile_context * w.get("asset_profile_context", 0)
            + data_quality * w.get("data_quality", 0)
        )

        # Apply conflict penalty
        candidate_score = max(0.0, candidate_score - (conflict_score * 0.5))

        # Simple quality and confidence
        quality_score = data_quality * 0.8 + 0.2
        confidence_score = (candidate_score * 0.7) + (quality_score * 0.3)

        # Determine if passed
        passed = (
            candidate_score >= self.profile.min_candidate_score
            and quality_score >= self.profile.min_quality_score
            and conflict_score <= self.profile.max_conflict_score
        )

        active_events = events_df["event_name"].tolist() if not events_df.empty else []
        primary_group = (
            events_df["event_group"].value_counts().index[0]
            if not events_df.empty
            else "unknown"
        )

        cand_id = build_candidate_id(
            symbol, timeframe, str(timestamp), candidate_type, directional_bias
        )

        return SignalCandidate(
            symbol=symbol,
            timeframe=timeframe,
            timestamp=str(timestamp),
            candidate_id=cand_id,
            candidate_type=candidate_type,
            directional_bias=directional_bias,
            primary_event_group=primary_group,
            active_events=active_events,
            event_count=len(active_events),
            event_strength_score=event_strength,
            category_confluence_score=category_confluence,
            trend_context_score=trend_context,
            regime_context_score=regime_context,
            mtf_context_score=mtf_context,
            macro_context_score=macro_context,
            asset_profile_context_score=asset_profile_context,
            data_quality_score=data_quality,
            conflict_score=conflict_score,
            risk_precheck_score=risk_precheck,
            candidate_score=float(np.clip(candidate_score, 0.0, 1.0)),
            confidence_score=float(np.clip(confidence_score, 0.0, 1.0)),
            quality_score=float(np.clip(quality_score, 0.0, 1.0)),
            passed_pre_filters=passed,
            warnings=[],
            notes="",
        )

    def score_timestamps(
        self,
        symbol: str,
        timeframe: str,
        events_df: pd.DataFrame,
        context_frames: dict[str, pd.DataFrame],
    ) -> tuple[list[SignalCandidate], dict]:

        candidates = []
        if events_df is None or events_df.empty:
            return [], {"processed_timestamps": 0}

        timestamps = events_df["timestamp"].unique()

        for ts_str in timestamps:
            ts = pd.to_datetime(ts_str)
            ts_events = events_df[events_df["timestamp"] == ts_str]

            # Find unique candidate types and biases for this timestamp
            types_biases = ts_events[
                ["candidate_type", "directional_bias"]
            ].drop_duplicates()

            for _, row in types_biases.iterrows():
                cand_type = row["candidate_type"]
                bias = row["directional_bias"]

                # Filter events for this specific type/bias context to score
                sub_events = ts_events[
                    (ts_events["candidate_type"] == cand_type)
                    & (ts_events["directional_bias"] == bias)
                ]

                candidate = self.score_candidate(
                    symbol, timeframe, ts, cand_type, bias, sub_events, context_frames
                )
                candidates.append(candidate)

        summary = {
            "processed_timestamps": len(timestamps),
            "generated_candidates": len(candidates),
        }

        return candidates, summary
