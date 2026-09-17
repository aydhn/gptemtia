# -*- coding: utf-8 -*-
"""Phase 153: Portfolio Source Preservation Guards Module.

Guards that raw input datasets, upstream databases, and source files are never mutated,
overwritten, or deleted during portfolio construction processes.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from .portfolio_construction_config import PortfolioConstructionProfile
from .portfolio_construction_labels import (
    PORTFOLIO_GUARD_DOMAIN,
    PORTFOLIO_CONTRACT_READY,
)

SOURCE_PRESERVATION_GUARDS: List[Dict[str, Any]] = [
    {
        "guard_id": "GUARD_PORTFOLIO_IMMUTABLE_INPUTS",
        "guard_name": "Portfolio Immutable Inputs Guard",
        "detection_target": "in_place_input_modification",
        "description": "Girdi veri setlerinin yerinde degistirilmesini (mutation) engelleyen muhafiz.",
    },
    {
        "guard_id": "GUARD_NO_RAW_SOURCE_OVERWRITE",
        "guard_name": "No Raw Source Overwrite Guard",
        "detection_target": "raw_file_overwrites",
        "description": "Ham kaynak dosyalarinin uzerine yazilmasini engelleyen muhafiz.",
    },
    {
        "guard_id": "GUARD_APPEND_ONLY_AUDIT_TRAIL",
        "guard_name": "Append-Only Audit Trail Guard",
        "detection_target": "audit_log_tampering",
        "description": "Denetim izlerinin yalnizca ekleme (append-only) seklinde tutulmasini saglayan muhafiz.",
    },
]


def build_portfolio_source_preservation_guard_registry(
    profile: PortfolioConstructionProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame registry of portfolio source preservation guards."""
    rows = []
    for g in SOURCE_PRESERVATION_GUARDS:
        rows.append({
            "guard_id": g["guard_id"],
            "guard_name": g["guard_name"],
            "detection_target": g["detection_target"],
            "description": g["description"],
            "current_phase": profile.current_phase,
            "contract_only": True,
            "non_production": True,
            "is_active": True,
            "status": PORTFOLIO_CONTRACT_READY,
        })

    df = pd.DataFrame(rows)
    summary = {
        "domain": PORTFOLIO_GUARD_DOMAIN,
        "guard_category": "source_preservation",
        "active_profile": profile.profile_name,
        "total_guards": len(df),
        "all_active": True,
        "status": PORTFOLIO_CONTRACT_READY,
    }
    return df, summary


def validate_portfolio_source_preservation(operation_type: str) -> Dict[str, Any]:
    """Validate that the operation is non-destructive and preserves original sources."""
    destructive_ops = ["overwrite_raw", "drop_table", "delete_source", "truncate_lake"]
    is_safe = operation_type.lower() not in destructive_ops
    return {
        "is_safe": is_safe,
        "operation_type": operation_type,
        "status": "PASS" if is_safe else "BLOCKED_BY_SOURCE_PRESERVATION_GUARD",
        "contract_only": True,
    }
