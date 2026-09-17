# -*- coding: utf-8 -*-
"""Unit tests for Phase 142 Master Disabled Execution Safeguards."""

import pytest
from advanced_model_drift_monitoring.drift_execution_disabled import (
    build_all_drift_disabled_execution_items,
    summarize_drift_disabled_executions,
    validate_all_drift_execution_safeguards,
)


def test_master_disabled_executions():
    items = build_all_drift_disabled_execution_items()
    assert len(items) == 7
    summary = summarize_drift_disabled_executions(items)
    assert summary["all_disabled_verified"] is True
    assert summary["governance_status"] == "FULLY_PROTECTED"


def test_validate_all_safeguards():
    # Compliant request
    res = validate_all_drift_execution_safeguards({"mode": "dry_run_contract_only"})
    assert res["all_safeguards_passed"] is True

    # Violating request
    with pytest.raises(RuntimeError):
        validate_all_drift_execution_safeguards({"send_alert": True})
