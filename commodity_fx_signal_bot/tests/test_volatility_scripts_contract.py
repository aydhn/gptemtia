import importlib


def test_run_volatility_feature_preview_contract():
    mod = importlib.import_module("scripts.run_volatility_feature_preview")
    assert hasattr(mod, "main")
    if hasattr(mod, "parse_args"):
        assert hasattr(mod, "parse_args")


def test_run_volatility_batch_build_contract():
    mod = importlib.import_module("scripts.run_volatility_batch_build")
    assert hasattr(mod, "main")
    if hasattr(mod, "parse_args"):
        assert hasattr(mod, "parse_args")


def test_run_volatility_event_preview_contract():
    mod = importlib.import_module("scripts.run_volatility_event_preview")
    assert hasattr(mod, "main")
    if hasattr(mod, "parse_args"):
        assert hasattr(mod, "parse_args")


def test_run_volatility_status_contract():
    mod = importlib.import_module("scripts.run_volatility_status")
    assert hasattr(mod, "main")
    if hasattr(mod, "parse_args"):
        assert hasattr(mod, "parse_args")
