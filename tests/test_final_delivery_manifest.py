# -*- coding: utf-8 -*-
"""Unit tests for Phase 160: final_delivery_manifest."""

from advanced_final_delivery.final_delivery_manifest import build_final_delivery_manifest


def test_build_final_delivery_manifest():
    df, summary = build_final_delivery_manifest()
    assert not df.empty
    assert isinstance(summary, dict)
    assert 'status' in summary
