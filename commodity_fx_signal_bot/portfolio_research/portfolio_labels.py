# Portfolio report type labels
PORTFOLIO_REPORT_TYPES = [
    "portfolio_research",
    "correlation_report",
    "diversification_report",
    "exposure_report",
    "virtual_basket_report",
    "basket_tracking_report",
    "concentration_risk_report",
    "unknown_portfolio_report",
]

# Basket type labels
BASKET_TYPES = [
    "equal_weight_basket",
    "research_score_weighted_basket",
    "risk_adjusted_basket",
    "paper_performance_weighted_basket",
    "custom_virtual_basket",
    "unknown_basket",
]

# Diversification labels
DIVERSIFICATION_LABELS = [
    "well_diversified",
    "moderately_diversified",
    "concentrated",
    "highly_concentrated",
    "insufficient_data",
    "unknown_diversification",
]

# Exposure labels
EXPOSURE_LABELS = [
    "balanced_exposure",
    "asset_class_concentrated",
    "symbol_concentrated",
    "currency_concentrated",
    "unknown_exposure",
]


def list_portfolio_report_type_labels() -> list[str]:
    return PORTFOLIO_REPORT_TYPES.copy()


def list_basket_type_labels() -> list[str]:
    return BASKET_TYPES.copy()


def list_diversification_labels() -> list[str]:
    return DIVERSIFICATION_LABELS.copy()


def list_exposure_labels() -> list[str]:
    return EXPOSURE_LABELS.copy()


def validate_portfolio_report_type(label: str) -> None:
    if label not in PORTFOLIO_REPORT_TYPES:
        raise ValueError(f"Invalid portfolio report type label: {label}")


def validate_basket_type(label: str) -> None:
    if label not in BASKET_TYPES:
        raise ValueError(f"Invalid basket type label: {label}. Note: this is a virtual basket, not a real portfolio instruction.")


def validate_diversification_label(label: str) -> None:
    if label not in DIVERSIFICATION_LABELS:
        raise ValueError(f"Invalid diversification label: {label}. Note: well_diversified is not investment advice.")


def validate_exposure_label(label: str) -> None:
    if label not in EXPOSURE_LABELS:
        raise ValueError(f"Invalid exposure label: {label}")
