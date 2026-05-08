import pytest
import importlib

def test_scripts_importable():
    importlib.import_module("scripts.run_ml_training_preview")
    importlib.import_module("scripts.run_ml_model_evaluation_preview")
    importlib.import_module("scripts.run_ml_training_batch")
    importlib.import_module("scripts.run_ml_model_registry_status")
    importlib.import_module("scripts.run_ml_model_artifact_status")
