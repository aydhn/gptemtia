# Factor Type Labels
FACTOR_TYPES = [
    "trend_factor",
    "momentum_factor",
    "volatility_factor",
    "carry_proxy_factor",
    "value_proxy_factor",
    "defensive_factor",
    "inflation_sensitivity_factor",
    "usdtry_sensitivity_factor",
    "gold_relative_factor",
    "oil_relative_factor",
    "composite_factor",
    "unknown_factor"
]

# Factor Direction Labels
FACTOR_DIRECTIONS = [
    "higher_is_better",
    "lower_is_better",
    "neutral_direction",
    "unknown_direction"
]

# Factor Bucket Labels
FACTOR_BUCKETS = [
    "top_factor_bucket",
    "middle_factor_bucket",
    "bottom_factor_bucket",
    "insufficient_factor_data",
    "unknown_factor_bucket"
]

# Factor Research Labels
FACTOR_RESEARCH_LABELS = [
    "factor_supportive_context",
    "factor_conflicting_context",
    "factor_neutral_context",
    "factor_unstable_context",
    "factor_insufficient_data",
    "unknown_factor_context"
]

def list_factor_type_labels() -> list[str]:
    return FACTOR_TYPES

def list_factor_direction_labels() -> list[str]:
    return FACTOR_DIRECTIONS

def list_factor_bucket_labels() -> list[str]:
    return FACTOR_BUCKETS

def list_factor_research_labels() -> list[str]:
    return FACTOR_RESEARCH_LABELS

def validate_factor_type(label: str) -> None:
    if label not in FACTOR_TYPES:
        raise ValueError(f"Invalid factor type label: {label}")

def validate_factor_direction(label: str) -> None:
    if label not in FACTOR_DIRECTIONS:
        raise ValueError(f"Invalid factor direction label: {label}")

def validate_factor_bucket(label: str) -> None:
    if label not in FACTOR_BUCKETS:
        raise ValueError(f"Invalid factor bucket label: {label}")

def validate_factor_research_label(label: str) -> None:
    if label not in FACTOR_RESEARCH_LABELS:
        raise ValueError(f"Invalid factor research label: {label}")
