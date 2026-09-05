import pytest
import pandas as pd
from advanced_data_quality.data_quality_config import get_default_data_quality_profile
from advanced_data_quality.news_metadata_quality_rules import (
    build_news_metadata_quality_rule_set,
    check_news_metadata_quality,
    check_news_item_reference_quality,
)


def test_news_metadata_quality_rules():
    profile = get_default_data_quality_profile()
    df_rules, _ = build_news_metadata_quality_rule_set(profile)
    assert len(df_rules) >= 2

    # News metadata with forbidden full text
    bad_news = pd.DataFrame([
        {"item_id": "1", "timestamp": "2026-09-01", "source_name": "src", "title_or_summary_ref": "ref", "full_text": "article body..."}
    ])
    findings = check_news_metadata_quality(bad_news, "news_test_prov")
    assert any(f.finding_type == "finding_news_copyright_boundary" for f in findings)
    assert any(f.severity_label == "quality_critical" for f in findings)

    # Sentiment as signal breach
    signal_news = pd.DataFrame([{"sentiment_as_signal": True}])
    f_sig = check_news_item_reference_quality(signal_news, "news_test_prov")
    assert any(f.severity_label == "quality_critical" for f in f_sig)
