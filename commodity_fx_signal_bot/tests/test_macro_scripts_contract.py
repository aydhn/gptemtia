import importlib


def test_script_imports():
    scripts = [
        "scripts.run_macro_data_update",
        "scripts.run_macro_feature_preview",
        "scripts.run_macro_benchmark_preview",
        "scripts.run_macro_batch_build",
        "scripts.run_macro_status",
    ]
    for s in scripts:
        mod = importlib.import_module(s)
        assert hasattr(mod, "main")
