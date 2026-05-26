import importlib
import pytest
import sys
from pathlib import Path

# Add project root to sys path so scripts can be imported
sys.path.append(str(Path(__file__).resolve().parent.parent))

def test_run_documentation_pack_report_import():
    importlib.import_module("scripts.run_documentation_pack_report")

def test_run_documentation_quality_report_import():
    importlib.import_module("scripts.run_documentation_quality_report")

def test_run_safe_usage_docs_report_import():
    importlib.import_module("scripts.run_safe_usage_docs_report")

def test_run_script_reference_report_import():
    importlib.import_module("scripts.run_script_reference_report")

def test_run_output_reference_report_import():
    importlib.import_module("scripts.run_output_reference_report")

def test_run_documentation_status_import():
    importlib.import_module("scripts.run_documentation_status")
