"""Phase 128: Normalization Prep Contracts.

Defines normalization preparation specifications without mutating raw inputs.
"""

from typing import Dict, Tuple
import pandas as pd

from advanced_regime_rule_free.regime_rule_free_config import (
    RegimeRuleFreeProfile,
    get_default_regime_rule_free_profile,
)

NORMALIZATION_PREP_CONTRACTS = [
    {
        "normalization_method": "min_max_prep_contract",
        "description": "Transforms features into [0, 1] range preserving zero lookahead by using historical rolling bounds.",
        "requires_rolling_window": True,
        "mutation_allowed": False,
        "non_signal": True,
    },
    {
        "normalization_method": "zscore_prep_contract",
        "description": "Standardizes features using rolling mean and rolling standard deviation.",
        "requires_rolling_window": True,
        "mutation_allowed": False,
        "non_signal": True,
    },
    {
        "normalization_method": "robust_median_iqr_prep_contract",
        "description": "Normalizes features using rolling median and interquartile range for heavy-tailed returns.",
        "requires_rolling_window": True,
        "mutation_allowed": False,
        "non_signal": True,
    },
    {
        "normalization_method": "quantile_prep_contract",
        "description": "Maps arbitrary continuous distributions to uniform or Gaussian quantiles offline.",
        "requires_rolling_window": True,
        "mutation_allowed": False,
        "non_signal": True,
    },
]


def build_normalization_prep_contract_registry(
    profile: RegimeRuleFreeProfile | None = None,
) -> Tuple[pd.DataFrame, Dict]:
    """Build DataFrame and summary metadata for normalization prep contracts."""
    active_profile = profile or get_default_regime_rule_free_profile()

    rows = []
    for c in NORMALIZATION_PREP_CONTRACTS:
        row = c.copy()
        row["current_phase"] = active_profile.current_phase
        row["next_phase"] = active_profile.next_phase
        row["target_final_phase"] = active_profile.target_final_phase
        rows.append(row)

    df = pd.DataFrame(rows)
    summary = summarize_normalization_prep_contracts(df)
    return df, summary


def summarize_normalization_prep_contracts(df: pd.DataFrame) -> Dict:
    """Summarize normalization preparation contracts."""
    total = len(df)
    all_non_mutating = bool((~df["mutation_allowed"]).all()) if not df.empty else True
    all_non_signal = bool(df["non_signal"].all()) if not df.empty else True

    return {
        "total_normalization_contracts": total,
        "all_non_mutating": all_non_mutating,
        "all_non_signal": all_non_signal,
        "status": "VALID" if all_non_mutating and all_non_signal else "INVALID",
    }
