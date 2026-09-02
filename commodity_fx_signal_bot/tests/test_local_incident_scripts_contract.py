import importlib

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
