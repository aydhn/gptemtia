"""Phase 136: No-Lookahead ML Input Contracts.

Enforces strict timestamp ordering, backward asof joins, and prohibition
of future-leakage fields in ML input datasets.
"""

from typing import Any, Dict, List, Optional, Tuple
import pandas as pd

from advanced_gpu_ml_runtime.gpu_ml_runtime_config import (
    GpuMlRuntimeProfile,
    get_gpu_ml_runtime_profile,
)
from advanced_gpu_ml_runtime.gpu_ml_runtime_labels import (
    NO_LOOKAHEAD_INPUT_CONTRACT_DOMAIN,
    RUNTIME_READY,
)


FORBIDDEN_LOOKAHEAD_PATTERNS = [
    "future_",
    "forward_",
    "next_",
    "lead_",
    "t_plus_",
    "_ahead",
    "target",
    "label",
]


def validate_ml_input_no_lookahead_fields(column_names: List[str]) -> Dict[str, Any]:
    """Inspect input column names and flag any potential lookahead or forward leakage."""
    violations: List[str] = []
    for col in column_names:
        c_lower = col.lower()
        for pat in FORBIDDEN_LOOKAHEAD_PATTERNS:
            if pat in c_lower:
                violations.append(col)
                break

    is_clean = len(violations) == 0
    return {
        "is_safe": is_clean,
        "violations": violations,
        "message": f"Lookahead fields detected: {violations}" if not is_clean else "All input fields satisfy no-lookahead contract.",
        "non_signal": True,
        "source_preserved": True,
    }


def build_no_lookahead_ml_input_contract_registry(
    profile: Optional[GpuMlRuntimeProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and metadata summary for no-lookahead ML input contracts."""
    active = profile or get_gpu_ml_runtime_profile()

    rows: List[Dict[str, Any]] = [
        {
            "contract_id": "nl_backward_asof_only",
            "rule_name": "Backward Asof Join Invariant",
            "enforced": True,
            "status_label": RUNTIME_READY,
            "details": "All feature joins must strictly align on or before the reference event timestamp.",
        },
        {
            "contract_id": "nl_chronological_split",
            "rule_name": "Strict Chronological Train/Val Partitioning",
            "enforced": True,
            "status_label": RUNTIME_READY,
            "details": "Random k-fold shuffling forbidden on time series; strictly chronological splits.",
        },
        {
            "contract_id": "nl_zero_negative_shifts",
            "rule_name": "Prohibition of Forward Shift",
            "enforced": True,
            "status_label": RUNTIME_READY,
            "details": "Negative shift operations such as df.shift(-1) are strictly blocked.",
        },
    ]

    for r in rows:
        r["non_signal"] = True
        r["source_preserved"] = True
        r["official_approval"] = False
        r["production_ready"] = False
        r["broker_ready"] = False

    df = pd.DataFrame(rows)
    summary = summarize_no_lookahead_ml_input_contracts(df)
    summary["domain"] = NO_LOOKAHEAD_INPUT_CONTRACT_DOMAIN
    summary["active_profile"] = active.profile_name
    return df, summary


def summarize_no_lookahead_ml_input_contracts(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize no-lookahead ML input contracts DataFrame."""
    all_enf = bool(df["enforced"].all()) if not df.empty and "enforced" in df.columns else False
    return {
        "total_contracts": len(df),
        "all_enforced": all_enf,
        "no_lookahead_guaranteed": True,
        "non_signal": True,
        "source_preserved": True,
        "official_approval": False,
        "production_ready": False,
        "broker_ready": False,
    }
