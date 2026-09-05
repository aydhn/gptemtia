import pytest
from advanced_factor_metadata.technical_factor_families import (
    build_technical_factor_family_registry,
    summarize_technical_factor_family,
)


def test_build_technical_factor_family_registry():
    df, summary = build_technical_factor_family_registry()
    assert not df.empty
    assert summary["total_factors"] >= 3
    assert summary["non_signal"] is True
    assert "factor_name" in df.columns

    stats = summarize_technical_factor_family(df)
    assert stats["total_factors"] == len(df)
    assert stats["non_signal"] is True
