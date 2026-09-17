# -*- coding: utf-8 -*-
"""Unit tests for Phase 157 Portfolio Acceptance Models."""

import pytest
from advanced_portfolio_acceptance.portfolio_acceptance_models import (
    PortfolioAcceptanceProfileItem,
    PortfolioAcceptanceComponentItem,
    PortfolioAcceptanceCheckpoint,
    PortfolioPhaseAcceptanceItem,
    PortfolioValidationEvidenceItem,
    PortfolioAcceptanceBoundaryItem,
    PortfolioAcceptanceFinding,
    PortfolioAcceptanceReadinessScore,
    PortfolioAcceptanceManifest,
    PortfolioAcceptanceManualReviewItem,
)


def test_models_instantiation():
    prof = PortfolioAcceptanceProfileItem(
        profile_name="test_profile",
        description="test description",
    )
    assert prof.current_phase == 157
    assert prof.target_final_phase == 160
    assert prof.next_phase == 158
    assert prof.production_ready is False
    assert prof.broker_ready is False

    chk = PortfolioAcceptanceCheckpoint(
        checkpoint_id="CHK-TEST",
        component_name="test_component",
        expected_module="test_module",
    )
    assert chk.contract_only is True
    assert chk.production_ready is False

    score = PortfolioAcceptanceReadinessScore(
        overall_score=0.95,
        classification="contract_ready",
        meets_threshold=True,
        total_checks=10,
        passed_checks=10,
        warning_count=0,
        blocker_count=0,
    )
    assert score.overall_score == 0.95
    assert score.production_ready is False

    with pytest.raises(ValueError):
        PortfolioAcceptanceReadinessScore(
            overall_score=1.5,
            classification="invalid",
            meets_threshold=True,
            total_checks=10,
            passed_checks=10,
            warning_count=0,
            blocker_count=0,
        )

    mnf = PortfolioAcceptanceManifest(manifest_id="MNF-TEST")
    assert mnf.portfolio_block_completed is True
    assert mnf.portfolio_constructed is False
    assert mnf.portfolio_optimized is False
    assert mnf.risk_report_generated is False
    assert mnf.scenario_executed is False
    assert mnf.drawdown_control_executed is False
    assert mnf.broker_ready is False
    assert mnf.production_ready is False
