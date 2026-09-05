"""Phase 124 Feature Store Integration Domain Registry."""

from typing import Any, Dict, Optional, Tuple
import pandas as pd

from advanced_feature_store_integration.feature_store_integration_config import (
    FeatureStoreIntegrationProfile,
    get_default_feature_store_integration_profile,
)
from advanced_feature_store_integration.feature_store_integration_labels import (
    FEATURE_STORE_INTEGRATION_DOMAIN_LABELS,
)


def build_feature_store_integration_domain_registry(
    profile: Optional[FeatureStoreIntegrationProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build registry of integration domains."""
    prof = profile or get_default_feature_store_integration_profile()
    records = []
    for idx, domain_name in enumerate(FEATURE_STORE_INTEGRATION_DOMAIN_LABELS, start=1):
        records.append({
            "domain_id": f"DOM_{idx:03d}",
            "domain_name": domain_name,
            "phase": prof.current_phase,
            "non_signal": True,
            "source_preserved": True,
            "destructive_action_allowed": False,
            "status": "active",
        })

    df = pd.DataFrame(records)
    summary = {
        "total_domains": len(records),
        "phase": prof.current_phase,
        "target_final_phase": prof.target_final_phase,
        "next_phase": prof.next_phase,
        "non_signal": True,
        "source_preserved": True,
    }
    return df, summary


def summarize_feature_store_integration_domain_registry(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize domain registry."""
    return {
        "total_domains": len(df) if not df.empty else 0,
        "non_signal": True,
        "source_preserved": True,
    }
