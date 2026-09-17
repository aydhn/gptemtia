# -*- coding: utf-8 -*-
"""Phase 151 Unit Tests: Health Check."""

from advanced_benchmark_evaluation.benchmark_evaluation_config import (
    get_default_benchmark_evaluation_profile,
)
from advanced_benchmark_evaluation.benchmark_evaluation_health import (
    build_benchmark_evaluation_health_check,
)


def test_health():
    profile = get_default_benchmark_evaluation_profile()
    df, s = build_benchmark_evaluation_health_check(profile=profile)

    assert not df.empty
    assert len(df) >= 10
    assert "check_id" in df.columns
    assert (df["status"] == "HEALTHY").all()
    assert s["all_healthy"] is True
    assert s["non_signal"] is True
