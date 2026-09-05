import pytest
import pandas as pd
from advanced_news_metadata.news_provider_config import get_default_news_provider_profile
from advanced_news_metadata.news_quality import (
    check_news_provider_profile_quality,
    check_news_metadata_schema_quality,
    check_for_forbidden_terms_in_news_layer,
    build_news_quality_report
)

def test_news_quality():
    profile = get_default_news_provider_profile()
    df_sample = pd.DataFrame([{"a": 1}])
    q_prof = check_news_provider_profile_quality(df_sample, profile)
    assert q_prof["quality_score"] == 1.0

    rep = build_news_quality_report({"test": "ok"})
    assert rep["status"] == "pass"

    terms_check = check_for_forbidden_terms_in_news_layer("Bu rapor bilgilendirme amaçlıdır.")
    assert terms_check["valid"] is True
