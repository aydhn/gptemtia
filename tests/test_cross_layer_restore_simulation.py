import pytest
from pathlib import Path
from local_dr.dr_config import get_default_local_dr_profile
from local_dr.cross_layer_restore_simulation import (
    build_cross_layer_restore_simulation_report,
    simulate_cross_layer_restore_requirements,
    detect_cross_layer_restore_gaps,
    summarize_cross_layer_restore_simulation
)

def test_cross_layer_restore_simulation():
    profile = get_default_local_dr_profile()
    project_root = Path(".")
    
    df = simulate_cross_layer_restore_requirements(project_root, profile)
    assert not df.empty
    
    gaps = detect_cross_layer_restore_gaps(df)
    assert gaps.empty
    
    summary = summarize_cross_layer_restore_simulation(df)
    assert summary["total"] > 0
    assert summary["gaps"] == 0
    
    df_report, report_summary = build_cross_layer_restore_simulation_report(project_root, profile)
    assert not df_report.empty
    assert report_summary["total"] > 0
