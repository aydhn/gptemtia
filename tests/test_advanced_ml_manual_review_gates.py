# -*- coding: utf-8 -*-
"""Unit tests for Advanced ML Manual Review Gates."""

import pytest
from advanced_ml_acceptance.advanced_ml_manual_review_gates import (
    build_advanced_ml_manual_review_gate_registry,
    summarize_advanced_ml_manual_review_gates,
)


def test_manual_review_gates():
    df, summary = build_advanced_ml_manual_review_gate_registry()
    assert not df.empty
    assert len(df) == 10
    assert summary["manual_review_required"] is True
    assert summary["non_signal"] is True
    assert summary["status"] == "QUEUED"

    s = summarize_advanced_ml_manual_review_gates(df)
    assert s["gate_count"] == 10
    assert s["manual_review_required"] is True
