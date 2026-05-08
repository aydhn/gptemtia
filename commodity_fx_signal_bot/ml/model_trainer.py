import pandas as pd
from dataclasses import dataclass, asdict
from datetime import datetime, timezone
from .training_config import MLTrainingProfile
from .preprocessing import BasicPreprocessor
from .baseline_models import create_baseline_model

@dataclass
class ModelTrainingResult:
    model_id: str
    symbol: str
    timeframe: str
    training_profile: str
    dataset_profile: str
    model_family: str
    task_type: str
    target_column: str
    train_rows: int
    validation_rows: int
    test_rows: int
    feature_count: int
    trained_at_utc: str
    status: str
    metrics: dict
    warnings: list[str]

def build_model_id(symbol: str, timeframe: str, profile_name: str, model_family: str, target_column: str) -> str:
    safe_target = target_column.replace("_", "-")
    return f"{symbol}_{timeframe}_{profile_name}_{model_family}_{safe_target}"

def model_training_result_to_dict(result: ModelTrainingResult) -> dict:
    return asdict(result)

class MLModelTrainer:
    def __init__(self, profile: MLTrainingProfile):
        self.profile = profile

    def prepare_training_data(
        self,
        dataset: pd.DataFrame,
        target_column: str,
    ) -> tuple[pd.DataFrame, pd.Series, dict]:
        if target_column not in dataset.columns:
            return pd.DataFrame(), pd.Series(), {"warnings": [f"Target column '{target_column}' not found in dataset"]}

        y = dataset[target_column]
        X = dataset.drop(columns=[target_column])

        return X, y, {"warnings": []}

    def train_model(
        self,
        X_train: pd.DataFrame,
        y_train: pd.Series,
        model_family: str | None = None,
    ) -> tuple[object, BasicPreprocessor, dict]:
        if model_family is None:
            model_family = self.profile.default_model_family

        preprocessor = BasicPreprocessor(
            drop_high_nan_features=self.profile.drop_high_nan_features,
            max_nan_ratio=self.profile.max_feature_nan_ratio,
            enable_imputation=self.profile.enable_basic_imputation,
            enable_scaling=self.profile.enable_basic_scaling
        )

        X_train_trans = preprocessor.fit_transform(X_train, y_train)

        model = create_baseline_model(model_family, self.profile.task_type)
        model.fit(X_train_trans, y_train)

        return model, preprocessor, {"warnings": []}

    def train_from_dataset(
        self,
        symbol: str,
        timeframe: str,
        dataset: pd.DataFrame,
        split_manifest: dict | None = None,
        model_family: str | None = None,
    ) -> tuple[object, BasicPreprocessor, ModelTrainingResult, dict]:

        if model_family is None:
            model_family = self.profile.default_model_family

        model_id = build_model_id(symbol, timeframe, self.profile.name, model_family, self.profile.target_column)

        X, y, prep_res = self.prepare_training_data(dataset, self.profile.target_column)
        if prep_res["warnings"]:
            result = ModelTrainingResult(
                model_id=model_id,
                symbol=symbol,
                timeframe=timeframe,
                training_profile=self.profile.name,
                dataset_profile=self.profile.dataset_profile,
                model_family=model_family,
                task_type=self.profile.task_type,
                target_column=self.profile.target_column,
                train_rows=0,
                validation_rows=0,
                test_rows=0,
                feature_count=0,
                trained_at_utc=datetime.now(timezone.utc).isoformat(),
                status="insufficient_data",
                metrics={},
                warnings=prep_res["warnings"]
            )
            return None, None, result, prep_res

        train_indices = split_manifest.get("train_indices", list(range(len(dataset)))) if split_manifest else list(range(len(dataset)))
        test_indices = split_manifest.get("test_indices", []) if split_manifest else []
        val_indices = split_manifest.get("validation_indices", []) if split_manifest else []

        X_train = X.iloc[train_indices]
        y_train = y.iloc[train_indices]

        if len(X_train) < self.profile.min_train_rows:
            warnings = [f"Insufficient training data: {len(X_train)} rows (minimum {self.profile.min_train_rows})"]
            result = ModelTrainingResult(
                model_id=model_id,
                symbol=symbol,
                timeframe=timeframe,
                training_profile=self.profile.name,
                dataset_profile=self.profile.dataset_profile,
                model_family=model_family,
                task_type=self.profile.task_type,
                target_column=self.profile.target_column,
                train_rows=len(X_train),
                validation_rows=len(val_indices),
                test_rows=len(test_indices),
                feature_count=X_train.shape[1],
                trained_at_utc=datetime.now(timezone.utc).isoformat(),
                status="insufficient_data",
                metrics={},
                warnings=warnings
            )
            return None, None, result, {"warnings": warnings}

        model, preprocessor, train_res = self.train_model(X_train, y_train, model_family)

        result = ModelTrainingResult(
            model_id=model_id,
            symbol=symbol,
            timeframe=timeframe,
            training_profile=self.profile.name,
            dataset_profile=self.profile.dataset_profile,
            model_family=model_family,
            task_type=self.profile.task_type,
            target_column=self.profile.target_column,
            train_rows=len(X_train),
            validation_rows=len(val_indices),
            test_rows=len(test_indices),
            feature_count=len(preprocessor.get_feature_names()),
            trained_at_utc=datetime.now(timezone.utc).isoformat(),
            status="trained_candidate",
            metrics={},
            warnings=train_res["warnings"]
        )

        return model, preprocessor, result, {"warnings": train_res["warnings"]}
