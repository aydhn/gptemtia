import pytest
import importlib
import sys
from pathlib import Path

# Ensures scripts can be imported without executing
def test_scenario_scripts_importable():
    scripts_dir = Path(__file__).parent.parent / "scripts"
    sys.path.insert(0, str(scripts_dir.parent))

    import scripts.run_scenario_registry_report
    import scripts.run_sample_data_builder
    import scripts.run_scenario_dry_run
    import scripts.run_case_study_report
    import scripts.run_demo_workflow_report
    import scripts.run_end_to_end_demo_report
    import scripts.run_scenario_status

    # Just asserting they don't crash on import
    assert True
