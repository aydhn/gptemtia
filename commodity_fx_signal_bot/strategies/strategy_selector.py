import pandas as pd

from strategies.strategy_candidate import StrategyCandidate, build_strategy_id
from strategies.strategy_config import StrategySelectionProfile
from strategies.strategy_mapper import CandidateToStrategyMapper


class StrategySelector:
    def __init__(self, profile: StrategySelectionProfile):
        self.profile = profile
        self.mapper = CandidateToStrategyMapper(profile)

    def select_for_decision(
        self,
        symbol: str,
        timeframe: str,
        decision_row: pd.Series,
        context_snapshot: dict,
    ) -> list[StrategyCandidate]:
        fit_df, _ = self.mapper.build_family_fit_table(decision_row, context_snapshot)
        candidates = []

        timestamp_str = str(decision_row.name) if decision_row.name else "unknown"
        source_decision_id = str(decision_row.get("decision_id", "unknown"))
        source_decision_label = str(decision_row.get("decision_label", "unknown"))
        directional_bias = str(decision_row.get("directional_bias", "neutral"))
        candidate_type = str(decision_row.get("candidate_type", "unknown"))

        if fit_df.empty:
            return []

        for _, fit_row in fit_df.iterrows():
            family = fit_row["family"]
            selection_score = fit_row["selection_score"]
            fit_score = fit_row["fit_score"]
            block_reasons = fit_row.get("block_reasons", [])
            watchlist_reasons = []

            status = "unknown"
            passed = False

            if family == "no_trade":
                status = "no_trade_candidate"
            elif family == "watchlist":
                status = "watchlist_candidate"
            elif (
                float(decision_row.get("quality_score", 0.0))
                < self.profile.min_decision_quality
            ):
                status = "insufficient_quality"
                block_reasons.append("Low decision quality")
            elif fit_row["conflict_penalty"] > self.profile.max_conflict_score:
                status = "conflict_blocked"
                block_reasons.append("Conflict score too high")
            elif (
                selection_score >= self.profile.min_selection_score
                and fit_score >= self.profile.min_fit_score
            ):
                status = "selected_candidate"
                passed = True
            else:
                status = "blocked_candidate"
                if selection_score < self.profile.min_selection_score:
                    block_reasons.append("Selection score below threshold")
                if fit_score < self.profile.min_fit_score:
                    block_reasons.append("Fit score below threshold")

            if status == "blocked_candidate" and self.profile.allow_watchlist_family:
                status = "watchlist_candidate"
                watchlist_reasons.extend(block_reasons)
                block_reasons = []

            if directional_bias.upper() in ["BUY", "SELL", "OPEN_LONG", "OPEN_SHORT"]:
                directional_bias = "neutral"

            candidate = StrategyCandidate(
                symbol=symbol,
                timeframe=timeframe,
                timestamp=timestamp_str,
                strategy_id=build_strategy_id(
                    symbol, timeframe, timestamp_str, family, source_decision_id
                ),
                strategy_family=family,
                strategy_status=status,
                source_decision_id=source_decision_id,
                source_decision_label=source_decision_label,
                directional_bias=directional_bias,
                candidate_type=candidate_type,
                decision_score=float(decision_row.get("decision_score", 0.0)),
                decision_confidence=float(decision_row.get("confidence", 0.0)),
                decision_quality_score=float(decision_row.get("quality_score", 0.0)),
                strategy_selection_score=selection_score,
                strategy_fit_score=fit_score,
                regime_fit_score=fit_row["regime_fit"],
                mtf_fit_score=fit_row["mtf_fit"],
                macro_fit_score=fit_row["macro_fit"],
                asset_profile_fit_score=fit_row["asset_profile_fit"],
                conflict_penalty=fit_row["conflict_penalty"],
                strategy_readiness_score=float(
                    decision_row.get("strategy_readiness", 0.0)
                ),
                passed_strategy_filters=passed,
                block_reasons=block_reasons,
                watchlist_reasons=watchlist_reasons,
                warnings=fit_row.get("warnings", []),
            )
            candidates.append(candidate)

        return candidates

    def select_for_decision_frame(
        self,
        symbol: str,
        timeframe: str,
        decisions_df: pd.DataFrame,
        context_frames: dict[str, pd.DataFrame],
    ) -> tuple[list[StrategyCandidate], dict]:
        all_candidates = []
        from config.paths import LAKE_DIR
        from data.storage.data_lake import DataLake
        from strategies.strategy_context import StrategyContextLoader

        loader = StrategyContextLoader(DataLake(LAKE_DIR))

        for ts, row in decisions_df.iterrows():
            snapshot = loader.get_context_snapshot(context_frames, ts)
            candidates = self.select_for_decision(symbol, timeframe, row, snapshot)
            all_candidates.extend(candidates)

        summary = {
            "processed_decisions": len(decisions_df),
            "generated_candidates": len(all_candidates),
        }

        return all_candidates, summary
