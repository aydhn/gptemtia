import pytest
from scenarios.scenario_config import get_default_scenario_profile
from scenarios.module_demo_flows import build_all_module_demo_flows, validate_module_demo_flow

def test_module_demo_flows():
    profile = get_default_scenario_profile()
    df, summary = build_all_module_demo_flows(profile)
    assert not df.empty
    assert summary["total_modules"] > 0

    # Check first flow
    flow = df.iloc[0].to_dict()
    val = validate_module_demo_flow(flow)
    assert val["is_valid"] is True
