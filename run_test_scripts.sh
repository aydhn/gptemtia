#!/usr/bin/env bash
cd commodity_fx_signal_bot
python -m scripts.run_longterm_domain_registry
python -m scripts.run_final_longterm_operations_binder
python -m scripts.run_yearly_review_calendar
python -m scripts.run_lifecycle_maintenance_workbook
python -m scripts.run_deprecation_rehearsal
python -m scripts.run_v1x_roadmap_governance
python -m scripts.run_lifecycle_quality_report
python -m scripts.run_lifecycle_status
