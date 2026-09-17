"""Test suite for Phase 139 GPU Training Metadata-Only News Guards."""

from advanced_gpu_training_governance.gpu_training_governance_config import (
    get_default_gpu_training_governance_profile,
)
from advanced_gpu_training_governance.gpu_training_metadata_only_news_guards import (
    build_gpu_training_metadata_only_news_guard_registry,
    summarize_gpu_training_metadata_only_news_guards,
    validate_gpu_training_metadata_only_news_columns,
)


def test_build_gpu_training_metadata_only_news_guard_registry():
    profile = get_default_gpu_training_governance_profile()
    df, summary = build_gpu_training_metadata_only_news_guard_registry(profile)

    assert len(df) == 3
    assert summary["total_guards"] == 3
    assert summary["all_enforced"] is True
    assert summary["non_signal"] is True


def test_validate_gpu_training_metadata_only_news_columns():
    clean_cols = ["news_id", "headline_length", "source_domain", "published_hour"]
    res_clean = validate_gpu_training_metadata_only_news_columns(clean_cols)
    assert res_clean["is_clean"] is True
    assert res_clean["status"] == "PASS"

    dirty_cols = ["news_id", "full_text", "article_body", "raw_content", "scraped_html", "embedding_vector", "sentiment_score"]
    res_dirty = validate_gpu_training_metadata_only_news_columns(dirty_cols)
    assert res_dirty["is_clean"] is False
    assert len(res_dirty["violating_columns"]) >= 5
    assert res_dirty["status"] == "FAIL_RAW_NEWS_OR_NLP"
