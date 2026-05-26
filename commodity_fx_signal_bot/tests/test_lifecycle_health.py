import pandas as pd
from maintenance.lifecycle_health import calculate_storage_pressure_score, infer_storage_health_label
from maintenance.maintenance_config import get_default_maintenance_profile

def test_lifecycle_health():
    profile = get_default_maintenance_profile()

    inv_data = [
        {"size_bytes": 100, "lifecycle_label": "active"},
    ]
    inv_df = pd.DataFrame(inv_data)

    score = calculate_storage_pressure_score(inv_df, profile)
    assert score == 0.0

    assert infer_storage_health_label(0.1) == "healthy_storage"
    assert infer_storage_health_label(0.95) == "critical_storage_pressure"
