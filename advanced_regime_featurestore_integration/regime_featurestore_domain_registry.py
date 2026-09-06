"""Phase 134: Regime FeatureStore Domain Registry.

Registers all operational domains within the Regime FeatureStore integration layer.
"""

from typing import Any, Dict, Optional, Tuple
import pandas as pd

from advanced_regime_featurestore_integration.regime_featurestore_config import (
    RegimeFeatureStoreProfile,
    get_regime_featurestore_profile,
)
from advanced_regime_featurestore_integration.regime_featurestore_labels import (
    ALL_DOMAINS,
    REGIME_FEATURESTORE_DOMAIN,
    REGIME_STORE_READY,
)


def build_regime_featurestore_domain_registry(
    profile: Optional[RegimeFeatureStoreProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Construct tabular domain registry covering all Phase 134 operational domains."""
    active_profile = profile or get_regime_featurestore_profile()

    rows = []
    for domain_name in sorted(list(ALL_DOMAINS)):
        rows.append({
            "domain_name": domain_name,
            "category": domain_name.replace("_domain", ""),
            "current_phase": 134,
            "target_final_phase": 160,
            "next_phase": 135,
            "non_signal": True,
            "source_preserved": True,
            "production_ready": False,
            "broker_ready": False,
            "status": REGIME_STORE_READY,
        })

    df = pd.DataFrame(rows)
    summary = {
        "domain": REGIME_FEATURESTORE_DOMAIN,
        "total_domains": len(rows),
        "active_profile": active_profile.profile_name,
        "current_phase": 134,
        "target_final_phase": 160,
        "next_phase": 135,
        "status": REGIME_STORE_READY,
        "non_signal": True,
    }
    return df, summary


def summarize_regime_featurestore_domain_registry(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize domain registry DataFrame."""
    return {
        "total_domains": len(df),
        "domain_names": df["domain_name"].tolist() if not df.empty else [],
        "all_non_signal": bool((df["non_signal"] == True).all()) if not df.empty else True,
    }
