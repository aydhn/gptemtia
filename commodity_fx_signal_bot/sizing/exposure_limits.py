import pandas as pd
from typing import Dict, Any, Optional
from sizing.sizing_config import SizingProfile


def calculate_symbol_exposure_proxy(
    sizing_df: Optional[pd.DataFrame], symbol: str
) -> float:
    """Calculates the theoretical exposure proxy for a specific symbol."""
    if sizing_df is None or sizing_df.empty or "symbol" not in sizing_df.columns:
        return 0.0

    if "capped_theoretical_risk_amount" not in sizing_df.columns:
        return 0.0

    mask = sizing_df["symbol"] == symbol
    # Assume only 'approved' candidates represent existing proxy exposure
    if "sizing_label" in sizing_df.columns:
        mask = mask & (sizing_df["sizing_label"] == "sizing_approved_candidate")

    return float(sizing_df[mask]["capped_theoretical_risk_amount"].sum())


def calculate_asset_class_exposure_proxy(
    sizing_df: Optional[pd.DataFrame], asset_class: str
) -> float:
    """Calculates the theoretical exposure proxy for a specific asset class."""
    if sizing_df is None or sizing_df.empty or "asset_class" not in sizing_df.columns:
        return 0.0

    if "capped_theoretical_risk_amount" not in sizing_df.columns:
        return 0.0

    mask = sizing_df["asset_class"] == asset_class
    if "sizing_label" in sizing_df.columns:
        mask = mask & (sizing_df["sizing_label"] == "sizing_approved_candidate")

    return float(sizing_df[mask]["capped_theoretical_risk_amount"].sum())


def calculate_directional_exposure_proxy(
    sizing_df: Optional[pd.DataFrame], directional_bias: str
) -> float:
    """Calculates the theoretical exposure proxy for a specific direction (long/short)."""
    if (
        sizing_df is None
        or sizing_df.empty
        or "directional_bias" not in sizing_df.columns
    ):
        return 0.0

    if "capped_theoretical_risk_amount" not in sizing_df.columns:
        return 0.0

    mask = sizing_df["directional_bias"] == directional_bias
    if "sizing_label" in sizing_df.columns:
        mask = mask & (sizing_df["sizing_label"] == "sizing_approved_candidate")

    return float(sizing_df[mask]["capped_theoretical_risk_amount"].sum())


def check_exposure_limits(
    candidate_context: Dict[str, Any],
    existing_sizing_df: Optional[pd.DataFrame],
    profile: SizingProfile,
) -> Dict[str, Any]:
    """Checks exposure limits and returns proxy values and flags."""

    symbol = candidate_context.get("symbol", "")
    asset_class = candidate_context.get("asset_class", "")
    direction = candidate_context.get("directional_bias", "")

    symbol_exp = calculate_symbol_exposure_proxy(existing_sizing_df, symbol)
    ac_exp = calculate_asset_class_exposure_proxy(existing_sizing_df, asset_class)
    dir_exp = calculate_directional_exposure_proxy(existing_sizing_df, direction)

    equity = profile.theoretical_account_equity
    max_symbol = equity * profile.max_risk_per_symbol
    max_ac = equity * profile.max_risk_per_asset_class

    # We don't have a directional limit in the profile yet, but could add one.

    symbol_passed = symbol_exp < max_symbol
    ac_passed = ac_exp < max_ac

    warnings = []
    if not symbol_passed:
        warnings.append(
            f"Symbol exposure proxy ({symbol_exp}) exceeds limit ({max_symbol})."
        )
    if not ac_passed:
        warnings.append(
            f"Asset class exposure proxy ({ac_exp}) exceeds limit ({max_ac})."
        )

    return {
        "symbol_exposure_proxy": symbol_exp,
        "asset_class_exposure_proxy": ac_exp,
        "directional_exposure_proxy": dir_exp,
        "symbol_limit_passed": symbol_passed,
        "asset_class_limit_passed": ac_passed,
        "directional_limit_passed": True,  # Always pass for now as there's no limit defined
        "exposure_warnings": warnings,
    }
