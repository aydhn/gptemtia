# Target type labels
TARGET_FORWARD_RETURN = "forward_return"
TARGET_DIRECTION_CLASS = "direction_class"
TARGET_FUTURE_VOLATILITY = "future_volatility"
TARGET_FUTURE_DRAWDOWN = "future_drawdown"
TARGET_CANDIDATE_OUTCOME = "candidate_outcome"
TARGET_TRADE_RESULT = "trade_result"
TARGET_REWARD_RISK_OUTCOME = "reward_risk_outcome"
TARGET_UNKNOWN = "unknown_target"

# Direction class labels
DIR_UP = "up"
DIR_DOWN = "down"
DIR_FLAT = "flat"
DIR_UNKNOWN = "unknown"

# Candidate outcome labels
OUTCOME_POSITIVE = "positive_outcome"
OUTCOME_NEGATIVE = "negative_outcome"
OUTCOME_NEUTRAL = "neutral_outcome"
OUTCOME_INVALID = "invalid_outcome"
OUTCOME_UNKNOWN = "unknown_outcome"

# Split labels
SPLIT_TRAIN = "train"
SPLIT_VALIDATION = "validation"
SPLIT_TEST = "test"
SPLIT_PURGED_TRAIN = "purged_train"
SPLIT_EMBARGO = "embargo"
SPLIT_UNKNOWN = "unknown_split"

# Dataset status labels
STATUS_READY = "dataset_ready_candidate"
STATUS_WARNING = "dataset_warning_candidate"
STATUS_REJECTED = "dataset_rejected_candidate"
STATUS_INSUFFICIENT_ROWS = "insufficient_rows"
STATUS_EXCESSIVE_NAN = "excessive_missing_values"
STATUS_LEAKAGE_RISK = "leakage_risk_high"
STATUS_UNKNOWN = "unknown_dataset_status"

def list_target_type_labels() -> list[str]:
    return [
        TARGET_FORWARD_RETURN, TARGET_DIRECTION_CLASS, TARGET_FUTURE_VOLATILITY,
        TARGET_FUTURE_DRAWDOWN, TARGET_CANDIDATE_OUTCOME, TARGET_TRADE_RESULT,
        TARGET_REWARD_RISK_OUTCOME, TARGET_UNKNOWN
    ]

def list_direction_class_labels() -> list[str]:
    return [DIR_UP, DIR_DOWN, DIR_FLAT, DIR_UNKNOWN]

def list_candidate_outcome_labels() -> list[str]:
    return [OUTCOME_POSITIVE, OUTCOME_NEGATIVE, OUTCOME_NEUTRAL, OUTCOME_INVALID, OUTCOME_UNKNOWN]

def list_ml_split_labels() -> list[str]:
    return [SPLIT_TRAIN, SPLIT_VALIDATION, SPLIT_TEST, SPLIT_PURGED_TRAIN, SPLIT_EMBARGO, SPLIT_UNKNOWN]

def list_dataset_status_labels() -> list[str]:
    return [
        STATUS_READY, STATUS_WARNING, STATUS_REJECTED, STATUS_INSUFFICIENT_ROWS,
        STATUS_EXCESSIVE_NAN, STATUS_LEAKAGE_RISK, STATUS_UNKNOWN
    ]

def validate_target_type_label(label: str) -> None:
    if label not in list_target_type_labels():
        raise ValueError(f"Invalid target type label: {label}")

def validate_direction_class_label(label: str) -> None:
    if label not in list_direction_class_labels():
        raise ValueError(f"Invalid direction class label: {label}")

def validate_candidate_outcome_label(label: str) -> None:
    if label not in list_candidate_outcome_labels():
        raise ValueError(f"Invalid candidate outcome label: {label}")

def validate_dataset_status_label(label: str) -> None:
    if label not in list_dataset_status_labels():
        raise ValueError(f"Invalid dataset status label: {label}")
