import pandas as pd
from maintenance.maintenance_quality import check_storage_inventory_quality, check_for_forbidden_terms_in_maintenance
from maintenance.maintenance_config import get_default_maintenance_profile

def test_maintenance_quality():
    profile = get_default_maintenance_profile()

    assert check_storage_inventory_quality(None, profile)["valid"] is False

    inv_df = pd.DataFrame([{"artifact_id": "1", "lifecycle_label": "active"}])
    assert check_storage_inventory_quality(inv_df, profile)["valid"] is True

    res = check_for_forbidden_terms_in_maintenance("This will do a live order")
    assert res["found"] is True
    assert "live order" in res["terms"]

    res2 = check_for_forbidden_terms_in_maintenance("This is a cleanup candidate")
    assert res2["found"] is False
