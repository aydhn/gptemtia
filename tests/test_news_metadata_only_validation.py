import pytest
import pandas as pd
from advanced_feature_validation.news_metadata_only_validation import (
    validate_news_metadata_only_columns,
    FORBIDDEN_NEWS_COLUMNS,
)


def test_news_metadata_only_validation():
    assert "article_body" in FORBIDDEN_NEWS_COLUMNS
    assert "full_text" in FORBIDDEN_NEWS_COLUMNS
    assert "raw_content" in FORBIDDEN_NEWS_COLUMNS

    df_valid = pd.DataFrame({
        "timestamp": [1, 2],
        "news_headline_count": [3, 5],
        "news_topic_energy": [1, 0],
    })
    res_valid = validate_news_metadata_only_columns(df_valid)
    assert res_valid["is_valid"] is True

    df_invalid = pd.DataFrame({
        "timestamp": [1, 2],
        "article_body": ["Full text of article", "Another full text"],
    })
    res_invalid = validate_news_metadata_only_columns(df_invalid)
    assert res_invalid["is_valid"] is False
    assert "article_body" in res_invalid["forbidden_found"]
