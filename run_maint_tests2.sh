cd commodity_fx_signal_bot
source ../venv/bin/activate 2>/dev/null || source .venv/bin/activate 2>/dev/null || true
python -m pytest tests/test_maintenance_checklist.py tests/test_maintenance_report_builder.py tests/test_maintenance_scripts_contract.py -v
