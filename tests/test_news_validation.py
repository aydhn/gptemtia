import pytest
import pandas as pd
from advanced_news_metadata.news_provider_config import get_default_news_provider_profile
from advanced_news_metadata.news_validation import (
    validate_news_provider_profile_registry,
    validate_news_metadata_schema,
    validate_news_safety_boundary,
    validate_no_forbidden_news_claims,
    build_news_validation_report
)

def test_news_validation():
    profile = get_default_news_provider_profile()
    df_sample = pd.DataFrame([{"metadata_only": True, "field_name": "metadata_only"}])
    res = validate_news_metadata_schema(df_sample, profile)
    assert res["valid"] is True

    claim_res = validate_no_forbidden_news_claims("Bu rapor araştırma amaçlıdır ve yatırım tavsiyesi değildir.")
    assert claim_res["valid"] is True

    claim_bad = validate_no_forbidden_news_claims("Kesin AL tavsiyesidir ve live trading approved")
    assert claim_bad["valid"] is False
