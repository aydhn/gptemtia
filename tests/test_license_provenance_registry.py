from advanced_data_lineage.data_lineage_config import get_default_data_lineage_profile
from advanced_data_lineage.license_provenance_registry import (
    build_license_provenance_registry,
    summarize_license_provenance_registry,
)


def test_license_provenance():
    profile = get_default_data_lineage_profile()
    df, summary = build_license_provenance_registry(profile)
    assert len(df) >= 5
    assert summary["zero_unrestricted_redistribution"] is True
    assert summary["manual_review_count"] >= 1
