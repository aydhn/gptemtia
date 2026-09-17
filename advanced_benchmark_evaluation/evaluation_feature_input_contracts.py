# -*- coding: utf-8 -*-
"""Phase 151: Evaluation Feature Input Contracts Module.

Defines feature input contracts for strategy evaluation.
Links to FeatureStore metadata catalog and enforces canonical namespaces.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_benchmark_evaluation.benchmark_evaluation_config import BenchmarkEvaluationProfile
from advanced_benchmark_evaluation.benchmark_evaluation_labels import (
    LABEL_DEPENDENCY_DOMAIN,
    STATUS_EVALUATION_CONTRACT_READY,
)

FEATURE_INPUT_CONTRACTS: List[Dict[str, Any]] = [
    {
        "contract_id": "FEAT_INP_FEATURESTORE_LINK",
        "feature_set": "technical_volatility_momentum",
        "upstream_phase_ref": "phase_124_featurestore",
        "namespace_format": "canonical factor__<family>__<asset>__<symbol>__<name>__<win>",
        "description": "Doğrulanmış FeatureStore faktör seti entegrasyon sözleşmesi.",
    },
    {
        "contract_id": "FEAT_INP_REGIME_CONTEXT",
        "feature_set": "regime_state_features",
        "upstream_phase_ref": "phase_134_regime_featurestore",
        "namespace_format": "canonical regime__<state>__<symbol>",
        "description": "Piyasa rejimi durum göstergeleri entegrasyon sözleşmesi.",
    },
    {
        "contract_id": "FEAT_INP_NEWS_METADATA_ONLY",
        "feature_set": "news_event_metadata",
        "upstream_phase_ref": "phase_111_news_metadata",
        "namespace_format": "news_meta__<tag>__count",
        "description": "Yalnızca metaveri içeren (tam metin içermeyen) haber etiket sözleşmesi.",
    },
]


def build_evaluation_feature_input_contract_registry(
    profile: BenchmarkEvaluationProfile | None = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame registry of evaluation feature input contracts."""
    rows: List[Dict[str, Any]] = []

    for c in FEATURE_INPUT_CONTRACTS:
        rows.append(
            {
                "contract_id": c["contract_id"],
                "feature_set": c["feature_set"],
                "upstream_phase_ref": c["upstream_phase_ref"],
                "namespace_format": c["namespace_format"],
                "description": c["description"],
                "status": STATUS_EVALUATION_CONTRACT_READY,
                "non_signal": True,
            }
        )

    df = pd.DataFrame(rows)
    summary = {
        "domain": LABEL_DEPENDENCY_DOMAIN,
        "total_contracts": len(df),
        "status": STATUS_EVALUATION_CONTRACT_READY,
        "non_signal": True,
    }
    return df, summary
