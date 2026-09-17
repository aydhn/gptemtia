# -*- coding: utf-8 -*-
from advanced_benchmark_evaluation.benchmark_evaluation_config import get_default_benchmark_evaluation_profile
from advanced_benchmark_evaluation.benchmark_universe_report_contracts import build_benchmark_universe_report_contract_registry

def test_build_benchmark_universe_report_contract_registry():
    profile = get_default_benchmark_evaluation_profile()
    df, summary = build_benchmark_universe_report_contract_registry(profile)
    assert not df.empty
    assert 'universe_id' in df.columns
    assert (df['non_signal'] == True).all()
    assert summary['all_execution_disabled'] is True
