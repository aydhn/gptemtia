from advanced_data_lineage.data_lineage_config import get_default_data_lineage_profile
from advanced_data_lineage.source_reference_registry import (
    build_source_reference_registry,
    build_default_source_references,
)


def test_source_references():
    profile = get_default_data_lineage_profile()
    refs = build_default_source_references(profile)
    assert len(refs) >= 8

    df, summary = build_source_reference_registry(profile)
    assert len(df) >= 8
    assert summary["zero_credentials"] is True
    assert summary["zero_full_text"] is True
