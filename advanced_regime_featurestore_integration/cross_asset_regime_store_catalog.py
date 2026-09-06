"""Phase 134: Cross-Asset Regime Store Catalog.

Connects Phase 131 cross-asset regime alignment and divergence context to the FeatureStore catalog.
"""

from typing import Any, Dict, List, Optional, Tuple
import pandas as pd

from advanced_regime_featurestore_integration.regime_featurestore_config import (
    RegimeFeatureStoreProfile,
    get_regime_featurestore_profile,
)
from advanced_regime_featurestore_integration.regime_featurestore_labels import (
    CROSS_ASSET_STORE_CATALOG_DOMAIN,
    REGIME_STORE_READY,
    STORE_ENTITY_CROSS_ASSET_CONTEXT,
)

CANONICAL_CROSS_ASSET_ITEMS: List[Dict[str, Any]] = [
    {
        "store_catalog_name": "cross_asset_commodity_macro_context",
        "store_entity_type": STORE_ENTITY_CROSS_ASSET_CONTEXT,
        "source_phase": 131,
        "source_component": "advanced_cross_asset_regime_context",
        "source_report_ref": "reports/output/advanced_cross_asset_regime_context/report_balanced_local_cross_asset_regime_context.json",
        "validation_acceptance_ref": "phase_133_gate_cross_asset_acceptance_pass",
        "no_lookahead_accepted": True,
        "metadata_only_news_accepted": True,
        "source_preserved": True,
        "non_signal": True,
        "manual_review_required": False,
        "production_ready": False,
        "broker_ready": False,
    },
    {
        "store_catalog_name": "cross_asset_fx_commodity_context",
        "store_entity_type": STORE_ENTITY_CROSS_ASSET_CONTEXT,
        "source_phase": 131,
        "source_component": "advanced_cross_asset_regime_context",
        "source_report_ref": "reports/output/advanced_cross_asset_regime_context/report_balanced_local_cross_asset_regime_context.json",
        "validation_acceptance_ref": "phase_133_gate_cross_asset_acceptance_pass",
        "no_lookahead_accepted": True,
        "metadata_only_news_accepted": True,
        "source_preserved": True,
        "non_signal": True,
        "manual_review_required": False,
        "production_ready": False,
        "broker_ready": False,
    },
    {
        "store_catalog_name": "cross_asset_fx_macro_context",
        "store_entity_type": STORE_ENTITY_CROSS_ASSET_CONTEXT,
        "source_phase": 131,
        "source_component": "advanced_cross_asset_regime_context",
        "source_report_ref": "reports/output/advanced_cross_asset_regime_context/report_balanced_local_cross_asset_regime_context.json",
        "validation_acceptance_ref": "phase_133_gate_cross_asset_acceptance_pass",
        "no_lookahead_accepted": True,
        "metadata_only_news_accepted": True,
        "source_preserved": True,
        "non_signal": True,
        "manual_review_required": False,
        "production_ready": False,
        "broker_ready": False,
    },
]


def build_cross_asset_regime_store_catalog(
    profile: Optional[RegimeFeatureStoreProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Construct DataFrame and summary for cross-asset regime store catalog."""
    active_profile = profile or get_regime_featurestore_profile()
    df = pd.DataFrame(CANONICAL_CROSS_ASSET_ITEMS)
    summary = {
        "domain": CROSS_ASSET_STORE_CATALOG_DOMAIN,
        "total_items": len(df),
        "active_profile": active_profile.profile_name,
        "source_phase": 131,
        "current_phase": 134,
        "target_final_phase": 160,
        "next_phase": 135,
        "all_non_signal": bool((df["non_signal"] == True).all()),
        "all_source_preserved": bool((df["source_preserved"] == True).all()),
        "production_ready": False,
        "broker_ready": False,
        "status": REGIME_STORE_READY,
    }
    return df, summary


def summarize_cross_asset_regime_store_catalog(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize cross-asset regime catalog DataFrame."""
    return {
        "total_items": len(df),
        "catalog_names": df["store_catalog_name"].tolist() if not df.empty else [],
        "all_non_signal": bool((df["non_signal"] == True).all()) if not df.empty else True,
    }
