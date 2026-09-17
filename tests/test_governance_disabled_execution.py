# -*- coding: utf-8 -*-
"""Unit tests for Phase 144 Governance Disabled Execution Reports."""

import pytest
from advanced_model_governance.model_governance_config import get_model_governance_profile
from advanced_model_governance.governance_model_registry_write_disabled import (
    build_governance_model_registry_write_disabled_report,
)
from advanced_model_governance.governance_model_artifact_disabled import (
    build_governance_model_artifact_disabled_report,
)
from advanced_model_governance.governance_deployment_disabled import (
    build_governance_deployment_disabled_report,
)
from advanced_model_governance.governance_production_approval_disabled import (
    build_governance_production_approval_disabled_report,
)
from advanced_model_governance.governance_broker_ready_disabled import (
    build_governance_broker_ready_disabled_report,
)
from advanced_model_governance.governance_live_trading_disabled import (
    build_governance_live_trading_disabled_report,
)
from advanced_model_governance.governance_prediction_disabled import (
    build_governance_prediction_disabled_report,
)
from advanced_model_governance.governance_training_disabled import (
    build_governance_training_disabled_report,
)
from advanced_model_governance.governance_signal_generation_disabled import (
    build_governance_signal_generation_disabled_report,
)
from advanced_model_governance.governance_performance_claim_disabled import (
    build_governance_performance_claim_disabled_report,
)


def test_all_governance_disabled_reports():
    prof = get_model_governance_profile()

    reports = [
        build_governance_model_registry_write_disabled_report(prof),
        build_governance_model_artifact_disabled_report(prof),
        build_governance_deployment_disabled_report(prof),
        build_governance_production_approval_disabled_report(prof),
        build_governance_broker_ready_disabled_report(prof),
        build_governance_live_trading_disabled_report(prof),
        build_governance_prediction_disabled_report(prof),
        build_governance_training_disabled_report(prof),
        build_governance_signal_generation_disabled_report(prof),
        build_governance_performance_claim_disabled_report(prof),
    ]

    assert len(reports) == 10
    for df, summary in reports:
        assert len(df) >= 1
        assert "is_disabled" in df.columns
        assert (df["is_disabled"] == True).all()
        assert summary.get("is_disabled") is True or summary.get("all_disabled") is True
