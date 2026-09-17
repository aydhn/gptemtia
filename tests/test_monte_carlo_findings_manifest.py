# -*- coding: utf-8 -*-
"""Phase 149 Unit Tests: Monte Carlo Findings, Scoring, and Manifest."""

from advanced_monte_carlo_robustness.monte_carlo_config import get_default_monte_carlo_profile
from advanced_monte_carlo_robustness.monte_carlo_manual_review import (
    build_monte_carlo_manual_review_queue,
)
from advanced_monte_carlo_robustness.monte_carlo_findings import (
    build_monte_carlo_findings_registry,
)
from advanced_monte_carlo_robustness.monte_carlo_readiness_scoring import (
    build_monte_carlo_readiness_score_report,
    classify_monte_carlo_readiness_score,
)
from advanced_monte_carlo_robustness.monte_carlo_manifest import (
    build_monte_carlo_robustness_manifest,
)


def test_manual_review_queue():
    profile = get_default_monte_carlo_profile()
    df, summary = build_monte_carlo_manual_review_queue(profile)
    assert not df.empty
    assert summary["total_review_items"] >= 4
    assert summary["pending_review_count"] >= 4


def test_findings_registry():
    profile = get_default_monte_carlo_profile()
    df, summary = build_monte_carlo_findings_registry(profile)
    assert not df.empty
    assert summary["total_findings"] >= 3
    assert summary["critical_count"] == 0


def test_readiness_scoring():
    profile = get_default_monte_carlo_profile()
    df, summary = build_monte_carlo_readiness_score_report(profile)
    assert not df.empty
    assert summary["score"] >= 0.75
    assert summary["meets_threshold"] is True
    assert summary["manual_review_required"] is True

    assert classify_monte_carlo_readiness_score(0.1) == "blocked"
    assert classify_monte_carlo_readiness_score(0.4) == "incomplete"
    assert classify_monte_carlo_readiness_score(0.6) == "contract_ready_with_manual_review"
    assert classify_monte_carlo_readiness_score(0.9) == "monte_carlo_robustness_contract_ready_non_production"


def test_monte_carlo_manifest():
    profile = get_default_monte_carlo_profile()
    df, summary = build_monte_carlo_robustness_manifest(profile)
    assert not df.empty
    assert summary["current_phase"] == 149
    assert summary["target_final_phase"] == 160
    assert summary["next_phase"] == 150
    assert summary["all_negative_invariants_satisfied"] is True
    assert summary["phase_150_handoff_ready"] is True
