# -*- coding: utf-8 -*-
"""Unit tests for Phase 155 Risk Reporting Models."""

from advanced_risk_reporting.risk_reporting_models import (
    RiskReportingProfileItem,
    RiskReportContract,
    ExposureAttributionContract,
    LimitMonitoringContract,
    RiskMetricPlaceholder,
    ExposurePlaceholder,
    LimitMonitoringPlaceholder,
    RiskReportingGuardItem,
    RiskReportingDisabledExecutionItem,
    RiskReportingFinding,
    RiskReportingReadinessScore,
    RiskReportingManifest,
    RiskReportingManualReviewItem,
)


def test_risk_report_contract_model():
    model = RiskReportContract(
        contract_name="Test Risk Contract",
        report_family="risk_summary",
        portfolio_construction_ref="DEP-PC-153",
        portfolio_optimization_ref="DEP-PO-154",
        backtest_acceptance_ref="DEP-BA-152",
        model_governance_ref="DEP-MG-144",
        regime_context_ref="DEP-RG-135",
        featurestore_ref="DEP-FS-125",
        no_lookahead_guard_ref="GRD-NL-001",
        investment_advice_guard_ref="GRD-IA-001",
    )
    assert model.contract_name == "Test Risk Contract"
    assert model.risk_reporting_execution_allowed is False
    assert model.live_trading_allowed is False
    assert model.manual_review_required is True


def test_exposure_attribution_contract_model():
    model = ExposureAttributionContract(
        contract_name="Test Exposure Contract",
        exposure_family="gross_exposure",
        description="Gross exposure description",
        mathematical_formulation="sum(|w_i|)",
    )
    assert model.contract_name == "Test Exposure Contract"
    assert model.is_placeholder is True
    assert model.exposure_calculated is False
    assert model.allows_execution is False


def test_limit_monitoring_contract_model():
    model = LimitMonitoringContract(
        contract_name="Test Limit Contract",
        limit_family="drawdown_limit",
        description="Drawdown limit description",
        limit_type="hard_limit",
        threshold_metadata="threshold=0.15",
    )
    assert model.contract_name == "Test Limit Contract"
    assert model.is_placeholder is True
    assert model.is_enforced_live is False
    assert model.allows_alerting is False


def test_risk_reporting_manifest_model():
    manifest = RiskReportingManifest()
    assert manifest.current_phase == 155
    assert manifest.target_final_phase == 160
    assert manifest.next_phase == 156
    assert manifest.non_production is True
    assert manifest.risk_report_generated is False
    assert manifest.phase_156_handoff_ready is True
