"""Phase 133: Regime Validation Acceptance Domain Registry."""

from typing import Any, Dict, Optional, Tuple
import pandas as pd

from advanced_regime_validation_acceptance.regime_validation_acceptance_config import (
    RegimeValidationAcceptanceProfile,
    get_default_regime_validation_acceptance_profile,
)
from advanced_regime_validation_acceptance.regime_validation_acceptance_labels import (
    list_regime_validation_acceptance_domain_labels,
)


def build_regime_validation_acceptance_domain_registry(
    profile: Optional[RegimeValidationAcceptanceProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build registry DataFrame of functional domains in Phase 133."""
    p = profile or get_default_regime_validation_acceptance_profile()
    domain_labels = list_regime_validation_acceptance_domain_labels()

    rows = []
    for idx, domain_label in enumerate(domain_labels):
        category = "core"
        if "gate" in domain_label:
            category = "gates"
        elif "lookahead" in domain_label or "timestamp" in domain_label or "backward" in domain_label:
            category = "temporal_integrity"
        elif "forbidden" in domain_label or "news" in domain_label or "source" in domain_label:
            category = "data_boundaries"
        elif "signal" in domain_label or "prediction" in domain_label or "execution" in domain_label:
            category = "absence_assurance"
        elif "matrix" in domain_label or "state" in domain_label or "transition" in domain_label or "cross_asset" in domain_label or "macro" in domain_label:
            category = "component_acceptance"
        elif "dependency" in domain_label:
            category = "dependency_acceptance"
        elif "finding" in domain_label or "review" in domain_label or "score" in domain_label:
            category = "findings_scoring"
        elif "manifest" in domain_label or "handoff" in domain_label or "health" in domain_label or "safety" in domain_label or "validation" in domain_label:
            category = "audit_manifest"

        rows.append(
            {
                "domain_index": idx + 1,
                "domain_label": domain_label,
                "category": category,
                "profile_name": p.profile_name,
                "non_signal": True,
                "source_preserved": True,
                "official_approval": False,
                "production_ready": False,
                "broker_ready": False,
            }
        )
    df = pd.DataFrame(rows)
    summary = {
        "total_domains": len(df),
        "profile_name": p.profile_name,
        "all_non_signal": True,
        "all_source_preserved": True,
    }
    return df, summary


def summarize_regime_validation_acceptance_domains(df: pd.DataFrame) -> Dict[str, Any]:
    """Return summary dictionary for domain registry DataFrame."""
    return {
        "total_domains": len(df),
        "all_non_signal": bool(df["non_signal"].all()) if "non_signal" in df.columns else True,
        "all_source_preserved": bool(df["source_preserved"].all()) if "source_preserved" in df.columns else True,
    }
