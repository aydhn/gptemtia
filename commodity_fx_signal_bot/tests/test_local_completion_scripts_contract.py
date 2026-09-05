import importlib

def test_scripts():
    scripts = [
        "scripts.run_completion_domain_registry",
        "scripts.run_final_system_closure_dossier",
        "scripts.run_terminal_handoff_pack",
        "scripts.run_knowledge_freeze_rehearsal",
        "scripts.run_last_mile_audit_binder",
        "scripts.run_project_completion_readiness",
        "scripts.run_completion_quality_report",
        "scripts.run_completion_status"
    ]
    for s in scripts:
        mod = importlib.import_module(s)
        assert hasattr(mod, "main")
