"""Unit tests for Phase 119 system health check."""

import pytest
from pathlib import Path
from advanced_cross_asset_alignment.cross_asset_alignment_health import (
    build_cross_asset_alignment_health_check,
    summarize_cross_asset_alignment_health,
)


def test_cross_asset_alignment_health():
    project_root = Path(__file__).resolve().parent.parent
    df, summary = build_cross_asset_alignment_health_check(project_root)

    assert len(df) >= 30
    assert summary["health_status"] == "HEALTHY"
    assert summary["all_healthy"] is True
    assert summary["unhealthy_components"] == 0
    assert summary["prior_phases_healthy"] is True
