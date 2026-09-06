"""Phase 134: Candidate State Store Catalog.

Connects Phase 128 rule-free candidate state preparations to the FeatureStore catalog.
"""

from typing import Any, Dict, List, Optional, Tuple
import pandas as pd

from advanced_regime_featurestore_integration.regime_featurestore_config import (
    RegimeFeatureStoreProfile,
    get_regime_featurestore_profile,
)
from advanced_regime_featurestore_integration.regime_featurestore_labels import (
    CANDIDATE_STATE_STORE_CATALOG_DOMAIN,
    REGIME_STORE_READY,
    STORE_ENTITY_CANDIDATE_STATE,
)

CANONICAL_CANDIDATE_STATE_ITEMS: List[Dict[str, Any]] = [
    {
        "store_catalog_name": "candidate_state_growth_inflation_prep",
        "store_entity_type": STORE_ENTITY_CANDIDATE_STATE,
        "source_phase": 128,
        "source_component": "advanced_regime_rule_free",
        "source_report_ref": "reports/output/advanced_regime_rule_free/report_balanced_local_regime_rule_free.json",
        "validation_acceptance_ref": "phase_133_gate_candidate_state_pass",
        "no_lookahead_accepted": True,
        "metadata_only_news_accepted": True,
        "source_preserved": True,
        "non_signal": True,
        "manual_review_required": False,
        "production_ready": False,
        "broker_ready": False,
    },
    {
        "store_catalog_name": "candidate_state_volatility_liquidity_prep",
        "store_entity_type": STORE_ENTITY_CANDIDATE_STATE,
        "source_phase": 128,
        "source_component": "advanced_regime_rule_free",
        "source_report_ref": "reports/output/advanced_regime_rule_free/report_balanced_local_regime_rule_free.json",
        "validation_acceptance_ref": "phase_133_gate_candidate_state_pass",
        "no_lookahead_accepted": True,
        "metadata_only_news_accepted": True,
        "source_preserved": True,
        "non_signal": True,
        "manual_review_required": False,
        "production_ready": False,
        "broker_ready": False,
    },
    {
        "store_catalog_name": "candidate_state_trend_range_prep",
        "store_entity_type": STORE_ENTITY_CANDIDATE_STATE,
        "source_phase": 128,
        "source_component": "advanced_regime_rule_free",
        "source_report_ref": "reports/output/advanced_regime_rule_free/report_balanced_local_regime_rule_free.json",
        "validation_acceptance_ref": "phase_133_gate_candidate_state_pass",
        "no_lookahead_accepted": True,
        "metadata_only_news_accepted": True,
        "source_preserved": True,
        "non_signal": True,
        "manual_review_required": False,
        "production_ready": False,
        "broker_ready": False,
    },
]


def build_candidate_state_store_catalog(
    profile: Optional[RegimeFeatureStoreProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Construct DataFrame and summary for candidate state store catalog."""
    active_profile = profile or get_regime_featurestore_profile()
    df = pd.DataFrame(CANONICAL_CANDIDATE_STATE_ITEMS)
    summary = {
        "domain": CANDIDATE_STATE_STORE_CATALOG_DOMAIN,
        "total_items": len(df),
        "active_profile": active_profile.profile_name,
        "source_phase": 128,
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


def summarize_candidate_state_store_catalog(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize candidate state catalog DataFrame."""
    return {
        "total_items": len(df),
        "catalog_names": df["store_catalog_name"].tolist() if not df.empty else [],
        "all_non_signal": bool((df["non_signal"] == True).all()) if not df.empty else True,
    }
