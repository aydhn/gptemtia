# -*- coding: utf-8 -*-
"""Unit tests for Phase 154 Findings, Readiness Score and Master Manifest."""

from advanced_portfolio_optimization.portfolio_optimization_config import (
    get_default_portfolio_optimization_profile,
)
from advanced_portfolio_optimization.portfolio_optimization_findings import (
    build_portfolio_optimization_findings_registry,
)
from advanced_portfolio_optimization.portfolio_optimization_readiness_scoring import (
    build_portfolio_optimization_readiness_score_report,
    calculate_portfolio_optimization_readiness_score,
)
from advanced_portfolio_optimization.portfolio_optimization_manifest import (
    build_portfolio_optimization_manifest,
)


def test_findings_registry():
    profile = get_default_portfolio_optimization_profile()
    df, summary = build_portfolio_optimization_findings_registry(profile)
    assert not df.empty
    assert summary["blocker_count"] == 0
    assert summary["finding_count"] == 3


def test_readiness_scoring():
    profile = get_default_portfolio_optimization_profile()
    df, summary = build_portfolio_optimization_readiness_score_report(profile)
    assert not df.empty
    assert summary["readiness_score"] >= 0.75
    assert summary["is_contract_ready"] is True
    assert summary["classification"] == "portfolio_optimization_contract_ready_non_production"


def test_master_manifest():
    profile = get_default_portfolio_optimization_profile()
    df, summary = build_portfolio_optimization_manifest(profile)
    assert not df.empty
    assert summary["current_phase"] == 154
    assert summary["next_phase"] == 155
    assert summary["target_final_phase"] == 160
    assert summary["portfolio_optimized"] is False
    assert summary["portfolio_weights_generated"] is False
    assert summary["allocation_generated"] is False
    assert summary["rebalance_generated"] is False
    assert summary["phase_155_handoff_ready"] is True
