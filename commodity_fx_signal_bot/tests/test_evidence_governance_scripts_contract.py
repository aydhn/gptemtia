import pytest
import importlib
import sys
import os

def test_scripts_importable():
    scripts = [
        "scripts.run_evidence_artifact_inventory",
        "scripts.run_policy_control_mapping",
        "scripts.run_audit_evidence_binder",
        "scripts.run_evidence_traceability_matrix",
        "scripts.run_governance_evidence_export",
        "scripts.run_evidence_quality_report",
        "scripts.run_evidence_status"
    ]

    sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

    for script in scripts:
        mod = importlib.import_module(script)
        assert hasattr(mod, "main")
