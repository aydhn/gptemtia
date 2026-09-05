from advanced_data_lineage.data_lineage_config import get_default_data_lineage_profile
from advanced_data_lineage.transformation_provenance_registry import (
    build_transformation_provenance_registry,
    build_default_transformation_provenance_records,
)


def test_transformation_provenance():
    profile = get_default_data_lineage_profile()
    records = build_default_transformation_provenance_records(profile)
    assert len(records) >= 8

    df, summary = build_transformation_provenance_registry(profile)
    assert len(df) >= 8
    assert summary["all_source_preserved"] is True
    assert summary["zero_destructive_actions"] is True
