import pandas as pd
from maintenance.maintenance_checklist import build_maintenance_checklist, evaluate_maintenance_checklist
from maintenance.maintenance_config import get_default_maintenance_profile

def test_maintenance_checklist():
    profile = get_default_maintenance_profile()
    cl = build_maintenance_checklist(profile)
    assert len(cl) > 0

    eval_cl = evaluate_maintenance_checklist(cl, {"total_files": 10}, {}, {})
    assert "passed" in eval_cl.columns
    # inv_01 should pass because total_files > 0
    assert eval_cl[eval_cl["item_id"] == "inv_01"].iloc[0]["passed"] == True
