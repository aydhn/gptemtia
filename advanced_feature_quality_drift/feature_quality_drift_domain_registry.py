"""Phase 123 Feature Quality and Drift Domain Registry.

Builds immutable DataFrame and metadata summary of diagnostic domains.
"""

from typing import Any, Dict, Tuple
import pandas as pd

from advanced_feature_quality_drift.feature_quality_drift_config import (
    FeatureQualityDriftProfile,
    get_default_feature_quality_drift_profile,
)
from advanced_feature_quality_drift.feature_quality_drift_labels import list_quality_drift_domain_labels


def build_feature_quality_drift_domain_registry(
    profile: FeatureQualityDriftProfile | None = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and summary of all supported quality and drift domains."""
    active_profile = profile or get_default_feature_quality_drift_profile()
    domains = list_quality_drift_domain_labels()

    records = []
    for d in domains:
        records.append({
            "domain": d,
            "category": d.split("_")[-1] if "_" in d else "general",
            "enforced": True,
            "non_signal": True,
            "current_phase": active_profile.current_phase,
        })

    df = pd.DataFrame(records)
    summary = {
        "active_profile": active_profile.name,
        "total_domains": len(records),
        "current_phase": active_profile.current_phase,
        "target_final_phase": active_profile.target_final_phase,
        "next_phase": active_profile.next_phase,
        "non_signal": True,
    }
    return df, summary
