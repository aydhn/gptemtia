import pandas as pd
from signals.signal_candidate import SignalCandidate, signal_candidate_to_dict


class SignalCandidatePool:
    def __init__(self):
        self.candidates: list[SignalCandidate] = []

    def add(self, candidate: SignalCandidate) -> None:
        self.candidates.append(candidate)

    def extend(self, candidates: list[SignalCandidate]) -> None:
        self.candidates.extend(candidates)

    def to_dataframe(self) -> pd.DataFrame:
        if not self.candidates:
            return pd.DataFrame()
        return pd.DataFrame([signal_candidate_to_dict(c) for c in self.candidates])

    @classmethod
    def from_dataframe(cls, df: pd.DataFrame) -> "SignalCandidatePool":
        pool = cls()
        if df is None or df.empty:
            return pool

        for _, row in df.iterrows():
            d = row.to_dict()
            # Handle potential lists parsing from string if loaded from csv/parquet
            if isinstance(d.get("active_events"), str):
                try:
                    import ast

                    d["active_events"] = ast.literal_eval(d["active_events"])
                except:
                    d["active_events"] = []
            if isinstance(d.get("warnings"), str):
                try:
                    import ast

                    d["warnings"] = ast.literal_eval(d["warnings"])
                except:
                    d["warnings"] = []

            c = SignalCandidate(**d)
            pool.add(c)
        return pool

    def rank(self, top_n: int | None = None) -> list[SignalCandidate]:
        ranked = sorted(self.candidates, key=lambda c: c.candidate_score, reverse=True)
        if top_n is not None:
            return ranked[:top_n]
        return ranked

    def summarize(self) -> dict:
        total = len(self.candidates)
        if total == 0:
            return {"total_candidates": 0, "passed_candidates": 0}

        passed = sum(1 for c in self.candidates if c.passed_pre_filters)

        symbols = {}
        for c in self.candidates:
            symbols[c.symbol] = symbols.get(c.symbol, 0) + 1

        cand_types = {}
        for c in self.candidates:
            cand_types[c.candidate_type] = cand_types.get(c.candidate_type, 0) + 1

        biases = {}
        for c in self.candidates:
            biases[c.directional_bias] = biases.get(c.directional_bias, 0) + 1

        avg_score = sum(c.candidate_score for c in self.candidates) / total
        avg_conf = sum(c.confidence_score for c in self.candidates) / total

        return {
            "total_candidates": total,
            "passed_candidates": passed,
            "by_symbol": symbols,
            "by_timeframe": {"1d": total},  # simplified
            "by_candidate_type": cand_types,
            "by_directional_bias": biases,
            "average_candidate_score": avg_score,
            "average_confidence_score": avg_conf,
            "top_candidates": [c.candidate_id for c in self.rank(5)],
        }
