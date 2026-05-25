import pytest
import importlib

def test_command_catalog_script_contract():
    script = importlib.import_module("scripts.run_command_catalog_report")
    assert hasattr(script, "main")

def test_guided_workflow_script_contract():
    script = importlib.import_module("scripts.run_guided_workflow_report")
    assert hasattr(script, "main")

def test_safe_runbook_script_contract():
    script = importlib.import_module("scripts.run_safe_runbook_report")
    assert hasattr(script, "main")

def test_project_status_script_contract():
    script = importlib.import_module("scripts.run_project_status_report")
    assert hasattr(script, "main")

def test_project_consolidation_script_contract():
    script = importlib.import_module("scripts.run_project_consolidation_report")
    assert hasattr(script, "main")

def test_analyst_command_query_script_contract():
    script = importlib.import_module("scripts.run_analyst_command_query")
    assert hasattr(script, "main")

def test_command_center_status_script_contract():
    script = importlib.import_module("scripts.run_command_center_status")
    assert hasattr(script, "main")
