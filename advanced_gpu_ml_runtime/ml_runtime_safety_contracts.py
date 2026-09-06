"""Phase 136: ML Runtime Safety Contracts.

Establishes formal, enforceable safety contracts prohibiting live trading,
broker execution, model training, model inference, and target/label generation.
"""

from typing import Any, Dict, List, Optional, Tuple
import pandas as pd

from advanced_gpu_ml_runtime.gpu_ml_runtime_config import (
    GpuMlRuntimeProfile,
    get_gpu_ml_runtime_profile,
)
from advanced_gpu_ml_runtime.gpu_ml_runtime_labels import (
    RUNTIME_SAFETY_CONTRACT_DOMAIN,
    RUNTIME_READY,
)


SAFETY_CONTRACTS: List[Dict[str, Any]] = [
    {
        "contract_id": "no_live_trading_contract",
        "topic": "Live Trading Prohibition",
        "enforced": True,
        "prohibition_rule": "Zero real capital exposure, zero order routing, zero exchange integration.",
        "details": "Model execution layer has zero connection to live accounts.",
    },
    {
        "contract_id": "no_broker_contract",
        "topic": "Broker Integration Prohibition",
        "enforced": True,
        "prohibition_rule": "Zero broker API calls, zero fix/rest broker connections.",
        "details": "Broker communication strictly forbidden.",
    },
    {
        "contract_id": "no_signal_generation_contract",
        "topic": "Signal Generation Prohibition",
        "enforced": True,
        "prohibition_rule": "Zero buy/sell recommendations, trade alerts, or directional trade directives.",
        "details": "Outputs are non-signal research foundations.",
    },
    {
        "contract_id": "no_model_training_contract",
        "topic": "Model Training Prohibition in Phase 136",
        "enforced": True,
        "prohibition_rule": "Zero fit, train, gradient descent, or optimization routine execution.",
        "details": "Phase 136 is runtime discovery and governance only.",
    },
    {
        "contract_id": "no_inference_contract",
        "topic": "Inference and Prediction Prohibition in Phase 136",
        "enforced": True,
        "prohibition_rule": "Zero predict, forecast, transform, or scoring evaluations on data.",
        "details": "Model evaluation strictly blocked.",
    },
    {
        "contract_id": "no_target_label_contract",
        "topic": "Target and Label Generation Prohibition",
        "enforced": True,
        "prohibition_rule": "Zero forward return calculation, shift(-1), future return, or ground truth labels.",
        "details": "No supervised targets generated in Phase 136.",
    },
    {
        "contract_id": "no_backtest_optimizer_contract",
        "topic": "Backtest and Optimizer Execution Prohibition",
        "enforced": True,
        "prohibition_rule": "Zero strategy simulation, parameter tuning, or portfolio optimization.",
        "details": "No backtest harness invoked.",
    },
    {
        "contract_id": "no_artifact_persistence_contract",
        "topic": "Model Artifact Persistence Prohibition",
        "enforced": True,
        "prohibition_rule": "Zero serialized weights, torchscript saves, or model checkpoint files.",
        "details": "Governance placeholders only.",
    },
    {
        "contract_id": "no_model_registry_write_contract",
        "topic": "Model Registry Write Prohibition",
        "enforced": True,
        "prohibition_rule": "Zero model versioning commits or registry writes.",
        "details": "Model registry writes disabled in foundation phase.",
    },
    {
        "contract_id": "metadata_only_news_contract",
        "topic": "Metadata-Only News Boundary",
        "enforced": True,
        "prohibition_rule": "Zero full text, raw article body, scraped HTML, or sentiment model outputs in ML inputs.",
        "details": "Guarantees copyright and data purity.",
    },
    {
        "contract_id": "no_source_overwrite_contract",
        "topic": "Source Data Preservation",
        "enforced": True,
        "prohibition_rule": "Zero file deletion, overwrite, mutation, or destructive cleaning.",
        "details": "DataLake records remain immutable.",
    },
    {
        "contract_id": "local_offline_only_contract",
        "topic": "Local Offline Execution Boundary",
        "enforced": True,
        "prohibition_rule": "Zero scraping, zero remote API polling, zero cloud deployment.",
        "details": "Strictly local execution.",
    },
]


def validate_ml_runtime_safety_contract(contract: Dict[str, Any]) -> Dict[str, Any]:
    """Validate a single safety contract."""
    is_enforced = bool(contract.get("enforced", False))
    return {
        "contract_id": contract.get("contract_id", "unknown"),
        "is_valid": is_enforced,
        "non_signal": True,
        "source_preserved": True,
    }


def build_ml_runtime_safety_contract_registry(
    profile: Optional[GpuMlRuntimeProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and metadata summary for ML runtime safety contracts."""
    active = profile or get_gpu_ml_runtime_profile()

    rows: List[Dict[str, Any]] = []
    for c in SAFETY_CONTRACTS:
        rows.append(
            {
                "contract_id": c["contract_id"],
                "topic": c["topic"],
                "enforced": c["enforced"],
                "prohibition_rule": c["prohibition_rule"],
                "status_label": RUNTIME_READY,
                "non_signal": True,
                "source_preserved": True,
                "official_approval": False,
                "production_ready": False,
                "broker_ready": False,
                "details": c["details"],
            }
        )

    df = pd.DataFrame(rows)
    summary = summarize_ml_runtime_safety_contracts(df)
    summary["domain"] = RUNTIME_SAFETY_CONTRACT_DOMAIN
    summary["active_profile"] = active.profile_name
    return df, summary


def summarize_ml_runtime_safety_contracts(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize ML runtime safety contracts DataFrame."""
    all_enf = bool(df["enforced"].all()) if not df.empty and "enforced" in df.columns else False
    return {
        "total_contracts": len(df),
        "all_enforced": all_enf,
        "non_signal": True,
        "source_preserved": True,
        "official_approval": False,
        "production_ready": False,
        "broker_ready": False,
    }
