import pytest
import pandas as pd
from advanced_data_quality.data_quality_config import get_default_data_quality_profile
from advanced_data_quality.news_copyright_quality_rules import (
    build_news_metadata_copyright_quality_rule_set,
    check_news_copyright_boundary,
)


def test_news_copyright_quality_rules():
    profile = get_default_data_quality_profile()
    df_rules, _ = build_news_metadata_copyright_quality_rule_set(profile)
    assert len(df_rules) >= 3

    # Forbidden article body check
    bad_df = pd.DataFrame([
        {"item_id": "n1", "article_body": "full text of copyrighted article..."}
    ])
    findings = check_news_copyright_boundary(bad_df, "test_p")
    assert any(f.severity_label == "quality_critical" for f in findings)
    assert any("article_body" in f.field_name for f in findings)
