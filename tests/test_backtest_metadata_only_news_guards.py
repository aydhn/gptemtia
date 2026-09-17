# -*- coding: utf-8 -*-
"""Phase 150 Unit Tests: Backtest Metadata-Only News Guards."""

from advanced_backtest_governance.backtest_governance_config import (
    get_default_backtest_governance_profile,
)
from advanced_backtest_governance.backtest_metadata_only_news_guards import (
    build_backtest_metadata_only_news_guard_registry,
    validate_backtest_metadata_only_news_columns,
    METADATA_ONLY_RULES,
)


def test_build_backtest_metadata_only_news_guards():
    profile = get_default_backtest_governance_profile()
    df, summary = build_backtest_metadata_only_news_guard_registry(profile)

    assert not df.empty
    assert len(df) == 4
    assert "guard_id" in df.columns
    assert "guard_name" in df.columns
    assert (df["status"] == "ACTIVE").all()
    assert summary["all_active"] is True
    assert summary["total_guards"] == 4
    assert len(METADATA_ONLY_RULES) == 4


def test_validate_backtest_metadata_only_news_columns():
    invalid_cols = ["headline", "article_body", "raw_content", "embedding"]
    res_inv = validate_backtest_metadata_only_news_columns(invalid_cols)
    assert res_inv["is_clean"] is False
    assert res_inv["is_blocked"] is True
    assert len(res_inv["violating_columns"]) > 0

    valid_cols = ["headline_hash", "source_code", "timestamp", "topic_tag"]
    res_val = validate_backtest_metadata_only_news_columns(valid_cols)
    assert res_val["is_clean"] is True
    assert res_val["is_blocked"] is False
    assert len(res_val["violating_columns"]) == 0
