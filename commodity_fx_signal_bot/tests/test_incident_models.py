from local_incident_response.incident_models import (
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
