import pandas as pd
from advanced_data_normalization.string_case_slug_normalization import (
    normalize_slug_value,
    normalize_upper_token,
    normalize_string_dataframe,
    build_string_case_slug_normalization_registry,
)
from advanced_data_normalization.data_normalization_config import get_default_data_normalization_profile


def test_normalize_slug_and_token():
    assert normalize_slug_value("Hello World 2026") == "hello_world_2026"
    assert normalize_slug_value("EUR/USD Pair") == "eur_usd_pair"
    assert normalize_upper_token("central bank") == "CENTRAL_BANK"


def test_normalize_string_dataframe():
    raw_df = pd.DataFrame([{"text": "Commodity Spot"}])
    norm_df, findings = normalize_string_dataframe(raw_df, fields=["text"])

    assert "text" in norm_df.columns
    assert "normalized_text" in norm_df.columns
    assert norm_df["normalized_text"].iloc[0] == "commodity_spot"


def test_string_slug_report():
    prof = get_default_data_normalization_profile()
    df, summary = build_string_case_slug_normalization_registry(prof)
    assert not df.empty
