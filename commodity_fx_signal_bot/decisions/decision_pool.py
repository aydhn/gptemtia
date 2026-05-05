import pandas as pd
from typing import List, Dict, Optional
from .decision_candidate import DecisionCandidate, decision_candidate_to_dict


class DecisionCandidatePool:
    def __init__(self):
        self.decisions: List[DecisionCandidate] = []

    def add(self, decision: DecisionCandidate) -> None:
        self.decisions.append(decision)

    def extend(self, decisions: List[DecisionCandidate]) -> None:
        self.decisions.extend(decisions)

    def to_dataframe(self) -> pd.DataFrame:
        if not self.decisions:
            return pd.DataFrame()
        dicts = [decision_candidate_to_dict(d) for d in self.decisions]
        df = pd.DataFrame(dicts)
        if "timestamp" in df.columns:
            df["timestamp"] = pd.to_datetime(df["timestamp"])
            df.set_index("timestamp", inplace=True)
        return df

    @classmethod
    def from_dataframe(cls, df: pd.DataFrame) -> "DecisionCandidatePool":
        pool = cls()
        if df is None or df.empty:
            return pool

        df = df.reset_index()
        for _, row in df.iterrows():
            d = row.to_dict()
            if "timestamp" in d and isinstance(d["timestamp"], pd.Timestamp):
                d["timestamp"] = d["timestamp"].isoformat()

            # Convert string representations of lists back to lists if needed
            for list_col in ["no_trade_reasons", "conflict_reasons", "warnings"]:
                if list_col in d and isinstance(d[list_col], str):
                    import ast

                    try:
                        d[list_col] = ast.literal_eval(d[list_col])
                    except:
                        d[list_col] = []

            # Handle potential missing fields from older formats gracefully
            expected_fields = DecisionCandidate.__dataclass_fields__.keys()
            filtered_d = {k: v for k, v in d.items() if k in expected_fields}

            try:
                pool.add(DecisionCandidate(**filtered_d))
            except Exception:
                pass

        return pool

    def rank(self, top_n: Optional[int] = None) -> List[DecisionCandidate]:
        ranked = sorted(self.decisions, key=lambda d: d.decision_score, reverse=True)
        if top_n is not None:
            return ranked[:top_n]
        return ranked

    def summarize(self) -> Dict:
        if not self.decisions:
            return {
                "total_decisions": 0,
                "passed_decisions": 0,
                "by_symbol": {},
                "by_timeframe": {},
                "by_decision_label": {},
                "by_directional_bias": {},
                "by_candidate_type": {},
                "average_decision_score": 0.0,
                "average_confidence": 0.0,
                "average_strategy_readiness": 0.0,
                "top_decisions": [],
            }

        df = self.to_dataframe()

        return {
            "total_decisions": len(self.decisions),
            "passed_decisions": sum(
                1 for d in self.decisions if d.passed_decision_filters
            ),
            "by_symbol": (
                df["symbol"].value_counts().to_dict() if "symbol" in df.columns else {}
            ),
            "by_timeframe": (
                df["timeframe"].value_counts().to_dict()
                if "timeframe" in df.columns
                else {}
            ),
            "by_decision_label": (
                df["decision_label"].value_counts().to_dict()
                if "decision_label" in df.columns
                else {}
            ),
            "by_directional_bias": (
                df["directional_bias"].value_counts().to_dict()
                if "directional_bias" in df.columns
                else {}
            ),
            "by_candidate_type": (
                df["candidate_type"].value_counts().to_dict()
                if "candidate_type" in df.columns
                else {}
            ),
            "average_decision_score": (
                float(df["decision_score"].mean())
                if "decision_score" in df.columns
                else 0.0
            ),
            "average_confidence": (
                float(df["decision_confidence"].mean())
                if "decision_confidence" in df.columns
                else 0.0
            ),
            "average_strategy_readiness": (
                float(df["strategy_readiness_score"].mean())
                if "strategy_readiness_score" in df.columns
                else 0.0
            ),
            "top_decisions": [d.decision_id for d in self.rank(5)],
        }
