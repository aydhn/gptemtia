# -*- coding: utf-8 -*-
"""
Phase 137 - Advanced ML Dataset Contracts and Experiment Registry
Manual review queue builder.

All recommendations are purely inspect/audit based.
Strictly prohibits auto-fix, auto-materialize, auto-train, auto-drop, or auto-impute.
"""

from typing import Dict, List, Optional, Tuple
import pandas as pd

from advanced_ml_dataset_registry.advanced_ml_dataset_config import (
    AdvancedMlDatasetProfile,
    get_default_advanced_ml_dataset_profile,
)
from advanced_ml_dataset_registry.advanced_ml_dataset_models import (
    MlDatasetManualReviewItem,
)

MANUAL_REVIEW_ACTIONS = [
    {
        "review_id": "MR-137-001",
        "domain": "dataset_source_catalog_domain",
        "description": "Inspect upstream Phase 116-136 source catalog references to verify presence of metadata pointers",
        "recommendation": "inspect dataset source catalog references and ensure zero raw data loading",
        "priority": "high",
        "auto_fix_forbidden": True,
        "non_signal": True,
    },
    {
        "review_id": "MR-137-002",
        "domain": "dataset_schema_domain",
        "description": "Inspect schema contracts to confirm required metadata fields and ensure absence of target/signal columns",
        "recommendation": "inspect schema required fields and confirm zero forbidden columns",
        "priority": "high",
        "auto_fix_forbidden": True,
        "non_signal": True,
    },
    {
        "review_id": "MR-137-003",
        "domain": "time_index_policy_domain",
        "description": "Inspect time index policy to verify strict UTC parsing and strict monotonic ordering requirements",
        "recommendation": "inspect time index policy and enforce UTC timezone validation",
        "priority": "medium",
        "auto_fix_forbidden": True,
        "non_signal": True,
    },
    {
        "review_id": "MR-137-004",
        "domain": "time_series_split_policy_domain",
        "description": "Inspect split policy placeholders to confirm non-execution and verify no train/test materialization",
        "recommendation": "inspect split policy placeholders to ensure dry-run contract fidelity",
        "priority": "medium",
        "auto_fix_forbidden": True,
        "non_signal": True,
    },
    {
        "review_id": "MR-137-005",
        "domain": "leakage_guard_domain",
        "description": "Inspect leakage guards to guarantee prohibition of shift(-1) and future return joins",
        "recommendation": "inspect leakage and no-lookahead guards before Phase 138 handoff",
        "priority": "critical",
        "auto_fix_forbidden": True,
        "non_signal": True,
    },
    {
        "review_id": "MR-137-006",
        "domain": "metadata_only_news_guard_domain",
        "description": "Inspect news guards to ensure only metadata headers/event tags are used, blocking all article bodies",
        "recommendation": "inspect metadata-only news guards and verify zero full text / HTML content",
        "priority": "critical",
        "auto_fix_forbidden": True,
        "non_signal": True,
    },
    {
        "review_id": "MR-137-007",
        "domain": "feature_snapshot_contract_domain",
        "description": "Inspect FeatureStore accepted catalog references to ensure alignment with Phase 134/135 regimes",
        "recommendation": "inspect FeatureStore accepted references and verify snapshot contracts are unmaterialized",
        "priority": "high",
        "auto_fix_forbidden": True,
        "non_signal": True,
    },
    {
        "review_id": "MR-137-008",
        "domain": "experiment_permission_domain",
        "description": "Inspect experiment registry permissions to confirm training, inference, and artifact persistence blocks",
        "recommendation": "inspect experiment registry permissions and enforce zero-training policy",
        "priority": "critical",
        "auto_fix_forbidden": True,
        "non_signal": True,
    },
    {
        "review_id": "MR-137-009",
        "domain": "phase_138_handoff_domain",
        "description": "Inspect prerequisites and dry-run training harness boundaries prior to Phase 138 kickoff",
        "recommendation": "inspect Phase 138 dry-run harness blockers and safety preconditions",
        "priority": "high",
        "auto_fix_forbidden": True,
        "non_signal": True,
    },
]


def build_ml_dataset_manual_review_queue(
    profile: Optional[AdvancedMlDatasetProfile] = None,
) -> Tuple[pd.DataFrame, Dict]:
    """Build DataFrame and summary for the manual review queue."""
    p = profile or get_default_advanced_ml_dataset_profile()
    df = pd.DataFrame(MANUAL_REVIEW_ACTIONS)
    summary = summarize_ml_dataset_manual_review_queue(df)
    return df, summary


def summarize_ml_dataset_manual_review_queue(df: pd.DataFrame) -> Dict:
    """Summarize the manual review queue."""
    critical_count = int((df["priority"] == "critical").sum()) if "priority" in df.columns else 0
    return {
        "total_review_items": len(df),
        "critical_review_items": critical_count,
        "auto_fix_allowed": False,
        "auto_drop_allowed": False,
        "auto_materialize_allowed": False,
        "auto_train_allowed": False,
        "non_signal": True,
        "manual_review_required": True,
    }
