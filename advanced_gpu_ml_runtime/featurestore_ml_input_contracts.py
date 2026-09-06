"""Phase 136: FeatureStore ML Input Contracts.

Defines input contracts connecting FeatureStore catalogs to ML research
under strict non-signal, no-training, and source preservation constraints.
"""

from typing import Any, Dict, List, Optional, Tuple
import pandas as pd

from advanced_gpu_ml_runtime.gpu_ml_runtime_config import (
    GpuMlRuntimeProfile,
    get_gpu_ml_runtime_profile,
)
from advanced_gpu_ml_runtime.gpu_ml_runtime_labels import (
    FEATURESTORE_INPUT_CONTRACT_DOMAIN,
    RUNTIME_READY,
)


FEATURESTORE_CATALOG_INPUTS: List[Dict[str, Any]] = [
    {
        "contract_id": "fs_input_price_technicals",
        "source_store_catalog": "technical_indicators_catalog",
        "source_phase": 117,
        "details": "Technical features across RSI, MACD, Moving Averages without future shifts.",
    },
    {
        "contract_id": "fs_input_feature_grid",
        "source_store_catalog": "multi_window_feature_grid_catalog",
        "source_phase": 118,
        "details": "Multi-window standardized rolling indicator grid matrices.",
    },
    {
        "contract_id": "fs_input_macro_indicators",
        "source_store_catalog": "macro_indicator_catalog",
        "source_phase": 119,
        "details": "Macroeconomic release time-series with publication lag alignment.",
    },
    {
        "contract_id": "fs_input_economic_calendar",
        "source_store_catalog": "economic_calendar_catalog",
        "source_phase": 120,
        "details": "Calendar surprise metrics and event windows.",
    },
    {
        "contract_id": "fs_input_news_metadata",
        "source_store_catalog": "news_metadata_catalog",
        "source_phase": 120,
        "details": "Topic flags and sentiment metadata strictly excluding raw text and HTML.",
    },
    {
        "contract_id": "fs_input_cross_asset",
        "source_store_catalog": "cross_asset_regime_catalog",
        "source_phase": 134,
        "details": "Cross-asset correlation, divergence, and linkage metrics.",
    },
    {
        "contract_id": "fs_input_regime_matrix",
        "source_store_catalog": "regime_matrix_store_catalog",
        "source_phase": 134,
        "details": "Regime feature matrices cataloged in FeatureStore.",
    },
    {
        "contract_id": "fs_input_regime_validation",
        "source_store_catalog": "regime_validation_store_catalog",
        "source_phase": 134,
        "details": "Validation-accepted asof join references and quality metadata.",
    },
]


def build_featurestore_ml_input_contract_registry(
    profile: Optional[GpuMlRuntimeProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and metadata summary for FeatureStore ML input contracts."""
    active = profile or get_gpu_ml_runtime_profile()

    rows: List[Dict[str, Any]] = []
    for item in FEATURESTORE_CATALOG_INPUTS:
        rows.append(
            {
                "contract_id": item["contract_id"],
                "source_store_catalog": item["source_store_catalog"],
                "source_phase": item["source_phase"],
                "accepted_reference_required": True,
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
                "details": item["details"],
            }
        )

    df = pd.DataFrame(rows)
    summary = summarize_featurestore_ml_input_contracts(df)
    summary["domain"] = FEATURESTORE_INPUT_CONTRACT_DOMAIN
    summary["active_profile"] = active.profile_name
    return df, summary


def summarize_featurestore_ml_input_contracts(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize FeatureStore ML input contracts DataFrame."""
    return {
        "total_contracts": len(df),
        "status_label": RUNTIME_READY,
        "non_signal": True,
        "source_preserved": True,
        "official_approval": False,
        "production_ready": False,
        "broker_ready": False,
    }
