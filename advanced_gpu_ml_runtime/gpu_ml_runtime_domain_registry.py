"""Phase 136: GPU ML Runtime Domain Registry.

Builds and catalogs all functional domains in the GPU ML Runtime foundation layer.
"""

from typing import Any, Dict, List, Optional, Tuple
import pandas as pd

from advanced_gpu_ml_runtime.gpu_ml_runtime_config import (
    GpuMlRuntimeProfile,
    get_gpu_ml_runtime_profile,
)
from advanced_gpu_ml_runtime.gpu_ml_runtime_labels import (
    GPU_ML_RUNTIME_DOMAIN,
    RUNTIME_READY,
    LOCAL_HARDWARE_DOMAIN,
    GPU_CAPABILITY_DOMAIN,
    CPU_CAPABILITY_DOMAIN,
    MEMORY_CAPABILITY_DOMAIN,
    CUDA_CAPABILITY_DOMAIN,
    TORCH_CAPABILITY_DOMAIN,
    SKLEARN_CAPABILITY_DOMAIN,
    NUMPY_PANDAS_CAPABILITY_DOMAIN,
    OPTIONAL_DEPENDENCY_DOMAIN,
    ACCELERATOR_BACKEND_DOMAIN,
    ENVIRONMENT_SNAPSHOT_DOMAIN,
    RUNTIME_SAFETY_CONTRACT_DOMAIN,
    EXPERIMENT_PERMISSION_DOMAIN,
    TRAINING_DISABLED_DOMAIN,
    INFERENCE_DISABLED_DOMAIN,
    TARGET_LABEL_DISABLED_DOMAIN,
    ARTIFACT_GOVERNANCE_PLACEHOLDER_DOMAIN,
    REGIME_METADATA_INPUT_CONTRACT_DOMAIN,
    FEATURESTORE_INPUT_CONTRACT_DOMAIN,
    NO_LOOKAHEAD_INPUT_CONTRACT_DOMAIN,
    METADATA_ONLY_NEWS_INPUT_CONTRACT_DOMAIN,
    SOURCE_PRESERVATION_INPUT_CONTRACT_DOMAIN,
    PHASE_137_HANDOFF_DOMAIN,
)


DOMAIN_SPECS: List[Dict[str, Any]] = [
    {"domain": LOCAL_HARDWARE_DOMAIN, "topic": "Local Hardware Discovery", "scope": "Platform and architecture discovery"},
    {"domain": GPU_CAPABILITY_DOMAIN, "topic": "GPU Capability Registry", "scope": "Local GPU and CUDA query metadata"},
    {"domain": CPU_CAPABILITY_DOMAIN, "topic": "CPU Capability Registry", "scope": "CPU cores and architecture query"},
    {"domain": MEMORY_CAPABILITY_DOMAIN, "topic": "Memory Capability Registry", "scope": "System RAM and swap limits"},
    {"domain": CUDA_CAPABILITY_DOMAIN, "topic": "CUDA Availability Report", "scope": "CUDA runtime driver and version check"},
    {"domain": TORCH_CAPABILITY_DOMAIN, "topic": "PyTorch Runtime Capability", "scope": "Torch import and CUDA linkage without tensors"},
    {"domain": SKLEARN_CAPABILITY_DOMAIN, "topic": "Scikit-Learn Runtime Capability", "scope": "sklearn availability without fitting"},
    {"domain": NUMPY_PANDAS_CAPABILITY_DOMAIN, "topic": "NumPy/Pandas Runtime Capability", "scope": "Core array and dataframe foundation"},
    {"domain": OPTIONAL_DEPENDENCY_DOMAIN, "topic": "Optional ML Dependencies", "scope": "LightGBM/XGBoost/CatBoost/ONNX/Optuna/SHAP status"},
    {"domain": ACCELERATOR_BACKEND_DOMAIN, "topic": "Accelerator Backend Registry", "scope": "CPU, CUDA, and future acceleration backends"},
    {"domain": ENVIRONMENT_SNAPSHOT_DOMAIN, "topic": "ML Runtime Environment Snapshot", "scope": "Non-sensitive runtime operational snapshot"},
    {"domain": RUNTIME_SAFETY_CONTRACT_DOMAIN, "topic": "ML Runtime Safety Contracts", "scope": "Non-signal, no-broker, no-order safety guarantees"},
    {"domain": EXPERIMENT_PERMISSION_DOMAIN, "topic": "Experiment Permission Policies", "scope": "Allowed discovery, blocked training/predict policies"},
    {"domain": TRAINING_DISABLED_DOMAIN, "topic": "Training Disabled Policies", "scope": "Enforced block on model fit and training routines"},
    {"domain": INFERENCE_DISABLED_DOMAIN, "topic": "Inference Disabled Policies", "scope": "Enforced block on prediction and inference"},
    {"domain": TARGET_LABEL_DISABLED_DOMAIN, "topic": "Target/Label Disabled Policies", "scope": "Enforced block on future returns and labels"},
    {"domain": ARTIFACT_GOVERNANCE_PLACEHOLDER_DOMAIN, "topic": "Artifact Governance Placeholders", "scope": "Model card, artifact manifest schemas"},
    {"domain": REGIME_METADATA_INPUT_CONTRACT_DOMAIN, "topic": "Regime Metadata ML Input Contracts", "scope": "Phase 126-135 regime context contracts"},
    {"domain": FEATURESTORE_INPUT_CONTRACT_DOMAIN, "topic": "FeatureStore ML Input Contracts", "scope": "FeatureStore namespace and query contracts"},
    {"domain": NO_LOOKAHEAD_INPUT_CONTRACT_DOMAIN, "topic": "No-Lookahead ML Input Contracts", "scope": "Enforced chronological asof boundaries"},
    {"domain": METADATA_ONLY_NEWS_INPUT_CONTRACT_DOMAIN, "topic": "Metadata-Only News ML Input Contracts", "scope": "Zero raw text or scraped HTML in inputs"},
    {"domain": SOURCE_PRESERVATION_INPUT_CONTRACT_DOMAIN, "topic": "Source Preservation ML Input Contracts", "scope": "Zero source mutation or destructive actions"},
    {"domain": PHASE_137_HANDOFF_DOMAIN, "topic": "Phase 137 ML Dataset Handoff", "scope": "Specifications for dataset contracts & experiment registry"},
]


def build_gpu_ml_runtime_domain_registry(
    profile: Optional[GpuMlRuntimeProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and metadata summary for GPU ML runtime domain registry."""
    active = profile or get_gpu_ml_runtime_profile()
    rows = []
    for spec in DOMAIN_SPECS:
        rows.append(
            {
                "domain": spec["domain"],
                "topic": spec["topic"],
                "scope": spec["scope"],
                "status_label": RUNTIME_READY,
                "non_signal": True,
                "source_preserved": True,
            }
        )

    df = pd.DataFrame(rows)
    summary: Dict[str, Any] = {
        "domain": GPU_ML_RUNTIME_DOMAIN,
        "active_profile": active.profile_name,
        "current_phase": active.current_phase,
        "target_final_phase": active.target_final_phase,
        "next_phase": active.next_phase,
        "total_domains": len(df),
        "non_signal": True,
        "status": RUNTIME_READY,
    }
    return df, summary
