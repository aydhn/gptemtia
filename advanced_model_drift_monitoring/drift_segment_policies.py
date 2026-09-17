"""Drift Segment Policies for Phase 142.

Defines segmentation and slicing policies for non-executing drift monitoring contracts.
Covers segmentation across asset classes, commodity sub-segments, currency pairs,
and volatility regimes without executing data slicing or metric calculations.
"""

from __future__ import annotations

from dataclasses import asdict
from typing import Any, Dict, List

from advanced_model_drift_monitoring.model_drift_models import DriftWindowPolicy


def build_drift_segment_policies() -> List[DriftWindowPolicy]:
    """Builds standard drift segmentation policies for monitoring contracts."""
    policies = [
        DriftWindowPolicy(
            policy_id="seg_asset_class_commodity",
            policy_name="Commodity Asset Class Segment",
            window_type="segment_slice",
            window_size="segment:commodity",
            stride=None,
            min_observations=100,
            lookback_days=180,
            execution_enabled=False,
            parameters={
                "segment_key": "asset_class",
                "segment_value": "commodity",
                "segment_type": "categorical_filter",
                "slice_column": "asset_class",
                "evaluation_mode": "contract_only",
            },
        ),
        DriftWindowPolicy(
            policy_id="seg_asset_class_forex",
            policy_name="Forex Asset Class Segment",
            window_type="segment_slice",
            window_size="segment:forex",
            stride=None,
            min_observations=100,
            lookback_days=180,
            execution_enabled=False,
            parameters={
                "segment_key": "asset_class",
                "segment_value": "forex",
                "segment_type": "categorical_filter",
                "slice_column": "asset_class",
                "evaluation_mode": "contract_only",
            },
        ),
        DriftWindowPolicy(
            policy_id="seg_volatility_high",
            policy_name="High Volatility Regime Segment",
            window_type="segment_slice",
            window_size="regime:high_volatility",
            stride=None,
            min_observations=50,
            lookback_days=90,
            execution_enabled=False,
            parameters={
                "segment_key": "volatility_regime",
                "segment_value": "high",
                "segment_type": "regime_filter",
                "slice_column": "regime_label",
                "evaluation_mode": "contract_only",
            },
        ),
        DriftWindowPolicy(
            policy_id="seg_volatility_low",
            policy_name="Low Volatility Regime Segment",
            window_type="segment_slice",
            window_size="regime:low_volatility",
            stride=None,
            min_observations=50,
            lookback_days=90,
            execution_enabled=False,
            parameters={
                "segment_key": "volatility_regime",
                "segment_value": "low",
                "segment_type": "regime_filter",
                "slice_column": "regime_label",
                "evaluation_mode": "contract_only",
            },
        ),
        DriftWindowPolicy(
            policy_id="seg_liquidity_tier1",
            policy_name="Tier 1 High Liquidity Segment",
            window_type="segment_slice",
            window_size="tier:high_liquidity",
            stride=None,
            min_observations=100,
            lookback_days=120,
            execution_enabled=False,
            parameters={
                "segment_key": "liquidity_tier",
                "segment_value": "tier1",
                "segment_type": "liquidity_bucket",
                "slice_column": "liquidity_tier",
                "evaluation_mode": "contract_only",
            },
        ),
    ]
    return policies


def validate_drift_segment_policy(policy: DriftWindowPolicy) -> Dict[str, Any]:
    """Validates that a segment policy maintains non-executing safety."""
    errors = []
    if policy.execution_enabled:
        errors.append("Segment policy must have execution_enabled=False.")
    if policy.min_observations <= 0:
        errors.append("min_observations must be greater than zero.")
    if not policy.policy_id.startswith("seg_"):
        errors.append("Policy ID must start with 'seg_'.")

    return {
        "valid": len(errors) == 0,
        "policy_id": policy.policy_id,
        "policy_name": policy.policy_name,
        "errors": errors,
        "policy": asdict(policy),
    }
