from advanced_feature_engine.feature_engine_config import get_default_feature_engine_profile
from advanced_feature_engine.feature_engine_domain_registry import (
    build_feature_engine_domain_registry,
    summarize_feature_engine_domain_registry,
)


def test_feature_engine_domain_registry():
    profile = get_default_feature_engine_profile()
    df, summary = build_feature_engine_domain_registry(profile)

    assert not df.empty
    assert len(df) >= 20
    assert "domain_label" in df.columns
    assert "domain_name" in df.columns
    assert summary["all_domains_defined"] is True
    assert summary["current_phase"] == 116
    assert summary["target_final_phase"] == 160
