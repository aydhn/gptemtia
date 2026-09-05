from advanced_data_lineage.data_lineage_config import get_default_data_lineage_profile
from advanced_data_lineage.lineage_findings import (
    build_lineage_finding_registry,
    create_lineage_finding,
    summarize_lineage_findings,
)


def test_lineage_findings():
    profile = get_default_data_lineage_profile()
    df, summary = build_lineage_finding_registry(profile)
    assert len(df) >= 3
    assert summary["manual_review_count"] >= 1
    assert "missing_quote_diagnostic" in summary["finding_types"]

    f = create_lineage_finding("type1", "fx", "prov1", "src1", message="test msg")
    assert f.finding_type == "type1"
    assert f.message == "test msg"
