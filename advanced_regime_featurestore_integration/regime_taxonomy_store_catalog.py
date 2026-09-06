"""Phase 134: Regime Taxonomy Store Catalog.

Connects Phase 126 regime taxonomy specifications to the FeatureStore catalog.
"""

from typing import Any, Dict, List, Optional, Tuple
import pandas as pd

from advanced_regime_featurestore_integration.regime_featurestore_config import (
    RegimeFeatureStoreProfile,
    get_regime_featurestore_profile,
)
from advanced_regime_featurestore_integration.regime_featurestore_labels import (
    REGIME_STORE_READY,
    STORE_ENTITY_REGIME_TAXONOMY,
    TAXONOMY_STORE_CATALOG_DOMAIN,
)

CANONICAL_TAXONOMY_ITEMS: List[Dict[str, Any]] = [
    {
        "store_catalog_name": "regime_taxonomy_macro_growth_inflation",
        "store_entity_type": STORE_ENTITY_REGIME_TAXONOMY,
        "source_phase": 126,
        "source_component": "advanced_regime_foundation",
        "source_report_ref": "reports/output/advanced_regime_foundation/report_balanced_local_regime_foundation.json",
        "validation_acceptance_ref": "phase_133_gate_matrix_acceptance_pass",
        "no_lookahead_accepted": True,
        "metadata_only_news_accepted": True,
        "source_preserved": True,
        "non_signal": True,
        "manual_review_required": False,
        "production_ready": False,
        "broker_ready": False,
    },
    {
        "store_catalog_name": "regime_taxonomy_volatility_liquidity",
        "store_entity_type": STORE_ENTITY_REGIME_TAXONOMY,
        "source_phase": 126,
        "source_component": "advanced_regime_foundation",
        "source_report_ref": "reports/output/advanced_regime_foundation/report_balanced_local_regime_foundation.json",
        "validation_acceptance_ref": "phase_133_gate_matrix_acceptance_pass",
        "no_lookahead_accepted": True,
        "metadata_only_news_accepted": True,
        "source_preserved": True,
        "non_signal": True,
        "manual_review_required": False,
        "production_ready": False,
        "broker_ready": False,
    },
    {
        "store_catalog_name": "regime_taxonomy_trend_mean_reversion",
        "store_entity_type": STORE_ENTITY_REGIME_TAXONOMY,
        "source_phase": 126,
        "source_component": "advanced_regime_foundation",
        "source_report_ref": "reports/output/advanced_regime_foundation/report_balanced_local_regime_foundation.json",
        "validation_acceptance_ref": "phase_133_gate_matrix_acceptance_pass",
        "no_lookahead_accepted": True,
        "metadata_only_news_accepted": True,
        "source_preserved": True,
        "non_signal": True,
        "manual_review_required": False,
        "production_ready": False,
        "broker_ready": False,
    },
    {
        "store_catalog_name": "regime_taxonomy_risk_sentiment_tail",
        "store_entity_type": STORE_ENTITY_REGIME_TAXONOMY,
        "source_phase": 126,
        "source_component": "advanced_regime_foundation",
        "source_report_ref": "reports/output/advanced_regime_foundation/report_balanced_local_regime_foundation.json",
        "validation_acceptance_ref": "phase_133_gate_matrix_acceptance_pass",
        "no_lookahead_accepted": True,
        "metadata_only_news_accepted": True,
        "source_preserved": True,
        "non_signal": True,
        "manual_review_required": False,
        "production_ready": False,
        "broker_ready": False,
    },
]


def build_regime_taxonomy_store_catalog(
    profile: Optional[RegimeFeatureStoreProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Construct DataFrame and summary for regime taxonomy store catalog."""
    active_profile = profile or get_regime_featurestore_profile()
    df = pd.DataFrame(CANONICAL_TAXONOMY_ITEMS)
    summary = {
        "domain": TAXONOMY_STORE_CATALOG_DOMAIN,
        "total_items": len(df),
        "active_profile": active_profile.profile_name,
        "source_phase": 126,
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


def summarize_regime_taxonomy_store_catalog(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize taxonomy catalog DataFrame."""
    return {
        "total_items": len(df),
        "catalog_names": df["store_catalog_name"].tolist() if not df.empty else [],
        "all_non_signal": bool((df["non_signal"] == True).all()) if not df.empty else True,
    }
