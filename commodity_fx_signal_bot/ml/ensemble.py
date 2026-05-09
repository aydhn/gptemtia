import pandas as pd
import numpy as np
from typing import Dict, Any, Tuple, List

from commodity_fx_signal_bot.ml.prediction_config import MLPredictionProfile

class ModelEnsembleBuilder:
    def __init__(self, profile: MLPredictionProfile):
        self.profile = profile

    def build_ensemble_prediction(
        self,
        prediction_frames: Dict[str, pd.DataFrame]
    ) -> Tuple[pd.DataFrame, Dict[str, Any]]:

        if not prediction_frames:
            return pd.DataFrame(), {"status": "empty"}

        # Group by task type
        task_groups = {}
        for model_id, df in prediction_frames.items():
            if df.empty:
                continue
            task = df["task_type"].iloc[0] if "task_type" in df.columns else "unknown"
            if task not in task_groups:
                task_groups[task] = []
            task_groups[task].append(df)

        results = {}
        summary = {"tasks": list(task_groups.keys())}

        for task, frames in task_groups.items():
            # Limit models per ensemble
            frames = frames[:self.profile.max_models_per_ensemble]

            if "classification" in task.lower():
                res_df = self.aggregate_classification_predictions(frames)
            else:
                res_df = self.aggregate_regression_predictions(frames)

            if not res_df.empty:
                results[task] = res_df

        # For this project, mostly interested in classification for directional bias
        main_task = "classification" if any("classification" in k for k in results) else list(results.keys())[0] if results else None

        if main_task and main_task in results:
            df = results[main_task]
            summary["ensemble_available"] = True
            summary["ensemble_model_count"] = df["ensemble_model_count"].iloc[0] if not df.empty else 0
            return df, summary

        return pd.DataFrame(), {"status": "no_valid_predictions"}

    def aggregate_classification_predictions(self, frames: List[pd.DataFrame]) -> pd.DataFrame:
        if not frames:
            return pd.DataFrame()

        # Align by index
        aligned = pd.concat([f[["predicted_label", "confidence_score", "class_probability_up", "class_probability_down"]] for f in frames], axis=1, keys=range(len(frames)))

        result = pd.DataFrame(index=frames[0].index)
        n_models = len(frames)
        result["ensemble_model_count"] = n_models

        if n_models == 0:
            return result

        # Mean probabilities
        if ("class_probability_up" in frames[0].columns) and ("class_probability_down" in frames[0].columns):
            up_probs = pd.concat([f["class_probability_up"] for f in frames], axis=1).mean(axis=1)
            down_probs = pd.concat([f["class_probability_down"] for f in frames], axis=1).mean(axis=1)

            result["ensemble_prediction_score"] = up_probs
            result["ensemble_confidence_score"] = np.maximum(up_probs, down_probs)

            # Simple predicted direction
            directions = []
            for i in range(len(up_probs)):
                u, d = up_probs.iloc[i], down_probs.iloc[i]
                if u > d and u > 0.5:
                    directions.append("predicted_up")
                elif d > u and d > 0.5:
                    directions.append("predicted_down")
                else:
                    directions.append("predicted_flat")
            result["ensemble_predicted_direction"] = directions

        else:
            result["ensemble_prediction_score"] = 0.5
            result["ensemble_confidence_score"] = 0.5
            result["ensemble_predicted_direction"] = "predicted_unknown"

        # Disagreement based on label variance
        # (Simplified: 1.0 - mean confidence)
        result["ensemble_disagreement_score"] = 1.0 - result["ensemble_confidence_score"]
        result["ensemble_uncertainty_score"] = result["ensemble_disagreement_score"]

        # Context Label
        context_labels = []
        for i in range(len(result)):
            conf = result["ensemble_confidence_score"].iloc[i]
            unc = result["ensemble_uncertainty_score"].iloc[i]
            if unc > self.profile.uncertainty_warning_threshold:
                context_labels.append("ml_context_uncertain")
            elif conf > self.profile.min_confidence_score:
                context_labels.append("ml_context_supportive")
            else:
                context_labels.append("ml_context_neutral")
        result["ensemble_context_label"] = context_labels

        return result

    def aggregate_regression_predictions(self, frames: List[pd.DataFrame]) -> pd.DataFrame:
        if not frames:
            return pd.DataFrame()

        result = pd.DataFrame(index=frames[0].index)
        n_models = len(frames)
        result["ensemble_model_count"] = n_models

        if "predicted_value" in frames[0].columns:
            vals = pd.concat([f["predicted_value"] for f in frames], axis=1)
            result["ensemble_predicted_value"] = vals.mean(axis=1)
            result["ensemble_prediction_score"] = vals.mean(axis=1) # Need calibration later

            # Disagreement = std dev relative to mean
            std = vals.std(axis=1)
            mean_abs = vals.mean(axis=1).abs()
            # Avoid div by 0
            mean_abs[mean_abs < 1e-6] = 1e-6
            result["ensemble_disagreement_score"] = (std / mean_abs).clip(0, 1)
        else:
            result["ensemble_predicted_value"] = np.nan
            result["ensemble_prediction_score"] = 0.5
            result["ensemble_disagreement_score"] = 1.0

        result["ensemble_confidence_score"] = 1.0 - result["ensemble_disagreement_score"]
        result["ensemble_uncertainty_score"] = result["ensemble_disagreement_score"]
        result["ensemble_predicted_direction"] = "predicted_unknown"
        result["ensemble_context_label"] = "ml_context_neutral"

        return result
