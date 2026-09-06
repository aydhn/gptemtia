"""Phase 136: Regime Metadata ML Input Contracts.

Defines input contracts connecting Phases 126-135 regime classification outputs
as non-directional feature contexts for upcoming ML experiments.
"""

from typing import Any, Dict, List, Optional, Tuple
import pandas as pd

from advanced_gpu_ml_runtime.gpu_ml_runtime_config import (
    GpuMlRuntimeProfile,
    get_gpu_ml_runtime_profile,
)
from advanced_gpu_ml_runtime.gpu_ml_runtime_labels import (
    REGIME_METADATA_INPUT_CONTRACT_DOMAIN,
    RUNTIME_READY,
)


REGIME_INPUT_CONTRACT_SPECS: List[Dict[str, Any]] = [
    {
        "contract_id": "contract_phase_126_regime_taxonomy",
        "source_component": "advanced_regime_foundation",
        "source_phase": 126,
        "dataset_entity": "market_behavior_regime_taxonomy",
        "accepted_reference_required": True,
        "details": "Taxonomy definitions and regime family mappings as discrete metadata inputs.",
    },
    {
        "contract_id": "contract_phase_127_regime_matrix",
        "source_component": "advanced_regime_matrix",
        "source_phase": 127,
        "dataset_entity": "regime_feature_matrix_contracts",
        "accepted_reference_required": True,
        "details": "Regime feature matrices and state dataset schemas with timestamp alignment.",
    },
    {
        "contract_id": "contract_phase_128_candidate_states",
        "source_component": "advanced_regime_rule_free",
        "source_phase": 128,
        "dataset_entity": "candidate_state_assignment_specs",
        "accepted_reference_required": True,
        "details": "Unsupervised prep contracts and candidate state metadata without trade signals.",
    },
    {
        "contract_id": "contract_phase_129_behavior_diagnostics",
        "source_component": "advanced_market_behavior_diagnostics",
        "source_phase": 129,
        "dataset_entity": "market_behavior_diagnostics_metrics",
        "accepted_reference_required": True,
        "details": "Quality and behavior consistency metrics as feature filtering gates.",
    },
    {
        "contract_id": "contract_phase_130_transition_stability",
        "source_component": "advanced_regime_transition",
        "source_phase": 130,
        "dataset_entity": "regime_transition_stability_metrics",
        "accepted_reference_required": True,
        "details": "State transition continuity and persistence metrics for sequence models.",
    },
    {
        "contract_id": "contract_phase_131_cross_asset_context",
        "source_component": "advanced_cross_asset_regime_context",
        "source_phase": 131,
        "dataset_entity": "cross_asset_regime_context_pairs",
        "accepted_reference_required": True,
        "details": "Cross-asset volatility, trend, and range linkages as multi-asset features.",
    },
    {
        "contract_id": "contract_phase_132_macro_event_news",
        "source_component": "advanced_macro_event_news_regime",
        "source_phase": 132,
        "dataset_entity": "macro_event_news_regime_context",
        "accepted_reference_required": True,
        "details": "Macro release lags, event windows, and news metadata tags strictly without raw text.",
    },
    {
        "contract_id": "contract_phase_133_validation_acceptance",
        "source_component": "advanced_regime_validation_acceptance",
        "source_phase": 133,
        "dataset_entity": "regime_validation_no_lookahead_gates",
        "accepted_reference_required": True,
        "details": "Accepted no-lookahead backward asof join specifications.",
    },
    {
        "contract_id": "contract_phase_134_featurestore_catalog",
        "source_component": "advanced_regime_featurestore_integration",
        "source_phase": 134,
        "dataset_entity": "regime_featurestore_catalogs",
        "accepted_reference_required": True,
        "details": "Standardized FeatureStore entity namespaces and read contracts.",
    },
    {
        "contract_id": "contract_phase_135_regime_manifest",
        "source_component": "advanced_regime_acceptance",
        "source_phase": 135,
        "dataset_entity": "regime_block_acceptance_manifest",
        "accepted_reference_required": True,
        "details": "Complete Phase 126-135 block acceptance verification and non-signal compliance.",
    },
]


def build_regime_metadata_ml_input_contract_registry(
    profile: Optional[GpuMlRuntimeProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and metadata summary for regime metadata ML input contracts."""
    active = profile or get_gpu_ml_runtime_profile()

    rows: List[Dict[str, Any]] = []
    for spec in REGIME_INPUT_CONTRACT_SPECS:
        rows.append(
            {
                "contract_id": spec["contract_id"],
                "source_component": spec["source_component"],
                "source_phase": spec["source_phase"],
                "dataset_entity": spec["dataset_entity"],
                "accepted_reference_required": spec["accepted_reference_required"],
                "no_lookahead_accepted_required": True,
                "metadata_only_news_accepted_required": True,
                "source_preserved_required": True,
                "non_signal_required": True,
                "target_label_forbidden": True,
                "prediction_forbidden": True,
                "model_training_allowed": False,
                "status_label": RUNTIME_READY,
                "manual_review_required": False,
                "non_signal": True,
                "source_preserved": True,
                "details": spec["details"],
            }
        )

    df = pd.DataFrame(rows)
    summary = summarize_regime_metadata_ml_input_contracts(df)
    summary["domain"] = REGIME_METADATA_INPUT_CONTRACT_DOMAIN
    summary["active_profile"] = active.profile_name
    return df, summary


def summarize_regime_metadata_ml_input_contracts(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize regime metadata ML input contracts DataFrame."""
    return {
        "total_contracts": len(df),
        "status_label": RUNTIME_READY,
        "all_source_preserved": True,
        "all_non_signal": True,
        "training_blocked": True,
        "official_approval": False,
        "production_ready": False,
        "broker_ready": False,
    }
