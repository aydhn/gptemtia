"""Phase 134: Regime FeatureStore Source Preservation Policies.

Enforces absolute immutability of existing upstream source datasets.
Prohibits file overwrite, deletion, moving, destructive cleaning, auto-imputation, and auto-feature-drop.
"""

from typing import Any, Dict, List, Optional, Tuple
import pandas as pd

from advanced_regime_featurestore_integration.regime_featurestore_config import (
    RegimeFeatureStoreProfile,
    get_regime_featurestore_profile,
)
from advanced_regime_featurestore_integration.regime_featurestore_labels import (
    REGIME_STORE_READY,
    SOURCE_PRESERVATION_POLICY_DOMAIN,
)

PROHIBITED_SOURCE_ACTIONS: List[Dict[str, Any]] = [
    {"action_name": "overwrite_source", "description": "Modifying or overwriting existing upstream files"},
    {"action_name": "delete_source", "description": "Deleting historical regime files"},
    {"action_name": "move_source", "description": "Relocating existing dataset paths"},
    {"action_name": "destructive_clean", "description": "Pruning or truncating existing records permanently"},
    {"action_name": "auto_impute_overwrite", "description": "Replacing missing values in source datasets automatically"},
    {"action_name": "auto_drop_feature", "description": "Dropping columns from source dataframes automatically"},
    {"action_name": "mutate_input_dataframe", "description": "In-place mutation of input DataFrames"},
]


def build_regime_featurestore_source_preservation_policy_registry(
    profile: Optional[RegimeFeatureStoreProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Construct DataFrame and summary for source preservation policies."""
    active_profile = profile or get_regime_featurestore_profile()
    df = pd.DataFrame(PROHIBITED_SOURCE_ACTIONS)
    summary = {
        "domain": SOURCE_PRESERVATION_POLICY_DOMAIN,
        "total_prohibited_actions": len(df),
        "active_profile": active_profile.profile_name,
        "current_phase": 134,
        "target_final_phase": 160,
        "next_phase": 135,
        "status": REGIME_STORE_READY,
        "source_preserved": True,
        "non_signal": True,
    }
    return df, summary


def validate_regime_featurestore_source_preservation_action(action: str) -> Dict[str, Any]:
    """Validate whether an attempted file/data action violates source preservation."""
    prohibited_names = {item["action_name"].lower() for item in PROHIBITED_SOURCE_ACTIONS}
    is_prohibited = action.lower() in prohibited_names

    return {
        "action": action,
        "is_permitted": not is_prohibited,
        "is_prohibited": is_prohibited,
        "source_preserved": not is_prohibited,
    }


def summarize_regime_featurestore_source_preservation_policies(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize source preservation policy DataFrame."""
    return {
        "total_prohibited_actions": len(df),
        "action_names": df["action_name"].tolist() if not df.empty else [],
        "all_prohibited": True,
    }
