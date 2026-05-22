import importlib

def test_scripts():
    importlib.import_module("scripts.run_factor_research_report")
    importlib.import_module("scripts.run_factor_score_report")
    importlib.import_module("scripts.run_factor_backtest_report")
    importlib.import_module("scripts.run_factor_exposure_report")
    importlib.import_module("scripts.run_factor_neutral_report")
    importlib.import_module("scripts.run_factor_research_status")
