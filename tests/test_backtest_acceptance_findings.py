import pytest
import pandas as pd
from advanced_backtest_acceptance.backtest_acceptance_findings import (
    build_backtest_acceptance_findings_registry,
    create_backtest_acceptance_finding,
    FORBIDDEN_REMEDIATION_PHRASES,
)

def test_backtest_acceptance_findings():
    df, summary = build_backtest_acceptance_findings_registry()
    assert isinstance(df, pd.DataFrame)
    assert isinstance(summary, dict)
    assert len(df) == 1
    assert summary["total_findings"] == 1
    assert summary["critical_count"] == 0
    assert summary["status"] == "ACCEPTED"
    assert summary["non_signal"] is True

    # Invariants
    assert (df["non_signal"] == True).all()
    assert (df["non_production"] == True).all()
    assert (df["local_only"] == True).all()

    # Factory valid test
    f = create_backtest_acceptance_finding(
        finding_type="audit_note",
        phase_ref="Phase 152",
        severity_label="INFO",
        message="Audit completed",
        recommendation="Maintain offline policy and document review.",
    )
    assert f.finding_type == "audit_note"
    assert f.manual_review_required is True
    assert f.non_signal is True

    # Factory invalid remediation tests
    for forbidden in ["auto-run backtest", "auto-approve strategy", "auto-allocate capital", "auto-send broker order", "auto-deploy"]:
        with pytest.raises(ValueError, match="Prohibited remediation proposal detected"):
            create_backtest_acceptance_finding(
                finding_type="violation_attempt",
                phase_ref="Phase 152",
                severity_label="CRITICAL",
                message="Bad recommendation attempt",
                recommendation=f"We should {forbidden} now",
            )
