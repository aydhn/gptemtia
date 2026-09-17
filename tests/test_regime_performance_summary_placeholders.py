# -*- coding: utf-8 -*-
from advanced_benchmark_evaluation.benchmark_evaluation_config import get_default_benchmark_evaluation_profile
from advanced_benchmark_evaluation.regime_performance_summary_placeholders import build_regime_performance_summary_placeholder_registry

def test_build_regime_performance_summary_placeholder_registry():
    profile = get_default_benchmark_evaluation_profile()
    df, summary = build_regime_performance_summary_placeholder_registry(profile)
    assert not df.empty
    assert len(df) >= 2
    assert (df['is_calculated'] == False).all()
    assert (df['non_signal'] == True).all()
    assert summary['all_uncalculated'] is True
    assert summary['non_signal'] is True
