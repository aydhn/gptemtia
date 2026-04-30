import pytest
import importlib
import sys


def test_run_mean_reversion_event_preview_contract():
    mod = importlib.import_module("scripts.run_mean_reversion_event_preview")
    assert hasattr(mod, "main")
    assert hasattr(mod, "parse_args")


def test_run_mean_reversion_status_contract():
    mod = importlib.import_module("scripts.run_mean_reversion_status")
    assert hasattr(mod, "main")
    assert hasattr(mod, "parse_args")
