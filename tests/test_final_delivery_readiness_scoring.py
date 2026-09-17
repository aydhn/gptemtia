# -*- coding: utf-8 -*-
"""Unit tests for Phase 160: final_delivery_readiness_scoring."""

from advanced_final_delivery.final_delivery_readiness_scoring import build_final_delivery_readiness_score_report


def test_build_final_delivery_readiness_score_report():
    df, summary = build_final_delivery_readiness_score_report()
    assert not df.empty
    assert isinstance(summary, dict)
    assert 'status' in summary
