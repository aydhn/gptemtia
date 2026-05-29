import pytest
from scenarios.scenario_report_builder import (
    build_scenario_registry_markdown_report, build_scenario_disclaimer
)

def test_report_builder_disclaimer():
    disc = build_scenario_disclaimer()
    assert "offline" in disc.lower()
    assert "yatırım tavsiyesi değildir" in disc.lower()

def test_markdown_report():
    md = build_scenario_registry_markdown_report({"total_scenarios": 1})
    assert "Scenario Registry Report" in md
    assert "offline" in md.lower()
