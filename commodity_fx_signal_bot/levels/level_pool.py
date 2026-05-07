import pandas as pd
from levels.level_candidate import StopTargetLevelCandidate, level_candidate_to_dict


class StopTargetLevelCandidatePool:
    def __init__(self):
        self.candidates: list[StopTargetLevelCandidate] = []

    def add(self, candidate: StopTargetLevelCandidate) -> None:
        self.candidates.append(candidate)

    def extend(self, candidates: list[StopTargetLevelCandidate]) -> None:
        self.candidates.extend(candidates)

    def to_dataframe(self) -> pd.DataFrame:
        if not self.candidates:
            return pd.DataFrame()
        data = [level_candidate_to_dict(c) for c in self.candidates]
        df = pd.DataFrame(data)
        if "timestamp" in df.columns:
            try:
                df["timestamp"] = pd.to_datetime(df["timestamp"])
                df.set_index("timestamp", inplace=True)
            except Exception:
                pass
        return df

    def rank(self, top_n: int | None = None) -> list[StopTargetLevelCandidate]:
        if not self.candidates:
            return []

        def sort_key(c):
            rr = c.reward_risk if c.reward_risk is not None else 0.0
            return (c.stop_target_readiness_score, rr)

        sorted_cands = sorted(self.candidates, key=sort_key, reverse=True)
        if top_n is not None:
            return sorted_cands[:top_n]
        return sorted_cands

    def summarize(self) -> dict:
        if not self.candidates:
            return {
                "total_level_candidates": 0,
                "passed_level_candidates": 0,
                "rejected_level_candidates": 0,
                "watchlist_level_candidates": 0,
                "by_symbol": {},
                "by_timeframe": {},
                "by_strategy_family": {},
                "by_asset_class": {},
                "by_level_label": {},
                "by_level_method": {},
                "average_reward_risk": 0.0,
                "average_stop_distance_pct": 0.0,
                "average_target_distance_pct": 0.0,
                "top_level_candidates": [],
            }

        passed = sum(1 for c in self.candidates if c.passed_level_filters)
        rejected = sum(1 for c in self.candidates if "rejected" in c.level_label)
        watchlist = sum(1 for c in self.candidates if "watchlist" in c.level_label)

        rr_vals = [c.reward_risk for c in self.candidates if c.reward_risk is not None]
        avg_rr = sum(rr_vals) / len(rr_vals) if rr_vals else 0.0

        stop_pcts = [
            c.stop_distance_pct
            for c in self.candidates
            if c.stop_distance_pct is not None
        ]
        avg_stop_pct = sum(stop_pcts) / len(stop_pcts) if stop_pcts else 0.0

        target_pcts = [
            c.target_distance_pct
            for c in self.candidates
            if c.target_distance_pct is not None
        ]
        avg_tgt_pct = sum(target_pcts) / len(target_pcts) if target_pcts else 0.0

        return {
            "total_level_candidates": len(self.candidates),
            "passed_level_candidates": passed,
            "rejected_level_candidates": rejected,
            "watchlist_level_candidates": watchlist,
            "by_symbol": pd.Series([c.symbol for c in self.candidates])
            .value_counts()
            .to_dict(),
            "by_timeframe": pd.Series([c.timeframe for c in self.candidates])
            .value_counts()
            .to_dict(),
            "by_strategy_family": pd.Series(
                [c.strategy_family for c in self.candidates]
            )
            .value_counts()
            .to_dict(),
            "by_asset_class": pd.Series([c.asset_class for c in self.candidates])
            .value_counts()
            .to_dict(),
            "by_level_label": pd.Series([c.level_label for c in self.candidates])
            .value_counts()
            .to_dict(),
            "by_level_method": pd.Series([c.level_method for c in self.candidates])
            .value_counts()
            .to_dict(),
            "average_reward_risk": avg_rr,
            "average_stop_distance_pct": avg_stop_pct,
            "average_target_distance_pct": avg_tgt_pct,
            "top_level_candidates": [c.level_id for c in self.rank(5)],
        }
