from dataclasses import dataclass
from typing import Dict, List, Optional, Tuple

class ConfigError(Exception):
    """Exception raised for errors in ML Prediction Configuration."""
    pass

@dataclass(frozen=True)
class MLPredictionProfile:
    name: str
    description: str
    dataset_profile: str
    training_profile: str
    allowed_model_families: Tuple[str, ...]
    min_model_quality_score: float = 0.50
    min_dataset_quality_score: float = 0.50
    max_leakage_risk_score: float = 0.20
    min_confidence_score: float = 0.40
    uncertainty_warning_threshold: float = 0.60
    allow_warning_models: bool = False
    use_calibration: bool = True
    use_ensemble: bool = True
    max_models_per_ensemble: int = 5
    enabled: bool = True
    notes: str = ""

_PREDICTION_PROFILES: Dict[str, MLPredictionProfile] = {
    "balanced_offline_prediction": MLPredictionProfile(
        name="balanced_offline_prediction",
        description="General purpose offline prediction candidate profile.",
        dataset_profile="balanced_supervised_dataset",
        training_profile="balanced_baseline_training",
        allowed_model_families=("dummy", "logistic_regression", "random_forest", "hist_gradient_boosting"),
        min_model_quality_score=0.50,
        min_dataset_quality_score=0.50,
        max_leakage_risk_score=0.20,
        min_confidence_score=0.40,
        uncertainty_warning_threshold=0.60,
        allow_warning_models=False,
        use_calibration=True,
        use_ensemble=True,
        max_models_per_ensemble=5,
        enabled=True,
        notes="General purpose offline prediction profile."
    ),
    "conservative_offline_prediction": MLPredictionProfile(
        name="conservative_offline_prediction",
        description="Strict quality and low leakage tolerance offline prediction profile.",
        dataset_profile="balanced_supervised_dataset",
        training_profile="balanced_baseline_training",
        allowed_model_families=("dummy", "logistic_regression", "random_forest", "hist_gradient_boosting"),
        min_model_quality_score=0.65,
        min_dataset_quality_score=0.65,
        max_leakage_risk_score=0.10,
        min_confidence_score=0.55,
        uncertainty_warning_threshold=0.60,
        allow_warning_models=False,
        use_calibration=True,
        use_ensemble=True,
        max_models_per_ensemble=3,
        enabled=True,
        notes="Strict quality and low leakage tolerance."
    ),
    "classification_prediction_profile": MLPredictionProfile(
        name="classification_prediction_profile",
        description="Direction/candidate outcome classification models.",
        dataset_profile="balanced_supervised_dataset",
        training_profile="balanced_baseline_training",
        allowed_model_families=("dummy", "logistic_regression", "random_forest", "hist_gradient_boosting"),
        use_calibration=True,
        enabled=True,
        notes="Classification models for direction."
    ),
    "regression_prediction_profile": MLPredictionProfile(
        name="regression_prediction_profile",
        description="Forward return regression models.",
        dataset_profile="balanced_supervised_dataset",
        training_profile="forward_return_regression_training",
        allowed_model_families=("dummy", "random_forest", "hist_gradient_boosting"),
        use_calibration=False,
        enabled=True,
        notes="Forward return regression models."
    ),
    "candidate_outcome_prediction_profile": MLPredictionProfile(
        name="candidate_outcome_prediction_profile",
        description="Candidate outcome prediction models.",
        dataset_profile="candidate_outcome_dataset",
        training_profile="candidate_outcome_training",
        allowed_model_families=("dummy", "random_forest", "hist_gradient_boosting"),
        enabled=True,
        notes="Candidate outcome prediction models."
    ),
}

def get_ml_prediction_profile(name: str) -> MLPredictionProfile:
    """Retrieve an MLPredictionProfile by name."""
    if name not in _PREDICTION_PROFILES:
        raise ConfigError(f"Prediction profile '{name}' not found.")
    return _PREDICTION_PROFILES[name]

def list_ml_prediction_profiles(enabled_only: bool = True) -> List[MLPredictionProfile]:
    """Return a list of available prediction profiles."""
    if enabled_only:
        return [p for p in _PREDICTION_PROFILES.values() if p.enabled]
    return list(_PREDICTION_PROFILES.values())

def get_default_ml_prediction_profile() -> MLPredictionProfile:
    """Return the default ML prediction profile."""
    from config.settings import settings
    return get_ml_prediction_profile(settings.default_ml_prediction_profile)

def validate_ml_prediction_profiles() -> None:
    """Validate all registered ML prediction profiles."""
    for name, profile in _PREDICTION_PROFILES.items():
        if not profile.allowed_model_families:
            raise ConfigError(f"Profile '{name}' has empty allowed_model_families.")
        if not (0.0 <= profile.min_model_quality_score <= 1.0):
            raise ConfigError(f"Profile '{name}' min_model_quality_score out of bounds (0-1).")
        if not (0.0 <= profile.min_dataset_quality_score <= 1.0):
            raise ConfigError(f"Profile '{name}' min_dataset_quality_score out of bounds (0-1).")
        if not (0.0 <= profile.max_leakage_risk_score <= 1.0):
            raise ConfigError(f"Profile '{name}' max_leakage_risk_score out of bounds (0-1).")
        if not (0.0 <= profile.min_confidence_score <= 1.0):
            raise ConfigError(f"Profile '{name}' min_confidence_score out of bounds (0-1).")
        if profile.max_models_per_ensemble <= 0:
            raise ConfigError(f"Profile '{name}' max_models_per_ensemble must be positive.")

# Run validation on import
validate_ml_prediction_profiles()
