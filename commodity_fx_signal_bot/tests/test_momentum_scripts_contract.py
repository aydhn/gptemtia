import pytest
import importlib


def test_run_momentum_feature_preview_contract():
    mod = importlib.import_module("scripts.run_momentum_feature_preview")
    assert hasattr(mod, "main")
    assert hasattr(mod, "parse_args")


def test_run_momentum_batch_build_contract():
    mod = importlib.import_module("scripts.run_momentum_batch_build")
    assert hasattr(mod, "main")
    assert hasattr(mod, "parse_args")


def test_run_momentum_event_preview_contract():
    mod = importlib.import_module("scripts.run_momentum_event_preview")
    assert hasattr(mod, "main")
    assert hasattr(mod, "parse_args")


def test_run_momentum_status_contract():
    mod = importlib.import_module("scripts.run_momentum_status")
    assert hasattr(mod, "main")
