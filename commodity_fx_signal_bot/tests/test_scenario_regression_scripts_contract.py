import pytest
import sys
from pathlib import Path

def test_scripts_importable():
    import scripts.run_scenario_regression_registry
    import scripts.run_golden_output_report
    import scripts.run_snapshot_comparison_report
    import scripts.run_deterministic_replay_report
    import scripts.run_demo_acceptance_report
    import scripts.run_scenario_regression_status
    assert True
