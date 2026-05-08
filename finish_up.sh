#!/bin/bash
cd commodity_fx_signal_bot

PYTHONPATH=. pytest tests/test_dataset_*.py tests/test_target_engineering.py tests/test_feature_matrix_builder.py tests/test_leakage_checks.py tests/test_splitters.py tests/test_ml_dataset_scripts_contract.py > out_pytest.txt 2>&1
cat out_pytest.txt | grep -E "failed|passed"
rm out_pytest.txt
