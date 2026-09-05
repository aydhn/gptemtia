from advanced_data_lineage.data_lineage_config import get_default_data_lineage_profile
from advanced_data_lineage.schema_provenance_registry import (
    build_schema_provenance_registry,
    build_default_schema_provenance_records,
)


def test_schema_provenance():
    profile = get_default_data_lineage_profile()
    records = build_default_schema_provenance_records(profile)
    assert len(records) >= 8

    df, summary = build_schema_provenance_registry(profile)
    assert len(df) >= 8
    assert "fx_quote_schema" in summary["schema_names"]
