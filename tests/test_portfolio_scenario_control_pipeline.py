# -*- coding: utf-8 -*-
from advanced_portfolio_scenario_control.portfolio_scenario_control_pipeline import PortfolioScenarioControlPipeline

def test_pipeline_run():
    pipe = PortfolioScenarioControlPipeline()
    res = pipe.run_pipeline(save=False)
    assert res["overall_score"] >= 0.50
    assert res["manifest_status"] == "READY"
    assert res["health_status"] == "HEALTHY"
    assert res["validation_status"] == "VALIDATION_PASS"
    assert res["phase_157_handoff_ready"] is True
