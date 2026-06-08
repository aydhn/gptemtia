
import pytest
import importlib

def test_sensitive_file_scan_script_imports():
    mod = importlib.import_module("scripts.run_sensitive_file_scan")
    assert hasattr(mod, "main")

def test_env_template_audit_script_imports():
    mod = importlib.import_module("scripts.run_env_template_audit")
    assert hasattr(mod, "main")

def test_credential_boundary_report_script_imports():
    mod = importlib.import_module("scripts.run_credential_boundary_report")
    assert hasattr(mod, "main")

def test_private_data_protection_script_imports():
    mod = importlib.import_module("scripts.run_private_data_protection_report")
    assert hasattr(mod, "main")

def test_secret_remediation_report_script_imports():
    mod = importlib.import_module("scripts.run_secret_remediation_report")
    assert hasattr(mod, "main")

def test_secrets_quality_report_script_imports():
    mod = importlib.import_module("scripts.run_secrets_quality_report")
    assert hasattr(mod, "main")

def test_secrets_hygiene_status_script_imports():
    mod = importlib.import_module("scripts.run_secrets_hygiene_status")
    assert hasattr(mod, "main")
