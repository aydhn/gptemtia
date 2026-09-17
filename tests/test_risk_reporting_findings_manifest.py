# -*- coding: utf-8 -*-
"""Unit tests for Risk Reporting Findings, Manual Review, Scoring and Manifest."""

from advanced_risk_reporting.risk_reporting_config import get_default_risk_reporting_profile
from advanced_risk_reporting.risk_reporting_findings import build_risk_reporting_findings_registry
from advanced_risk_reporting.risk_reporting_manual_review import build_risk_reporting_manual_review_queue
from advanced_risk_reporting.risk_reporting_readiness_scoring import build_risk_reporting_readiness_score_report
from advanced_risk_reporting.risk_reporting_manifest import build_risk_reporting_manifest


def test_build_findings_scoring_manifest():
    profile = get_default_risk_reporting_profile()

    df_fnd, s_fnd = build_risk_reporting_findings_registry(profile)
    assert not df_fnd.empty
    assert s_fnd["finding_count"] >= 1

    df_mrq, s_mrq = build_risk_reporting_manual_review_queue(profile)
    assert not df_mrq.empty
    assert s_mrq["review_count"] >= 1

    df_score, s_score = build_risk_reporting_readiness_score_report(profile)
    assert not df_score.empty
    assert s_score["is_contract_ready"] is True
    assert s_score["meets_threshold"] is True

    df_mnf, s_mnf = build_risk_reporting_manifest(profile)
    assert not df_mnf.empty
    assert s_mnf["current_phase"] == 155
    assert s_mnf["next_phase"] == 156
    assert s_mnf["phase_156_handoff_ready"] is True
