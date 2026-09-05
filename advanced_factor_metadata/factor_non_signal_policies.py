"""Phase 122 Factor Non-Signal Policies Registry.

Enforces structural non-signal policies guaranteeing factors cannot be utilized
as trade signals, execution instructions, or directional recommendations.
Strictly non-signal and research-only.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_factor_metadata.factor_metadata_config import (
    FactorMetadataProfile,
    get_default_factor_metadata_profile,
)
from advanced_factor_metadata.factor_metadata_labels import FACTOR_READY
from advanced_factor_metadata.factor_metadata_models import FORBIDDEN_FACTOR_TOKENS

NON_SIGNAL_POLICIES: List[Dict[str, Any]] = [
    {
        "policy_id": "nsp_01_no_buy_sell_signals",
        "policy_name": "Prohibition of Buy/Sell Signals",
        "description": "Factors must never be categorized, labeled, or output as buy/sell signals.",
        "enforcement": "STRICT_FILTER",
    },
    {
        "policy_id": "nsp_02_no_directional_claims",
        "policy_name": "Prohibition of Directional Claims",
        "description": "No factor value shall imply certainty of upward or downward price movement.",
        "enforcement": "TEXT_AUDIT",
    },
    {
        "policy_id": "nsp_03_no_strategy_rules",
        "policy_name": "Prohibition of Strategy Rule Synthesis",
        "description": "Factors must not be automatically compiled into threshold-based trading rules.",
        "enforcement": "STRUCTURAL_BARRIER",
    },
    {
        "policy_id": "nsp_04_no_target_label_generation",
        "policy_name": "Prohibition of ML Targets/Labels",
        "description": "Factors must not serve as ground-truth target variables or class labels in this phase.",
        "enforcement": "SCHEMA_VALIDATION",
    },
    {
        "policy_id": "nsp_05_no_broker_execution",
        "policy_name": "Prohibition of Broker or Order Routing",
        "description": "Zero integration with execution brokers, live APIs, or order dispatchers.",
        "enforcement": "RUNTIME_ISOLATION",
    },
]


def build_factor_non_signal_policy_registry(
    profile: FactorMetadataProfile | None = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build Factor Non-Signal Policy Registry DataFrame and summary."""
    active_profile = profile or get_default_factor_metadata_profile()

    records = [dict(p) for p in NON_SIGNAL_POLICIES]
    df = pd.DataFrame(records)

    summary = {
        "active_profile": active_profile.name,
        "total_policies": len(records),
        "current_phase": active_profile.current_phase,
        "target_final_phase": active_profile.target_final_phase,
        "non_signal": True,
        "status": FACTOR_READY,
    }
    return df, summary


def validate_factor_non_signal_policy(
    text: str | None = None,
    df: pd.DataFrame | None = None,
) -> Dict[str, Any]:
    """Validate that given text and/or dataframe adheres to non-signal policies."""
    violations: List[str] = []

    if text:
        text_lower = text.lower()
        for token in FORBIDDEN_FACTOR_TOKENS:
            if token in text_lower:
                violations.append(f"Forbidden token '{token}' detected in text")

    if df is not None:
        for col in df.columns:
            col_lower = str(col).lower()
            for token in FORBIDDEN_FACTOR_TOKENS:
                if token in col_lower:
                    violations.append(f"Forbidden token '{token}' detected in column '{col}'")

    is_compliant = len(violations) == 0
    return {
        "is_compliant": is_compliant,
        "violations": violations,
        "non_signal": is_compliant,
    }


def summarize_factor_non_signal_policy(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize factor non-signal policy DataFrame."""
    return {
        "total_policies": len(df),
        "status": FACTOR_READY,
        "non_signal": True,
    }
