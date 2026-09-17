# -*- coding: utf-8 -*-
"""Unit tests for Phase 160: final_delivery_source_overwrite_disabled."""

from advanced_final_delivery.final_delivery_source_overwrite_disabled import build_final_delivery_source_overwrite_disabled_report


def test_build_final_delivery_source_overwrite_disabled_report():
    df, summary = build_final_delivery_source_overwrite_disabled_report()
    assert not df.empty
    assert isinstance(summary, dict)
    assert 'status' in summary
