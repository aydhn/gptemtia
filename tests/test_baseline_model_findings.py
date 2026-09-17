# -*- coding: utf-8 -*-
"""Unit tests for baseline model findings."""

import pytest
import pandas as pd
from advanced_baseline_ml_models.baseline_model_findings import (
    FINDING_TYPES,
    create_baseline_model_finding,
    build_baseline_model_findings_registry,
    summarize_baseline_model_findings,
)


def test_create_baseline_model_finding():
    finding = create_baseline_model_finding(
        finding_type="real_training_request_blocked",
        model_domain="baseline_ml_models",
        severity_label="CRITICAL",
        message="Real training request blocked by policy",
        recommendation="Use contract-only dry-run harness",
    )
    assert finding.finding_id.startswith("finding_")
    assert finding.finding_type == "real_training_request_blocked"
    assert finding.severity_label == "CRITICAL"
    assert finding.manual_review_required is True
    assert finding.blocking_status is True


def test_build_baseline_model_findings_registry_clean():
    df, summary = build_baseline_model_findings_registry()
    assert isinstance(df, pd.DataFrame)
    assert len(df) == 0
    assert summary["total_findings"] == 0
    assert summary["critical_blockers"] == 0
    assert summary["clean_baseline_contracts"] is True
    assert summary["non_signal"] is True
    assert summary["production_ready"] is False
    assert summary["broker_ready"] is False


def test_summarize_baseline_model_findings_with_rows():
    df = pd.DataFrame([
        {
            "finding_id": "f1",
            "finding_type": "test",
            "model_domain": "dom",
            "severity_label": "CRITICAL",
            "message": "msg",
            "recommendation": "rec",
            "manual_review_required": True,
            "blocking_status": True,
            "created_at": "2026-09-13T00:00:00Z",
        }
    ])
    summary = summarize_baseline_model_findings(df)
    assert summary["total_findings"] == 1
    assert summary["critical_blockers"] == 1
    assert summary["clean_baseline_contracts"] is False
