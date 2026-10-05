
import pytest
import sys
from importlib import import_module

def test_local_hardening_scripts_contract():
    scripts = [
        "scripts.run_hardening_domain_registry",
        "scripts.run_dead_code_review",
        "scripts.run_contract_freeze_catalog",
        "scripts.run_documentation_freeze",
        "scripts.run_rc_dry_run_freeze",
        "scripts.run_freeze_quality_report",
        "scripts.run_freeze_status"
    ]
    for s in scripts:
        mod = import_module(s)
        assert hasattr(mod, "parse_args")
        assert hasattr(mod, "main")
