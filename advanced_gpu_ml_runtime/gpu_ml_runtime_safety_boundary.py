"""Phase 136: GPU ML Runtime Safety Boundary.

Defines NO-GO rules and SAFE-GO principles separating offline runtime discovery
from live execution, automated trading, and model training.
"""

from typing import Any, Dict, List, Optional, Tuple
import pandas as pd

from advanced_gpu_ml_runtime.gpu_ml_runtime_config import (
    GpuMlRuntimeProfile,
    get_gpu_ml_runtime_profile,
)
from advanced_gpu_ml_runtime.gpu_ml_runtime_labels import (
    SAFETY_DOMAIN,
    RUNTIME_READY,
)


NO_GO_CONDITIONS = [
    "live trading",
    "broker integration",
    "real order",
    "investment advice",
    "signal generation",
    "directional certainty",
    "strategy/backtest/optimizer execution",
    "model training/model fit/model predict/model inference/model transform",
    "clustering/unsupervised/ensemble/calibration execution",
    "target/label/prediction",
    "sentiment model output",
    "full article/article body/raw content/scraped HTML usage",
    "embedding/vector generation",
    "artifact persistence/model registry write",
    "official approval/production-ready/broker-ready",
    "source overwrite/destructive cleaning",
    "auto-imputation/auto-feature-drop",
    "scraping",
    "credential output",
    "deployment",
]

SAFE_GO_CONDITIONS = [
    "local/offline hardware capability discovery",
    "GPU/CPU/memory capability metadata",
    "dependency availability metadata",
    "ML runtime environment snapshot without secrets",
    "safety contract generation",
    "experiment permission registry",
    "ML input contract generation",
    "no-lookahead accepted reference mapping",
    "metadata-only news accepted reference mapping",
    "source-preserved input contract mapping",
    "Phase 137 dataset/experiment handoff",
]


def build_gpu_ml_runtime_no_go_conditions(
    profile: Optional[GpuMlRuntimeProfile] = None,
) -> pd.DataFrame:
    """Build DataFrame of NO-GO boundary rules."""
    rows = [
        {
            "condition_type": "NO-GO",
            "condition_name": cond,
            "enforced": True,
            "status_label": RUNTIME_READY,
            "non_signal": True,
            "source_preserved": True,
            "official_approval": False,
            "production_ready": False,
            "broker_ready": False,
        }
        for cond in NO_GO_CONDITIONS
    ]
    return pd.DataFrame(rows)


def build_gpu_ml_runtime_safe_go_conditions(
    profile: Optional[GpuMlRuntimeProfile] = None,
) -> pd.DataFrame:
    """Build DataFrame of SAFE-GO operational principles."""
    rows = [
        {
            "condition_type": "SAFE-GO",
            "condition_name": cond,
            "active": True,
            "status_label": RUNTIME_READY,
            "non_signal": True,
            "source_preserved": True,
            "official_approval": False,
            "production_ready": False,
            "broker_ready": False,
        }
        for cond in SAFE_GO_CONDITIONS
    ]
    return pd.DataFrame(rows)


def build_gpu_ml_runtime_safety_boundary(
    profile: Optional[GpuMlRuntimeProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build unified safety boundary DataFrame and metadata summary."""
    active = profile or get_gpu_ml_runtime_profile()

    no_go_df = build_gpu_ml_runtime_no_go_conditions(active)
    safe_go_df = build_gpu_ml_runtime_safe_go_conditions(active)

    combined_df = pd.concat([no_go_df, safe_go_df], ignore_index=True)
    summary = summarize_gpu_ml_runtime_safety_boundary(combined_df)
    summary["domain"] = SAFETY_DOMAIN
    summary["active_profile"] = active.profile_name
    return combined_df, summary


def summarize_gpu_ml_runtime_safety_boundary(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize safety boundary DataFrame."""
    no_go_count = int((df["condition_type"] == "NO-GO").sum()) if not df.empty and "condition_type" in df.columns else 0
    safe_go_count = int((df["condition_type"] == "SAFE-GO").sum()) if not df.empty and "condition_type" in df.columns else 0
    return {
        "total_conditions": len(df),
        "no_go_count": no_go_count,
        "safe_go_count": safe_go_count,
        "safety_status": "SECURE",
        "live_trading_prohibited": True,
        "model_training_prohibited": True,
        "non_signal": True,
        "source_preserved": True,
        "official_approval": False,
        "production_ready": False,
        "broker_ready": False,
    }
