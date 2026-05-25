import pytest
import pandas as pd
from performance.performance_config import get_default_performance_profile
from performance.optimization_recommendations import (
    build_runtime_optimization_recommendations,
    build_memory_optimization_recommendations,
    build_cache_optimization_recommendations,
    build_safe_optimization_recommendation_report
)

def test_build_runtime_optimization_recommendations():
    bn_df = pd.DataFrame([
        {"module_name": "m1", "bottleneck_type": "runtime_bottleneck", "severity": "high"},
        {"module_name": "m2", "bottleneck_type": "runtime_bottleneck", "severity": "medium"}
    ])

    res = build_runtime_optimization_recommendations(bn_df)
    assert len(res) == 2
    assert "medium_risk_optimization_candidate" in res["risk_level"].values

def test_build_memory_optimization_recommendations():
    bn_df = pd.DataFrame([
        {"module_name": "m1", "bottleneck_type": "memory_bottleneck", "severity": "high"},
    ])

    res = build_memory_optimization_recommendations(bn_df)
    assert len(res) == 1
    assert res.iloc[0]["risk_level"] == "high_risk_manual_review_required"

def test_build_cache_optimization_recommendations():
    bn_df = pd.DataFrame([
        {"module_name": "m1", "bottleneck_type": "io_bottleneck", "severity": "medium"},
    ])

    res = build_cache_optimization_recommendations(None, bn_df)
    assert len(res) == 1
    assert res.iloc[0]["risk_level"] == "medium_risk_optimization_candidate"

def test_build_safe_optimization_recommendation_report():
    profile = get_default_performance_profile()
    bn_df = pd.DataFrame([
        {"module_name": "m1", "bottleneck_type": "runtime_bottleneck", "severity": "high"},
        {"module_name": "m2", "bottleneck_type": "memory_bottleneck", "severity": "medium"}
    ])

    df, summary = build_safe_optimization_recommendation_report(bn_df, profile)
    assert len(df) == 2
    assert summary["total_recommendations"] == 2

    # Recommendations don't auto patch
    # Confirmed conceptually
