from maintenance.retention_policies import build_default_retention_policies, retention_policies_to_dataframe, apply_retention_policy_to_inventory
from maintenance.maintenance_config import get_default_maintenance_profile
import pandas as pd

def test_default_policies():
    profile = get_default_maintenance_profile()
    policies = build_default_retention_policies(profile)
    assert len(policies) > 0

    raw_policy = next((p for p in policies if p.retention_category == "raw_data_retention"), None)
    assert raw_policy is not None
    assert raw_policy.protected is True

    df = retention_policies_to_dataframe(policies)
    assert "retention_category" in df.columns

def test_apply_retention_policy():
    profile = get_default_maintenance_profile()
    policies = build_default_retention_policies(profile)
    policies_df = retention_policies_to_dataframe(policies)

    inv_data = [{
        "artifact_id": "1", "path": "a", "retention_category": "raw_data_retention",
        "protected": False, "age_days": 1000
    }]
    inv_df = pd.DataFrame(inv_data)

    result = apply_retention_policy_to_inventory(inv_df, policies_df, profile)
    assert result.iloc[0]["lifecycle_label"] == "protected_artifact"
