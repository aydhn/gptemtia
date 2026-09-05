from advanced_data_normalization.data_normalization_config import get_default_data_normalization_profile
from advanced_data_normalization.data_normalization_domain_registry import (
    build_data_normalization_domain_registry,
    build_default_data_normalization_domains,
    summarize_data_normalization_domains,
)


def test_domain_registry():
    prof = get_default_data_normalization_profile()
    df, summary = build_data_normalization_domain_registry(prof)
    assert not df.empty
    assert len(df) >= 25
    assert "fx_symbol_normalization_domain" in df["domain_label"].tolist()
    assert summary["current_phase"] == 113
