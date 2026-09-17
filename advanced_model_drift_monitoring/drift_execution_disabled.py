"""Master Disabled Execution Safeguards Aggregator for Phase 142.

Aggregates and verifies all non-executing safety enforcements across drift calculation,
alerting, retraining triggers, model actions, predictions, and data mutations.
"""

from __future__ import annotations

from dataclasses import asdict
from typing import Any, Dict, List

from advanced_model_drift_monitoring.drift_alerting_disabled import (
    assert_drift_alerting_disabled,
    build_drift_alerting_disabled_item,
)
from advanced_model_drift_monitoring.drift_metric_calculation_disabled import (
    assert_drift_metric_calculation_disabled,
    build_drift_metric_calculation_disabled_item,
)
from advanced_model_drift_monitoring.drift_model_action_disabled import (
    assert_drift_model_action_disabled,
    build_drift_model_action_disabled_item,
)
from advanced_model_drift_monitoring.drift_prediction_disabled import (
    assert_drift_prediction_disabled,
    build_drift_prediction_disabled_item,
)
from advanced_model_drift_monitoring.drift_retraining_trigger_disabled import (
    assert_drift_retraining_trigger_disabled,
    build_drift_retraining_trigger_disabled_item,
)
from advanced_model_drift_monitoring.model_drift_models import DriftDisabledExecutionItem


def build_drift_data_modification_disabled_item() -> DriftDisabledExecutionItem:
    """Builds the disabled execution item for data modification."""
    return DriftDisabledExecutionItem(
        execution_id="dis_exec_data_mod_006",
        execution_type="drift_data_modification_disabled",
        target_component="data_lake_storage",
        status="active_enforcement",
        is_disabled=True,
        disabled_reason="Destructive data overwriting, in-place cleaning, or imputation are strictly forbidden.",
        remediation_required="Preserve all existing data sources immutably.",
        metadata={"phase": 142},
    )


def build_drift_feature_drop_disabled_item() -> DriftDisabledExecutionItem:
    """Builds the disabled execution item for automated feature dropping."""
    return DriftDisabledExecutionItem(
        execution_id="dis_exec_feat_drop_007",
        execution_type="drift_feature_drop_disabled",
        target_component="feature_selector",
        status="active_enforcement",
        is_disabled=True,
        disabled_reason="Automated dropping of drifting features is strictly forbidden without governance signoff.",
        remediation_required="Flag drifting features in contracts; do not drop columns automatically.",
        metadata={"phase": 142},
    )


def build_all_drift_disabled_execution_items() -> List[DriftDisabledExecutionItem]:
    """Builds the complete registry of all disabled execution safeguards."""
    return [
        build_drift_metric_calculation_disabled_item(),
        build_drift_alerting_disabled_item(),
        build_drift_retraining_trigger_disabled_item(),
        build_drift_model_action_disabled_item(),
        build_drift_prediction_disabled_item(),
        build_drift_data_modification_disabled_item(),
        build_drift_feature_drop_disabled_item(),
    ]


def summarize_drift_disabled_executions(
    items: List[DriftDisabledExecutionItem],
) -> Dict[str, Any]:
    """Summarizes all disabled execution safeguards."""
    all_disabled = all(item.is_disabled for item in items)
    by_type = {item.execution_type: item.is_disabled for item in items}

    return {
        "total_enforcements": len(items),
        "all_disabled_verified": all_disabled,
        "enforcements_by_type": by_type,
        "governance_status": "FULLY_PROTECTED" if all_disabled else "SAFETY_BREACH",
        "items": [asdict(item) for item in items],
    }


def validate_all_drift_execution_safeguards(request_params: Dict[str, Any]) -> Dict[str, Any]:
    """Runs all safeguard assertions against incoming request parameters."""
    res1 = assert_drift_metric_calculation_disabled(request_params)
    res2 = assert_drift_alerting_disabled(request_params)
    res3 = assert_drift_retraining_trigger_disabled(request_params)
    res4 = assert_drift_model_action_disabled(request_params)
    res5 = assert_drift_prediction_disabled(request_params)

    return {
        "all_safeguards_passed": True,
        "checked_assertions": [res1, res2, res3, res4, res5],
    }
