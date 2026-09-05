import pandas as pd
from advanced_data_normalization.region_currency_normalization import (
    normalize_region_code,
    normalize_currency_code,
    normalize_region_currency_dataframe,
    build_region_country_currency_normalization_registry,
)
from advanced_data_normalization.data_normalization_config import get_default_data_normalization_profile


def test_normalize_region_currency():
    assert normalize_region_code("United States") == "US"
    assert normalize_region_code("USA") == "US"
    assert normalize_region_code("Türkiye") == "TR"
    assert normalize_region_code("Turkey") == "TR"
    assert normalize_currency_code("USDollar") == "USD"
    assert normalize_currency_code("Turkish Lira") == "TRY"


def test_normalize_region_currency_dataframe():
    raw_df = pd.DataFrame([{"region": "United States", "currency": "USDollar"}])
    norm_df, findings = normalize_region_currency_dataframe(raw_df, region_field="region", currency_field="currency")

    assert "normalized_region" in norm_df.columns
    assert "normalized_currency" in norm_df.columns
    assert norm_df["normalized_region"].iloc[0] == "US"
    assert norm_df["normalized_currency"].iloc[0] == "USD"


def test_region_currency_report():
    prof = get_default_data_normalization_profile()
    df, summary = build_region_country_currency_normalization_registry(prof)
    assert not df.empty
    assert summary["total_mappings"] >= 10
