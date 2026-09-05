"""Phase 126: Regime Non-Signal Policies.

Defines non-signal governance policies ensuring regime outputs are never treated as trading signals.
"""

import re
from typing import Any, Dict, List, Optional, Tuple
import pandas as pd

from advanced_regime_foundation.regime_foundation_config import (
    RegimeFoundationProfile,
    get_default_regime_foundation_profile,
)

NON_SIGNAL_POLICIES: List[Dict[str, Any]] = [
    {
        "policy_id": "nsp_01_no_trade_instructions",
        "policy_name": "prohibit_trade_instructions",
        "statement": "Regime state outputs shall never generate BUY/SELL orders or long/short recommendations",
        "enforcement": "MANDATORY_INVARIANT",
        "non_signal": True,
    },
    {
        "policy_id": "nsp_02_context_only",
        "policy_name": "environmental_context_only",
        "statement": "Regimes represent environmental volatility, trend, and macro conditions, not market entry triggers",
        "enforcement": "MANDATORY_INVARIANT",
        "non_signal": True,
    },
    {
        "policy_id": "nsp_03_no_directional_certainty",
        "policy_name": "prohibit_directional_certainty",
        "statement": "Taxonomy terms such as bullish/bearish are prohibited in favor of persistent or reverting context",
        "enforcement": "MANDATORY_INVARIANT",
        "non_signal": True,
    },
    {
        "policy_id": "nsp_04_no_target_prediction",
        "policy_name": "prohibit_target_and_prediction_generation",
        "statement": "Regime values are descriptive descriptive indicators, never supervised ML target labels or price predictions",
        "enforcement": "MANDATORY_INVARIANT",
        "non_signal": True,
    },
    {
        "policy_id": "nsp_05_no_model_training",
        "policy_name": "prohibit_unsupervised_supervised_training",
        "statement": "No model training (HMM, GMM, clustering, SVM) is executed during foundation phase",
        "enforcement": "MANDATORY_INVARIANT",
        "non_signal": True,
    },
    {
        "policy_id": "nsp_06_no_strategy_backtest",
        "policy_name": "prohibit_strategy_and_backtest_execution",
        "statement": "Regimes shall not trigger backtesting, strategy execution, or portfolio optimization",
        "enforcement": "MANDATORY_INVARIANT",
        "non_signal": True,
    },
]

FORBIDDEN_PHRASES_PATTERNS: List[str] = [
    r"\bal\s*aç\b",
    r"\bsat\s*aç\b",
    r"\blong\s*aç\b",
    r"\bshort\s*aç\b",
    r"\bkesin\s*al\b",
    r"\bkesin\s*sat\b",
    r"\bbuy\s*signal\b",
    r"\bsell\s*signal\b",
    r"\btrade\s*signal\b",
    r"\btrade\s*recommendation\b",
    r"\byatırım\s*tavsiyesi\b",
    r"\bposition\s*aç\b",
    r"\bmodel\s*prediction\b",
    r"\bofficial\s*approval\b",
    r"\bproduction\s*ready\b",
    r"\bbroker\s*ready\b",
]


def build_regime_non_signal_policy_registry(
    profile: Optional[RegimeFoundationProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and summary for regime non-signal policy registry."""
    active_profile = profile or get_default_regime_foundation_profile()
    df = pd.DataFrame(NON_SIGNAL_POLICIES)
    summary = {
        "active_profile": active_profile.profile_name,
        "total_policies": len(df),
        "all_mandatory": bool((df["enforcement"] == "MANDATORY_INVARIANT").all()),
        "all_non_signal": bool((df["non_signal"] == True).all()),
        "current_phase": active_profile.current_phase,
        "target_final_phase": active_profile.target_final_phase,
        "next_phase": active_profile.next_phase,
        "official_approval": False,
        "production_ready": False,
        "broker_ready": False,
    }
    return df, summary


def validate_regime_non_signal_text(text: str) -> Dict[str, Any]:
    """Scan input text for forbidden directional or execution phrases."""
    matches = []
    text_lower = text.lower()
    for pattern in FORBIDDEN_PHRASES_PATTERNS:
        if re.search(pattern, text_lower):
            matches.append(pattern)

    return {
        "is_valid": len(matches) == 0,
        "forbidden_matches_count": len(matches),
        "forbidden_patterns_matched": matches,
        "non_signal": True,
    }


def summarize_regime_non_signal_policies(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize regime non-signal policies DataFrame."""
    return {
        "total_policies": len(df),
        "policy_names": list(df["policy_name"].unique()) if "policy_name" in df.columns else [],
        "all_mandatory": True,
        "non_signal": True,
    }
