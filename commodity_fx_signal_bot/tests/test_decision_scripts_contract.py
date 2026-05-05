import importlib


def test_scripts_importable():
    scripts = [
        "scripts.run_decision_candidate_preview",
        "scripts.run_decision_batch_build",
        "scripts.run_decision_pool_preview",
        "scripts.run_decision_status",
    ]

    for script in scripts:
        mod = importlib.import_module(script)
        assert hasattr(mod, "main")
