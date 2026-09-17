# -*- coding: utf-8 -*-
"""Unit tests for Phase 160: final_delivery_release_candidate_evidence."""

from advanced_final_delivery.final_delivery_release_candidate_evidence import build_final_delivery_release_candidate_evidence_registry


def test_build_final_delivery_release_candidate_evidence_registry():
    df, summary = build_final_delivery_release_candidate_evidence_registry()
    assert not df.empty
    assert isinstance(summary, dict)
    assert 'status' in summary
