import pytest
import importlib
import sys
import os

sys.path.append(os.getcwd())

def test_scripts_importable():
    # If there's a syntax error, this will fail
    importlib.import_module("scripts.run_symbol_research_report")
    importlib.import_module("scripts.run_universe_research_report")
    importlib.import_module("scripts.run_daily_research_digest_report")
    importlib.import_module("scripts.run_research_ranking_report")
    importlib.import_module("scripts.run_research_report_status")

def test_scripts_main_guard():
    # We just want to ensure we don't accidentally execute main on import
    # The import test above already covers this implicitly since it didn't exit,
    # but we explicitly assert here for documentation
    mod1 = importlib.import_module("scripts.run_symbol_research_report")
    assert hasattr(mod1, "main")
    mod2 = importlib.import_module("scripts.run_universe_research_report")
    assert hasattr(mod2, "main")
