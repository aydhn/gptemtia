import pandas as pd

from strategies.strategy_candidate import StrategyCandidate, strategy_candidate_to_dict


class StrategyCandidatePool:
    def __init__(self):
        self.strategies: list[StrategyCandidate] = []

    def add(self, candidate: StrategyCandidate) -> None:
        self.strategies.append(candidate)

    def extend(self, candidates: list[StrategyCandidate]) -> None:
        self.strategies.extend(candidates)

    def to_dataframe(self) -> pd.DataFrame:
        if not self.strategies:
            return pd.DataFrame()

        dicts = []
        for c in self.strategies:
            d = strategy_candidate_to_dict(c)
            d["block_reasons"] = ",".join(d["block_reasons"])
            d["watchlist_reasons"] = ",".join(d["watchlist_reasons"])
            d["warnings"] = ",".join(d["warnings"])
            dicts.append(d)

        df = pd.DataFrame(dicts)
        if "timestamp" in df.columns:
            df["timestamp"] = pd.to_datetime(df["timestamp"])
            df.set_index("timestamp", inplace=True)
            df.sort_index(inplace=True)

        return df

    @classmethod
    def from_dataframe(cls, df: pd.DataFrame) -> "StrategyCandidatePool":
        pool = cls()
        if df is None or df.empty:
            return pool

        df_reset = df.reset_index()
        if "timestamp" not in df_reset.columns and "index" in df_reset.columns:
            df_reset.rename(columns={"index": "timestamp"}, inplace=True)

        for _, row in df_reset.iterrows():
            d = row.to_dict()
            for list_field in ["block_reasons", "watchlist_reasons", "warnings"]:
                if list_field in d and isinstance(d[list_field], str):
                    d[list_field] = d[list_field].split(",") if d[list_field] else []
                elif list_field not in d:
                    d[list_field] = []

            candidate = StrategyCandidate(
                symbol=d.get("symbol", "unknown"),
                timeframe=d.get("timeframe", "1d"),
                timestamp=str(d.get("timestamp", "")),
                strategy_id=d.get("strategy_id", ""),
                strategy_family=d.get("strategy_family", "unknown"),
                strategy_status=d.get("strategy_status", "unknown"),
                source_decision_id=d.get("source_decision_id", ""),
                source_decision_label=d.get("source_decision_label", "unknown"),
                directional_bias=d.get("directional_bias", "neutral"),
                candidate_type=d.get("candidate_type", "unknown"),
                decision_score=float(d.get("decision_score", 0.0)),
                decision_confidence=float(d.get("decision_confidence", 0.0)),
                decision_quality_score=float(d.get("decision_quality_score", 0.0)),
                strategy_selection_score=float(d.get("strategy_selection_score", 0.0)),
                strategy_fit_score=float(d.get("strategy_fit_score", 0.0)),
                regime_fit_score=float(d.get("regime_fit_score", 0.0)),
                mtf_fit_score=float(d.get("mtf_fit_score", 0.0)),
                macro_fit_score=float(d.get("macro_fit_score", 0.0)),
                asset_profile_fit_score=float(d.get("asset_profile_fit_score", 0.0)),
                conflict_penalty=float(d.get("conflict_penalty", 0.0)),
                strategy_readiness_score=float(d.get("strategy_readiness_score", 0.0)),
                passed_strategy_filters=bool(d.get("passed_strategy_filters", False)),
                block_reasons=d["block_reasons"],
                watchlist_reasons=d["watchlist_reasons"],
                warnings=d["warnings"],
                notes=d.get("notes", ""),
            )
            pool.add(candidate)

        return pool

    def rank(self, top_n: int | None = None) -> list[StrategyCandidate]:
        ranked = sorted(
            self.strategies, key=lambda x: x.strategy_selection_score, reverse=True
        )
        if top_n is not None:
            return ranked[:top_n]
        return ranked

    def summarize(self) -> dict:
        total = len(self.strategies)
        passed = sum(1 for c in self.strategies if c.passed_strategy_filters)

        by_symbol = {}
        by_family = {}
        by_status = {}
        by_bias = {}

        total_selection_score = 0.0
        total_fit_score = 0.0

        for c in self.strategies:
            by_symbol[c.symbol] = by_symbol.get(c.symbol, 0) + 1
            by_family[c.strategy_family] = by_family.get(c.strategy_family, 0) + 1
            by_status[c.strategy_status] = by_status.get(c.strategy_status, 0) + 1
            by_bias[c.directional_bias] = by_bias.get(c.directional_bias, 0) + 1

            total_selection_score += c.strategy_selection_score
            total_fit_score += c.strategy_fit_score

        avg_selection = total_selection_score / total if total > 0 else 0.0
        avg_fit = total_fit_score / total if total > 0 else 0.0

        return {
            "total_strategy_candidates": total,
            "passed_strategy_candidates": passed,
            "by_symbol": by_symbol,
            "by_timeframe": {"1d": total},
            "by_strategy_family": by_family,
            "by_strategy_status": by_status,
            "by_directional_bias": by_bias,
            "average_selection_score": avg_selection,
            "average_fit_score": avg_fit,
        }
