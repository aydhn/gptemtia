import re

with open("commodity_fx_signal_bot/config/settings.py", "r") as f:
    content = f.read()

ml_settings_code = """
    # Phase 29: ML Dataset Preparation
    ml_dataset_enabled: bool = field(
        default_factory=lambda: str(os.getenv("ML_DATASET_ENABLED", "true")).lower()
        == "true"
    )
    ml_target_engineering_enabled: bool = field(
        default_factory=lambda: str(
            os.getenv("ML_TARGET_ENGINEERING_ENABLED", "true")
        ).lower()
        == "true"
    )
    default_ml_dataset_profile: str = field(
        default_factory=lambda: os.getenv(
            "DEFAULT_ML_DATASET_PROFILE", "balanced_supervised_dataset"
        )
    )
    default_ml_dataset_timeframe: str = field(
        default_factory=lambda: os.getenv("DEFAULT_ML_DATASET_TIMEFRAME", "1d")
    )
    ml_default_forward_return_horizons: tuple[int, ...] = field(
        default_factory=lambda: tuple(
            int(x.strip())
            for x in os.getenv("ML_DEFAULT_FORWARD_RETURN_HORIZONS", "1,3,5,10,20").split(",")
            if x.strip()
        )
    )
    ml_default_forward_volatility_horizons: tuple[int, ...] = field(
        default_factory=lambda: tuple(
            int(x.strip())
            for x in os.getenv("ML_DEFAULT_FORWARD_VOLATILITY_HORIZONS", "5,10,20").split(",")
            if x.strip()
        )
    )
    ml_default_future_drawdown_horizons: tuple[int, ...] = field(
        default_factory=lambda: tuple(
            int(x.strip())
            for x in os.getenv("ML_DEFAULT_FUTURE_DRAWDOWN_HORIZONS", "5,10,20").split(",")
            if x.strip()
        )
    )
    ml_direction_threshold: float = field(
        default_factory=lambda: float(os.getenv("ML_DIRECTION_THRESHOLD", "0.002"))
    )
    ml_positive_return_threshold: float = field(
        default_factory=lambda: float(os.getenv("ML_POSITIVE_RETURN_THRESHOLD", "0.005"))
    )
    ml_negative_return_threshold: float = field(
        default_factory=lambda: float(os.getenv("ML_NEGATIVE_RETURN_THRESHOLD", "-0.005"))
    )
    ml_min_rows_for_dataset: int = field(
        default_factory=lambda: int(os.getenv("ML_MIN_ROWS_FOR_DATASET", "200"))
    )
    ml_max_feature_nan_ratio: float = field(
        default_factory=lambda: float(os.getenv("ML_MAX_FEATURE_NAN_RATIO", "0.35"))
    )
    ml_max_target_nan_ratio: float = field(
        default_factory=lambda: float(os.getenv("ML_MAX_TARGET_NAN_RATIO", "0.20"))
    )
    ml_use_purged_split: bool = field(
        default_factory=lambda: str(os.getenv("ML_USE_PURGED_SPLIT", "true")).lower()
        == "true"
    )
    ml_embargo_bars: int = field(
        default_factory=lambda: int(os.getenv("ML_EMBARGO_BARS", "5"))
    )
    ml_test_size_ratio: float = field(
        default_factory=lambda: float(os.getenv("ML_TEST_SIZE_RATIO", "0.20"))
    )
    ml_validation_size_ratio: float = field(
        default_factory=lambda: float(os.getenv("ML_VALIDATION_SIZE_RATIO", "0.20"))
    )
    ml_save_feature_matrix: bool = field(
        default_factory=lambda: str(os.getenv("ML_SAVE_FEATURE_MATRIX", "true")).lower()
        == "true"
    )
    ml_save_target_frame: bool = field(
        default_factory=lambda: str(os.getenv("ML_SAVE_TARGET_FRAME", "true")).lower()
        == "true"
    )
    ml_save_supervised_dataset: bool = field(
        default_factory=lambda: str(
            os.getenv("ML_SAVE_SUPERVISED_DATASET", "true")
        ).lower()
        == "true"
    )

    def __post_init__(self):
"""

content = content.replace("    def __post_init__(self):", ml_settings_code)

with open("commodity_fx_signal_bot/config/settings.py", "w") as f:
    f.write(content)
