#!/bin/bash
set -e

# Format with black
python3 -m pip install black
black research_planning/ scripts/run_research_*.py scripts/run_priority_*.py scripts/run_next_best_*.py scripts/run_roadmap_health_*.py tests/test_planning_*.py tests/test_signal_*.py tests/test_task_*.py tests/test_backlog_*.py tests/test_priority_*.py tests/test_next_best_*.py tests/test_research_debt*.py tests/test_research_opp*.py tests/test_roadmap_health*.py tests/test_milestone_*.py tests/test_research_planning_*.py || true

# Test specifically our new modules
pytest tests/test_planning_config.py tests/test_planning_labels.py tests/test_planning_models.py tests/test_signal_sources.py tests/test_task_registry.py tests/test_backlog_builder.py tests/test_priority_scoring.py tests/test_next_best_experiment.py tests/test_research_debt.py tests/test_research_opportunities.py tests/test_roadmap_health.py tests/test_task_dependencies.py tests/test_milestone_tracking.py tests/test_task_orchestration_plan.py tests/test_planning_quality.py tests/test_planning_report_builder.py tests/test_planning_pipeline.py tests/test_research_planning_scripts_contract.py

echo "Phase 48 complete."
