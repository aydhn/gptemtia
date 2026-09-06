"""Phase 136: GPU ML Runtime Profile Registry.

Builds and summarizes configured GPU ML runtime foundation profiles.
"""

from typing import Any, Dict, Optional, Tuple
import pandas as pd

from advanced_gpu_ml_runtime.gpu_ml_runtime_config import (
    GpuMlRuntimeProfile,
    get_gpu_ml_runtime_profile,
    list_gpu_ml_runtime_profiles,
)
from advanced_gpu_ml_runtime.gpu_ml_runtime_labels import (
    GPU_ML_RUNTIME_PROFILE_DOMAIN,
    RUNTIME_READY,
)


def build_gpu_ml_runtime_profile_registry(
    profile: Optional[GpuMlRuntimeProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and metadata summary for GPU ML runtime profile registry."""
    active = profile or get_gpu_ml_runtime_profile()
    profiles = list_gpu_ml_runtime_profiles()

    rows = []
    for p in profiles:
        rows.append(
            {
                "profile_name": p.profile_name,
                "description": p.description,
                "current_phase": p.current_phase,
                "target_final_phase": p.target_final_phase,
                "next_phase": p.next_phase,
                "dry_run_default": p.dry_run_default,
                "local_only": p.local_only,
                "non_production": p.non_production,
                "research_only": p.research_only,
                "allow_live_trading": p.allow_live_trading,
                "allow_model_training": p.allow_model_training,
                "allow_model_predict": p.allow_model_predict,
                "allow_target_label_generation": p.allow_target_label_generation,
                "min_readiness_score": p.min_readiness_score,
                "enabled": p.enabled,
                "status_label": RUNTIME_READY,
                "non_signal": True,
            }
        )

    df = pd.DataFrame(rows)
    summary: Dict[str, Any] = {
        "domain": GPU_ML_RUNTIME_PROFILE_DOMAIN,
        "active_profile": active.profile_name,
        "current_phase": active.current_phase,
        "target_final_phase": active.target_final_phase,
        "next_phase": active.next_phase,
        "total_profiles": len(df),
        "non_signal": True,
        "status": RUNTIME_READY,
    }
    return df, summary
