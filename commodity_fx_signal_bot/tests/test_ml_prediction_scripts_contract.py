import pytest
import sys
import importlib

def test_run_ml_prediction_preview_import():
    import commodity_fx_signal_bot.scripts.run_ml_prediction_preview as script
    assert hasattr(script, "main")

def test_run_ml_prediction_batch_import():
    import commodity_fx_signal_bot.scripts.run_ml_prediction_batch as script
    assert hasattr(script, "main")

def test_run_ml_ensemble_preview_import():
    import commodity_fx_signal_bot.scripts.run_ml_ensemble_preview as script
    assert hasattr(script, "main")

def test_run_ml_prediction_context_build_import():
    import commodity_fx_signal_bot.scripts.run_ml_prediction_context_build as script
    assert hasattr(script, "main")

def test_run_ml_prediction_status_import():
    import commodity_fx_signal_bot.scripts.run_ml_prediction_status as script
    assert hasattr(script, "main")
