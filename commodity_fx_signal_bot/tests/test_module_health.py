import pytest
import pandas as pd
from command_center.module_health import (
    calculate_module_health_score,
    infer_module_health_label,
    build_module_health_table,
    summarize_module_health
)

def test_module_health_score():
    row1 = pd.Series({"data_lake_available": True, "reports_available": True, "script_count": 5, "test_count": 10})
    score1 = calculate_module_health_score(row1)
    assert score1 == 1.0

    row2 = pd.Series({"data_lake_available": False, "reports_available": False, "script_count": 0, "test_count": 0})
    score2 = calculate_module_health_score(row2)
    assert score2 == 0.0

def test_infer_module_health_label():
    assert infer_module_health_label(1.0) == "healthy_offline_module"
    assert infer_module_health_label(0.5) == "incomplete_module"
    assert infer_module_health_label(0.1) == "missing_outputs"
    assert infer_module_health_label(0.0) == "unknown_health"
    assert infer_module_health_label(1.0, ["warning!"]) == "usable_with_warnings"

def test_module_health_table():
    status_df = pd.DataFrame([
        {"module_name": "mod_a", "data_lake_available": True, "reports_available": True, "script_count": 5, "test_count": 10, "warnings": []}
    ])
    health_df = build_module_health_table(status_df)
    assert not health_df.empty
    assert health_df.iloc[0]["health_score"] == 1.0

    summary = summarize_module_health(health_df)
    assert summary["healthy_modules"] == 1
