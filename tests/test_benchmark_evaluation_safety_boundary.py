# -*- coding: utf-8 -*-
"""Phase 151 Unit Tests: Safety Boundary."""

from advanced_benchmark_evaluation.benchmark_evaluation_config import (
    get_default_benchmark_evaluation_profile,
)
from advanced_benchmark_evaluation.benchmark_evaluation_safety_boundary import (
    build_benchmark_evaluation_safety_boundary,
    build_benchmark_evaluation_no_go_conditions,
    build_benchmark_evaluation_safe_go_conditions,
)


def test_safety_boundary():
    profile = get_default_benchmark_evaluation_profile()
    df_nogo, s_nogo = build_benchmark_evaluation_no_go_conditions(profile)
    assert not df_nogo.empty
    assert len(df_nogo) >= 15
    assert (df_nogo["status"] == "ENFORCED").all()

    df_safego, s_safego = build_benchmark_evaluation_safe_go_conditions(profile)
    assert not df_safego.empty
    assert len(df_safego) >= 7

    df, s = build_benchmark_evaluation_safety_boundary(profile)
    assert not df.empty
    assert s["safety_status"] == "SECURE"
    assert s["non_signal"] is True
