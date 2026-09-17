# -*- coding: utf-8 -*-
"""Phase 151: Evaluation Source Preservation Guards Module.

Guards raw source datasets against overwriting, destructive cleaning,
auto-imputation, and auto-feature-dropping.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_benchmark_evaluation.benchmark_evaluation_config import BenchmarkEvaluationProfile
from advanced_benchmark_evaluation.benchmark_evaluation_labels import (
    LABEL_CLAIM_GUARD_DOMAIN,
    STATUS_EVALUATION_CONTRACT_READY,
)

FORBIDDEN_DATA_ACTIONS = [
    "source_overwrite",
    "destructive_cleaning",
    "auto_imputation",
    "auto_feature_drop",
    "file_deletion",
    "overwrite_raw_file",
    "drop_missing_columns",
    "impute_forward_fill",
]

SOURCE_PRESERVATION_GUARDS: List[Dict[str, Any]] = [
    {
        "guard_id": "GUARD_NO_SOURCE_OVERWRITE",
        "guard_name": "Prohibition of Raw Source Overwrite Guard",
        "detection_target": "file_write_over_source",
        "description": "Ham kaynak dosyalarının üzerine yazılmasını kesin olarak engelleyen muhafız.",
    },
    {
        "guard_id": "GUARD_NO_DESTRUCTIVE_CLEANING",
        "guard_name": "Prohibition of Destructive Cleaning Guard",
        "detection_target": "auto_drop_and_destructive_edits",
        "description": "Bozuk veya eksik verileri sessizce silen veya budayan işlemleri engelleyen muhafız.",
    },
    {
        "guard_id": "GUARD_NO_AUTO_IMPUTATION",
        "guard_name": "Prohibition of Auto-Imputation Guard",
        "detection_target": "synthetic_gap_filling",
        "description": "İstatistiksel sapmaya yol açabilecek kontrolsüz sentetik doldurmayı engelleyen muhafız.",
    },
]


def build_evaluation_source_preservation_guard_registry(
    profile: BenchmarkEvaluationProfile | None = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame registry of source preservation guards."""
    rows: List[Dict[str, Any]] = []

    for g in SOURCE_PRESERVATION_GUARDS:
        rows.append(
            {
                "guard_id": g["guard_id"],
                "guard_name": g["guard_name"],
                "detection_target": g["detection_target"],
                "description": g["description"],
                "is_active": True,
                "status": STATUS_EVALUATION_CONTRACT_READY,
                "non_signal": True,
            }
        )

    df = pd.DataFrame(rows)
    summary = {
        "domain": LABEL_CLAIM_GUARD_DOMAIN,
        "total_guards": len(df),
        "all_active": True,
        "status": STATUS_EVALUATION_CONTRACT_READY,
        "non_signal": True,
    }
    return df, summary


def validate_evaluation_source_preservation_action(action: str) -> Dict[str, Any]:
    """Validate a requested data action against source preservation policies."""
    act_lower = str(action).lower()
    is_forbidden = any(f in act_lower for f in FORBIDDEN_DATA_ACTIONS)

    return {
        "action": action,
        "is_permitted": not is_forbidden,
        "is_forbidden": is_forbidden,
        "status": "PASS" if not is_forbidden else "BLOCKED_BY_SOURCE_PRESERVATION_GUARD",
        "policy_action": "ALLOW" if not is_forbidden else "ACTION_BLOCKED_BY_POLICY",
        "non_signal": True,
    }
