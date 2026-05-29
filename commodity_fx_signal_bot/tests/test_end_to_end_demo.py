import pytest
from scenarios.scenario_config import get_default_scenario_profile
from scenarios.end_to_end_demo import (
    build_end_to_end_offline_demo_plan, build_end_to_end_demo_expected_outputs,
    build_end_to_end_demo_report, summarize_end_to_end_demo
)

def test_end_to_end_demo():
    profile = get_default_scenario_profile()
    plan_df = build_end_to_end_offline_demo_plan(profile)
    exp_df = build_end_to_end_demo_expected_outputs(profile)

    assert not plan_df.empty
    assert not exp_df.empty

    summary = summarize_end_to_end_demo(plan_df)
    assert summary["total_steps"] == len(plan_df)

    json_str, report_dict = build_end_to_end_demo_report(plan_df, exp_df)
    assert "plan_steps" in report_dict
    assert len(report_dict["plan_steps"]) == len(plan_df)
