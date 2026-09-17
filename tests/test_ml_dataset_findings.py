"""Test suite for Phase 137 ML Dataset Findings Registry."""

import pytest
from advanced_ml_dataset_registry.ml_dataset_findings import (
    build_ml_dataset_findings_registry,
    create_ml_dataset_finding,
    summarize_ml_dataset_findings,
)


def test_build_findings():
    df, summary = build_ml_dataset_findings_registry()
    assert not df.empty
    assert summary["total_findings"] >= 5
    assert summary["auto_fix_allowed"] is False
    assert summary["non_signal"] is True


def test_create_finding():
    finding = create_ml_dataset_finding(
        finding_type="missing_dataset_contract",
        dataset_domain="dataset_contract_domain",
        severity_label="WARNING",
        message="Test finding message",
        recommendation="Inspect manually",
    )
    assert finding.finding_id.startswith("FIND-")
    assert finding.auto_fix_forbidden is True
    assert finding.non_signal is True
