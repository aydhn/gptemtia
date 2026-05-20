.PHONY: setup test test-fast lint typecheck health security workflow-status dx dry-run-daily dry-run-full

setup:
	python -m pip install -r requirements.txt
	python -m pip install -r requirements-dev.txt

test:
	python -m pytest

test-fast:
	python -m pytest -q

lint:
	python -m ruff check .

typecheck:
	python -m mypy .

health:
	python -m scripts.run_system_healthcheck

security:
	python -m scripts.run_security_audit

workflow-status:
	python -m scripts.run_workflow_status

dx:
	python -m scripts.run_local_dev_check

dry-run-daily:
	python -m scripts.run_daily_research_workflow --timeframe 1d

dry-run-full:
	python -m scripts.run_full_research_workflow --timeframe 1d
