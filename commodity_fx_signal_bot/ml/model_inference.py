import pandas as pd
import numpy as np
from typing import Tuple, Dict, Any, Optional

class OfflineModelInference:
    def __init__(self, model, preprocessor, model_metadata: Dict[str, Any], feature_schema: Optional[Dict[str, Any]] = None):
        self.model = model
        self.preprocessor = preprocessor
        self.metadata = model_metadata
        self.schema = feature_schema

        self.task_type = self.metadata.get("task_type", "classification")
        self.model_family = self.metadata.get("model_family", "unknown")
        self.target_column = self.metadata.get("target_column", "unknown_target")

    def predict_frame(self, X: pd.DataFrame) -> Tuple[pd.DataFrame, Dict[str, Any]]:
        """Run predictions on the entire frame."""
        if X.empty:
            return pd.DataFrame(), {"status": "empty_input"}

        try:
            preds = self.model.predict(X)

            result_df = pd.DataFrame(index=X.index)
            result_df["model_id"] = self.metadata.get("model_id", "unknown")
            result_df["model_family"] = self.model_family
            result_df["task_type"] = self.task_type
            result_df["target_column"] = self.target_column
            result_df["raw_prediction"] = preds

            if self.task_type == "classification" or self.task_type == "classification_prediction":
                result_df["predicted_label"] = preds
                result_df["predicted_value"] = np.nan

                if hasattr(self.model, "predict_proba"):
                    probas = self.model.predict_proba(X)
                    classes = self.model.classes_ if hasattr(self.model, "classes_") else [str(i) for i in range(probas.shape[1])]

                    for i, cls in enumerate(classes):
                        result_df[f"class_probability_{cls}"] = probas[:, i]

                    # Extract up/down probas based on common naming conventions
                    up_cols = [c for c in classes if "up" in str(c).lower() or str(c) == "1"]
                    down_cols = [c for c in classes if "down" in str(c).lower() or str(c) == "-1"]

                    if up_cols:
                        result_df["class_probability_up"] = probas[:, list(classes).index(up_cols[0])]
                    else:
                        result_df["class_probability_up"] = 0.0

                    if down_cols:
                        result_df["class_probability_down"] = probas[:, list(classes).index(down_cols[0])]
                    else:
                        result_df["class_probability_down"] = 0.0

                    # Simple confidence: max probability
                    result_df["confidence_score"] = np.max(probas, axis=1)
                else:
                    result_df["confidence_score"] = 0.5  # Neutral if no proba
            else:
                # Regression
                result_df["predicted_label"] = None
                result_df["predicted_value"] = preds
                result_df["confidence_score"] = 0.5 # Handled by calibration later

            return result_df, {"status": "success", "rows": len(result_df)}

        except Exception as e:
            return pd.DataFrame(), {"status": "error", "error": str(e)}

    def predict_latest(self, X: pd.DataFrame) -> Tuple[Dict[str, Any], Dict[str, Any]]:
        """Predict for just the last row."""
        if X.empty:
            return {}, {"status": "empty_input"}

        df, status = self.predict_frame(X.iloc[-1:])
        if df.empty:
            return {}, status

        return df.iloc[-1].to_dict(), status
