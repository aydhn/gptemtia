"""Phase 127: Regime Matrix Non-Signal Policies.

Defines non-signal principles and text validation functions enforcing zero trading signals.
"""

import re
from typing import Any, Dict, List, Optional, Tuple
import pandas as pd

from advanced_regime_matrix.regime_matrix_config import (
    RegimeMatrixProfile,
    get_default_regime_matrix_profile,
)

FORBIDDEN_SIGNAL_PATTERNS = [
    r"\bbuy\s+signal\b",
    r"\bsell\s+signal\b",
    r"\blong\s+entry\b",
    r"\bshort\s+entry\b",
    r"\btrade\s+recommendation\b",
    r"\btarget\s+price\b",
    r"\bprofit\s+target\b",
    r"\bposition\s+size\b",
    r"\bopen\s+position\b",
    r"\bclose\s+position\b",
]

NON_SIGNAL_POLICIES: List[Dict[str, Any]] = [
    {
        "policy_id": "nsp_no_buy_sell_signals",
        "name": "Zero Buy/Sell Signals",
        "description": "Regime feature matrices and candidate datasets must never generate or imply buy/sell triggers.",
        "is_active": True,
        "non_signal": True,
    },
    {
        "policy_id": "nsp_no_directional_claims",
        "name": "Zero Directional Certainty",
        "description": "Observations describe structural market volatility or trend, never a directional investment guarantee.",
        "is_active": True,
        "non_signal": True,
    },
    {
        "policy_id": "nsp_no_model_predictions",
        "name": "Zero Target or Prediction Modeling",
        "description": "Candidate states are structural research descriptors, not machine learning labels or forecasts.",
        "is_active": True,
        "non_signal": True,
    },
    {
        "policy_id": "nsp_no_broker_order_execution",
        "name": "Zero Broker Order Execution",
        "description": "System prohibits automated broker connections, execution adapters, and real order dispatch.",
        "is_active": True,
        "non_signal": True,
    },
    {
        "policy_id": "nsp_no_position_sizing",
        "name": "Zero Position Sizing Recommendations",
        "description": "Prohibits portfolio allocation, position sizing, leverage calculation, or risk exposure advice.",
        "is_active": True,
        "non_signal": True,
    },
    {
        "policy_id": "nsp_no_unsupervised_label_assignment",
        "name": "Zero Label/Target Assignment to States",
        "description": "Candidate context states remain unlabelled structural indicators, not ground-truth targets.",
        "is_active": True,
        "non_signal": True,
    },
]


def scan_text_for_signal_claims(text: str) -> List[str]:
    """Scan arbitrary text for forbidden trade signal phrases and return matched violations."""
    violations = []
    for pat in FORBIDDEN_SIGNAL_PATTERNS:
        matches = re.findall(pat, text, re.IGNORECASE)
        if matches:
            violations.extend(matches)
    return violations


def validate_feature_columns_non_signal(columns: List[str]) -> bool:
    """Validate that a list of column names contains zero trading signal or target keywords."""
    forbidden_tokens = [
        "signal", "buy", "sell", "target", "pred", "forecast", "long_entry", "short_entry", "profit",
    ]
    for col in columns:
        col_lower = str(col).lower()
        for tok in forbidden_tokens:
            if tok in col_lower:
                return False
    return True


def build_regime_matrix_non_signal_policy_registry(
    profile: Optional[RegimeMatrixProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build the non-signal policy registry."""
    p = profile or get_default_regime_matrix_profile()

    rows = []
    for pol in NON_SIGNAL_POLICIES:
        p_copy = pol.copy()
        p_copy["current_phase"] = p.current_phase
        p_copy["target_final_phase"] = p.target_final_phase
        p_copy["next_phase"] = p.next_phase
        p_copy["source_preserved"] = True
        p_copy["status"] = "matrix_ready"
        rows.append(p_copy)

    df = pd.DataFrame(rows)
    summary = summarize_regime_matrix_non_signal_policies(df)
    return df, summary


def validate_regime_matrix_non_signal_text(text: str) -> Dict[str, Any]:
    """Scan arbitrary text or documentation for forbidden trade signal phrases."""
    violations = scan_text_for_signal_claims(text)
    is_valid = len(violations) == 0
    return {
        "is_valid": is_valid,
        "violation_count": len(violations),
        "violations": violations,
        "non_signal": True,
    }


def summarize_regime_matrix_non_signal_policies(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize the non-signal policies."""
    return {
        "total_policies": len(df),
        "policy_ids": df["policy_id"].tolist() if not df.empty else [],
        "all_active": bool(df["is_active"].all()) if not df.empty else True,
        "all_enforced": bool(df["is_active"].all()) if not df.empty else True,
        "all_non_signal": bool(df["non_signal"].all()) if not df.empty else True,
        "status": "matrix_ready",
    }


build_regime_matrix_non_signal_policies = build_regime_matrix_non_signal_policy_registry

