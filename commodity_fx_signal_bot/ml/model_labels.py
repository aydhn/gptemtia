# Task type labels
TASK_CLASSIFICATION = "classification"
TASK_REGRESSION = "regression"

# Model family labels
MODEL_FAMILY_DUMMY = "dummy"
MODEL_FAMILY_LOGISTIC_REGRESSION = "logistic_regression"
MODEL_FAMILY_RANDOM_FOREST = "random_forest"
MODEL_FAMILY_HIST_GRADIENT_BOOSTING = "hist_gradient_boosting"
MODEL_FAMILY_UNKNOWN = "unknown_model_family"

# Model status labels
STATUS_TRAINED_CANDIDATE = "trained_candidate"
STATUS_EVALUATION_PASSED_CANDIDATE = "evaluation_passed_candidate"
STATUS_EVALUATION_WARNING_CANDIDATE = "evaluation_warning_candidate"
STATUS_EVALUATION_FAILED_CANDIDATE = "evaluation_failed_candidate"
STATUS_INSUFFICIENT_DATA = "insufficient_data"
STATUS_LEAKAGE_RISK_HIGH = "leakage_risk_high"
STATUS_INVALID_TARGET = "invalid_target"
STATUS_UNKNOWN = "unknown_model_status"

# Evaluation severity labels
SEVERITY_LOW = "low"
SEVERITY_MODERATE = "moderate"
SEVERITY_ELEVATED = "elevated"
SEVERITY_HIGH = "high"
SEVERITY_EXTREME = "extreme"
SEVERITY_UNKNOWN = "unknown"


def list_task_type_labels() -> list[str]:
    return [TASK_CLASSIFICATION, TASK_REGRESSION]

def list_model_family_labels() -> list[str]:
    return [
        MODEL_FAMILY_DUMMY,
        MODEL_FAMILY_LOGISTIC_REGRESSION,
        MODEL_FAMILY_RANDOM_FOREST,
        MODEL_FAMILY_HIST_GRADIENT_BOOSTING,
        MODEL_FAMILY_UNKNOWN,
    ]

def list_model_status_labels() -> list[str]:
    return [
        STATUS_TRAINED_CANDIDATE,
        STATUS_EVALUATION_PASSED_CANDIDATE,
        STATUS_EVALUATION_WARNING_CANDIDATE,
        STATUS_EVALUATION_FAILED_CANDIDATE,
        STATUS_INSUFFICIENT_DATA,
        STATUS_LEAKAGE_RISK_HIGH,
        STATUS_INVALID_TARGET,
        STATUS_UNKNOWN,
    ]

def validate_task_type(label: str) -> None:
    if label not in list_task_type_labels():
        raise ValueError(f"Invalid task type: {label}")

def validate_model_family(label: str) -> None:
    if label not in list_model_family_labels():
        raise ValueError(f"Invalid model family: {label}")

def validate_model_status(label: str) -> None:
    if label not in list_model_status_labels():
        raise ValueError(f"Invalid model status: {label}")

def is_classification_task(task_type: str) -> bool:
    return task_type == TASK_CLASSIFICATION

def is_regression_task(task_type: str) -> bool:
    return task_type == TASK_REGRESSION
