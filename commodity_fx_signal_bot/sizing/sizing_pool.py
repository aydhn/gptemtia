import pandas as pd
from typing import List, Dict, Any, Optional
from sizing.sizing_candidate import SizingCandidate, sizing_candidate_to_dict

class SizingCandidatePool:
    def __init__(self):
        self.candidates: List[SizingCandidate] = []

    def add(self, candidate: SizingCandidate) -> None:
        self.candidates.append(candidate)

    def extend(self, candidates: List[SizingCandidate]) -> None:
        self.candidates.extend(candidates)

    def to_dataframe(self) -> pd.DataFrame:
        if not self.candidates:
            return pd.DataFrame()
        records = [sizing_candidate_to_dict(c) for c in self.candidates]
        df = pd.DataFrame(records)
        if "timestamp" in df.columns:
            df["timestamp"] = pd.to_datetime(df["timestamp"])
            df.set_index("timestamp", inplace=True)
        return df

    @classmethod
    def from_dataframe(cls, df: pd.DataFrame) -> "SizingCandidatePool":
        pool = cls()
        if df is None or df.empty:
            return pool

        reset_df = df.reset_index()
        for _, row in reset_df.iterrows():
            row_dict = row.to_dict()
            if "timestamp" in row_dict and pd.isna(row_dict["timestamp"]):
                row_dict["timestamp"] = str(row.name) if isinstance(row.name, (pd.Timestamp, str)) else ""
            elif "timestamp" in row_dict:
                row_dict["timestamp"] = str(row_dict["timestamp"])

            candidate = SizingCandidate(**row_dict)
            pool.add(candidate)
        return pool

    def rank(self, top_n: Optional[int] = None) -> List[SizingCandidate]:
        ranked = sorted(self.candidates, key=lambda c: c.sizing_readiness_score, reverse=True)
        if top_n is not None:
            return ranked[:top_n]
        return ranked

    def summarize(self) -> Dict[str, Any]:
        total = len(self.candidates)
        passed = sum(1 for c in self.candidates if c.sizing_label == "sizing_approved_candidate")
        rejected = sum(1 for c in self.candidates if c.sizing_label in ["sizing_rejected_candidate", "sizing_zero_candidate", "invalid_risk_candidate"])
        watchlist = sum(1 for c in self.candidates if c.sizing_label == "sizing_watchlist_candidate")

        by_symbol = {}
        for c in self.candidates:
            by_symbol[c.symbol] = by_symbol.get(c.symbol, 0) + 1

        avg_readiness = sum(c.sizing_readiness_score for c in self.candidates) / total if total > 0 else 0.0

        return {
            "total_sizing_candidates": total,
            "passed_sizing_candidates": passed,
            "rejected_sizing_candidates": rejected,
            "watchlist_sizing_candidates": watchlist,
            "by_symbol": by_symbol,
            "average_sizing_readiness": avg_readiness,
            "top_sizing_candidates": [c.sizing_id for c in self.rank(top_n=5)]
        }
