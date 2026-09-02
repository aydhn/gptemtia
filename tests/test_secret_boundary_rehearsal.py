import pytest
from pathlib import Path
from local_dr.dr_config import get_default_local_dr_profile
from local_dr.secret_boundary_rehearsal import (
    build_secret_boundary_incident_rehearsal,
    simulate_secret_in_archive_incident,
    simulate_secret_in_report_incident,
    build_secret_boundary_manual_response_steps,
    summarize_secret_boundary_rehearsal
)

def test_secret_boundary_rehearsal():
    profile = get_default_local_dr_profile()
    project_root = Path(".")
    
    df1 = simulate_secret_in_archive_incident(project_root, profile)
    assert not df1.empty
    
    df2 = simulate_secret_in_report_incident(project_root, profile)
    assert not df2.empty
    
    df_steps = build_secret_boundary_manual_response_steps(profile)
    assert not df_steps.empty
    
    summary = summarize_secret_boundary_rehearsal(df1)
    assert summary["total_incidents"] > 0
    
    df_report, report_summary = build_secret_boundary_incident_rehearsal(project_root, profile)
    assert not df_report.empty
    assert report_summary["total_incidents"] > 0
