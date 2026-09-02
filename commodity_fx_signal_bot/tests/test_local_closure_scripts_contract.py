
import importlib

def test_scripts():
    scripts = [
        "scripts.run_closure_domain_registry",
        "scripts.run_final_meta_review",
        "scripts.run_lessons_learned_compendium",
        "scripts.run_future_roadmap_backlog",
        "scripts.run_v1_local_closure_dossier",
        "scripts.run_closure_quality_report",
        "scripts.run_closure_status"
    ]
    for s in scripts:
        mod = importlib.import_module(s)
        assert hasattr(mod, "main")
