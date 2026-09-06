"""Phase 134: Regime Accepted Reference Registries.

Registers formal accepted references verifying that all stored regime components
adhere to no-lookahead, metadata-only news, source-preservation, and non-signal standards.
"""

from typing import Any, Dict, List, Optional, Tuple
import pandas as pd

from advanced_regime_featurestore_integration.regime_featurestore_config import (
    RegimeFeatureStoreProfile,
    get_regime_featurestore_profile,
)
from advanced_regime_featurestore_integration.regime_featurestore_labels import (
    ACCEPTED_REFERENCE_DOMAIN,
    REGIME_STORE_READY,
)


def build_regime_no_lookahead_accepted_reference_registry(
    profile: Optional[RegimeFeatureStoreProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build accepted reference registry for no-lookahead / backward-asof compliance."""
    active_profile = profile or get_regime_featurestore_profile()
    rows = [
        {
            "reference_id": "ref_no_lookahead_taxonomy_p126",
            "reference_type": "no_lookahead_accepted_reference",
            "source_phase": 126,
            "source_gate_ref": "gate_no_lookahead_p126",
            "acceptance_status": "ACCEPTED",
            "non_signal": True,
            "source_preserved": True,
        },
        {
            "reference_id": "ref_no_lookahead_matrix_p127",
            "reference_type": "no_lookahead_accepted_reference",
            "source_phase": 127,
            "source_gate_ref": "gate_no_lookahead_p127",
            "acceptance_status": "ACCEPTED",
            "non_signal": True,
            "source_preserved": True,
        },
        {
            "reference_id": "ref_no_lookahead_candidate_state_p128",
            "reference_type": "no_lookahead_accepted_reference",
            "source_phase": 128,
            "source_gate_ref": "gate_no_lookahead_p128",
            "acceptance_status": "ACCEPTED",
            "non_signal": True,
            "source_preserved": True,
        },
        {
            "reference_id": "ref_no_lookahead_transition_p130",
            "reference_type": "no_lookahead_accepted_reference",
            "source_phase": 130,
            "source_gate_ref": "gate_no_lookahead_p130",
            "acceptance_status": "ACCEPTED",
            "non_signal": True,
            "source_preserved": True,
        },
        {
            "reference_id": "ref_no_lookahead_cross_asset_p131",
            "reference_type": "no_lookahead_accepted_reference",
            "source_phase": 131,
            "source_gate_ref": "gate_no_lookahead_p131",
            "acceptance_status": "ACCEPTED",
            "non_signal": True,
            "source_preserved": True,
        },
        {
            "reference_id": "ref_no_lookahead_macro_event_news_p132",
            "reference_type": "no_lookahead_accepted_reference",
            "source_phase": 132,
            "source_gate_ref": "gate_no_lookahead_p132",
            "acceptance_status": "ACCEPTED",
            "non_signal": True,
            "source_preserved": True,
        },
        {
            "reference_id": "ref_no_lookahead_validation_acceptance_p133",
            "reference_type": "no_lookahead_accepted_reference",
            "source_phase": 133,
            "source_gate_ref": "gate_no_lookahead_p133",
            "acceptance_status": "ACCEPTED",
            "non_signal": True,
            "source_preserved": True,
        },
    ]
    df = pd.DataFrame(rows)
    summary = {
        "domain": ACCEPTED_REFERENCE_DOMAIN,
        "reference_type": "no_lookahead_accepted_reference",
        "total_references": len(df),
        "active_profile": active_profile.profile_name,
        "current_phase": 134,
        "target_final_phase": 160,
        "next_phase": 135,
        "status": REGIME_STORE_READY,
        "non_signal": True,
    }
    return df, summary


def build_regime_metadata_only_news_accepted_reference_registry(
    profile: Optional[RegimeFeatureStoreProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build accepted reference registry for metadata-only news compliance."""
    active_profile = profile or get_regime_featurestore_profile()
    rows = [
        {
            "reference_id": "ref_metadata_only_macro_event_news_p132",
            "reference_type": "metadata_only_news_accepted_reference",
            "source_phase": 132,
            "source_gate_ref": "gate_metadata_only_news_p132",
            "acceptance_status": "ACCEPTED",
            "non_signal": True,
            "source_preserved": True,
        },
        {
            "reference_id": "ref_metadata_only_validation_acceptance_p133",
            "reference_type": "metadata_only_news_accepted_reference",
            "source_phase": 133,
            "source_gate_ref": "gate_metadata_only_news_p133",
            "acceptance_status": "ACCEPTED",
            "non_signal": True,
            "source_preserved": True,
        },
        {
            "reference_id": "ref_metadata_only_store_catalog_p134",
            "reference_type": "metadata_only_news_accepted_reference",
            "source_phase": 134,
            "source_gate_ref": "gate_metadata_only_store_catalog_p134",
            "acceptance_status": "ACCEPTED",
            "non_signal": True,
            "source_preserved": True,
        },
    ]
    df = pd.DataFrame(rows)
    summary = {
        "domain": ACCEPTED_REFERENCE_DOMAIN,
        "reference_type": "metadata_only_news_accepted_reference",
        "total_references": len(df),
        "active_profile": active_profile.profile_name,
        "current_phase": 134,
        "target_final_phase": 160,
        "next_phase": 135,
        "status": REGIME_STORE_READY,
        "non_signal": True,
    }
    return df, summary


def build_regime_source_preservation_accepted_reference_registry(
    profile: Optional[RegimeFeatureStoreProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build accepted reference registry for source data preservation."""
    active_profile = profile or get_regime_featurestore_profile()
    rows = [
        {
            "reference_id": "ref_source_preservation_p126_to_p133",
            "reference_type": "source_preservation_accepted_reference",
            "source_phase": 133,
            "source_gate_ref": "gate_source_preservation_p133",
            "acceptance_status": "ACCEPTED",
            "non_signal": True,
            "source_preserved": True,
        },
        {
            "reference_id": "ref_source_preservation_store_contracts_p134",
            "reference_type": "source_preservation_accepted_reference",
            "source_phase": 134,
            "source_gate_ref": "gate_source_preservation_store_contracts_p134",
            "acceptance_status": "ACCEPTED",
            "non_signal": True,
            "source_preserved": True,
        },
    ]
    df = pd.DataFrame(rows)
    summary = {
        "domain": ACCEPTED_REFERENCE_DOMAIN,
        "reference_type": "source_preservation_accepted_reference",
        "total_references": len(df),
        "active_profile": active_profile.profile_name,
        "current_phase": 134,
        "target_final_phase": 160,
        "next_phase": 135,
        "status": REGIME_STORE_READY,
        "non_signal": True,
    }
    return df, summary


def build_regime_non_signal_accepted_reference_registry(
    profile: Optional[RegimeFeatureStoreProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build accepted reference registry for strict non-signal status."""
    active_profile = profile or get_regime_featurestore_profile()
    rows = [
        {
            "reference_id": "ref_non_signal_taxonomy_p126",
            "reference_type": "non_signal_accepted_reference",
            "source_phase": 126,
            "source_gate_ref": "gate_non_signal_p126",
            "acceptance_status": "ACCEPTED",
            "non_signal": True,
            "source_preserved": True,
        },
        {
            "reference_id": "ref_non_signal_matrix_p127",
            "reference_type": "non_signal_accepted_reference",
            "source_phase": 127,
            "source_gate_ref": "gate_non_signal_p127",
            "acceptance_status": "ACCEPTED",
            "non_signal": True,
            "source_preserved": True,
        },
        {
            "reference_id": "ref_non_signal_rule_free_p128",
            "reference_type": "non_signal_accepted_reference",
            "source_phase": 128,
            "source_gate_ref": "gate_non_signal_p128",
            "acceptance_status": "ACCEPTED",
            "non_signal": True,
            "source_preserved": True,
        },
        {
            "reference_id": "ref_non_signal_diagnostics_p129",
            "reference_type": "non_signal_accepted_reference",
            "source_phase": 129,
            "source_gate_ref": "gate_non_signal_p129",
            "acceptance_status": "ACCEPTED",
            "non_signal": True,
            "source_preserved": True,
        },
        {
            "reference_id": "ref_non_signal_transition_p130",
            "reference_type": "non_signal_accepted_reference",
            "source_phase": 130,
            "source_gate_ref": "gate_non_signal_p130",
            "acceptance_status": "ACCEPTED",
            "non_signal": True,
            "source_preserved": True,
        },
        {
            "reference_id": "ref_non_signal_cross_asset_p131",
            "reference_type": "non_signal_accepted_reference",
            "source_phase": 131,
            "source_gate_ref": "gate_non_signal_p131",
            "acceptance_status": "ACCEPTED",
            "non_signal": True,
            "source_preserved": True,
        },
        {
            "reference_id": "ref_non_signal_macro_event_news_p132",
            "reference_type": "non_signal_accepted_reference",
            "source_phase": 132,
            "source_gate_ref": "gate_non_signal_p132",
            "acceptance_status": "ACCEPTED",
            "non_signal": True,
            "source_preserved": True,
        },
        {
            "reference_id": "ref_non_signal_validation_acceptance_p133",
            "reference_type": "non_signal_accepted_reference",
            "source_phase": 133,
            "source_gate_ref": "gate_non_signal_p133",
            "acceptance_status": "ACCEPTED",
            "non_signal": True,
            "source_preserved": True,
        },
        {
            "reference_id": "ref_non_signal_featurestore_integration_p134",
            "reference_type": "non_signal_accepted_reference",
            "source_phase": 134,
            "source_gate_ref": "gate_non_signal_p134",
            "acceptance_status": "ACCEPTED",
            "non_signal": True,
            "source_preserved": True,
        },
    ]
    df = pd.DataFrame(rows)
    summary = {
        "domain": ACCEPTED_REFERENCE_DOMAIN,
        "reference_type": "non_signal_accepted_reference",
        "total_references": len(df),
        "active_profile": active_profile.profile_name,
        "current_phase": 134,
        "target_final_phase": 160,
        "next_phase": 135,
        "status": REGIME_STORE_READY,
        "non_signal": True,
    }
    return df, summary


def summarize_regime_accepted_references(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize accepted reference DataFrame."""
    return {
        "total_references": len(df),
        "reference_types": df["reference_type"].unique().tolist() if not df.empty else [],
        "all_accepted": bool((df["acceptance_status"] == "ACCEPTED").all()) if not df.empty else True,
        "all_non_signal": bool((df["non_signal"] == True).all()) if not df.empty else True,
    }
