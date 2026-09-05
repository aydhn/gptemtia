from advanced_regime_matrix.regime_matrix_config import get_default_regime_matrix_profile
from advanced_regime_matrix.regime_matrix_domain_registry import (
    build_regime_matrix_domain_registry,
)


def test_build_regime_matrix_domain_registry():
    prof = get_default_regime_matrix_profile()
    df, s = build_regime_matrix_domain_registry(prof)
    assert len(df) >= 6
    assert s["total_domains"] >= 6
    assert s["all_non_signal"] is True
    domains = set(df["domain_name"].values)
    assert "technical_volatility" in domains
    assert "factor_trend" in domains
    assert "cross_asset" in domains
