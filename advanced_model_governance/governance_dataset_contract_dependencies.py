# -*- coding: utf-8 -*-
"""Phase 144: Governance Dataset Contract Dependencies Registry."""

from typing import Any, Dict, List, Optional, Tuple
import pandas as pd
from advanced_model_governance.model_governance_config import (
    ModelGovernanceProfile,
    get_model_governance_profile,
)

DATASET_DEP_SPECS: List[Dict[str, str]] = [
    {"dependency_name": "phase_137_dataset_contracts", "source": "Phase 137", "interface": "DatasetContractRegistry", "status": "SATISFIED"},
    {"dependency_name": "phase_137_time_index_policies", "source": "Phase 137", "interface": "TimeIndexPolicy", "status": "SATISFIED"},
    {"dependency_name": "phase_137_purged_split_policies", "source": "Phase 137", "interface": "PurgedSplitPolicy", "status": "SATISFIED"},
]


def build_governance_dataset_contract_dependency_registry(
    profile: Optional[ModelGovernanceProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and summary for dataset contract dependencies."""
    prof = profile or get_model_governance_profile()
    records = []
    for spec in DATASET_DEP_SPECS:
        row = dict(spec)
        row["phase"] = prof.current_phase
        row["non_signal"] = True
        records.append(row)

    df = pd.DataFrame(records)
    summary = summarize_governance_dataset_contract_dependencies(df)
    return df, summary


def summarize_governance_dataset_contract_dependencies(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize dataset contract dependencies."""
    return {
        "total_dependencies": len(df),
        "all_satisfied": bool((df["status"] == "SATISFIED").all()),
        "non_signal": bool(df["non_signal"].all()),
    }
