import importlib

def test_script_imports():
    scripts = [
        "scripts.run_ml_context_integration_preview",
        "scripts.run_model_alignment_preview",
        "scripts.run_ml_conflict_filter_preview",
        "scripts.run_ml_integration_batch",
        "scripts.run_ml_integration_status",
    ]
    for s in scripts:
        mod = importlib.import_module(s)
        assert hasattr(mod, "main")
