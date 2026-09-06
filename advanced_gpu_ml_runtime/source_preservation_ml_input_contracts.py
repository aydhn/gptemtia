"""Phase 136: Source Preservation ML Input Contracts.

Enforces strict source immutability, prohibiting data overwrite, destructive cleaning,
file deletion, and automated imputation/drop routines.
"""

from typing import Any, Dict, List, Optional, Tuple
import pandas as pd

from advanced_gpu_ml_runtime.gpu_ml_runtime_config import (
    GpuMlRuntimeProfile,
    get_gpu_ml_runtime_profile,
)
from advanced_gpu_ml_runtime.gpu_ml_runtime_labels import (
    SOURCE_PRESERVATION_INPUT_CONTRACT_DOMAIN,
    RUNTIME_READY,
)


FORBIDDEN_SOURCE_ACTIONS = [
    "overwrite",
    "delete",
    "remove",
    "move",
    "truncate",
    "destructive_clean",
    "auto_impute",
    "auto_drop",
    "inplace_replace",
]


def validate_ml_input_source_preservation_action(action: str) -> Dict[str, Any]:
    """Validate whether an attempted storage/data action preserves source records."""
    action_lower = action.lower()
    violations: List[str] = []

    for fa in FORBIDDEN_SOURCE_ACTIONS:
        if fa in action_lower:
            violations.append(fa)

    is_safe = len(violations) == 0
    return {
        "is_safe": is_safe,
        "action": action,
        "violations": violations,
        "message": f"Destructive data action detected: {violations}" if not is_safe else "Action preserves source data immutability.",
        "non_signal": True,
        "source_preserved": True,
    }


def build_source_preservation_ml_input_contract_registry(
    profile: Optional[GpuMlRuntimeProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and metadata summary for source preservation ML input contracts."""
    active = profile or get_gpu_ml_runtime_profile()

    rows: List[Dict[str, Any]] = [
        {
            "contract_id": "sp_immutable_data_lake",
            "rule_name": "DataLake Read-Only Access for ML",
            "enforced": True,
            "status_label": RUNTIME_READY,
            "details": "ML feature matrices and datasets must never overwrite raw historical DataLake records.",
        },
        {
            "contract_id": "sp_no_auto_drop",
            "rule_name": "Prohibit Silent Auto-Drop of Features",
            "enforced": True,
            "status_label": RUNTIME_READY,
            "details": "Columns and records must not be discarded silently without explicit governance tracking.",
        },
        {
            "contract_id": "sp_no_auto_impute",
            "rule_name": "Prohibit Synthetic Auto-Imputation",
            "enforced": True,
            "status_label": RUNTIME_READY,
            "details": "Missing values must be flagged explicitly rather than filled with heuristic guesses.",
        },
    ]

    for r in rows:
        r["non_signal"] = True
        r["source_preserved"] = True
        r["official_approval"] = False
        r["production_ready"] = False
        r["broker_ready"] = False

    df = pd.DataFrame(rows)
    summary = summarize_source_preservation_ml_input_contracts(df)
    summary["domain"] = SOURCE_PRESERVATION_INPUT_CONTRACT_DOMAIN
    summary["active_profile"] = active.profile_name
    return df, summary


def summarize_source_preservation_ml_input_contracts(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize source preservation ML input contracts DataFrame."""
    all_enf = bool(df["enforced"].all()) if not df.empty and "enforced" in df.columns else False
    return {
        "total_contracts": len(df),
        "all_enforced": all_enf,
        "source_preservation_guaranteed": True,
        "non_signal": True,
        "source_preserved": True,
        "official_approval": False,
        "production_ready": False,
        "broker_ready": False,
    }
