import pytest
from advanced_feature_validation.feature_validation_findings import (
    clear_findings,
    create_finding,
    get_all_findings,
    get_findings_summary,
)


def test_feature_validation_findings():
    clear_findings()
    assert len(get_all_findings()) == 0

    f1 = create_finding(
        rule_id="RULE-VAL-001",
        column_name="col_x",
        severity="CRITICAL",
        finding_type="FORBIDDEN_COLUMN",
        message="Forbidden column present",
    )
    assert f1.finding_id.startswith("FIND-")
    assert len(get_all_findings()) == 1

    summary = get_findings_summary()
    assert summary["total_findings"] == 1
    assert summary["critical"] == 1
    assert summary["high"] == 0
