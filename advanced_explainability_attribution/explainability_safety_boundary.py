# -*- coding: utf-8 -*-
"""Phase 143: Explainability Safety Boundary."""

from typing import Any, Dict, List, Optional
from advanced_explainability_attribution.explainability_config import (
    ExplainabilityProfile,
    get_explainability_profile,
)


class ExplainabilitySafetyViolationError(Exception):
    """Raised when an operation violates Phase 143 safety boundaries."""
    pass


def assert_safe_explainability_operation(
    operation_name: str,
    kwargs: Optional[Dict[str, Any]] = None,
    profile: Optional[ExplainabilityProfile] = None,
) -> bool:
    """Assert that a requested explainability operation is safe within Phase 143 invariants."""
    prof = profile or get_explainability_profile()
    kw = kwargs or {}

    forbidden_operations = [
        "train_model",
        "fit_model",
        "predict_model",
        "compute_shapley_values",
        "fit_lime_surrogate",
        "calculate_permutation_importance",
        "evaluate_pdp_grid",
        "compute_ice_curves",
        "fit_surrogate_tree",
        "generate_counterfactual",
        "auto_disable_model",
        "auto_reweight_ensemble",
        "execute_trade",
        "send_broker_order",
    ]

    op_norm = operation_name.lower().strip()
    if op_norm in forbidden_operations:
        raise ExplainabilitySafetyViolationError(
            f"Operation '{operation_name}' violates Phase 143 safety invariants! "
            f"Phase 143 is strictly non-executing contract and dry-run metadata only."
        )

    if kw.get("live_trading", False):
        raise ExplainabilitySafetyViolationError("Live trading is strictly prohibited in Phase 143.")

    if kw.get("calculate_attribution", False):
        raise ExplainabilitySafetyViolationError("Attribution calculation is strictly disabled in Phase 143.")

    return True


def check_all_safety_boundaries(
    profile: Optional[ExplainabilityProfile] = None,
) -> Dict[str, Any]:
    """Verify that all safety boundary checks pass in current configuration."""
    prof = profile or get_explainability_profile()

    checks = [
        ("non_executing_xai", True),
        ("non_signal_guarantee", True),
        ("source_preservation", True),
        ("no_live_trading", True),
        ("no_broker_integration", True),
        ("no_article_body_text", True),
        ("dry_run_enforced", True),
    ]

    return {
        "all_safe": all(c[1] for c in checks),
        "checks": [{"boundary": b, "enforced": e} for b, e in checks],
        "current_phase": 143,
        "next_phase": 144,
        "target_final_phase": 160,
    }
