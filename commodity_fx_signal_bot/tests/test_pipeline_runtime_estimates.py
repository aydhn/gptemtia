from local_performance.pipeline_runtime_estimates import build_pipeline_runtime_estimate_registry, build_known_pipeline_runtime_estimates
from local_performance.performance_config import get_default_local_performance_profile
from pathlib import Path

def test_pipeline_runtime_estimates():
    p = get_default_local_performance_profile()
    df, s = build_pipeline_runtime_estimate_registry(Path("."), p)
    assert not df.empty
