"""Phase 123 Feature Quality Input Contract Registry.

Defines input contracts and validation expectations for data ingested into the
feature quality diagnostic pipeline.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_feature_quality_drift.feature_quality_drift_config import (
    FeatureQualityDriftProfile,
    get_default_feature_quality_drift_profile,
)

QUALITY_INPUT_CONTRACTS: List[Dict[str, Any]] = [
    {
        "contract_id": "contract_df_immutability",
        "contract_name": "DataFrame Immutability Contract",
        "description": "Diagnostic pipeline must never mutate input DataFrames in place.",
        "severity": "quality_critical",
        "enforced": True,
    },
    {
        "contract_id": "contract_non_destructive",
        "contract_name": "Non-Destructive Handling Contract",
        "description": "Never automatically drop, filter, or impute rows or columns with missing/infinite values.",
        "severity": "quality_critical",
        "enforced": True,
    },
    {
        "contract_id": "contract_schema_metadata",
        "contract_name": "Schema and Metadata Contract",
        "description": "Input datasets must preserve timestamp ordering and feature column definitions.",
        "severity": "quality_high",
        "enforced": True,
    },
    {
        "contract_id": "contract_forbidden_columns",
        "contract_name": "Forbidden Forward-Looking Column Contract",
        "description": "Input datasets must contain zero target, prediction, or future return columns.",
        "severity": "quality_critical",
        "enforced": True,
    },
    {
        "contract_id": "contract_news_metadata_only",
        "contract_name": "News Metadata Only Contract",
        "description": "News features must contain metadata-only fields; no full text or embedding vectors.",
        "severity": "quality_critical",
        "enforced": True,
    },
]


def build_feature_quality_input_contract_registry(
    profile: FeatureQualityDriftProfile | None = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and summary of quality input contracts."""
    active_profile = profile or get_default_feature_quality_drift_profile()

    records = []
    for c in QUALITY_INPUT_CONTRACTS:
        records.append({
            "contract_id": c["contract_id"],
            "contract_name": c["contract_name"],
            "description": c["description"],
            "severity": c["severity"],
            "enforced": c["enforced"],
            "non_signal": True,
            "destructive_action_allowed": False,
        })

    df = pd.DataFrame(records)
    summary = {
        "active_profile": active_profile.name,
        "total_contracts": len(records),
        "current_phase": active_profile.current_phase,
        "non_signal": True,
        "destructive_action_allowed": False,
    }
    return df, summary
