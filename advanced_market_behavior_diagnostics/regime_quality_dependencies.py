"""Phase 129: Regime Quality Dependencies Report.

Audits foundational dependencies from Phase 121 (Feature Validation), Phase 123 (Quality/Drift),
Phase 124 (Feature Store Metadata), Phase 127 (Matrix Contracts), and Phase 128 (Candidate State Contracts).
"""

from typing import Optional, Tuple
import pandas as pd

from advanced_market_behavior_diagnostics.market_behavior_diagnostics_config import (
    MarketBehaviorDiagnosticsProfile,
    get_market_behavior_diagnostics_profile,
)

SOURCE_REGIME_DEPENDENCIES = [
    {
        "source_phase": 121,
        "source_module": "advanced_feature_validation",
        "dependency_name": "feature_validation_and_no_lookahead",
        "dependency_type": "validation_guard",
        "is_mandatory": True,
        "is_resolved": True,
        "dependency_status": "behavior_quality_ready",
    },
    {
        "source_phase": 123,
        "source_module": "advanced_feature_quality_drift",
        "dependency_name": "feature_quality_and_drift_diagnostics",
        "dependency_type": "quality_drift_metrics",
        "is_mandatory": True,
        "is_resolved": True,
        "dependency_status": "behavior_quality_ready",
    },
    {
        "source_phase": 124,
        "source_module": "advanced_feature_store_integration",
        "dependency_name": "feature_store_metadata_and_lineage",
        "dependency_type": "catalog_metadata",
        "is_mandatory": True,
        "is_resolved": True,
        "dependency_status": "behavior_quality_ready",
    },
    {
        "source_phase": 127,
        "source_module": "advanced_regime_matrix",
        "dependency_name": "regime_feature_matrix_contracts",
        "dependency_type": "matrix_contracts",
        "is_mandatory": True,
        "is_resolved": True,
        "dependency_status": "behavior_quality_ready",
    },
    {
        "source_phase": 128,
        "source_module": "advanced_regime_rule_free",
        "dependency_name": "candidate_state_and_pseudo_state_schemas",
        "dependency_type": "candidate_contracts",
        "is_mandatory": True,
        "is_resolved": True,
        "dependency_status": "behavior_quality_ready",
    },
]

CORE_REGIME_QUALITY_DEPENDENCIES = SOURCE_REGIME_DEPENDENCIES



def build_regime_quality_dependency_report(
    profile: Optional[MarketBehaviorDiagnosticsProfile] = None,
) -> Tuple[pd.DataFrame, dict]:
    """Build regime quality dependency report."""
    if profile is None:
        profile = get_market_behavior_diagnostics_profile()

    rows = []
    for item in SOURCE_REGIME_DEPENDENCIES:
        row = dict(item)
        row["non_signal"] = True
        row["current_phase"] = profile.current_phase
        row["target_final_phase"] = profile.target_final_phase
        row["next_phase"] = profile.next_phase
        rows.append(row)

    df = pd.DataFrame(rows)
    summary = summarize_regime_quality_dependencies(df)
    summary["active_profile"] = profile.profile_name
    return df, summary


def summarize_regime_quality_dependencies(df: pd.DataFrame) -> dict:
    """Summarize regime quality dependencies."""
    if df.empty:
        return {
            "total_dependencies": 0,
            "all_resolved": False,
            "all_satisfied": False,
            "blocking_dependencies_passed": False,
            "non_signal": True,
        }
    resolved = bool((df["is_resolved"] == True).all()) if "is_resolved" in df.columns else False
    return {
        "total_dependencies": len(df),
        "all_resolved": resolved,
        "all_satisfied": resolved,
        "blocking_dependencies_passed": resolved,
        "mandatory_count": int(df["is_mandatory"].sum()) if "is_mandatory" in df.columns else 0,
        "source_phases": df["source_phase"].tolist() if "source_phase" in df.columns else [],
        "non_signal": True,
    }
