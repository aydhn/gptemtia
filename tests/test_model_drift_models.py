# -*- coding: utf-8 -*-
"""Unit tests for Phase 142 Data Models."""

import pytest
from advanced_model_drift_monitoring.model_drift_models import (
    DriftMonitoringContract,
    DriftLinkageItem,
    DriftWindowPolicy,
    DriftThresholdPlaceholder,
    DriftMetricPlaceholder,
    DriftDisabledExecutionItem,
    DriftGuardItem,
    DriftFinding,
    DriftReadinessScore,
)


def test_data_model_instantiation():
    contract = DriftMonitoringContract(
        contract_id="test_contract_001",
        domain="model_drift",
        target_name="candidate_models",
        contract_version="1.0.0",
        status="active",
        execution_mode="non_executing_contract",
        reference_window="ref_win_1",
        current_window="curr_win_1",
        threshold_policy=None,
        linkage_target="Phase 140",
    )
    assert contract.contract_id == "test_contract_001"
    assert contract.execution_mode == "non_executing_contract"

    finding = DriftFinding(
        finding_id="find_001",
        domain="data_drift",
        target_name="raw_features",
        severity="info",
        finding_type="audit",
        description="Test description",
        recommended_action="None",
        requires_human_review=False,
        execution_blocked=True,
    )
    assert finding.execution_blocked is True
