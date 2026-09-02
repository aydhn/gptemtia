import pytest
from local_dr.dr_config import get_default_local_dr_profile
from local_dr.incident_playbooks import (
    build_missing_artifact_incident_playbook,
    build_corrupted_report_incident_playbook,
    build_broken_datalake_incident_playbook,
    build_missing_dependency_incident_playbook,
    build_broken_documentation_incident_playbook,
    build_failed_quality_gate_incident_playbook,
    build_failed_cross_layer_incident_playbook,
    build_all_incident_playbooks
)

def test_incident_playbooks():
    profile = get_default_local_dr_profile()
    
    pb, data = build_missing_artifact_incident_playbook(profile)
    assert pb and data
    
    pb, data = build_corrupted_report_incident_playbook(profile)
    assert pb and data
    
    pb, data = build_broken_datalake_incident_playbook(profile)
    assert pb and data
    
    pb, data = build_missing_dependency_incident_playbook(profile)
    assert pb and data
    
    pb, data = build_broken_documentation_incident_playbook(profile)
    assert pb and data
    
    pb, data = build_failed_quality_gate_incident_playbook(profile)
    assert pb and data
    
    pb, data = build_failed_cross_layer_incident_playbook(profile)
    assert pb and data
    
    df, summary = build_all_incident_playbooks(profile)
    assert not df.empty
    assert summary["total_playbooks"] > 0
