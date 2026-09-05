from advanced_data_normalization.cross_domain_mapping_report import (
    build_cross_domain_normalized_mapping_report,
    summarize_cross_domain_normalized_mapping,
)
from advanced_data_normalization.data_normalization_config import get_default_data_normalization_profile


def test_cross_domain_mapping():
    prof = get_default_data_normalization_profile()
    df, summary = build_cross_domain_normalized_mapping_report(prof)
    assert not df.empty
    assert summary["total_mappings"] >= 5
    domains = df["mapping_domain"].tolist()
    assert "fx_to_news_tag" in domains
    assert "commodity_to_news_tag" in domains
