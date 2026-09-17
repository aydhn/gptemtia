# -*- coding: utf-8 -*-
"""Unit tests for Phase 140 Ensemble Findings."""

from advanced_ensemble_model_registry.ensemble_findings import (
    build_ensemble_findings,
    validate_ensemble_findings,
    summarize_ensemble_findings,
)


def test_ensemble_findings():
    findings = build_ensemble_findings()
    assert len(findings) == 3
    assert validate_ensemble_findings(findings) is True

    summary = summarize_ensemble_findings(findings)
    assert summary["total_findings"] == 3
    assert summary["all_auto_fix_prohibited"] is True
    assert summary["all_non_signal"] is True
