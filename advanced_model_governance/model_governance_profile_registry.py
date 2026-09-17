# -*- coding: utf-8 -*-
"""Phase 144: Model Governance Profile Registry."""

from typing import Any, Dict, Optional, Tuple
import pandas as pd
from advanced_model_governance.model_governance_config import (
    PROFILES,
    ModelGovernanceProfile,
    get_model_governance_profile,
)


def build_model_governance_profile_registry(
    profile: Optional[ModelGovernanceProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and summary for all model governance profiles."""
    prof = profile or get_model_governance_profile()
    records = []
    for p_name, p in PROFILES.items():
        records.append({
            "profile_name": p.profile_name,
            "display_name": p.display_name,
            "description": p.description,
            "current_phase": p.current_phase,
            "target_final_phase": p.target_final_phase,
            "next_phase": p.next_phase,
            "dry_run_default": p.dry_run_default,
            "local_only": p.local_only,
            "non_production": p.non_production,
            "research_only": p.research_only,
            "min_readiness_score": p.min_readiness_score,
            "allow_live_trading": p.allow_live_trading,
            "allow_broker_integration": p.allow_broker_integration,
            "allow_real_order": p.allow_real_order,
            "allow_investment_advice": p.allow_investment_advice,
            "allow_model_training": p.allow_model_training,
            "allow_model_predict": p.allow_model_predict,
            "allow_model_registry_write": p.allow_model_registry_write,
            "allow_artifact_persistence": p.allow_artifact_persistence,
            "allow_production_approval": p.allow_production_approval,
            "allow_broker_ready_approval": p.allow_broker_ready_approval,
            "allow_live_trading_approval": p.allow_live_trading_approval,
            "allow_official_approval_claim": p.allow_official_approval_claim,
            "allow_release_approval": p.allow_release_approval,
            "allow_real_audit_log": p.allow_real_audit_log,
            "is_active": (p.profile_name == prof.profile_name),
        })

    df = pd.DataFrame(records)
    summary = {
        "total_profiles": len(df),
        "active_profile": prof.profile_name,
        "current_phase": prof.current_phase,
        "target_final_phase": prof.target_final_phase,
        "all_local_only": bool(df["local_only"].all()),
        "all_non_production": bool(df["non_production"].all()),
        "all_trading_prohibited": not bool(df["allow_live_trading"].any()),
        "all_registry_write_prohibited": not bool(df["allow_model_registry_write"].any()),
        "all_approval_prohibited": not bool(df["allow_production_approval"].any()),
    }
    return df, summary
