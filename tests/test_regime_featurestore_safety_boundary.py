import pandas as pd
from advanced_regime_featurestore_integration.regime_featurestore_safety_boundary import (
    build_regime_featurestore_no_go_conditions,
    build_regime_featurestore_safe_go_conditions,
    build_regime_featurestore_safety_boundary,
    summarize_regime_featurestore_safety_boundary,
    CANONICAL_NO_GO_CONDITIONS,
    CANONICAL_SAFE_GO_CONDITIONS,
)


def test_build_regime_featurestore_safety_boundary():
    df, summary = build_regime_featurestore_safety_boundary()
    assert isinstance(df, pd.DataFrame)
    assert len(df) == len(CANONICAL_NO_GO_CONDITIONS) + len(CANONICAL_SAFE_GO_CONDITIONS)
    assert summary["safety_status"] == "SECURE"
    assert summary["no_go_count"] == 21
    assert summary["safe_go_count"] == 8
    assert summary["non_signal"] is True
    assert summary["current_phase"] == 134


def test_summarize_regime_featurestore_safety_boundary():
    df, _ = build_regime_featurestore_safety_boundary()
    summary = summarize_regime_featurestore_safety_boundary(df)
    assert summary["safety_status"] == "SECURE"
    assert summary["no_go_count"] == 21
    assert summary["safe_go_count"] == 8
