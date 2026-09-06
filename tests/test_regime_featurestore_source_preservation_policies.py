import pandas as pd
from advanced_regime_featurestore_integration.regime_featurestore_source_preservation_policies import (
    build_regime_featurestore_source_preservation_policy_registry,
    validate_regime_featurestore_source_preservation_action,
    summarize_regime_featurestore_source_preservation_policies,
    PROHIBITED_SOURCE_ACTIONS,
)


def test_build_regime_featurestore_source_preservation_policy_registry():
    df, summary = build_regime_featurestore_source_preservation_policy_registry()
    assert isinstance(df, pd.DataFrame)
    assert len(df) == 7
    assert summary["source_preserved"] is True
    assert summary["non_signal"] is True
    assert summary["current_phase"] == 134


def test_validate_regime_featurestore_source_preservation_action():
    res_safe = validate_regime_featurestore_source_preservation_action("append_metadata_record")
    assert res_safe["is_permitted"] is True
    assert res_safe["is_prohibited"] is False
    assert res_safe["source_preserved"] is True

    res_bad = validate_regime_featurestore_source_preservation_action("overwrite_source")
    assert res_bad["is_permitted"] is False
    assert res_bad["is_prohibited"] is True
    assert res_bad["source_preserved"] is False

    res_del = validate_regime_featurestore_source_preservation_action("delete_source")
    assert res_del["is_permitted"] is False


def test_summarize_regime_featurestore_source_preservation_policies():
    df, _ = build_regime_featurestore_source_preservation_policy_registry()
    summary = summarize_regime_featurestore_source_preservation_policies(df)
    assert summary["total_prohibited_actions"] == 7
    assert summary["all_prohibited"] is True
