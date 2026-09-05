import pytest
import glob
import sys

test_files = [
    "tests/test_research_engine_config.py",
    "tests/test_research_engine_labels.py",
    "tests/test_research_engine_models.py",
    "tests/test_research_engine_profile_registry.py",
    "tests/test_research_engine_domain_registry.py",
    "tests/test_research_context.py",
    "tests/test_research_request.py",
    "tests/test_research_result.py",
    "tests/test_research_engine_interfaces.py",
    "tests/test_data_access_interface.py",
    "tests/test_feature_interface.py",
    "tests/test_regime_interface.py",
    "tests/test_ml_interface.py",
    "tests/test_backtest_interface.py",
    "tests/test_portfolio_interface.py",
    "tests/test_report_interface.py",
    "tests/test_signal_research_interface.py",
    "tests/test_research_engine_gateway.py",
    "tests/test_research_engine_dry_run.py",
    "tests/test_research_engine_module_map.py",
    "tests/test_research_engine_dependency_map.py",
    "tests/test_research_engine_safety_boundary.py",
    "tests/test_research_engine_health.py",
    "tests/test_research_engine_scoring.py",
    "tests/test_research_engine_validation.py",
    "tests/test_research_engine_quality.py",
    "tests/test_research_engine_report_builder.py",
    "tests/test_research_engine_pipeline.py",
    "tests/test_advanced_research_engine_scripts_contract.py"
]

sys.exit(pytest.main(test_files))
