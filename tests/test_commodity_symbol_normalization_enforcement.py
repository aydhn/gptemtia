import pandas as pd
from advanced_data_normalization.commodity_symbol_normalization_enforcement import (
    normalize_commodity_symbol_value,
    normalize_commodity_symbol_dataframe,
    build_commodity_symbol_normalization_enforcement_report,
)
from advanced_data_normalization.data_normalization_config import get_default_data_normalization_profile


def test_normalize_commodity_symbol_value():
    assert normalize_commodity_symbol_value("GOLD") == "XAU/USD"
    assert normalize_commodity_symbol_value("XAUUSD") == "XAU/USD"
    assert normalize_commodity_symbol_value("CL") == "WTI_CRUDE_CONTINUOUS_PLACEHOLDER"
    assert normalize_commodity_symbol_value("BRENT") == "BRENT_CRUDE_CONTINUOUS_PLACEHOLDER"
    assert normalize_commodity_symbol_value("NG") == "NATURAL_GAS_CONTINUOUS_PLACEHOLDER"


def test_normalize_commodity_symbol_dataframe():
    raw_df = pd.DataFrame([{"symbol": "GOLD"}, {"symbol": "CL"}])
    norm_df, findings = normalize_commodity_symbol_dataframe(raw_df, field="symbol")

    assert "normalized_symbol" not in raw_df.columns
    assert "normalized_symbol" in norm_df.columns
    assert norm_df["normalized_symbol"].iloc[0] == "XAU/USD"
    assert norm_df["normalized_symbol"].iloc[1] == "WTI_CRUDE_CONTINUOUS_PLACEHOLDER"


def test_commodity_symbol_report():
    prof = get_default_data_normalization_profile()
    df, summary = build_commodity_symbol_normalization_enforcement_report(prof)
    assert not df.empty
    assert summary["total_mappings"] >= 5
