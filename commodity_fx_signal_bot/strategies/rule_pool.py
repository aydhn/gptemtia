import pandas as pd
from typing import Any
from .entry_exit_candidates import (
    EntryExitConditionCandidate,
    entry_exit_candidate_to_dict,
)
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

        for col in [
            "passed_conditions",
            "failed_conditions",
            "required_failures",
            "block_reasons",
            "warnings",
        ]:
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

        for col in [
            "passed_conditions",
            "failed_conditions",
            "required_failures",
            "block_reasons",
            "warnings",
        ]:
            if col in df_copy.columns:
                df_copy[col] = df_copy[col].apply(
                    lambda x: (
                        ast.literal_eval(x)
                        if isinstance(x, str) and x.startswith("[")
                        else []
                    )
                )

        for _, row in df_copy.iterrows():
            d = row.to_dict()
            d["timestamp"] = str(d["timestamp"])
            pool.add(EntryExitConditionCandidate(**d))

        return pool

    def rank(self, top_n: int | None = None) -> list[EntryExitConditionCandidate]:
        sorted_candidates = sorted(
            self.candidates,
            key=lambda x: (
                x.passed_rule_filters,
                x.match_score,
                x.confidence_score,
                x.quality_score,
            ),
            reverse=True,
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
            "top_rule_candidates": [],
        }

        if self.candidates:
            match_scores = []
            conf_scores = []

            for c in self.candidates:
                summary["by_symbol"][c.symbol] = (
                    summary["by_symbol"].get(c.symbol, 0) + 1
                )
                summary["by_timeframe"][c.timeframe] = (
                    summary["by_timeframe"].get(c.timeframe, 0) + 1
                )
                summary["by_strategy_family"][c.strategy_family] = (
                    summary["by_strategy_family"].get(c.strategy_family, 0) + 1
                )
                summary["by_rule_group"][c.rule_group] = (
                    summary["by_rule_group"].get(c.rule_group, 0) + 1
                )
                summary["by_condition_label"][c.condition_label] = (
                    summary["by_condition_label"].get(c.condition_label, 0) + 1
                )
                summary["by_rule_status"][c.rule_status] = (
                    summary["by_rule_status"].get(c.rule_status, 0) + 1
                )
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
