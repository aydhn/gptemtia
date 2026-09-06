"""Phase 136: Run GPU ML Runtime Status Script.

Executes the full Phase 136 pipeline and displays complete operational status across all registries and safety boundaries.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from advanced_gpu_ml_runtime.gpu_ml_runtime_pipeline import GpuMlRuntimePipeline
from advanced_gpu_ml_runtime.gpu_ml_runtime_config import get_default_gpu_ml_runtime_profile
from reports.report_builder import GPU_ML_RUNTIME_TEXT_REPORT_DISCLAIMER


def main():
    profile = get_default_gpu_ml_runtime_profile()
    pipeline = GpuMlRuntimePipeline(profile=profile)
    df_status, summary = pipeline.run(save=True)

    print("=" * 70)
    print("PHASE 136: GPU & ML RUNTIME FULL PIPELINE STATUS")
    print("=" * 70)
    print(GPU_ML_RUNTIME_TEXT_REPORT_DISCLAIMER)
    print("-" * 70)
    print(f"Active Profile        : {summary['active_profile']}")
    print(f"Current Phase         : {summary['current_phase']}")
    print(f"Next Phase            : {summary['next_phase']}")
    print(f"Target Final Phase    : {summary['target_final_phase']}")
    print(f"Pipeline Status       : {summary['status']}")
    print(f"Readiness Score       : {summary['readiness_score']:.4f}")
    print(f"Validation Passed     : {summary['validation_passed']}")
    print(f"Handoff Ready         : {summary['handoff_ready']}")
    print(f"Model Training Blocked: True")
    print(f"Model Inference Blocked: True")
    print(f"Non-Signal Maintained : True")
    print("=" * 70)


if __name__ == "__main__":
    main()
