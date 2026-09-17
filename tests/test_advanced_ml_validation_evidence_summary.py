# -*- coding: utf-8 -*-
"""Unit tests for Advanced ML Validation Evidence Summary."""

import pytest
from advanced_ml_acceptance.advanced_ml_validation_evidence_summary import (
    build_advanced_ml_validation_evidence_summary_registry,
    summarize_advanced_ml_validation_evidence_summary,
)


def test_validation_evidence_summary():
    df, summary = build_advanced_ml_validation_evidence_summary_registry()
    assert not df.empty
    assert len(df) >= 10
    assert summary["all_verified"] is True
    assert summary["non_signal"] is True
    assert summary["status"] == "VERIFIED"

    s = summarize_advanced_ml_validation_evidence_summary(df)
    assert s["evidence_count"] >= 10
    assert s["all_verified"] is True
