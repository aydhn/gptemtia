# -*- coding: utf-8 -*-
"""Unit tests for Phase 145: Advanced ML Acceptance Domain Registry."""

import pytest
from advanced_ml_acceptance.advanced_ml_acceptance_domain_registry import (
    build_advanced_ml_acceptance_domain_registry,
    summarize_advanced_ml_acceptance_domains,
)


def test_build_domain_registry():
    df, summary = build_advanced_ml_acceptance_domain_registry()
    assert not df.empty
    assert len(df) >= 25
    assert summary["current_phase"] == 145
    assert summary["target_final_phase"] == 160
    assert summary["next_phase"] == 146
    assert summary["non_signal"] is True

    s = summarize_advanced_ml_acceptance_domains(df)
    assert s["domain_count"] >= 25
    assert s["non_signal"] is True
