class LabelError(Exception):
    pass

SYNTHETIC_INDEX_TYPE_LABELS = [
    "metals_composite_index",
    "energy_composite_index",
    "agriculture_softs_composite_index",
    "fx_try_composite_index",
    "commodity_composite_index",
    "commodity_fx_composite_index",
    "inflation_hedge_proxy_index",
    "usdtry_relative_commodity_index",
    "gold_relative_universe_index",
    "oil_relative_universe_index",
    "custom_synthetic_index",
    "unknown_synthetic_index",
]

WEIGHTING_SCHEME_LABELS = [
    "equal_weight",
    "inverse_volatility_weight",
    "research_score_weight",
    "market_proxy_weight",
    "risk_adjusted_weight",
    "custom_weight",
    "unknown_weighting",
]

RELATIVE_STRENGTH_LABELS = [
    "strong_leader",
    "moderate_leader",
    "neutral_relative_strength",
    "moderate_laggard",
    "strong_laggard",
    "insufficient_data",
    "unknown_relative_strength",
]

ROTATION_LABELS = [
    "rotation_candidate_leader",
    "rotation_candidate_improving",
    "rotation_candidate_neutral",
    "rotation_candidate_weakening",
    "rotation_candidate_laggard",
    "insufficient_rotation_data",
    "unknown_rotation",
]

def list_synthetic_index_type_labels() -> list[str]:
    return SYNTHETIC_INDEX_TYPE_LABELS.copy()

def list_weighting_scheme_labels() -> list[str]:
    return WEIGHTING_SCHEME_LABELS.copy()

def list_relative_strength_labels() -> list[str]:
    return RELATIVE_STRENGTH_LABELS.copy()

def list_rotation_labels() -> list[str]:
    return ROTATION_LABELS.copy()

def validate_synthetic_index_type(label: str) -> None:
    if label not in SYNTHETIC_INDEX_TYPE_LABELS:
        raise LabelError(f"Invalid synthetic index type label: {label}")

def validate_weighting_scheme(label: str) -> None:
    if label not in WEIGHTING_SCHEME_LABELS:
        raise LabelError(f"Invalid weighting scheme label: {label}")

def validate_relative_strength_label(label: str) -> None:
    if label not in RELATIVE_STRENGTH_LABELS:
        raise LabelError(f"Invalid relative strength label: {label}")
    if "buy" in label.lower() or "sell" in label.lower():
         raise LabelError(f"Invalid relative strength label: {label}. Cannot contain buy/sell.")

def validate_rotation_label(label: str) -> None:
    if label not in ROTATION_LABELS:
        raise LabelError(f"Invalid rotation label: {label}")
    if "buy" in label.lower() or "sell" in label.lower() or "trade" in label.lower():
         raise LabelError(f"Invalid rotation label: {label}. Cannot contain buy/sell/trade.")
