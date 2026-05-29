import pytest
import pandas as pd
from scenarios.scenario_config import get_default_scenario_profile
from scenarios.scenario_quality import (
    check_for_forbidden_terms_in_scenarios, build_scenario_quality_report
)

def test_forbidden_terms_check():
    res1 = check_for_forbidden_terms_in_scenarios(text="This is a safe offline test")
    assert res1["passed"] is True

    res2 = check_for_forbidden_terms_in_scenarios(text="Executing a LIVE ORDER now")
    assert res2["passed"] is False
    assert "live order" in res2["forbidden_terms_found"]

def test_false_positive_disclaimer():
    res = check_for_forbidden_terms_in_scenarios(text="Bu rapor yatırım tavsiyesi değildir.")
    assert res["passed"] is True

def test_scenario_quality_report():
    summary = {"info": "safe stuff"}
    df = pd.DataFrame({"command": ["python -m safe_script"], "is_safe": [True]})
    report = build_scenario_quality_report(summary, command_df=df)
    # Registry and fixture checks might fail because we passed None/empty,
    # but the terms check should pass.
    assert "forbidden_terms_found" in report
    assert len(report["forbidden_terms_found"]) == 0
