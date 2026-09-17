# -*- coding: utf-8 -*-
"""Phase 144: Governance Model Version Placeholders Registry."""

from typing import Any, Dict, List, Optional, Tuple
import pandas as pd
from advanced_model_governance.model_governance_config import (
    ModelGovernanceProfile,
    get_model_governance_profile,
)

VERSION_ITEMS: List[Dict[str, str]] = [
    {"version_id": "VER-144-01", "model_name": "baseline_linear_ridge", "contract_version": "v1.0.0-contract", "is_deployed": "NO", "notes": "Dry-run interface contract only."},
    {"version_id": "VER-144-02", "model_name": "candidate_lightgbm_regressor", "contract_version": "v1.0.0-contract", "is_deployed": "NO", "notes": "Dry-run interface contract only."},
    {"version_id": "VER-144-03", "model_name": "ensemble_stacking_meta", "contract_version": "v1.0.0-contract", "is_deployed": "NO", "notes": "Dry-run interface contract only."},
]


def build_governance_model_version_placeholder_registry(
    profile: Optional[ModelGovernanceProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and summary for model version placeholders."""
    prof = profile or get_model_governance_profile()
    records = []
    for item in VERSION_ITEMS:
        row = dict(item)
        row["phase"] = prof.current_phase
        row["is_placeholder"] = True
        row["deployed"] = False
        row["non_signal"] = True
        records.append(row)

    df = pd.DataFrame(records)
    summary = summarize_governance_model_version_placeholders(df)
    return df, summary


def summarize_governance_model_version_placeholders(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize model version placeholders."""
    return {
        "total_versions": len(df),
        "zero_deployed": not bool(df["deployed"].any()),
        "status": "VERSION_PLACEHOLDER_READY",
    }
