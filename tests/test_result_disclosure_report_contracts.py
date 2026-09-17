# -*- coding: utf-8 -*-
from advanced_benchmark_evaluation.benchmark_evaluation_config import get_default_benchmark_evaluation_profile
from advanced_benchmark_evaluation.result_disclosure_report_contracts import build_result_disclosure_report_contract_registry

def test_build_result_disclosure_report_contract_registry():
    profile = get_default_benchmark_evaluation_profile()
    df, summary = build_result_disclosure_report_contract_registry(profile)
    assert not df.empty
    assert 'disclosure_id' in df.columns
    assert (df['non_signal'] == True).all()
    assert summary['all_mandatory'] is True
