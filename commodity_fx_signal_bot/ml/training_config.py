from dataclasses import dataclass

@dataclass(frozen=True)
class MLTrainingProfile:
    name: str
    description: str
    dataset_profile: str
    target_column: str
    task_type: str
    model_families: tuple[str, ...]
    default_model_family: str
    cv_n_splits: int = 5
    cv_embargo_bars: int = 5
    min_train_rows: int = 300
    min_test_rows: int = 50
    max_feature_nan_ratio: float = 0.35
    drop_high_nan_features: bool = True
    enable_basic_imputation: bool = True
    enable_basic_scaling: bool = True
    save_model_artifacts: bool = True
    enabled: bool = True
    notes: str = ""

_TRAINING_PROFILES = {
    "balanced_baseline_training": MLTrainingProfile(
        name="balanced_baseline_training",
        description="Balanced baseline training profile",
        dataset_profile="balanced_supervised_dataset",
        target_column="target_direction_class_5",
        task_type="classification",
        model_families=("dummy", "logistic_regression", "random_forest", "hist_gradient_boosting"),
        default_model_family="random_forest",
        cv_n_splits=5,
        cv_embargo_bars=5,
        min_train_rows=300,
        min_test_rows=50,
        notes="Genel amaçlı baseline sınıflandırma eğitim profili."
    ),
    "light_price_action_training": MLTrainingProfile(
        name="light_price_action_training",
        description="Light price action training profile",
        dataset_profile="price_action_light_dataset",
        target_column="target_direction_class_5",
        task_type="classification",
        model_families=("dummy", "logistic_regression", "random_forest"),
        default_model_family="logistic_regression",
        notes="Daha sade feature set ile ilk baseline model denemeleri."
    ),
    "candidate_outcome_training": MLTrainingProfile(
        name="candidate_outcome_training",
        description="Candidate outcome training profile",
        dataset_profile="candidate_outcome_dataset",
        target_column="target_candidate_outcome",
        task_type="classification",
        model_families=("dummy", "random_forest", "hist_gradient_boosting"),
        default_model_family="random_forest",
        notes="Candidate outcome sınıflandırması için baseline eğitim profili."
    ),
    "forward_return_regression_training": MLTrainingProfile(
        name="forward_return_regression_training",
        description="Forward return regression training profile",
        dataset_profile="balanced_supervised_dataset",
        target_column="target_forward_return_5",
        task_type="regression",
        model_families=("dummy", "random_forest", "hist_gradient_boosting"),
        default_model_family="hist_gradient_boosting",
        notes="Forward return regresyon baseline profili."
    ),
    "conservative_training_debug": MLTrainingProfile(
        name="conservative_training_debug",
        description="Conservative training debug profile",
        dataset_profile="price_action_light_dataset",
        target_column="target_direction_class_3",
        task_type="classification",
        model_families=("dummy", "logistic_regression"),
        default_model_family="dummy",
        cv_n_splits=3,
        min_train_rows=100,
        min_test_rows=30,
        notes="Hızlı debug ve pipeline testi için."
    )
}

class ConfigError(Exception):
    pass

def get_ml_training_profile(name: str) -> MLTrainingProfile:
    if name not in _TRAINING_PROFILES:
        raise ConfigError(f"Profile {name} not found.")
    return _TRAINING_PROFILES[name]

def list_ml_training_profiles(enabled_only: bool = True) -> list[MLTrainingProfile]:
    if enabled_only:
        return [p for p in _TRAINING_PROFILES.values() if p.enabled]
    return list(_TRAINING_PROFILES.values())

def validate_ml_training_profiles() -> None:
    for name, p in _TRAINING_PROFILES.items():
        if p.task_type not in ("classification", "regression"):
            raise ValueError(f"Profile {name}: invalid task_type {p.task_type}")
        if not p.model_families:
            raise ValueError(f"Profile {name}: model_families empty")
        if p.default_model_family not in p.model_families:
            raise ValueError(f"Profile {name}: default_model_family not in model_families")
        if p.cv_n_splits < 2:
            raise ValueError(f"Profile {name}: cv_n_splits must be >= 2")
        if p.min_train_rows <= 0 or p.min_test_rows <= 0:
            raise ValueError(f"Profile {name}: min_train_rows/min_test_rows must be positive")
        if not (0.0 <= p.max_feature_nan_ratio <= 1.0):
            raise ValueError(f"Profile {name}: max_feature_nan_ratio must be between 0 and 1")

def get_default_ml_training_profile() -> MLTrainingProfile:
    from config.settings import settings
    profile_name = settings.default_ml_training_profile
    return get_ml_training_profile(profile_name)
