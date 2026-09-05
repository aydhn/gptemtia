import pytest
import pandas as pd
from advanced_news_metadata.news_provider_config import get_default_news_provider_profile
from advanced_news_metadata.news_scoring import (
    calculate_news_readiness_score,
    classify_news_readiness_score,
    build_news_readiness_score_report
)

def test_news_scoring():
    profile = get_default_news_provider_profile()
    df_sample = pd.DataFrame([{"a": 1}])
    health_df = pd.DataFrame([{"component": "c1", "status": "pass"}])
    score = calculate_news_readiness_score(
        df_sample, df_sample, df_sample, df_sample,
        df_sample, df_sample, df_sample, health_df, profile
    )
    assert 0.0 <= score <= 1.0
    cls = classify_news_readiness_score(score, profile)
    assert cls in ["HIGH", "MEDIUM", "LOW"]
