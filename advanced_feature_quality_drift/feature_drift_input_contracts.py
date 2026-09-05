"""Phase 123 Feature Drift Input Contract Registry.

Defines input contracts and preconditions required for baseline vs current drift comparison
and rolling stability monitoring.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_feature_quality_drift.feature_quality_drift_config import (
    FeatureQualityDriftProfile,
    get_default_feature_quality_drift_profile,
)

DRIFT_INPUT_CONTRACTS: List[Dict[str, Any]] = [
    {
        "contract_id": "contract_baseline_alignment",
        "contract_name": "Baseline Feature Alignment Contract",
        "description": "Baseline and current comparison windows must share identical feature column sets.",
        "severity": "drift_high",
        "enforced": True,
    },
    {
        "contract_id": "contract_min_sample_size",
        "contract_name": "Minimum Sample Size Contract",
        "description": "Comparison window requires minimum number of observations (>= 30) for valid statistical tests.",
        "severity": "drift_medium",
        "enforced": True,
    },
    {
        "contract_id": "contract_temporal_precedence",
        "contract_name": "Temporal Precedence Contract",
        "description": "Baseline window timestamps must precede or establish historical reference for comparison window.",
        "severity": "drift_critical",
        "enforced": True,
    },
    {
        "contract_id": "contract_non_signal_drift",
        "contract_name": "Non-Signal Drift Utilization Contract",
        "description": "Drift output must strictly remain diagnostic; no automated trade signals or parameter adjustments.",
        "severity": "drift_critical",
        "enforced": True,
    },
]


def build_feature_drift_input_contract_registry(
    profile: FeatureQualityDriftProfile | None = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and summary of drift input contracts."""
    active_profile = profile or get_default_feature_quality_drift_profile()

    records = []
    for c in DRIFT_INPUT_CONTRACTS:
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
