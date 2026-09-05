from advanced_data_lineage.data_lineage_config import get_default_data_lineage_profile
from advanced_data_lineage.metadata_only_provenance import (
    build_metadata_only_provenance_registry,
    summarize_metadata_only_provenance,
)


def test_metadata_only_provenance():
    profile = get_default_data_lineage_profile()
    df, summary = build_metadata_only_provenance_registry(profile)
    assert len(df) >= 3
    assert summary["all_metadata_only"] is True
    assert summary["all_scraping_prohibited"] is True
