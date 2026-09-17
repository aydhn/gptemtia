# -*- coding: utf-8 -*-
"""Unit tests for Phase 144 Model Card Contracts, Templates, Limitations, and Dependencies."""

import pytest
from advanced_model_governance.model_governance_config import get_model_governance_profile
from advanced_model_governance.model_card_contracts import (
    build_model_card_contract_registry,
)
from advanced_model_governance.model_card_templates import (
    build_model_card_template_registry,
)
from advanced_model_governance.model_card_sections import (
    build_model_card_section_registry,
)
from advanced_model_governance.model_card_limitations import (
    build_model_card_limitation_registry,
)
from advanced_model_governance.model_card_intended_use import (
    build_model_card_intended_use_registry,
)
from advanced_model_governance.model_card_prohibited_use import (
    build_model_card_prohibited_use_registry,
)
from advanced_model_governance.model_card_risk_disclosures import (
    build_model_card_risk_disclosure_registry,
)
from advanced_model_governance.model_card_validation_evidence import (
    build_model_card_validation_evidence_registry,
)
from advanced_model_governance.model_card_data_dependencies import (
    build_model_card_data_dependency_registry,
)
from advanced_model_governance.model_card_feature_dependencies import (
    build_model_card_feature_dependency_registry,
)
from advanced_model_governance.model_card_model_dependencies import (
    build_model_card_model_dependency_registry,
)
from advanced_model_governance.model_card_runtime_dependencies import (
    build_model_card_runtime_dependency_registry,
)


def test_model_card_contracts_registry():
    prof = get_model_governance_profile()
    df, summary = build_model_card_contract_registry(prof)
    assert len(df) >= 7
    assert summary["total_contracts"] >= 7
    assert "contract_name" in df.columns
    assert "model_family" in df.columns
    assert (df["production_ready_claim"] == False).all()
    assert (df["broker_ready_claim"] == False).all()


def test_model_card_templates():
    prof = get_model_governance_profile()
    df, summary = build_model_card_template_registry(prof)
    assert len(df) >= 4
    assert summary["total_templates"] >= 4
    assert "template_name" in df.columns
    assert "section_count" in df.columns


def test_model_card_sections():
    prof = get_model_governance_profile()
    df, summary = build_model_card_section_registry(prof)
    assert len(df) >= 10
    assert summary["total_sections"] >= 10
    assert "section_id" in df.columns
    assert "required" in df.columns
    assert (df["required"] == True).all()


def test_model_card_limitations():
    prof = get_model_governance_profile()
    df, summary = build_model_card_limitation_registry(prof)
    assert len(df) >= 5
    assert summary["total_limitations"] >= 5
    assert "limitation_id" in df.columns
    assert (df["is_enforced"] == True).all()


def test_model_card_intended_and_prohibited_use():
    prof = get_model_governance_profile()
    df_i, sum_i = build_model_card_intended_use_registry(prof)
    assert len(df_i) >= 4
    assert sum_i["total_intended_uses"] >= 4
    assert (df_i["non_production"] == True).all()

    df_p, sum_p = build_model_card_prohibited_use_registry(prof)
    assert len(df_p) >= 5
    assert sum_p["total_prohibitions"] >= 5
    assert (df_p["is_prohibited"] == True).all()
    assert (df_p["status"] == "BLOCKED_BY_POLICY").all()


def test_model_card_risk_disclosures():
    prof = get_model_governance_profile()
    df, summary = build_model_card_risk_disclosure_registry(prof)
    assert len(df) >= 4
    assert summary["total_risk_disclosures"] >= 4
    assert "risk_id" in df.columns
    assert (df["manual_review_required"] == True).all()


def test_model_card_validation_evidence():
    prof = get_model_governance_profile()
    df, summary = build_model_card_validation_evidence_registry(prof)
    assert len(df) >= 4
    assert summary["total_evidence_items"] >= 4
    assert (df["status"] == "VERIFIED").all()


def test_model_card_dependencies():
    prof = get_model_governance_profile()
    d_df, d_sum = build_model_card_data_dependency_registry(prof)
    assert len(d_df) >= 3
    assert d_sum["all_satisfied"] is True

    f_df, f_sum = build_model_card_feature_dependency_registry(prof)
    assert len(f_df) >= 3
    assert f_sum["all_satisfied"] is True

    m_df, m_sum = build_model_card_model_dependency_registry(prof)
    assert len(m_df) >= 3
    assert m_sum["all_satisfied"] is True

    r_df, r_sum = build_model_card_runtime_dependency_registry(prof)
    assert len(r_df) >= 3
    assert r_sum["all_satisfied"] is True
