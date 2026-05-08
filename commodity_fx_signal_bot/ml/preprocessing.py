import pandas as pd
import numpy as np

class BasicPreprocessor:
    def __init__(
        self,
        drop_high_nan_features: bool = True,
        max_nan_ratio: float = 0.35,
        enable_imputation: bool = True,
        enable_scaling: bool = True,
    ):
        self.drop_high_nan_features = drop_high_nan_features
        self.max_nan_ratio = max_nan_ratio
        self.enable_imputation = enable_imputation
        self.enable_scaling = enable_scaling

        self.feature_names_in_ = None
        self.numeric_features_ = None
        self.categorical_features_ = None
        self.dropped_features_ = []
        self.imputation_values_ = {}
        self.scaling_params_ = {}
        self.is_fitted = False

    def fit(self, X: pd.DataFrame, y: pd.Series | None = None) -> "BasicPreprocessor":
        X_fit = X.copy()

        # Determine features to drop
        self.dropped_features_ = []

        # Drop non-feature columns
        for col in X_fit.columns:
            if col.startswith("target_") or col in ["symbol", "timeframe", "date", "index"]:
                self.dropped_features_.append(col)

        # Handle nan ratio
        if self.drop_high_nan_features:
            nan_ratios = X_fit.isna().mean()
            for col, ratio in nan_ratios.items():
                if ratio > self.max_nan_ratio and col not in self.dropped_features_:
                    self.dropped_features_.append(col)

        self.feature_names_in_ = [c for c in X_fit.columns if c not in self.dropped_features_]
        X_fit = X_fit[self.feature_names_in_]

        # Replace inf with nan for stats
        X_fit = X_fit.replace([np.inf, -np.inf], np.nan)

        self.numeric_features_ = list(X_fit.select_dtypes(include=['number']).columns)
        self.categorical_features_ = list(X_fit.select_dtypes(include=['object', 'category']).columns)

        if self.enable_imputation:
            for col in self.numeric_features_:
                self.imputation_values_[col] = X_fit[col].median()

        if self.enable_scaling:
            for col in self.numeric_features_:
                mean = X_fit[col].mean()
                std = X_fit[col].std()
                self.scaling_params_[col] = {'mean': mean, 'std': std if std > 0 else 1.0}

        self.is_fitted = True
        return self

    def transform(self, X: pd.DataFrame) -> pd.DataFrame:
        if not self.is_fitted:
            raise RuntimeError("Preprocessor must be fitted before transform")

        X_trans = X.copy()

        # Keep only fitted features
        missing_cols = [c for c in self.feature_names_in_ if c not in X_trans.columns]
        for col in missing_cols:
            X_trans[col] = np.nan

        X_trans = X_trans[self.feature_names_in_]
        X_trans = X_trans.replace([np.inf, -np.inf], np.nan)

        if self.enable_imputation:
            for col in self.numeric_features_:
                val = self.imputation_values_.get(col, 0)
                if pd.isna(val):
                    val = 0
                X_trans[col] = X_trans[col].fillna(val)

        if self.enable_scaling:
            for col in self.numeric_features_:
                params = self.scaling_params_.get(col, {'mean': 0, 'std': 1.0})
                mean = params['mean']
                std = params['std']
                if pd.isna(mean) or pd.isna(std) or std == 0:
                    continue
                X_trans[col] = (X_trans[col] - mean) / std

        # Simple encoding for categorical
        if self.categorical_features_:
            X_trans = pd.get_dummies(X_trans, columns=self.categorical_features_, dummy_na=True)

        return X_trans

    def fit_transform(self, X: pd.DataFrame, y: pd.Series | None = None) -> pd.DataFrame:
        return self.fit(X, y).transform(X)

    def get_feature_names(self) -> list[str]:
        if not self.is_fitted:
            return []
        return self.feature_names_in_

    def summarize(self) -> dict:
        return {
            "is_fitted": self.is_fitted,
            "feature_count_in": len(self.feature_names_in_) if self.is_fitted else 0,
            "numeric_count": len(self.numeric_features_) if self.is_fitted else 0,
            "categorical_count": len(self.categorical_features_) if self.is_fitted else 0,
            "dropped_count": len(self.dropped_features_) if self.is_fitted else 0,
        }
