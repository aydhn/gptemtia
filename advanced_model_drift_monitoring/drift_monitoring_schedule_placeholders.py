"""Drift Monitoring Schedule Placeholders for Phase 142.

Defines non-executing monitoring schedule contracts (cadences, cron placeholders, intervals)
without activating active background runners, cron workers, or real-time polling.
"""

from __future__ import annotations

from dataclasses import asdict
from typing import Any, Dict, List

from advanced_model_drift_monitoring.model_drift_models import DriftWindowPolicy


def build_drift_monitoring_schedule_placeholders() -> List[DriftWindowPolicy]:
    """Builds non-executing drift monitoring schedule policies."""
    schedules = [
        DriftWindowPolicy(
            policy_id="sched_daily_drift_contract_audit",
            policy_name="Daily Drift Contract Placeholder Audit",
            window_type="schedule_placeholder",
            window_size="daily_audit",
            stride=None,
            min_observations=30,
            lookback_days=1,
            execution_enabled=False,
            parameters={
                "cadence": "daily",
                "cron_expression_placeholder": "0 0 * * *",
                "non_executing": True,
                "auto_trigger": False,
                "purpose": "Daily integrity verification of contract schemas and references.",
            },
        ),
        DriftWindowPolicy(
            policy_id="sched_weekly_feature_drift_evaluation",
            policy_name="Weekly Feature Drift Evaluation Placeholder",
            window_type="schedule_placeholder",
            window_size="weekly_evaluation",
            stride=None,
            min_observations=50,
            lookback_days=7,
            execution_enabled=False,
            parameters={
                "cadence": "weekly",
                "cron_expression_placeholder": "0 2 * * 1",
                "non_executing": True,
                "auto_trigger": False,
                "purpose": "Weekly placeholder contract for feature-level drift audits.",
            },
        ),
        DriftWindowPolicy(
            policy_id="sched_monthly_model_calibration_audit",
            policy_name="Monthly Model Calibration Drift Audit",
            window_type="schedule_placeholder",
            window_size="monthly_audit",
            stride=None,
            min_observations=100,
            lookback_days=30,
            execution_enabled=False,
            parameters={
                "cadence": "monthly",
                "cron_expression_placeholder": "0 3 1 * *",
                "non_executing": True,
                "auto_trigger": False,
                "purpose": "Monthly review of calibration drift contracts against Phase 141.",
            },
        ),
        DriftWindowPolicy(
            policy_id="sched_quarterly_retraining_governance_review",
            policy_name="Quarterly Retraining Governance Review Placeholder",
            window_type="schedule_placeholder",
            window_size="quarterly_governance",
            stride=None,
            min_observations=250,
            lookback_days=90,
            execution_enabled=False,
            parameters={
                "cadence": "quarterly",
                "cron_expression_placeholder": "0 4 1 1,4,7,10 *",
                "non_executing": True,
                "auto_trigger": False,
                "purpose": "Quarterly governance signoff placeholder for model retraining contracts.",
            },
        ),
    ]
    return schedules


def validate_drift_monitoring_schedule_placeholder(policy: DriftWindowPolicy) -> Dict[str, Any]:
    """Validates that a schedule placeholder adheres to non-executing governance."""
    errors = []
    if policy.execution_enabled:
        errors.append("Schedule policy must have execution_enabled=False.")
    if policy.parameters.get("auto_trigger") is True:
        errors.append("auto_trigger must be False in non-executing schedules.")
    if not policy.policy_id.startswith("sched_"):
        errors.append("Policy ID must start with 'sched_'.")

    return {
        "valid": len(errors) == 0,
        "policy_id": policy.policy_id,
        "policy_name": policy.policy_name,
        "errors": errors,
        "policy": asdict(policy),
    }
