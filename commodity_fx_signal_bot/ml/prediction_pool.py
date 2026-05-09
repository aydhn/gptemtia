from typing import List, Dict, Any, Optional
import pandas as pd
from commodity_fx_signal_bot.ml.prediction_candidate import MLPredictionCandidate, prediction_candidate_to_dict

class MLPredictionCandidatePool:
    def __init__(self):
        self.candidates: List[MLPredictionCandidate] = []

    def add(self, candidate: MLPredictionCandidate) -> None:
        self.candidates.append(candidate)

    def extend(self, candidates: List[MLPredictionCandidate]) -> None:
        self.candidates.extend(candidates)

    def to_dataframe(self) -> pd.DataFrame:
        if not self.candidates:
            return pd.DataFrame()
        return pd.DataFrame([prediction_candidate_to_dict(c) for c in self.candidates])

    @classmethod
    def from_dataframe(cls, df: pd.DataFrame) -> "MLPredictionCandidatePool":
        pool = cls()
        if df.empty:
            return pool
        for _, row in df.iterrows():
            # Minimal reconstruction
            candidate = MLPredictionCandidate(
                symbol=str(row.get("symbol", "")),
                timeframe=str(row.get("timeframe", "")),
                timestamp=str(row.get("timestamp", "")),
                prediction_id=str(row.get("prediction_id", "")),
                model_id=str(row.get("model_id", "")),
                model_family=str(row.get("model_family", "")),
                task_type=str(row.get("task_type", "")),
                target_column=str(row.get("target_column", "")),
                prediction_label=str(row.get("prediction_label", "")),
                predicted_direction=str(row.get("predicted_direction", "")),
                prediction_context_label=str(row.get("prediction_context_label", "")),
                raw_prediction=row.get("raw_prediction"),
                predicted_value=row.get("predicted_value"),
                prediction_score=row.get("prediction_score"),
                calibrated_score=row.get("calibrated_score"),
                confidence_score=float(row.get("confidence_score", 0.0)),
                uncertainty_score=float(row.get("uncertainty_score", 1.0)),
                model_quality_score=float(row.get("model_quality_score", 0.0)),
                dataset_quality_score=float(row.get("dataset_quality_score", 0.0)),
                leakage_risk_score=float(row.get("leakage_risk_score", 1.0)),
                schema_compatible=bool(row.get("schema_compatible", False)),
                passed_prediction_filters=bool(row.get("passed_prediction_filters", False)),
                warnings=row.get("warnings", []),
                notes=str(row.get("notes", ""))
            )
            pool.add(candidate)
        return pool

    def rank(self, top_n: Optional[int] = None) -> List[MLPredictionCandidate]:
        """Rank candidates by confidence (descending) and uncertainty (ascending)."""
        ranked = sorted(
            self.candidates,
            key=lambda c: (c.passed_prediction_filters, c.confidence_score, -c.uncertainty_score),
            reverse=True
        )
        if top_n is not None:
            return ranked[:top_n]
        return ranked

    def summarize(self) -> Dict[str, Any]:
        total = len(self.candidates)
        passed = sum(1 for c in self.candidates if c.passed_prediction_filters)
        rejected = sum(1 for c in self.candidates if "rejected" in c.prediction_label or "failed" in c.prediction_label)
        warnings = sum(1 for c in self.candidates if "warning" in c.prediction_label or "high_uncertainty" in c.prediction_label)

        by_symbol = {}
        by_timeframe = {}
        by_model_family = {}
        by_task_type = {}
        by_predicted_direction = {}

        confidences = []
        uncertainties = []

        for c in self.candidates:
            by_symbol[c.symbol] = by_symbol.get(c.symbol, 0) + 1
            by_timeframe[c.timeframe] = by_timeframe.get(c.timeframe, 0) + 1
            by_model_family[c.model_family] = by_model_family.get(c.model_family, 0) + 1
            by_task_type[c.task_type] = by_task_type.get(c.task_type, 0) + 1
            by_predicted_direction[c.predicted_direction] = by_predicted_direction.get(c.predicted_direction, 0) + 1
            confidences.append(c.confidence_score)
            uncertainties.append(c.uncertainty_score)

        avg_conf = sum(confidences) / len(confidences) if confidences else 0.0
        avg_unc = sum(uncertainties) / len(uncertainties) if uncertainties else 0.0

        top_candidates = [c.prediction_id for c in self.rank(top_n=5)]

        return {
            "total_prediction_candidates": total,
            "passed_prediction_candidates": passed,
            "rejected_prediction_candidates": rejected,
            "warning_prediction_candidates": warnings,
            "by_symbol": by_symbol,
            "by_timeframe": by_timeframe,
            "by_model_family": by_model_family,
            "by_task_type": by_task_type,
            "by_predicted_direction": by_predicted_direction,
            "average_confidence_score": avg_conf,
            "average_uncertainty_score": avg_unc,
            "top_prediction_candidates": top_candidates
        }
