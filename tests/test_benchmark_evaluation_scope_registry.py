# -*- coding: utf-8 -*-
from advanced_benchmark_evaluation.benchmark_evaluation_config import get_default_benchmark_evaluation_profile
from advanced_benchmark_evaluation.benchmark_evaluation_scope_registry import build_benchmark_evaluation_scope_registry

def test_build_benchmark_evaluation_scope_registry():
    profile = get_default_benchmark_evaluation_profile()
    df, summary = build_benchmark_evaluation_scope_registry(profile)
    assert not df.empty
    assert 'scope_name' in df.columns
    assert summary['all_excluded_blocked'] is True
    assert summary['non_signal'] is True
