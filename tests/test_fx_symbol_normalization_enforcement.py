import pandas as pd
from advanced_data_normalization.fx_symbol_normalization_enforcement import (
    normalize_fx_symbol_value,
    normalize_fx_symbol_dataframe,
    build_fx_symbol_normalization_enforcement_report,
)
from advanced_data_normalization.data_normalization_config import get_default_data_normalization_profile


def test_normalize_fx_symbol_value():
    assert normalize_fx_symbol_value("EURUSD") == "EUR/USD"
    assert normalize_fx_symbol_value("EUR_USD") == "EUR/USD"
    assert normalize_fx_symbol_value("USDTRY") == "USD/TRY"
    assert normalize_fx_symbol_value("GBPJPY") == "GBP/JPY"
    assert normalize_fx_symbol_value("UNKNOWN_VALUE") == "UNKNOWN_VALUE"


def test_normalize_fx_symbol_dataframe():
    raw_df = pd.DataFrame([{"pair": "EURUSD"}, {"pair": "USD_TRY"}, {"pair": "BAD"}])
    norm_df, findings = normalize_fx_symbol_dataframe(raw_df, field="pair")

    # Verify input df was NOT mutated
    assert "normalized_pair" not in raw_df.columns
    assert "normalized_pair" in norm_df.columns
    assert norm_df["normalized_pair"].iloc[0] == "EUR/USD"
    assert norm_df["normalized_pair"].iloc[1] == "USD/TRY"
    manual_findings = [f for f in findings if f.manual_review_required]
    assert len(manual_findings) == 1
    assert manual_findings[0].manual_review_required is True


def test_build_fx_symbol_report():
    prof = get_default_data_normalization_profile()
    df, summary = build_fx_symbol_normalization_enforcement_report(prof)
    assert not df.empty
    assert summary["total_rules"] >= 10
