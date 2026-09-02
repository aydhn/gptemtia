from local_performance.growth_estimates import build_report_output_growth_estimate, build_datalake_growth_estimate, build_generated_docs_growth_estimate
from local_performance.performance_config import get_default_local_performance_profile
from pathlib import Path

def test_growth_estimates():
    p = get_default_local_performance_profile()
    df1, _ = build_report_output_growth_estimate(Path("."), p)
    df2, _ = build_datalake_growth_estimate(Path("."), p)
    df3, _ = build_generated_docs_growth_estimate(Path("."), p)
    assert not df1.empty and not df2.empty and not df3.empty
