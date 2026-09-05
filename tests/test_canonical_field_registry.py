from advanced_data_normalization.data_normalization_config import get_default_data_normalization_profile
from advanced_data_normalization.canonical_field_registry import (
    build_canonical_field_registry,
    summarize_canonical_field_registry,
)


def test_canonical_field_registry():
    prof = get_default_data_normalization_profile()
    df, summary = build_canonical_field_registry(prof)
    assert not df.empty
    assert len(df) >= 25
    field_names = df["canonical_field_name"].tolist()
    assert "pair" in field_names
    assert "symbol" in field_names
    assert "timestamp" in field_names
