# -*- coding: utf-8 -*-
from advanced_benchmark_evaluation.benchmark_evaluation_config import get_default_benchmark_evaluation_profile
from advanced_benchmark_evaluation.strategy_limitation_placeholders import build_strategy_limitation_placeholder_registry

def test_build_strategy_limitation_placeholder_registry():
    profile = get_default_benchmark_evaluation_profile()
    df, summary = build_strategy_limitation_placeholder_registry(profile)
    assert not df.empty
    assert len(df) >= 2
    assert "limitation_id" in df.columns
    assert (df['non_signal'] == True).all()
    assert summary['non_signal'] is True
    assert summary['total_limitations'] >= 2
