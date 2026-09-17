"""Drift No-Lookahead Guards for Phase 142.

Enforces strict temporal ordering in drift monitoring contracts:
reference window end <= current window start, zero future leakage,
and zero forward-looking data points.
"""

from __future__ import annotations

from dataclasses import asdict
from typing import Any, Dict, List

from advanced_model_drift_monitoring.model_drift_models import DriftGuardItem


def build_drift_no_lookahead_guards() -> List[DriftGuardItem]:
    """Builds no-lookahead guard contracts for drift monitoring."""
    guards = [
        DriftGuardItem(
            guard_id="guard_no_lookahead_window_order",
            guard_name="Temporal Window Ordering Guard",
            guard_type="no_lookahead",
            status="active",
            is_active=True,
            description="Ensures reference window timestamp bounds strictly precede current evaluation window bounds.",
            validation_rule="ref_end_date <= curr_start_date",
            metadata={"enforcement": "strict_temporal_causality"},
        ),
        DriftGuardItem(
            guard_id="guard_no_forward_features",
            guard_name="Zero Forward Feature Leakage Guard",
            guard_type="no_lookahead",
            status="active",
            is_active=True,
            description="Verifies no feature in drift monitoring contracts depends on future-dated observations or lookahead labels.",
            validation_rule="no_future_index_in_features",
            metadata={"enforcement": "zero_leakage"},
        ),
    ]
    return guards


def validate_window_temporal_ordering(
    ref_end_date: str,
    curr_start_date: str,
) -> Dict[str, Any]:
    """Validates that reference window ends before or at current window start."""
    is_valid = ref_end_date <= curr_start_date
    return {
        "valid": is_valid,
        "ref_end_date": ref_end_date,
        "curr_start_date": curr_start_date,
        "error": None if is_valid else "Lookahead violation: ref_end_date is after curr_start_date.",
    }
