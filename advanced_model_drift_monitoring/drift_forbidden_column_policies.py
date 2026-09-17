"""Drift Forbidden Column Policies for Phase 142.

Enforces forbidden column policies across drift monitoring contracts:
blocks forward return targets, execution flags, live order fields,
and unauthorized account information from drift analysis.
"""

from __future__ import annotations

from dataclasses import asdict
from typing import Any, Dict, List, Set

from advanced_model_drift_monitoring.model_drift_models import DriftGuardItem

FORBIDDEN_DRIFT_COLUMNS: Set[str] = {
    "target_future_return",
    "target_next_day_price",
    "future_close",
    "realized_pnl",
    "order_id",
    "trade_action",
    "broker_account",
    "execution_price",
    "live_fill_status",
    "unauthorized_secret",
}


def build_drift_forbidden_column_guards() -> List[DriftGuardItem]:
    """Builds forbidden column guard items."""
    return [
        DriftGuardItem(
            guard_id="guard_forbidden_columns_drift",
            guard_name="Forbidden Columns Exclusion Guard",
            guard_type="forbidden_column",
            status="active",
            is_active=True,
            description="Excludes trading targets, execution artifacts, and forward prices from drift contracts.",
            validation_rule="disallow_forbidden_columns_set",
            metadata={"forbidden_columns": sorted(list(FORBIDDEN_DRIFT_COLUMNS))},
        )
    ]


def validate_drift_monitored_columns(columns: List[str]) -> Dict[str, Any]:
    """Validates that a list of monitored columns contains no forbidden fields."""
    violating = [col for col in columns if col.lower() in FORBIDDEN_DRIFT_COLUMNS]

    return {
        "valid": len(violating) == 0,
        "checked_columns_count": len(columns),
        "violating_columns": violating,
        "error": f"Forbidden columns detected: {violating}" if violating else None,
    }
