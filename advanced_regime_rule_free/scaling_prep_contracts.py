"""Phase 128: Scaling Prep Contracts.

Defines scaling contracts for multi-scale technical and macro features.
"""

from typing import Dict, Tuple
import pandas as pd

from advanced_regime_rule_free.regime_rule_free_config import (
    RegimeRuleFreeProfile,
    get_default_regime_rule_free_profile,
)

SCALING_PREP_CONTRACTS = [
    {
        "scaling_method": "standard_scaler_prep",
        "scaling_type": "unit_variance",
        "description": "Standard scaling contract specification for cross-sectional and temporal feature normalization.",
        "execution_allowed": False,
        "non_signal": True,
    },
    {
        "scaling_method": "max_abs_scaler_prep",
        "scaling_type": "sparse_preserving",
        "description": "Max-abs scaling contract preserving zero centers for sparse event inputs.",
        "execution_allowed": False,
        "non_signal": True,
    },
    {
        "scaling_method": "unit_vector_scaler_prep",
        "scaling_type": "norm_normalization",
        "description": "L2 unit-norm scaling contract for directional cosine distance comparison.",
        "execution_allowed": False,
        "non_signal": True,
    },
]


def build_scaling_prep_contract_registry(
    profile: RegimeRuleFreeProfile | None = None,
) -> Tuple[pd.DataFrame, Dict]:
    """Build DataFrame and summary metadata for scaling prep contracts."""
    active_profile = profile or get_default_regime_rule_free_profile()

    rows = []
    for s in SCALING_PREP_CONTRACTS:
        row = s.copy()
        row["current_phase"] = active_profile.current_phase
        row["next_phase"] = active_profile.next_phase
        row["target_final_phase"] = active_profile.target_final_phase
        rows.append(row)

    df = pd.DataFrame(rows)
    summary = summarize_scaling_prep_contracts(df)
    return df, summary


def summarize_scaling_prep_contracts(df: pd.DataFrame) -> Dict:
    """Summarize scaling preparation contracts."""
    total = len(df)
    all_non_executable = bool((~df["execution_allowed"]).all()) if not df.empty else True
    all_non_signal = bool(df["non_signal"].all()) if not df.empty else True

    return {
        "total_scaling_contracts": total,
        "all_execution_forbidden": all_non_executable,
        "all_non_signal": all_non_signal,
        "status": "VALID" if all_non_executable and all_non_signal else "INVALID",
    }
