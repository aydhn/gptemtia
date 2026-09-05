from advanced_data_lineage.data_lineage_config import get_default_data_lineage_profile
from advanced_data_lineage.provider_provenance_registry import (
    build_provider_provenance_registry,
    build_default_provider_provenance_records,
)


def test_provider_provenance():
    profile = get_default_data_lineage_profile()
    records = build_default_provider_provenance_records(profile)
    assert len(records) >= 8

    df, summary = build_provider_provenance_registry(profile)
    assert len(df) >= 8
    assert summary["high_confidence_count"] >= 5
