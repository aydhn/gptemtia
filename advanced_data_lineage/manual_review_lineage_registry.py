from typing import Tuple, Dict, Any, List
import pandas as pd

from advanced_data_lineage.data_lineage_config import DataLineageProfile


MANUAL_REVIEW_LINEAGE_ITEMS = [
    {
        "review_id": "rev_lin_001",
        "dataset_type": "dataset_macro_timeseries",
        "entity_name": "unknown_macro_unit",
        "source_reference": "raw_schema://macro/timeseries_raw_v1",
        "issue_description": "Non-standard unit string detected; flagged for analyst dictionary update",
        "safe_remediation": "Do not delete raw record. Record dictionary alias in normalization layer",
        "destructive_action_allowed": False,
        "source_preserved": True,
        "status": "pending_operator_review",
    },
    {
        "review_id": "rev_lin_002",
        "dataset_type": "dataset_commodity_spot",
        "entity_name": "unmapped_futures_root",
        "source_reference": "raw_schema://commodity/spot_raw_v1",
        "issue_description": "Commodity contract code does not match standard continuous root",
        "safe_remediation": "Keep original code in place. Register manual root mapping entry",
        "destructive_action_allowed": False,
        "source_preserved": True,
        "status": "pending_operator_review",
    },
    {
        "review_id": "rev_lin_003",
        "dataset_type": "dataset_provider_metadata",
        "entity_name": "licensed_provider_terms",
        "source_reference": "urn:feed:licensed:market_data_v2",
        "issue_description": "Vendor terms require periodic non-commercial re-verification",
        "safe_remediation": "Verify license policy before Phase 115 benchmark inclusion",
        "destructive_action_allowed": False,
        "source_preserved": True,
        "status": "pending_operator_review",
    },
]


def build_manual_review_lineage_registry(
    profile: DataLineageProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    df = pd.DataFrame.from_records(MANUAL_REVIEW_LINEAGE_ITEMS)
    summary = summarize_manual_review_lineage_registry(df)
    return df, summary


def summarize_manual_review_lineage_registry(df: pd.DataFrame) -> Dict[str, Any]:
    return {
        "total_manual_review_items": len(df),
        "review_ids": df["review_id"].tolist() if "review_id" in df.columns else [],
        "zero_destructive_actions": bool((~df["destructive_action_allowed"]).all()) if "destructive_action_allowed" in df.columns and len(df) > 0 else True,
        "all_source_preserved": bool(df["source_preserved"].all()) if "source_preserved" in df.columns and len(df) > 0 else True,
        "current_phase": 114,
        "target_final_phase": 160,
    }
