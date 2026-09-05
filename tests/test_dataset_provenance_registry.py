from advanced_data_lineage.data_lineage_config import get_default_data_lineage_profile
from advanced_data_lineage.dataset_provenance_registry import (
    build_dataset_provenance_registry,
    build_default_dataset_provenance_records,
)


def test_dataset_provenance():
    profile = get_default_data_lineage_profile()
    records = build_default_dataset_provenance_records(profile)
    assert len(records) >= 8

    df, summary = build_dataset_provenance_registry(profile)
    assert len(df) >= 8
    assert summary["all_source_preserved"] is True
