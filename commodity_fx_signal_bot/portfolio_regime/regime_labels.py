from typing import List

_PORTFOLIO_REGIME_LABELS = [
    "risk_on_regime",
    "risk_off_regime",
    "high_volatility_regime",
    "low_volatility_regime",
    "trend_positive_regime",
    "trend_negative_regime",
    "sideways_regime",
    "stress_regime",
    "recovery_regime",
    "unknown_regime"
]

_MACRO_SCENARIO_LABELS = [
    "usdtry_up_scenario",
    "usdtry_down_scenario",
    "gold_up_scenario",
    "gold_down_scenario",
    "oil_up_scenario",
    "oil_down_scenario",
    "inflation_up_scenario",
    "inflation_down_scenario",
    "broad_risk_off_scenario",
    "broad_risk_on_scenario",
    "unknown_scenario"
]

_STRESS_SEVERITY_LABELS = [
    "mild_stress",
    "moderate_stress",
    "severe_stress",
    "extreme_stress",
    "unknown_stress"
]

_DRAWDOWN_CLUSTER_LABELS = [
    "shallow_drawdown_cluster",
    "moderate_drawdown_cluster",
    "deep_drawdown_cluster",
    "prolonged_drawdown_cluster",
    "recovery_cluster",
    "unknown_drawdown_cluster"
]

def list_portfolio_regime_labels() -> List[str]:
    return _PORTFOLIO_REGIME_LABELS.copy()

def list_macro_scenario_labels() -> List[str]:
    return _MACRO_SCENARIO_LABELS.copy()

def list_stress_severity_labels() -> List[str]:
    return _STRESS_SEVERITY_LABELS.copy()

def list_drawdown_cluster_labels() -> List[str]:
    return _DRAWDOWN_CLUSTER_LABELS.copy()

def validate_portfolio_regime_label(label: str) -> None:
    if label not in _PORTFOLIO_REGIME_LABELS:
        raise ValueError(f"Invalid portfolio regime label: {label}")

def validate_macro_scenario_label(label: str) -> None:
    if label not in _MACRO_SCENARIO_LABELS:
        raise ValueError(f"Invalid macro scenario label: {label}")

def validate_stress_severity_label(label: str) -> None:
    if label not in _STRESS_SEVERITY_LABELS:
        raise ValueError(f"Invalid stress severity label: {label}")

def validate_drawdown_cluster_label(label: str) -> None:
    if label not in _DRAWDOWN_CLUSTER_LABELS:
        raise ValueError(f"Invalid drawdown cluster label: {label}")
