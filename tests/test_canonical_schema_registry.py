from advanced_data_normalization.data_normalization_config import get_default_data_normalization_profile
from advanced_data_normalization.canonical_schema_registry import (
    build_canonical_schema_registry,
    summarize_canonical_schema_registry,
)


def test_canonical_schema_registry():
    prof = get_default_data_normalization_profile()
    df, summary = build_canonical_schema_registry(prof)
    assert not df.empty
    assert len(df) >= 10
    assert "dataset_fx_quote" in summary["dataset_types"]
    assert "dataset_commodity_spot" in summary["dataset_types"]
    assert "dataset_macro_timeseries" in summary["dataset_types"]
    assert "dataset_news_metadata" in summary["dataset_types"]
