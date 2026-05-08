import pandas as pd
from .dataset_config import MLDatasetProfile

class SupervisedDatasetBuilder:
    def __init__(self, profile: MLDatasetProfile):
        self.profile = profile

    def align_features_and_targets(
        self,
        X: pd.DataFrame,
        y: pd.DataFrame,
    ) -> tuple[pd.DataFrame, pd.DataFrame, dict]:
        """Align features and targets by index."""
        warnings = []

        # Keep only common indices
        common_idx = X.index.intersection(y.index)

        if len(common_idx) == 0:
            warnings.append("No overlapping indices between features and targets")
            return pd.DataFrame(), pd.DataFrame(), {"warnings": warnings}

        X_aligned = X.loc[common_idx]
        y_aligned = y.loc[common_idx]

        return X_aligned, y_aligned, {"warnings": warnings, "aligned_rows": len(common_idx)}

    def build_supervised_dataset(
        self,
        X: pd.DataFrame,
        y: pd.DataFrame,
        metadata: dict | None = None,
    ) -> tuple[pd.DataFrame, dict]:
        """Combine aligned X and y into a single dataset. Keeps them separate conceptually."""
        X_aligned, y_aligned, align_summary = self.align_features_and_targets(X, y)
        warnings = align_summary.get("warnings", [])

        if X_aligned.empty:
            return pd.DataFrame(), {"warnings": warnings}

        # Prefix target columns if not already
        y_renamed = y_aligned.copy()
        for col in y_renamed.columns:
            if not col.startswith("target_"):
                y_renamed.rename(columns={col: f"target_{col}"}, inplace=True)

        # Join them safely (they are already aligned, but concat is safer)
        dataset = pd.concat([X_aligned, y_renamed], axis=1)

        summary = {
            "row_count": len(dataset),
            "feature_columns": list(X_aligned.columns),
            "target_columns": list(y_renamed.columns),
            "start_date": str(dataset.index.min()) if not dataset.empty else None,
            "end_date": str(dataset.index.max()) if not dataset.empty else None,
            "warnings": warnings
        }

        if metadata:
            summary.update(metadata)

        return dataset, summary

    def select_target(
        self,
        dataset: pd.DataFrame,
        target_col: str,
    ) -> tuple[pd.DataFrame, pd.Series, dict]:
        """Split a supervised dataset into X and a specific y series."""
        warnings = []

        if target_col not in dataset.columns:
             warnings.append(f"Target column '{target_col}' not found in dataset")
             return pd.DataFrame(), pd.Series(dtype='float64'), {"warnings": warnings}

        # Find all target columns to drop them from X
        target_cols = [c for c in dataset.columns if c.startswith("target_")]

        X = dataset.drop(columns=target_cols)
        y = dataset[target_col]

        # Drop rows where target is NaN (typical for supervised learning)
        valid_idx = y.dropna().index
        X_clean = X.loc[valid_idx]
        y_clean = y.loc[valid_idx]

        return X_clean, y_clean, {
             "original_rows": len(dataset),
             "clean_rows": len(X_clean),
             "dropped_nan_targets": len(dataset) - len(X_clean),
             "warnings": warnings
        }
