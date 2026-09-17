# -*- coding: utf-8 -*-
from advanced_benchmark_evaluation.benchmark_evaluation_config import get_default_benchmark_evaluation_profile
from advanced_benchmark_evaluation.evaluation_input_data_contracts import build_evaluation_input_data_contract_registry

def test_build_evaluation_input_data_contract_registry():
    profile = get_default_benchmark_evaluation_profile()
    df, summary = build_evaluation_input_data_contract_registry(profile)
    assert not df.empty
    assert 'contract_id' in df.columns
    assert (df['non_signal'] == True).all()
    assert summary['non_signal'] is True
