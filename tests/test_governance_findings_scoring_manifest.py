# -*- coding: utf-8 -*-
"""Unit tests for Phase 144 Governance Findings, Manual Review, Readiness Scoring, and Manifest."""

import pytest
from advanced_model_governance.model_governance_config import get_model_governance_profile
from advanced_model_governance.governance_findings import (
    build_governance_findings_registry,
)
from advanced_model_governance.governance_manual_review import (
    build_governance_manual_review_queue,
)
from advanced_model_governance.governance_readiness_scoring import (
    build_governance_readiness_score_report,
)
from advanced_model_governance.model_governance_manifest import (
    build_model_governance_manifest,
)


def test_governance_findings_registry():
    prof = get_model_governance_profile()
    df, summary = build_governance_findings_registry(prof)
    assert len(df) >= 3
    assert summary["total_findings"] >= 3
    assert "finding_id" in df.columns
    assert "severity_label" in df.columns
    assert "recommendation" in df.columns


def test_governance_manual_review_queue():
    prof = get_model_governance_profile()
    df, summary = build_governance_manual_review_queue(prof)
    assert len(df) >= 3
    assert summary["total_queue_items"] >= 3
    assert "queue_id" in df.columns
    assert "blocked_actions" in df.columns


def test_governance_readiness_scoring():
    prof = get_model_governance_profile()
    df, summary = build_governance_readiness_score_report(prof)
    assert len(df) == 1
    assert summary["readiness_score"] == 1.0
    assert summary["classification"] == "governance_contract_ready"
    assert summary["meets_threshold"] is True
    assert summary["production_ready"] is False
    assert summary["broker_ready"] is False


def test_model_governance_manifest():
    prof = get_model_governance_profile()
    df, summary = build_model_governance_manifest(prof)
    assert len(df) == 1
    assert summary["current_phase"] == 144
    assert summary["next_phase"] == 145
    assert summary["target_final_phase"] == 160
    assert summary["production_ready"] is False
    assert summary["broker_ready"] is False
    assert summary["live_trading_approved"] is False
    assert summary["status"] == "MANIFEST_VERIFIED"
