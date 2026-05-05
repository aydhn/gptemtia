import pytest
import importlib


def test_preview_script_importable():
    script = importlib.import_module("scripts.run_asset_profile_preview")
    assert hasattr(script, "main")


def test_group_event_script_importable():
    script = importlib.import_module("scripts.run_asset_group_event_preview")
    assert hasattr(script, "main")


def test_batch_script_importable():
    script = importlib.import_module("scripts.run_asset_profile_batch_build")
    assert hasattr(script, "main")


def test_status_script_importable():
    script = importlib.import_module("scripts.run_asset_profile_status")
    assert hasattr(script, "main")
