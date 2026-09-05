import pandas as pd
from advanced_data_normalization.news_topic_tag_normalization_enforcement import (
    normalize_news_topic_value,
    normalize_news_tag_value,
    normalize_news_tags_dataframe,
    build_news_topic_tag_normalization_enforcement_report,
)
from advanced_data_normalization.data_normalization_config import get_default_data_normalization_profile


def test_normalize_news_topic_and_tag():
    assert normalize_news_topic_value("central bank") == "CENTRAL_BANK"
    assert normalize_news_topic_value("inflation") == "INFLATION"
    assert normalize_news_tag_value("crude oil") == "CRUDE_OIL"
    assert normalize_news_tag_value("risk sentiment") == "RISK_SENTIMENT"


def test_normalize_news_tags_dataframe():
    raw_df = pd.DataFrame([{"tags": "central bank"}, {"tags": "inflation"}])
    norm_df, findings = normalize_news_tags_dataframe(raw_df, fields=["tags"])

    assert "normalized_tags" in norm_df.columns
    assert norm_df["normalized_tags"].iloc[0] == "CENTRAL_BANK"
    assert norm_df["normalized_tags"].iloc[1] == "INFLATION"


def test_news_topic_tag_report():
    prof = get_default_data_normalization_profile()
    df, summary = build_news_topic_tag_normalization_enforcement_report(prof)
    assert not df.empty
    assert summary["total_mappings"] >= 5
