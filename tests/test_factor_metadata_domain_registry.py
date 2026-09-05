import pytest
from advanced_factor_metadata.factor_metadata_domain_registry import build_factor_metadata_domain_registry


def test_build_factor_metadata_domain_registry():
    df, summary = build_factor_metadata_domain_registry()
    assert not df.empty
    assert summary["total_domains"] >= 32
    assert summary["non_signal"] is True
    assert summary["current_phase"] == 122
    assert "domain_label" in df.columns
    assert "domain_name" in df.columns
