# -*- coding: utf-8 -*-
"""Unit tests for Advanced ML Findings Registry."""

import pytest
from advanced_ml_acceptance.advanced_ml_findings import (
    build_advanced_ml_findings_registry,
    create_advanced_ml_finding,
    summarize_advanced_ml_findings,
)


def test_findings_registry():
    df, summary = build_advanced_ml_findings_registry()
    assert not df.empty
    assert summary["total_findings"] >= 3
    assert summary["non_signal"] is True

    s = summarize_advanced_ml_findings(df)
    assert s["finding_count"] >= 3


def test_forbidden_recommendations_rejected():
    with pytest.raises(ValueError):
        create_advanced_ml_finding(
            finding_type="illegal_rec",
            phase_ref="Phase 145",
            severity_label="CRITICAL",
            message="Test msg",
            recommendation="approve production immediately",
        )

    with pytest.raises(ValueError):
        create_advanced_ml_finding(
            finding_type="illegal_rec",
            phase_ref="Phase 145",
            severity_label="CRITICAL",
            message="Test msg",
            recommendation="auto-deploy model to server",
        )

    with pytest.raises(ValueError):
        create_advanced_ml_finding(
            finding_type="illegal_rec",
            phase_ref="Phase 145",
            severity_label="CRITICAL",
            message="Test msg",
            recommendation="auto-generate signal for user",
        )
