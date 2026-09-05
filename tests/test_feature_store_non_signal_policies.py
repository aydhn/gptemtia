from advanced_feature_store_integration.feature_store_non_signal_policies import (
    build_feature_store_non_signal_policy_registry,
    validate_feature_store_non_signal_text,
    summarize_feature_store_non_signal_policies,
)

def test_non_signal_policies():
    df, s = build_feature_store_non_signal_policy_registry()
    assert not df.empty
    assert s["non_signal"] is True

    safe_text = "Feature store metadata and schema definitions for offline research."
    assert validate_feature_store_non_signal_text(safe_text)["is_compliant"] is True

    forbidden_text = "This generates a buy signal with target forward_return."
    res = validate_feature_store_non_signal_text(forbidden_text)
    assert res["is_compliant"] is False
    assert len(res["findings"]) >= 2
