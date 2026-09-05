from advanced_data_lineage.data_lineage_config import get_default_data_lineage_profile
from advanced_data_lineage.provenance_source_registry import (
    build_provenance_source_registry,
    build_default_provenance_sources,
)


def test_provenance_sources():
    profile = get_default_data_lineage_profile()
    sources = build_default_provenance_sources(profile)
    assert len(sources) >= 8

    df, summary = build_provenance_source_registry(profile)
    assert len(df) >= 8
    assert summary["all_no_scraping"] is True
    assert "fx_dry_run_fixture_source" in summary["source_names"]
