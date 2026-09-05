from advanced_data_lineage.data_lineage_config import get_default_data_lineage_profile
from advanced_data_lineage.transformation_audit_trail import (
    build_transformation_audit_trail_registry,
    summarize_transformation_audit_trail,
)


def test_transformation_audit_trail():
    profile = get_default_data_lineage_profile()
    df, summary = build_transformation_audit_trail_registry(profile)
    assert len(df) >= 5
    assert summary["all_source_preserved"] is True
    assert summary["zero_destructive_actions"] is True
    assert "fx_symbol_slashing" in summary["transformation_rules"]
