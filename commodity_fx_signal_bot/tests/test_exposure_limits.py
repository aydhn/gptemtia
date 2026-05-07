from sizing.exposure_limits import (
    calculate_symbol_exposure_proxy,
    calculate_asset_class_exposure_proxy,
    calculate_directional_exposure_proxy,
    check_exposure_limits
)
from sizing.sizing_config import get_default_sizing_profile
import pandas as pd

def test_calculate_symbol_exposure_proxy():
    df = pd.DataFrame({
        "symbol": ["GC=F", "GC=F", "EURUSD=X"],
        "sizing_label": ["sizing_approved_candidate", "sizing_rejected_candidate", "sizing_approved_candidate"],
        "capped_theoretical_risk_amount": [100.0, 500.0, 200.0]
    })

    # Only approved should be counted
    assert calculate_symbol_exposure_proxy(df, "GC=F") == 100.0
    assert calculate_symbol_exposure_proxy(df, "EURUSD=X") == 200.0
    assert calculate_symbol_exposure_proxy(df, "UNKNOWN") == 0.0

def test_calculate_asset_class_exposure_proxy():
    df = pd.DataFrame({
        "asset_class": ["metals", "metals", "forex"],
        "sizing_label": ["sizing_approved_candidate", "sizing_approved_candidate", "sizing_approved_candidate"],
        "capped_theoretical_risk_amount": [100.0, 150.0, 200.0]
    })

    assert calculate_asset_class_exposure_proxy(df, "metals") == 250.0

def test_calculate_directional_exposure_proxy():
    df = pd.DataFrame({
        "directional_bias": ["long", "short", "long"],
        "sizing_label": ["sizing_approved_candidate", "sizing_approved_candidate", "sizing_approved_candidate"],
        "capped_theoretical_risk_amount": [100.0, 150.0, 200.0]
    })

    assert calculate_directional_exposure_proxy(df, "long") == 300.0

def test_missing_df_exposure_proxy():
    assert calculate_symbol_exposure_proxy(None, "GC=F") == 0.0
