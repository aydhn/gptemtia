"""Unit tests for Phase 119 comprehensive validation report."""

import pytest
from advanced_cross_asset_alignment.cross_asset_alignment_validation import (
    build_cross_asset_alignment_validation_report,
    summarize_cross_asset_alignment_validation,
)


def test_validation_report():
    df, summary = build_cross_asset_alignment_validation_report()
    assert len(df) >= 5
    assert summary["all_passed"] is True
    assert summary["failed_checks"] == 0
    assert summary["validation_status"] == "PASS"
