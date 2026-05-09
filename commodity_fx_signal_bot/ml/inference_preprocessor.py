import pandas as pd
from typing import Tuple, Dict, Any, Optional

class InferencePreprocessor:
    def __init__(self, preprocessor, feature_schema: Optional[Dict[str, Any]] = None):
        self.preprocessor = preprocessor
        self.feature_schema = feature_schema or {}
        self.expected_features = self.feature_schema.get("features", [])

    def validate_input_schema(self, X: pd.DataFrame) -> Dict[str, Any]:
        if not self.expected_features:
            return {"valid": True, "note": "No schema to validate against"}

        input_cols = set(X.columns)
        expected_cols = set(self.expected_features)

        missing = list(expected_cols - input_cols)
        extra = list(input_cols - expected_cols)

        valid = len(missing) == 0
        return {
            "valid": valid,
            "missing_columns": missing,
            "extra_columns": extra
        }

    def align_features(self, X: pd.DataFrame) -> Tuple[pd.DataFrame, Dict[str, Any]]:
        """Align input frame to expected features. Add missing as NaN, drop extra. Drop targets."""
        X_aligned = X.copy()
        audit = {"dropped": [], "added": []}

        # Drop target columns if they accidentally leaked in
        target_cols = [c for c in X_aligned.columns if c.startswith("target_")]
        if target_cols:
            X_aligned = X_aligned.drop(columns=target_cols)
            audit["dropped_targets"] = target_cols

        if not self.expected_features:
            return X_aligned, audit

        # Add missing
        for col in self.expected_features:
            if col not in X_aligned.columns:
                X_aligned[col] = float('nan')
                audit["added"].append(col)

        # Drop extra
        for col in list(X_aligned.columns):
            if col not in self.expected_features:
                X_aligned = X_aligned.drop(columns=[col])
                audit["dropped"].append(col)

        # Ensure order
        X_aligned = X_aligned[self.expected_features]

        return X_aligned, audit

    def transform(self, X: pd.DataFrame) -> Tuple[pd.DataFrame, Dict[str, Any]]:
        if self.preprocessor is None:
            return X, {"status": "no_preprocessor"}

        try:
            # ONLY use transform, NEVER fit
            X_transformed = self.preprocessor.transform(X)
            # if preprocessor outputs numpy, wrap back to DataFrame
            if not isinstance(X_transformed, pd.DataFrame):
                X_transformed = pd.DataFrame(X_transformed, index=X.index, columns=X.columns)
            return X_transformed, {"status": "success"}
        except Exception as e:
            return X, {"status": "error", "error": str(e)}
