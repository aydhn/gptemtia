
import pytest
import sys
from importlib import import_module

def test_local_hardening_scripts_contract():
    scripts = [
        "commodity_fx_signal_bot.scripts.run_hardening_domain_registry",
        "commodity_fx_signal_bot.scripts.run_dead_code_review",
        "commodity_fx_signal_bot.scripts.run_contract_freeze_catalog",
        "commodity_fx_signal_bot.scripts.run_documentation_freeze",
        "commodity_fx_signal_bot.scripts.run_rc_dry_run_freeze",
        "commodity_fx_signal_bot.scripts.run_freeze_quality_report",
        "commodity_fx_signal_bot.scripts.run_freeze_status"
    ]
    for s in scripts:
        mod = import_module(s)
        assert hasattr(mod, "parse_args")
        assert hasattr(mod, "main")
