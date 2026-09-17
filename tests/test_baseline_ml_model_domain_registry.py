"""Test suite for Phase 138 Baseline ML Model Domain Registry."""

from advanced_baseline_ml_models.baseline_ml_model_config import (
    get_default_baseline_ml_model_profile,
)
from advanced_baseline_ml_models.baseline_ml_model_domain_registry import (
    build_baseline_ml_model_domain_registry,
    summarize_baseline_ml_model_domains,
)


def test_build_domain_registry():
    profile = get_default_baseline_ml_model_profile()
    df, summary = build_baseline_ml_model_domain_registry(profile)

    assert len(df) == 37
    assert summary["total_domains"] == 37
    assert summary["active_domains"] == 37
    assert summary["non_signal"] is True
    assert "domain_key" in df.columns
    assert "category" in df.columns
    assert "non_signal" in df.columns


def test_domain_categories():
    profile = get_default_baseline_ml_model_profile()
    df, _ = build_baseline_ml_model_domain_registry(profile)
    categories = set(df["category"].unique())
    assert "contracts" in categories
    assert "harness" in categories
    assert "guards" in categories
    assert "governance" in categories
