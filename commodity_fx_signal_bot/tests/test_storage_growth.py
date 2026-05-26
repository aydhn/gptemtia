import pandas as pd
from maintenance.storage_growth import build_storage_snapshot, calculate_storage_growth

def test_storage_growth():
    inv_data = [
        {"size_bytes": 100, "retention_category": "report_retention"},
        {"size_bytes": 200, "retention_category": "cache_retention"},
    ]
    inv_df = pd.DataFrame(inv_data)

    snap = build_storage_snapshot(inv_df)
    assert snap["total_size_bytes"] == 300
    assert snap["report_size_bytes"] == 100

    snap_df = pd.DataFrame([snap, {"total_size_bytes": 500}])
    growth = calculate_storage_growth(snap_df)
    assert growth.iloc[1]["growth_bytes"] == 200
