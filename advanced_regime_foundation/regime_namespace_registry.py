"""Phase 126: Regime Namespace Registry.

Enforces standardized lowercase snake_case naming conventions with mandatory regime_state_ prefix.
Blocks all forbidden trade words and prediction labels.
"""

import re
from typing import Any, Dict, List, Optional, Tuple
import pandas as pd

from advanced_regime_foundation.regime_foundation_config import (
    RegimeFoundationProfile,
    get_default_regime_foundation_profile,
)

FORBIDDEN_NAMESPACE_WORDS: List[str] = [
    "signal",
    "buy",
    "sell",
    "long",
    "short",
    "position",
    "target",
    "label",
    "prediction",
    "recommendation",
    "future_return",
    "forward_return",
    "next_return",
]

CANONICAL_NAMESPACES: List[Dict[str, Any]] = [
    {
        "namespace_id": "ns_01_trend",
        "pattern": "^regime_state_trend_[a-z0-9_]+$",
        "regime_family": "regime_family_trend",
        "example": "regime_state_trend_context",
        "description": "Namespace for trend regime state variables",
        "non_signal": True,
    },
    {
        "namespace_id": "ns_02_range",
        "pattern": "^regime_state_range_[a-z0-9_]+$",
        "regime_family": "regime_family_range",
        "example": "regime_state_range_context",
        "description": "Namespace for range regime state variables",
        "non_signal": True,
    },
    {
        "namespace_id": "ns_03_volatility",
        "pattern": "^regime_state_volatility_[a-z0-9_]+$",
        "regime_family": "regime_family_volatility",
        "example": "regime_state_volatility_high_context",
        "description": "Namespace for volatility regime state variables",
        "non_signal": True,
    },
    {
        "namespace_id": "ns_04_macro",
        "pattern": "^regime_state_macro_[a-z0-9_]+$",
        "regime_family": "regime_family_macro_context",
        "example": "regime_state_macro_event_context",
        "description": "Namespace for macro regime context variables",
        "non_signal": True,
    },
    {
        "namespace_id": "ns_05_news",
        "pattern": "^regime_state_news_[a-z0-9_]+$",
        "regime_family": "regime_family_news_metadata_context",
        "example": "regime_state_news_attention_context",
        "description": "Namespace for news metadata regime variables",
        "non_signal": True,
    },
    {
        "namespace_id": "ns_06_cross_asset",
        "pattern": "^regime_state_cross_asset_[a-z0-9_]+$",
        "regime_family": "regime_family_cross_asset_context",
        "example": "regime_state_cross_asset_context",
        "description": "Namespace for cross-asset regime variables",
        "non_signal": True,
    },
    {
        "namespace_id": "ns_07_transition",
        "pattern": "^regime_state_transition_[a-z0-9_]+$",
        "regime_family": "regime_family_composite_placeholder",
        "example": "regime_state_transition_placeholder",
        "description": "Namespace for transition placeholder variables",
        "non_signal": True,
    },
    {
        "namespace_id": "ns_08_uncertain",
        "pattern": "^regime_state_uncertain_[a-z0-9_]+$",
        "regime_family": "regime_family_composite_placeholder",
        "example": "regime_state_uncertain_placeholder",
        "description": "Namespace for uncertain diagnosis variables",
        "non_signal": True,
    },
]


def build_regime_state_name(regime_family: str, state_name: str) -> str:
    """Build a canonical regime state name complying with namespace rules."""
    clean_state = state_name.strip().lower().replace("-", "_").replace(" ", "_")
    if clean_state.startswith("regime_state_"):
        candidate = clean_state
    else:
        # Extract base family token if prefixed with regime_family_
        family_clean = regime_family.replace("regime_family_", "")
        candidate = f"regime_state_{family_clean}_{clean_state}"

    validation = validate_regime_state_name(candidate)
    if not validation["is_valid"]:
        raise ValueError(f"Constructed regime state name is invalid: {validation['issues']}")
    return candidate


def validate_regime_state_name(name: str) -> Dict[str, Any]:
    """Validate regime state name against canonical rules and forbidden words."""
    issues = []
    if not name:
        return {"is_valid": False, "issues": ["Name cannot be empty"], "name": name}

    # Must be lowercase snake_case
    if not re.match(r"^[a-z0-9_]+$", name):
        issues.append("Name must be lowercase snake_case alphanumeric characters and underscores")

    # Mandatory prefix
    if not name.startswith("regime_state_"):
        issues.append("Name must start with mandatory prefix 'regime_state_'")

    # Forbidden word check
    name_lower = name.lower()
    for forbidden in FORBIDDEN_NAMESPACE_WORDS:
        if forbidden in name_lower:
            issues.append(f"Name contains forbidden trade or prediction keyword: '{forbidden}'")

    return {
        "name": name,
        "is_valid": len(issues) == 0,
        "issues": issues,
        "non_signal": True,
    }


def build_regime_namespace_registry(
    profile: Optional[RegimeFoundationProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and summary for regime namespace registry."""
    active_profile = profile or get_default_regime_foundation_profile()
    df = pd.DataFrame(CANONICAL_NAMESPACES)
    summary = {
        "active_profile": active_profile.profile_name,
        "total_namespaces": len(df),
        "mandatory_prefix": "regime_state_",
        "all_non_signal": bool((df["non_signal"] == True).all()),
        "current_phase": active_profile.current_phase,
        "target_final_phase": active_profile.target_final_phase,
        "next_phase": active_profile.next_phase,
        "official_approval": False,
        "production_ready": False,
        "broker_ready": False,
    }
    return df, summary


def summarize_regime_namespace_registry(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize regime namespace registry DataFrame."""
    return {
        "total_namespaces": len(df),
        "patterns": list(df["pattern"].unique()) if "pattern" in df.columns else [],
        "mandatory_prefix": "regime_state_",
        "non_signal": True,
    }
