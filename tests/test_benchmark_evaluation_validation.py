# -*- coding: utf-8 -*-
from advanced_benchmark_evaluation.benchmark_evaluation_config import get_default_benchmark_evaluation_profile
from advanced_benchmark_evaluation.benchmark_evaluation_profile_registry import build_benchmark_evaluation_profile_registry
from advanced_benchmark_evaluation.benchmark_comparison_report_contracts import build_benchmark_comparison_report_contract_registry
from advanced_benchmark_evaluation.strategy_evaluation_report_contracts import build_strategy_evaluation_report_contract_registry
from advanced_benchmark_evaluation.benchmark_evaluation_manifest import build_benchmark_evaluation_manifest
from advanced_benchmark_evaluation.benchmark_evaluation_validation import (
    build_benchmark_evaluation_validation_report,
    validate_no_forbidden_benchmark_evaluation_claims,
)

def test_validation():
    profile = get_default_benchmark_evaluation_profile()
    df_prof, _ = build_benchmark_evaluation_profile_registry(profile)
    df_b_rep, _ = build_benchmark_comparison_report_contract_registry(profile)
    df_s_rep, _ = build_strategy_evaluation_report_contract_registry(profile)
    df_man, _ = build_benchmark_evaluation_manifest(profile)

    tables = {
        'profiles': df_prof,
        'benchmark_contracts': df_b_rep,
        'strategy_contracts': df_s_rep,
        'manifest': df_man,
        'guards': {},
    }
    df, s = build_benchmark_evaluation_validation_report(tables, profile)
    assert not df.empty
    assert (df['status'] == 'PASS').all()
    assert s['all_passed'] is True

    clean_check = validate_no_forbidden_benchmark_evaluation_claims(text='Research contract definition only.')
    assert clean_check['is_clean'] is True
