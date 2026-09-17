# -*- coding: utf-8 -*-
"""Unit tests for Advanced ML Acceptance Health Check."""

from pathlib import Path
import pytest
from advanced_ml_acceptance.advanced_ml_acceptance_health import (
    build_advanced_ml_acceptance_health_check,
    summarize_advanced_ml_acceptance_health,
)


def test_health_check():
    df, summary = build_advanced_ml_acceptance_health_check(Path("."))
    assert not df.empty
    assert summary["all_healthy"] is True
    assert summary["status"] == "HEALTHY"

    s = summarize_advanced_ml_acceptance_health(df)
    assert s["all_healthy"] is True
    assert s["non_signal"] is True
