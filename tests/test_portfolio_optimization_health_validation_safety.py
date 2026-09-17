# -*- coding: utf-8 -*-
"""Unit tests for Phase 154 Health, Validation and Safety Boundaries."""

from pathlib import Path
import pandas as pd

from advanced_portfolio_optimization.portfolio_optimization_config import (
    get_default_portfolio_optimization_profile,
)
from advanced_portfolio_optimization.portfolio_optimization_health import (
    build_portfolio_optimization_health_check,
)
from advanced_portfolio_optimization.portfolio_optimization_validation import (
    build_portfolio_optimization_validation_report,
)
from advanced_portfolio_optimization.portfolio_optimization_safety_boundary import (
    build_portfolio_optimization_safety_boundary,
)


def test_health_check():
    profile = get_default_portfolio_optimization_profile()
    project_root = Path(__file__).resolve().parents[1]
    df, summary = build_portfolio_optimization_health_check(project_root, profile)
    assert not df.empty
    assert summary["all_healthy"] is True
    assert summary["healthy_count"] == 19


def test_validation_report():
    profile = get_default_portfolio_optimization_profile()
    tables = {
        "profiles": pd.DataFrame([{"current_phase": 154, "allow_live_trading": False, "allow_portfolio_optimization": False}]),
        "contracts": pd.DataFrame([{"portfolio_optimization_allowed": False, "weight_generation_allowed": False, "live_trading_allowed": False}]),
        "objectives": pd.DataFrame([{"is_placeholder": True, "is_calculated": False}]),
        "constraints": pd.DataFrame([{"is_placeholder": True, "is_enforced_live": False}]),
        "manifest": pd.DataFrame([{"current_phase": 154, "portfolio_optimized": False, "portfolio_weights_generated": False, "allocation_generated": False, "rebalance_generated": False, "phase_155_handoff_ready": True}]),
        "summary": {"test": "valid"},
    }
    df, summary = build_portfolio_optimization_validation_report(tables, profile)
    assert not df.empty
    assert summary["all_checks_passed"] is True


def test_safety_boundary():
    profile = get_default_portfolio_optimization_profile()
    df, summary = build_portfolio_optimization_safety_boundary(profile)
    assert not df.empty
    assert summary["no_go_count"] >= 15
    assert summary["safe_go_count"] >= 8
