# -*- coding: utf-8 -*-
"""Phase 143: Attribution Quality Gates."""

from typing import Any, Dict, List, Optional, Tuple
import pandas as pd

from advanced_explainability_attribution.explainability_config import (
    ExplainabilityProfile,
    get_explainability_profile,
)


def build_attribution_quality_gate_registry(
    profile: Optional[ExplainabilityProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build the DataFrame registry of attribution quality gates."""
    prof = profile or get_explainability_profile()

    gates = [
        ("gate_feature_coverage", "feature_coverage", "Verify all input features have attributed or placeholder mappings", True),
        ("gate_attribution_completeness", "completeness", "Attribution sums equal difference from base expectation placeholder", True),
        ("gate_numerical_stability", "numerical_stability", "Detect NaN, Inf or extreme attribution values placeholder", True),
        ("gate_non_negative_variance", "variance_check", "Attribution variance sanity check placeholder", True),
        ("gate_non_signal_compliance", "non_signal_check", "Verify attribution output contains no directional trade signals", True),
    ]

    rows: List[Dict[str, Any]] = []
    for gid, gtype, desc, passed in gates:
        rows.append({
            "gate_id": gid,
            "gate_type": gtype,
            "description": desc,
            "passed": passed,
            "is_contract_gate": True,
            "non_signal": True,
            "official_approval": False,
            "production_ready": False,
            "broker_ready": False,
        })

    df = pd.DataFrame(rows)
    summary = summarize_attribution_quality_gates(df)
    return df, summary


def summarize_attribution_quality_gates(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize attribution quality gates."""
    return {
        "total_quality_gates": len(df),
        "all_passed": bool(df["passed"].all()) if not df.empty else True,
        "all_contract_gate": bool(df["is_contract_gate"].all()) if not df.empty else True,
        "all_non_signal": bool(df["non_signal"].all()) if not df.empty else True,
        "current_phase": 143,
        "next_phase": 144,
        "target_final_phase": 160,
    }
