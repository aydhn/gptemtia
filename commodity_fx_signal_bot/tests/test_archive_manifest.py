import pandas as pd
from portable_packaging.archive_manifest import (
    build_archive_plan_from_bundle_manifest,
    build_archive_manifest_json,
    validate_archive_plan_safety
)
from portable_packaging.packaging_config import get_default_portable_packaging_profile

def test_archive_manifest():
    profile = get_default_portable_packaging_profile()
    df = pd.DataFrame([{"include_policy": "include", "relative_path": "app.py", "safety_label": "safe"}])

    plan, sum = build_archive_plan_from_bundle_manifest(df, profile)
    assert not plan.empty
    assert plan["archive_action"].iloc[0] == "add"

    man = build_archive_manifest_json(plan, profile)
    assert man["planned_files"] == ["app.py"]

    val = validate_archive_plan_safety(plan, profile)
    assert val["is_safe"]
