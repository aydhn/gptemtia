from advanced_data_lineage.data_lineage_config import get_default_data_lineage_profile
from advanced_data_lineage.cross_domain_provenance_map import (
    build_cross_domain_provenance_map,
    summarize_cross_domain_provenance_map,
)


def test_cross_domain_provenance_map():
    profile = get_default_data_lineage_profile()
    df, summary = build_cross_domain_provenance_map(profile)
    assert len(df) >= 5
    assert summary["all_source_preserved"] is True
    assert "fx_to_news" in summary["domain_pairs"]
    assert "macro_to_calendar" in summary["domain_pairs"]
