import pandas as pd
from local_dr.dr_config import get_default_local_dr_profile
from local_dr.tabletop_scenarios import build_dr_tabletop_scenario_registry, build_tabletop_scenarios_for_domain, classify_tabletop_scenario_status, summarize_tabletop_scenarios

def test_tabletop_scenarios():
    profile = get_default_local_dr_profile()
    domain_df = pd.DataFrame([{"domain_label": "archive_restore_dr"}])
    
    scenarios = build_tabletop_scenarios_for_domain("archive_restore_dr", profile)
    assert len(scenarios) == 1
    
    df, summary = build_dr_tabletop_scenario_registry(domain_df, profile)
    assert isinstance(df, pd.DataFrame)
    assert len(df) == 1
    assert summary["total_scenarios"] == 1
    assert summary["tested_scenarios"] == 0
    
    assert classify_tabletop_scenario_status(pd.Series({"status": "tested"}), profile) == "tested"
