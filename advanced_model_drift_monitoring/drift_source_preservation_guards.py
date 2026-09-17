"""Drift Source Preservation Guards for Phase 142.

Enforces strict non-destructive invariants: historical data lakes, raw files,
and feature snapshots must be preserved immutably without file overwrites or deletes.
"""

from __future__ import annotations

from dataclasses import asdict
from typing import Any, Dict, List

from advanced_model_drift_monitoring.model_drift_models import DriftGuardItem


def build_drift_source_preservation_guards() -> List[DriftGuardItem]:
    """Builds source preservation guard contracts."""
    guards = [
        DriftGuardItem(
            guard_id="guard_source_preservation_immutability",
            guard_name="Immutable Source Data Preservation Guard",
            guard_type="source_preservation",
            status="active",
            is_active=True,
            description="Prohibits deletion, truncation, or in-place overwrite of underlying historical parquet/csv files.",
            validation_rule="no_destructive_storage_mutations",
            metadata={"enforcement": "read_only_source_access"},
        ),
    ]
    return guards


def validate_storage_operation_safety(operation_type: str) -> Dict[str, Any]:
    """Validates that storage operation is non-destructive."""
    destructive_ops = {"delete", "truncate", "drop_table", "overwrite_source", "rmdir"}
    is_safe = operation_type.lower() not in destructive_ops

    return {
        "is_safe": is_safe,
        "operation_type": operation_type,
        "error": f"Destructive operation blocked: '{operation_type}'" if not is_safe else None,
    }
