import pandas as pd
from typing import List, Dict, Optional
from risk.risk_candidate import RiskPrecheckCandidate, risk_candidate_to_dict


class RiskCandidatePool:
    def __init__(self):
        self.candidates: List[RiskPrecheckCandidate] = []

    def add(self, candidate: RiskPrecheckCandidate) -> None:
        self.candidates.append(candidate)

    def extend(self, candidates: List[RiskPrecheckCandidate]) -> None:
        self.candidates.extend(candidates)

    def to_dataframe(self) -> pd.DataFrame:
        if not self.candidates:
            return pd.DataFrame()
        return pd.DataFrame([risk_candidate_to_dict(c) for c in self.candidates])

    @classmethod
    def from_dataframe(cls, df: pd.DataFrame) -> "RiskCandidatePool":
        pool = cls()
        if df is None or df.empty:
            return pool
        for _, row in df.iterrows():
            d = row.to_dict()
            for k in ["blocking_reasons", "watchlist_reasons", "warnings"]:
                if isinstance(d.get(k), str):
                    d[k] = eval(d[k]) if d[k].startswith("[") else []
            pool.add(RiskPrecheckCandidate(**d))
        return pool

    def rank(self, top_n: Optional[int] = None) -> List[RiskPrecheckCandidate]:
        sorted_candidates = sorted(
            self.candidates, key=lambda x: x.risk_readiness_score, reverse=True
        )
        return sorted_candidates[:top_n] if top_n is not None else sorted_candidates

    def summarize(self) -> Dict:
        df = self.to_dataframe()
        if df.empty:
            return {
                "total_risk_candidates": 0,
                "passed_risk_candidates": 0,
                "rejected_risk_candidates": 0,
                "watchlist_risk_candidates": 0,
            }
        return {
            "total_risk_candidates": len(df),
            "passed_risk_candidates": int(df["passed_risk_precheck"].sum()),
            "rejected_risk_candidates": len(
                df[df["risk_label"] == "risk_rejection_candidate"]
            ),
            "watchlist_risk_candidates": len(
                df[df["risk_label"] == "risk_watchlist_candidate"]
            ),
            "by_symbol": (
                df["symbol"].value_counts().to_dict() if "symbol" in df else {}
            ),
            "by_timeframe": (
                df["timeframe"].value_counts().to_dict() if "timeframe" in df else {}
            ),
            "by_strategy_family": (
                df["strategy_family"].value_counts().to_dict()
                if "strategy_family" in df
                else {}
            ),
            "by_condition_label": (
                df["condition_label"].value_counts().to_dict()
                if "condition_label" in df
                else {}
            ),
            "by_risk_label": (
                df["risk_label"].value_counts().to_dict() if "risk_label" in df else {}
            ),
            "by_risk_severity": (
                df["risk_severity"].value_counts().to_dict()
                if "risk_severity" in df
                else {}
            ),
            "average_total_pretrade_risk": (
                float(df["total_pretrade_risk_score"].mean())
                if "total_pretrade_risk_score" in df
                else 0.0
            ),
            "average_risk_readiness": (
                float(df["risk_readiness_score"].mean())
                if "risk_readiness_score" in df
                else 0.0
            ),
        }
