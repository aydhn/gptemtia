"""Phase 132: Macro/Event/News Validation Dependencies Registry."""

from typing import Any, Dict, Optional, Tuple
import pandas as pd

from advanced_macro_event_news_regime.macro_event_news_regime_config import (
    MacroEventNewsRegimeProfile,
    get_macro_event_news_regime_profile,
)

DEFAULT_VALIDATION_DEPENDENCIES = [
    {
        "dependency_id": "val_dep_phase_120_fusion",
        "source_phase": "Phase 120",
        "description": "Macro/Calendar/News Feature Fusion integrity dependency.",
        "status": "active",
        "is_blocking": True,
    },
    {
        "dependency_id": "val_dep_phase_121_validation",
        "source_phase": "Phase 121",
        "description": "Feature Validation and Matrix Integrity no-lookahead dependency.",
        "status": "active",
        "is_blocking": True,
    },
    {
        "dependency_id": "val_dep_phase_127_matrix",
        "source_phase": "Phase 127",
        "description": "Regime Feature Matrix and State Dataset Contracts dependency.",
        "status": "active",
        "is_blocking": True,
    },
    {
        "dependency_id": "val_dep_phase_128_rule_free",
        "source_phase": "Phase 128",
        "description": "Candidate state contract no-lookahead dependency.",
        "status": "active",
        "is_blocking": True,
    },
    {
        "dependency_id": "val_dep_phase_129_behavior",
        "source_phase": "Phase 129",
        "description": "Market behavior diagnostics validation dependency.",
        "status": "active",
        "is_blocking": True,
    },
    {
        "dependency_id": "val_dep_phase_130_transition",
        "source_phase": "Phase 130",
        "description": "Regime transition stability and sequence validation dependency.",
        "status": "active",
        "is_blocking": True,
    },
    {
        "dependency_id": "val_dep_phase_131_cross_asset",
        "source_phase": "Phase 131",
        "description": "Cross-asset regime context no-lookahead dependency.",
        "status": "active",
        "is_blocking": True,
    },
    {
        "dependency_id": "val_dep_metadata_only_boundary",
        "source_phase": "Phase 132",
        "description": "Strict metadata-only news boundary compliance dependency.",
        "status": "active",
        "is_blocking": True,
    },
    {
        "dependency_id": "val_dep_source_preservation",
        "source_phase": "All",
        "description": "Strict zero-overwrite and non-destructive cleaning dependency.",
        "status": "active",
        "is_blocking": True,
    },
]


def build_macro_event_news_validation_dependency_registry(
    profile: Optional[MacroEventNewsRegimeProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build registry DataFrame of validation dependencies."""
    p = profile or get_macro_event_news_regime_profile()
    rows = []
    for item in DEFAULT_VALIDATION_DEPENDENCIES:
        row = dict(item)
        row["profile_name"] = p.profile_name
        row["non_signal"] = True
        row["source_preserved"] = True
        row["official_approval"] = False
        row["production_ready"] = False
        row["broker_ready"] = False
        rows.append(row)
    df = pd.DataFrame(rows)
    summary = {
        "total_validation_dependencies": len(df),
        "source_phases": df["source_phase"].unique().tolist(),
        "all_non_signal": True,
        "all_source_preserved": True,
    }
    return df, summary


def summarize_macro_event_news_validation_dependencies(df: pd.DataFrame) -> Dict[str, Any]:
    """Return summary dictionary for validation dependencies."""
    return {
        "total_dependencies": len(df),
        "blocking_count": int(df["is_blocking"].sum()) if "is_blocking" in df.columns else 0,
        "all_non_signal": bool(df["non_signal"].all()) if "non_signal" in df.columns else True,
    }
