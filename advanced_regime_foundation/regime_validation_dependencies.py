"""Phase 126: Regime Validation Dependencies Registry.

Registers mandatory validation invariants and non-negotiable checks required before regime processing.
"""

from typing import Any, Dict, List, Optional, Tuple
import pandas as pd

from advanced_regime_foundation.regime_foundation_config import (
    RegimeFoundationProfile,
    get_default_regime_foundation_profile,
)

VALIDATION_DEPENDENCIES: List[Dict[str, Any]] = [
    {
        "validation_id": "val_dep_01_no_forbidden_cols",
        "validation_rule": "no_forbidden_columns",
        "scope": "All regime input DataFrames and state schemas",
        "description": "Prohibits columns: signal, buy, sell, long, short, position, target, label, prediction, recommendation, future_return",
        "source_phase": 121,
        "enforcement": "STRICT_BLOCKING",
        "non_signal": True,
        "status": "ACTIVE",
    },
    {
        "validation_id": "val_dep_02_no_lookahead",
        "validation_rule": "no_lookahead_guarantee",
        "scope": "All time-series feature and factor inputs",
        "description": "Ensures all rolling calculations use closed past intervals [t-W, t] with zero shift(-1) or future leakage",
        "source_phase": 121,
        "enforcement": "STRICT_BLOCKING",
        "non_signal": True,
        "status": "ACTIVE",
    },
    {
        "validation_id": "val_dep_03_no_targets",
        "validation_rule": "no_target_or_prediction",
        "scope": "All regime taxonomies, contracts, and outputs",
        "description": "Enforces that regime state values are contextual environments, not predictive targets or ML labels",
        "source_phase": 126,
        "enforcement": "STRICT_BLOCKING",
        "non_signal": True,
        "status": "ACTIVE",
    },
    {
        "validation_id": "val_dep_04_timestamp_order",
        "validation_rule": "monotonic_timestamp_order",
        "scope": "Input series across all asset classes",
        "description": "Requires strictly increasing chronological index without backward jumps or duplicated timestamps",
        "source_phase": 121,
        "enforcement": "STRICT_BLOCKING",
        "non_signal": True,
        "status": "ACTIVE",
    },
    {
        "validation_id": "val_dep_05_metadata_only_news",
        "validation_rule": "metadata_only_news_context",
        "scope": "News inputs used for regime context",
        "description": "Guarantees zero full article text, scraped HTML, vector embeddings, or NLP sentiment models",
        "source_phase": 111,
        "enforcement": "STRICT_BLOCKING",
        "non_signal": True,
        "status": "ACTIVE",
    },
    {
        "validation_id": "val_dep_06_source_preservation",
        "validation_rule": "source_preservation_invariant",
        "scope": "Data Lake storage and transformations",
        "description": "Prohibits in-place file mutation, destructive cleaning, auto-imputation, and auto-feature-drop",
        "source_phase": 112,
        "enforcement": "STRICT_BLOCKING",
        "non_signal": True,
        "status": "ACTIVE",
    },
    {
        "validation_id": "val_dep_07_non_signal_compliance",
        "validation_rule": "non_signal_policy_compliance",
        "scope": "All textual outputs, reports, logs, and docstrings",
        "description": "Scans for and blocks 14+ commercial, execution, and directional certainty claim patterns",
        "source_phase": 126,
        "enforcement": "STRICT_BLOCKING",
        "non_signal": True,
        "status": "ACTIVE",
    },
    {
        "validation_id": "val_dep_08_store_validation_status",
        "validation_rule": "feature_store_validation_status",
        "scope": "Registered feature store entries",
        "description": "Requires VALIDATION_PASS status in Feature Store before permitting feature inclusion in regime matrix",
        "source_phase": 124,
        "enforcement": "STRICT_BLOCKING",
        "non_signal": True,
        "status": "ACTIVE",
    },
]


def build_regime_validation_dependency_registry(
    profile: Optional[RegimeFoundationProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and summary for regime validation dependency registry."""
    active_profile = profile or get_default_regime_foundation_profile()
    df = pd.DataFrame(VALIDATION_DEPENDENCIES)
    summary = {
        "active_profile": active_profile.profile_name,
        "total_rules": len(df),
        "all_blocking": bool((df["enforcement"] == "STRICT_BLOCKING").all()),
        "all_non_signal": bool((df["non_signal"] == True).all()),
        "current_phase": active_profile.current_phase,
        "target_final_phase": active_profile.target_final_phase,
        "next_phase": active_profile.next_phase,
        "official_approval": False,
        "production_ready": False,
        "broker_ready": False,
    }
    return df, summary


def summarize_regime_validation_dependencies(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize regime validation dependencies DataFrame."""
    return {
        "total_rules": len(df),
        "validation_rules": list(df["validation_rule"].unique()) if "validation_rule" in df.columns else [],
        "all_blocking": True,
        "non_signal": True,
    }
