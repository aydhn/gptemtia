import os
import re

def update_file(filename, search_pattern, replace_text, is_regex=False):
    if not os.path.exists(filename):
        print(f"File {filename} not found.")
        return
    with open(filename, "r") as f:
        content = f.read()

    if is_regex:
        new_content = re.sub(search_pattern, replace_text, content)
    else:
        new_content = content.replace(search_pattern, replace_text)

    if new_content != content:
        with open(filename, "w") as f:
            f.write(new_content)
        print(f"Updated {filename}")
    else:
        print(f"No changes made to {filename}")

update_file("commodity_fx_signal_bot/config/settings.py",
"""    ml_save_supervised_dataset: bool = field(
        default_factory=lambda: str(
            os.getenv("ML_SAVE_SUPERVISED_DATASET", "true")
        ).lower()
        == "true"
    )

    def __post_init__(self):""",
"""    ml_save_supervised_dataset: bool = field(
        default_factory=lambda: str(
            os.getenv("ML_SAVE_SUPERVISED_DATASET", "true")
        ).lower()
        == "true"
    )

    # Phase 30: ML Training Baseline
    ml_training_enabled: bool = field(
        default_factory=lambda: str(os.getenv("ML_TRAINING_ENABLED", "true")).lower() == "true"
    )
    ml_baseline_models_enabled: bool = field(
        default_factory=lambda: str(os.getenv("ML_BASELINE_MODELS_ENABLED", "true")).lower() == "true"
    )
    ml_model_registry_enabled: bool = field(
        default_factory=lambda: str(os.getenv("ML_MODEL_REGISTRY_ENABLED", "true")).lower() == "true"
    )
    default_ml_training_profile: str = field(
        default_factory=lambda: os.getenv("DEFAULT_ML_TRAINING_PROFILE", "balanced_baseline_training")
    )
    default_ml_training_timeframe: str = field(
        default_factory=lambda: os.getenv("DEFAULT_ML_TRAINING_TIMEFRAME", "1d")
    )
    default_ml_training_dataset_profile: str = field(
        default_factory=lambda: os.getenv("DEFAULT_ML_TRAINING_DATASET_PROFILE", "balanced_supervised_dataset")
    )
    default_ml_target_column: str = field(
        default_factory=lambda: os.getenv("DEFAULT_ML_TARGET_COLUMN", "target_direction_class_5")
    )
    ml_training_task_type: str = field(
        default_factory=lambda: os.getenv("ML_TRAINING_TASK_TYPE", "classification")
    )
    ml_allowed_model_families: tuple = field(
        default_factory=lambda: tuple(os.getenv("ML_ALLOWED_MODEL_FAMILIES", "dummy,logistic_regression,random_forest,hist_gradient_boosting").split(","))
    )
    ml_default_model_family: str = field(
        default_factory=lambda: os.getenv("ML_DEFAULT_MODEL_FAMILY", "random_forest")
    )
    ml_cv_n_splits: int = field(
        default_factory=lambda: int(os.getenv("ML_CV_N_SPLITS", "5"))
    )
    ml_cv_embargo_bars: int = field(
        default_factory=lambda: int(os.getenv("ML_CV_EMBARGO_BARS", "5"))
    )
    ml_min_train_rows: int = field(
        default_factory=lambda: int(os.getenv("ML_MIN_TRAIN_ROWS", "300"))
    )
    ml_min_test_rows: int = field(
        default_factory=lambda: int(os.getenv("ML_MIN_TEST_ROWS", "50"))
    )
    ml_max_feature_nan_ratio_for_training: float = field(
        default_factory=lambda: float(os.getenv("ML_MAX_FEATURE_NAN_RATIO_FOR_TRAINING", "0.35"))
    )
    ml_drop_high_nan_features: bool = field(
        default_factory=lambda: str(os.getenv("ML_DROP_HIGH_NAN_FEATURES", "true")).lower() == "true"
    )
    ml_enable_basic_imputation: bool = field(
        default_factory=lambda: str(os.getenv("ML_ENABLE_BASIC_IMPUTATION", "true")).lower() == "true"
    )
    ml_enable_basic_scaling: bool = field(
        default_factory=lambda: str(os.getenv("ML_ENABLE_BASIC_SCALING", "true")).lower() == "true"
    )
    ml_save_model_artifacts: bool = field(
        default_factory=lambda: str(os.getenv("ML_SAVE_MODEL_ARTIFACTS", "true")).lower() == "true"
    )
    ml_save_model_registry_entries: bool = field(
        default_factory=lambda: str(os.getenv("ML_SAVE_MODEL_REGISTRY_ENTRIES", "true")).lower() == "true"
    )
    ml_save_model_evaluation_reports: bool = field(
        default_factory=lambda: str(os.getenv("ML_SAVE_MODEL_EVALUATION_REPORTS", "true")).lower() == "true"
    )

    def __post_init__(self):""")
