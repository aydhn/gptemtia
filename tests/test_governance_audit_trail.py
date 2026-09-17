# -*- coding: utf-8 -*-
"""Unit tests for Phase 144 Governance Audit Trail Placeholders, Logs, and Lifecycle."""

import pytest
from advanced_model_governance.model_governance_config import get_model_governance_profile
from advanced_model_governance.governance_audit_trail_placeholders import (
    build_governance_audit_trail_placeholder_registry,
)
from advanced_model_governance.governance_decision_log_placeholders import (
    build_governance_decision_log_placeholder_registry,
)
from advanced_model_governance.governance_change_log_placeholders import (
    build_governance_change_log_placeholder_registry,
)
from advanced_model_governance.governance_owner_responsibility_placeholders import (
    build_governance_owner_responsibility_placeholder_registry,
)
from advanced_model_governance.governance_model_lifecycle_placeholders import (
    build_governance_model_lifecycle_placeholder_registry,
)
from advanced_model_governance.governance_model_version_placeholders import (
    build_governance_model_version_placeholder_registry,
)
from advanced_model_governance.governance_audit_placeholders import (
    build_governance_audit_placeholder_registry,
)


def test_governance_audit_trail_placeholders():
    prof = get_model_governance_profile()
    df, summary = build_governance_audit_trail_placeholder_registry(prof)
    assert len(df) >= 4
    assert summary["total_audit_placeholders"] >= 4
    assert (df["real_audit_log"] == False).all()
    assert summary["all_real_audit_log_false"] is True


def test_governance_decision_log_placeholders():
    prof = get_model_governance_profile()
    df, summary = build_governance_decision_log_placeholder_registry(prof)
    assert len(df) >= 3
    assert summary["total_decision_placeholders"] >= 3
    assert (df["is_placeholder"] == True).all()


def test_governance_change_log_placeholders():
    prof = get_model_governance_profile()
    df, summary = build_governance_change_log_placeholder_registry(prof)
    assert len(df) >= 3
    assert summary["total_change_placeholders"] >= 3
    assert (df["is_placeholder"] == True).all()


def test_governance_owner_responsibility_placeholders():
    prof = get_model_governance_profile()
    df, summary = build_governance_owner_responsibility_placeholder_registry(prof)
    assert len(df) >= 3
    assert summary["total_owner_roles"] >= 3
    assert (df["status"] == "ASSIGNED").all()


def test_governance_lifecycle_and_version_placeholders():
    prof = get_model_governance_profile()
    lif_df, lif_sum = build_governance_model_lifecycle_placeholder_registry(prof)
    assert len(lif_df) >= 5
    assert lif_sum["total_stages"] >= 5
    assert lif_sum["production_deployment_blocked"] is True

    ver_df, ver_sum = build_governance_model_version_placeholder_registry(prof)
    assert len(ver_df) >= 3
    assert ver_sum["total_versions"] >= 3
    assert ver_sum["zero_deployed"] is True

    gaud_df, gaud_sum = build_governance_audit_placeholder_registry(prof)
    assert len(gaud_df) >= 5
    assert gaud_sum["total_audit_placeholders"] >= 5
    assert gaud_sum["all_real_audit_log_false"] is True
