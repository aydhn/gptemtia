# -*- coding: utf-8 -*-
"""Phase 144: Model Governance Domain Registry."""

from typing import Any, Dict, Optional, Tuple
import pandas as pd
from advanced_model_governance.model_governance_config import (
    ModelGovernanceProfile,
    get_model_governance_profile,
)
from advanced_model_governance.model_governance_labels import (
    MODEL_GOVERNANCE_DOMAIN_LABELS,
)


def build_model_governance_domain_registry(
    profile: Optional[ModelGovernanceProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and summary for all model governance domains."""
    prof = profile or get_model_governance_profile()
    records = []
    for domain in MODEL_GOVERNANCE_DOMAIN_LABELS:
        records.append({
            "domain_name": domain,
            "phase": prof.current_phase,
            "is_active": True,
            "dry_run_only": prof.dry_run_default,
            "non_production": prof.non_production,
            "requires_manual_review": True,
            "execution_disabled": True,
            "non_signal": True,
        })

    df = pd.DataFrame(records)
    summary = {
        "total_domains": len(df),
        "phase": prof.current_phase,
        "all_dry_run": bool(df["dry_run_only"].all()),
        "all_non_production": bool(df["non_production"].all()),
        "all_non_signal": bool(df["non_signal"].all()),
    }
    return df, summary
