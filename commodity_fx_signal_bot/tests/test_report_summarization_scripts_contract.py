import pytest
import importlib
import sys

def test_scripts_contract():
    scripts = [
        "scripts.run_report_summary_registry",
        "scripts.run_executive_summary_report",
        "scripts.run_analyst_brief_report",
        "scripts.run_weekly_offline_review_pack",
        "scripts.run_research_digest_report",
        "scripts.run_summary_quality_report",
        "scripts.run_briefing_status",
    ]

    for s in scripts:
        mod = importlib.import_module(s)
        assert hasattr(mod, "main")
        assert hasattr(mod, "parse_args")
