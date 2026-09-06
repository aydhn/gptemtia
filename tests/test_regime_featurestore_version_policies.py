"""Tests for Phase 134 Regime FeatureStore Version Policies."""

from advanced_regime_featurestore_integration.regime_featurestore_version_policies import (
    build_regime_featurestore_version_policy_registry,
    validate_regime_featurestore_version_policy,
    summarize_regime_featurestore_version_policies,
)


def test_version_policies():
    df, summary = build_regime_featurestore_version_policy_registry()
    assert not df.empty
    assert (df["allow_overwrite"] == False).all()
    assert (df["allow_production_release_tag"] == False).all()

    s_res = summarize_regime_featurestore_version_policies(df)
    assert s_res["all_overwrites_prohibited"] is True

    valid_policy = {"policy_name": "safe_append", "allow_overwrite": False, "allow_production_release_tag": False}
    assert validate_regime_featurestore_version_policy(valid_policy)["is_valid"] is True

    bad_policy = {"policy_name": "bad_overwrite", "allow_overwrite": True}
    assert validate_regime_featurestore_version_policy(bad_policy)["is_valid"] is False
