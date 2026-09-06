import pandas as pd
from advanced_regime_featurestore_integration.regime_featurestore_non_signal_policies import (
    build_regime_featurestore_non_signal_policy_registry,
    validate_regime_featurestore_non_signal_text,
    summarize_regime_featurestore_non_signal_policies,
    FORBIDDEN_CLAIMS,
)


def test_build_regime_featurestore_non_signal_policy_registry():
    df, summary = build_regime_featurestore_non_signal_policy_registry()
    assert isinstance(df, pd.DataFrame)
    assert len(df) == 14
    assert summary["total_forbidden_claims"] == 14
    assert summary["non_signal"] is True
    assert summary["current_phase"] == 134


def test_validate_regime_featurestore_non_signal_text():
    clean_text = "This is a regime matrix snapshot for research analysis."
    res_clean = validate_regime_featurestore_non_signal_text(clean_text)
    assert res_clean["is_valid"] is True
    assert res_clean["non_signal"] is True

    bad_text = "Tavsiyemiz: KESIN AL sinyali veriyoruz. Model prediction: bullish."
    res_bad = validate_regime_featurestore_non_signal_text(bad_text)
    assert res_bad["is_valid"] is False
    assert "kesin al" in res_bad["found_violations"]
    assert "model prediction" in res_bad["found_violations"]


def test_summarize_regime_featurestore_non_signal_policies():
    df, _ = build_regime_featurestore_non_signal_policy_registry()
    summary = summarize_regime_featurestore_non_signal_policies(df)
    assert summary["total_forbidden_patterns"] == 14
    assert summary["all_strictly_forbidden"] is True
