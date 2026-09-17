# -*- coding: utf-8 -*-
"""Unit tests for Phase 144 Model Governance Contracts, Risk Register, and Controls."""

import pytest
from advanced_model_governance.model_governance_config import get_model_governance_profile
from advanced_model_governance.model_governance_contracts import (
    build_model_governance_contract_registry,
)
from advanced_model_governance.governance_validation_evidence import (
    build_governance_validation_evidence_registry,
)
from advanced_model_governance.governance_risk_register import (
    build_governance_risk_register,
)
from advanced_model_governance.governance_control_checklists import (
    build_governance_control_checklist_registry,
)
from advanced_model_governance.governance_compliance_placeholders import (
    build_governance_compliance_placeholder_registry,
)


def test_model_governance_contract_registry():
    prof = get_model_governance_profile()
    df, summary = build_model_governance_contract_registry(prof)
    assert len(df) >= 7
    assert summary["total_contracts"] >= 7
    assert "contract_name" in df.columns
    assert "governance_family" in df.columns
    assert (df["production_approval_allowed"] == False).all()
    assert (df["non_signal_required"] == True).all()


def test_governance_validation_evidence_registry():
    prof = get_model_governance_profile()
    df, summary = build_governance_validation_evidence_registry(prof)
    assert len(df) >= 5
    assert summary["total_evidence_sources"] >= 5
    assert "source" in df.columns
    assert "evidence_metric" in df.columns
    assert (df["passed"] == True).all()
    assert (df["non_signal"] == True).all()


def test_governance_risk_register():
    prof = get_model_governance_profile()
    df, summary = build_governance_risk_register(prof)
    assert len(df) >= 5
    assert summary["total_risks"] >= 5
    assert "risk_id" in df.columns
    assert "mitigation_strategy" in df.columns
    assert (df["manual_review_required"] == True).all()


def test_governance_control_checklist_registry():
    prof = get_model_governance_profile()
    df, summary = build_governance_control_checklist_registry(prof)
    assert len(df) >= 6
    assert summary["total_items"] >= 6
    assert "check_id" in df.columns
    assert "status" in df.columns
    assert (df["status"] == "PASSED").all()
    assert (df["enforced"] == True).all()


def test_governance_compliance_placeholder_registry():
    prof = get_model_governance_profile()
    df, summary = build_governance_compliance_placeholder_registry(prof)
    assert len(df) >= 3
    assert summary["total_placeholders"] >= 3
    assert (df["is_placeholder"] == True).all()
    assert (df["is_production_approval"] == False).all()
