import pytest
import pandas as pd
from local_maintenance.maintenance_config import get_default_local_maintenance_profile
from local_maintenance.maintenance_quality import build_maintenance_quality_report, check_for_forbidden_terms_in_maintenance

def test_maintenance_quality_report():
    profile = get_default_local_maintenance_profile()
    domain_df = pd.DataFrame([{"domain_id": "1"}])
    task_df = pd.DataFrame([{"task_id": "1"}])

    summary = {"total_tasks": 1, "disclaimer": "This is NOT an official maintenance contract."}

    quality = build_maintenance_quality_report(summary, domain_df, task_df, None, profile)

    assert "passed" in quality
    print(quality)
    assert quality["passed"]  # Should pass since fake df is valid and no forbidden terms

def test_check_for_forbidden_terms():
    # Should catch forbidden term
    res1 = check_for_forbidden_terms_in_maintenance("We will automatically deleted files.")
    assert not res1["passed"]

    # Should ignore if negated (simple negation logic)
    res2 = check_for_forbidden_terms_in_maintenance("This will not automatically deleted files.")
    assert res2["passed"]

    res3 = check_for_forbidden_terms_in_maintenance("yatırım tavsiyesidir")
    assert not res3["passed"]

    res4 = check_for_forbidden_terms_in_maintenance("yatırım tavsiyesi değildir")
    assert res4["passed"]
