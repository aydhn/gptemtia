# -*- coding: utf-8 -*-
from advanced_benchmark_evaluation.benchmark_evaluation_config import get_default_benchmark_evaluation_profile
from advanced_benchmark_evaluation.benchmark_report_execution_disabled import build_benchmark_report_execution_disabled_report
from advanced_benchmark_evaluation.strategy_evaluation_execution_disabled import build_strategy_evaluation_execution_disabled_report
from advanced_benchmark_evaluation.evaluation_metric_calculation_disabled import build_evaluation_metric_calculation_disabled_report
from advanced_benchmark_evaluation.evaluation_result_claim_disabled import build_evaluation_result_claim_disabled_report
from advanced_benchmark_evaluation.evaluation_strategy_approval_disabled import build_evaluation_strategy_approval_disabled_report
from advanced_benchmark_evaluation.evaluation_optimizer_disabled import build_evaluation_optimizer_disabled_report
from advanced_benchmark_evaluation.evaluation_model_training_disabled import build_evaluation_model_training_disabled_report
from advanced_benchmark_evaluation.evaluation_prediction_disabled import build_evaluation_prediction_disabled_report
from advanced_benchmark_evaluation.evaluation_live_trading_disabled import build_evaluation_live_trading_disabled_report
from advanced_benchmark_evaluation.evaluation_broker_execution_disabled import build_evaluation_broker_execution_disabled_report
from advanced_benchmark_evaluation.evaluation_deployment_disabled import build_evaluation_deployment_disabled_report

def test_build_benchmark_evaluation_disabled_execution():
    profile = get_default_benchmark_evaluation_profile()
    reports = [
        build_benchmark_report_execution_disabled_report(profile),
        build_strategy_evaluation_execution_disabled_report(profile),
        build_evaluation_metric_calculation_disabled_report(profile),
        build_evaluation_result_claim_disabled_report(profile),
        build_evaluation_strategy_approval_disabled_report(profile),
        build_evaluation_optimizer_disabled_report(profile),
        build_evaluation_model_training_disabled_report(profile),
        build_evaluation_prediction_disabled_report(profile),
        build_evaluation_live_trading_disabled_report(profile),
        build_evaluation_broker_execution_disabled_report(profile),
        build_evaluation_deployment_disabled_report(profile),
    ]
    for df, s in reports:
        assert not df.empty
        assert (df['is_disabled'] == True).all()
        assert s['is_disabled'] is True
        assert s['non_signal'] is True
