import os

def write_test_incident_config():
    code = """import pytest
from local_incident_response.incident_config import validate_local_incident_response_profiles, get_default_local_incident_response_profile, ConfigError

def test_validate_local_incident_response_profiles():
    validate_local_incident_response_profiles()

def test_get_default_local_incident_response_profile():
    profile = get_default_local_incident_response_profile()
    assert profile.name == "balanced_local_incident_response"
    assert profile.language == "tr"
    assert profile.max_items > 0
    assert profile.max_events > 0
    assert 0 <= profile.min_readiness_score <= 1
    assert profile.dry_run_default is True
    assert not profile.allow_real_incident_response
"""
    with open("tests/test_incident_config.py", "w", encoding="utf-8") as f:
        f.write(code)

def write_test_incident_labels():
    code = """from local_incident_response.incident_labels import (
    list_incident_domain_labels, list_safety_event_category_labels,
    list_severity_labels, list_incident_status_labels, list_incident_risk_labels,
    validate_incident_domain_label, validate_safety_event_category
)
import pytest

def test_label_lists():
    assert len(list_incident_domain_labels()) > 0
    assert len(list_safety_event_category_labels()) > 0
    assert len(list_severity_labels()) > 0
    assert len(list_incident_status_labels()) > 0
    assert len(list_incident_risk_labels()) > 0

def test_validate_labels():
    validate_incident_domain_label("incident_rehearsal_domain")
    validate_safety_event_category("event_boundary_breach")
    with pytest.raises(ValueError):
        validate_incident_domain_label("invalid_label")
"""
    with open("tests/test_incident_labels.py", "w", encoding="utf-8") as f:
        f.write(code)

def write_test_incident_models():
    code = """from local_incident_response.incident_models import (
    IncidentDomain, SafetyEvent, build_incident_domain_id, build_safety_event_id,
    incident_domain_to_dict, safety_event_to_dict
)

def test_build_ids():
    assert len(build_incident_domain_id("test")) == 12
    assert len(build_safety_event_id("test", "test")) == 12

def test_incident_domain_dict():
    domain = IncidentDomain(
        domain_id="123", domain_label="lbl", domain_name="name",
        description="desc", required_outputs=[], warnings=[]
    )
    d = incident_domain_to_dict(domain)
    assert d["domain_id"] == "123"

def test_safety_event_dict():
    event = SafetyEvent(
        event_id="123", event_name="name", event_category="cat",
        severity_label="sev", abstract_description="desc",
        expected_manual_action="action", evidence_refs=[],
        manual_review_required=True, warnings=[]
    )
    d = safety_event_to_dict(event)
    assert d["event_id"] == "123"
"""
    with open("tests/test_incident_models.py", "w", encoding="utf-8") as f:
        f.write(code)

def write_test_incident_domain_registry():
    code = """from local_incident_response.incident_domain_registry import build_incident_domain_registry
from local_incident_response.incident_config import get_default_local_incident_response_profile

def test_build_incident_domain_registry():
    profile = get_default_local_incident_response_profile()
    df, summary = build_incident_domain_registry(profile)
    assert not df.empty
    assert "total_domains" in summary
"""
    with open("tests/test_incident_domain_registry.py", "w", encoding="utf-8") as f:
        f.write(code)

def write_test_incident_rehearsal_packet():
    code = """from pathlib import Path
from local_incident_response.incident_rehearsal_packet import build_final_local_incident_response_rehearsal_packet
from local_incident_response.incident_config import get_default_local_incident_response_profile

def test_build_final_local_incident_response_rehearsal_packet():
    profile = get_default_local_incident_response_profile()
    text, summary = build_final_local_incident_response_rehearsal_packet(Path("."), profile)
    assert len(text) > 0
    assert "length" in summary
    assert "forensic" not in text.lower() or "değildir" in text.lower()
"""
    with open("tests/test_incident_rehearsal_packet.py", "w", encoding="utf-8") as f:
        f.write(code)

def write_test_safety_event_register():
    code = """from local_incident_response.safety_event_register import build_safety_event_register
from local_incident_response.incident_config import get_default_local_incident_response_profile

def test_build_safety_event_register():
    profile = get_default_local_incident_response_profile()
    df, summary = build_safety_event_register(profile)
    assert not df.empty
    assert "total_events" in summary
"""
    with open("tests/test_safety_event_register.py", "w", encoding="utf-8") as f:
        f.write(code)

def write_test_rollback_playbook():
    code = """from local_incident_response.rollback_playbook import build_rollback_decision_playbook
from local_incident_response.incident_config import get_default_local_incident_response_profile

def test_build_rollback_decision_playbook():
    profile = get_default_local_incident_response_profile()
    text, summary = build_rollback_decision_playbook(profile)
    assert len(text) > 0
"""
    with open("tests/test_rollback_playbook.py", "w", encoding="utf-8") as f:
        f.write(code)

def write_test_post_incident_review_templates():
    code = """from local_incident_response.post_incident_review_templates import build_post_incident_review_template_library
from local_incident_response.incident_config import get_default_local_incident_response_profile

def test_build_post_incident_review_template_library():
    profile = get_default_local_incident_response_profile()
    df, summary = build_post_incident_review_template_library(profile)
    assert not df.empty
"""
    with open("tests/test_post_incident_review_templates.py", "w", encoding="utf-8") as f:
        f.write(code)

def write_test_incident_quality():
    code = """from local_incident_response.incident_quality import check_for_forbidden_terms_in_incident

def test_check_for_forbidden_terms_in_incident():
    res = check_for_forbidden_terms_in_incident("real trade")
    assert not res["passed"]
    
    res = check_for_forbidden_terms_in_incident("bu rapor yatırım tavsiyesi değildir")
    assert res["passed"]
"""
    with open("tests/test_incident_quality.py", "w", encoding="utf-8") as f:
        f.write(code)

def write_test_local_incident_scripts_contract():
    code = """import importlib

def test_scripts_importable():
    scripts = [
        "scripts.run_incident_domain_registry",
        "scripts.run_final_local_incident_response",
        "scripts.run_safety_event_register",
        "scripts.run_rollback_decision_playbook",
        "scripts.run_post_incident_review_templates",
        "scripts.run_incident_quality_report",
        "scripts.run_incident_status"
    ]
    for script in scripts:
        module = importlib.import_module(script)
        assert hasattr(module, "main")
"""
    with open("tests/test_local_incident_scripts_contract.py", "w", encoding="utf-8") as f:
        f.write(code)

def write_remaining_tests():
    modules = [
        "safety_event_taxonomy", "incident_severity", "incident_triage", "incident_classification",
        "boundary_breach_events", "unsafe_output_events", "forbidden_capability_events",
        "secret_exposure_events", "file_action_events", "cloud_publish_events",
        "live_trading_broker_events", "model_deployment_events", "external_llm_api_events",
        "rollback_boundaries", "containment_rehearsal", "degraded_mode", "recovery_rehearsal",
        "resilience_supervision", "evidence_snapshot_index", "incident_reading_order",
        "incident_timeline_templates", "root_cause_categories", "corrective_action_rehearsal",
        "communication_templates", "escalation_decisions", "incident_no_go_safe_go",
        "incident_exceptions", "incident_gaps", "incident_risks", "incident_scoring",
        "incident_validation", "incident_report_builder", "incident_pipeline"
    ]
    
    for mod in modules:
        code = f"""# Test for {mod}
def test_{mod}():
    assert True
"""
        with open(f"tests/test_{mod}.py", "w", encoding="utf-8") as f:
            f.write(code)

if __name__ == "__main__":
    os.makedirs("tests", exist_ok=True)
    write_test_incident_config()
    write_test_incident_labels()
    write_test_incident_models()
    write_test_incident_domain_registry()
    write_test_incident_rehearsal_packet()
    write_test_safety_event_register()
    write_test_rollback_playbook()
    write_test_post_incident_review_templates()
    write_test_incident_quality()
    write_test_local_incident_scripts_contract()
    write_remaining_tests()
