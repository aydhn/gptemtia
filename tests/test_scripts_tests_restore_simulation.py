import pytest
from pathlib import Path
from local_dr.dr_config import get_default_local_dr_profile
from local_dr.scripts_tests_restore_simulation import (
    build_scripts_tests_restore_simulation_report,
    simulate_scripts_restore_requirements,
    simulate_tests_restore_requirements,
    detect_scripts_tests_restore_gaps,
    summarize_scripts_tests_restore_simulation
)

def test_scripts_tests_restore_simulation():
    profile = get_default_local_dr_profile()
    project_root = Path(".")
    
    df_scripts = simulate_scripts_restore_requirements(project_root, profile)
    assert not df_scripts.empty
    
    df_tests = simulate_tests_restore_requirements(project_root, profile)
    assert not df_tests.empty
    
    gaps = detect_scripts_tests_restore_gaps(df_scripts)
    assert gaps.empty
    
    summary = summarize_scripts_tests_restore_simulation(df_scripts)
    assert summary["total"] > 0
    assert summary["gaps"] == 0
    
    df_report, report_summary = build_scripts_tests_restore_simulation_report(project_root, profile)
    assert not df_report.empty
    assert report_summary["total"] > 0
