import pytest
import pandas as pd
from local_maintenance.maintenance_config import get_default_local_maintenance_profile
from local_maintenance.maintenance_validation import build_maintenance_validation_report, validate_no_scheduler_or_auto_upgrade_claims

def test_maintenance_validation_report():
    profile = get_default_local_maintenance_profile()
    tables = {
        "domains": pd.DataFrame([{"domain_id": "1"}]),
        "tasks": pd.DataFrame([{"task_id": "1"}]),
        "commands": pd.DataFrame([{"command": "python -m scripts.run_health"}])
    }

    df, summary = build_maintenance_validation_report(tables, profile)

    assert not df.empty
    assert summary["passed_checks"] > 0
    assert "SLA" in summary["disclaimer"]

def test_validate_no_scheduler_claims():
    # If the text says "It is NOT a production scheduler", it should pass.
    res1 = validate_no_scheduler_or_auto_upgrade_claims("This is not a production scheduler.")
    assert res1["valid"]

    res2 = validate_no_scheduler_or_auto_upgrade_claims("We have enabled the production scheduler.")
    assert not res2["valid"]
