import importlib

import pytest


def test_run_price_action_feature_preview_importable():
    module = importlib.import_module("scripts.run_price_action_feature_preview")
    assert hasattr(module, "main")


def test_run_price_action_event_preview_importable():
    module = importlib.import_module("scripts.run_price_action_event_preview")
    assert hasattr(module, "main")


def test_run_price_action_batch_build_importable():
    module = importlib.import_module("scripts.run_price_action_batch_build")
    assert hasattr(module, "main")


def test_run_price_action_status_importable():
    module = importlib.import_module("scripts.run_price_action_status")
    assert hasattr(module, "main")
