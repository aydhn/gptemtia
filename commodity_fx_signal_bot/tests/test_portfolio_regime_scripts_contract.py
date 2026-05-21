import pytest
import importlib

def test_script_imports():
    scripts = [
        "scripts.run_regime_portfolio_report",
        "scripts.run_macro_scenario_sensitivity_report",
        "scripts.run_basket_stress_test_report",
        "scripts.run_drawdown_cluster_report",
        "scripts.run_risk_regime_exposure_report",
        "scripts.run_portfolio_regime_status"
    ]

    for script in scripts:
        module = importlib.import_module(script)
        assert hasattr(module, "main"), f"{script} is missing main()"
