# -*- coding: utf-8 -*-
"""Unit tests for Phase 148: Domain Registry, Scope Registry, and Models."""

from dataclasses import asdict
import pytest
from advanced_stress_testing.stress_testing_config import (
    get_default_stress_testing_profile,
)
from advanced_stress_testing.stress_testing_domain_registry import (
    build_stress_testing_domain_registry,
    DOMAIN_DESCRIPTIONS,
)
from advanced_stress_testing.stress_testing_scope_registry import (
    build_stress_testing_scope_registry,
    SCOPE_ITEMS,
)
from advanced_stress_testing.stress_testing_models import (
    StressScenarioContract,
    ShockScenarioPlaceholder,
    StressMetricPlaceholder,
    StressGuardItem,
    StressDisabledExecutionItem,
    StressFinding,
    StressReadinessScore,
    StressTestingManifest,
    StressManualReviewItem,
)
from advanced_stress_testing.stress_testing_labels import (
    STRESS_CONTRACT_READY,
    EXECUTION_CONTRACT_ONLY,
    DOMAIN_LABELS,
)


def test_domain_registry():
    prof = get_default_stress_testing_profile()
    df, summary = build_stress_testing_domain_registry(prof)
    assert not df.empty
    assert len(df) == len(DOMAIN_LABELS)
    assert summary["total_domains"] == len(df)
    assert summary["all_non_signal"] is True
    assert summary["all_local_only"] is True
    assert summary["all_non_production"] is True
    assert "stress_scenario_contract_domain" in df["domain_name"].values


def test_scope_registry():
    prof = get_default_stress_testing_profile()
    df, summary = build_stress_testing_scope_registry(prof)
    assert not df.empty
    assert len(df) == len(SCOPE_ITEMS)
    assert summary["total_scope_items"] == len(df)
    assert summary["all_enforced"] is True
    assert summary["non_signal"] is True
    assert "no_live_trading" in df["scope_name"].values


def test_models_and_invariants():
    sc = StressScenarioContract(
        contract_name="gfc_2008_historical_stress",
        scenario_family="historical_crisis",
        description="2008 Global Financial Crisis stress scenario",
        realistic_backtest_ref="phase_146_realistic_backtest",
        walk_forward_ref="phase_147_walk_forward",
        transaction_cost_ref="phase_146_transaction_cost_models",
        slippage_model_ref="phase_146_slippage_models",
        regime_context_ref="phase_135_regime_classification",
        no_lookahead_guard_ref="phase_148_no_lookahead_guard",
        scenario_leakage_guard_ref="phase_148_scenario_leakage_guard",
    )
    d = asdict(sc)
    assert d["contract_name"] == "gfc_2008_historical_stress"
    assert d["stress_execution_allowed"] is False
    assert d["non_signal"] is True

    # Test negative invariant in post-init
    with pytest.raises(ValueError, match="stress_execution_allowed"):
        StressScenarioContract(
            contract_name="bad_contract",
            scenario_family="bad",
            description="bad",
            realistic_backtest_ref="ref",
            walk_forward_ref="ref",
            transaction_cost_ref="ref",
            slippage_model_ref="ref",
            regime_context_ref="ref",
            no_lookahead_guard_ref="ref",
            scenario_leakage_guard_ref="ref",
            stress_execution_allowed=True,
        )

    sh = ShockScenarioPlaceholder(
        placeholder_name="market_crash_shock",
        shock_type="market_shock",
        description="Simulated market plunge",
        magnitude_spec="-20% across risk assets",
    )
    assert asdict(sh)["real_execution_allowed"] is False

    with pytest.raises(ValueError, match="real_execution_allowed"):
        ShockScenarioPlaceholder(
            placeholder_name="bad_shock",
            shock_type="market_shock",
            description="bad",
            magnitude_spec="-20%",
            real_execution_allowed=True,
        )

    mp = StressMetricPlaceholder(
        metric_name="stressed_pnl",
        metric_category="pnl",
        description="Simulated PnL under stress",
        formula_spec="portfolio_value * shock_pct",
    )
    assert asdict(mp)["metric_calculated"] is False

    with pytest.raises(ValueError, match="metric_calculated"):
        StressMetricPlaceholder(
            metric_name="bad_metric",
            metric_category="pnl",
            description="bad",
            formula_spec="x",
            metric_calculated=True,
        )

    score = StressReadinessScore(
        score=1.0,
        classification="READY_FOR_PHASE_149_MONTE_CARLO_ROBUSTNESS_HANDOFF",
        total_findings=3,
        critical_blockers=0,
        meets_threshold=True,
    )
    assert score.score == 1.0

    with pytest.raises(ValueError, match="Readiness score"):
        StressReadinessScore(
            score=1.5,
            classification="BAD",
            total_findings=0,
            critical_blockers=0,
            meets_threshold=False,
        )


def test_labels():
    assert STRESS_CONTRACT_READY == "stress_contract_ready"
    assert EXECUTION_CONTRACT_ONLY == "execution_contract_only"
    assert len(DOMAIN_LABELS) >= 30
