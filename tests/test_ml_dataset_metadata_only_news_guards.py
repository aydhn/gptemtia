"""Test suite for Phase 137 ML Dataset Metadata-Only News Guards."""

import pytest
import pandas as pd
from advanced_ml_dataset_registry.ml_dataset_metadata_only_news_guards import (
    build_ml_dataset_metadata_only_news_guard_registry,
    validate_ml_dataset_metadata_only_news_columns,
    validate_no_forbidden_news_content,
    summarize_ml_dataset_metadata_only_news_guards,
)


def test_build_metadata_only_news_guards():
    df, summary = build_ml_dataset_metadata_only_news_guard_registry()
    assert not df.empty
    assert summary["total_news_guards"] >= 2


def test_validate_news_columns():
    good_cols = ["headline_hash", "topic_tag", "timestamp_utc"]
    v_good = validate_ml_dataset_metadata_only_news_columns(good_cols)
    assert v_good["valid"] is True

    bad_cols = ["headline_hash", "article_body", "full_text"]
    v_bad = validate_ml_dataset_metadata_only_news_columns(bad_cols)
    assert v_bad["valid"] is False


def test_validate_news_content():
    v_text = validate_no_forbidden_news_content(text="Here is raw article_body text")
    assert v_text["valid"] is False
