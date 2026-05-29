#!/bin/bash
set -e
source venv/bin/activate 2>/dev/null || true
python -m scripts.run_scenario_registry_report
python -m scripts.run_sample_data_builder
python -m scripts.run_scenario_dry_run
python -m scripts.run_case_study_report
python -m scripts.run_demo_workflow_report
python -m scripts.run_end_to_end_demo_report
python -m scripts.run_scenario_status
