from portable_packaging.packaging_quality import (
    check_environment_snapshot_quality,
    check_dependency_inventory_quality,
    check_install_verification_quality,
    check_bundle_manifest_quality,
    check_packaging_safety_quality,
    build_packaging_quality_report
)
import pandas as pd
from portable_packaging.packaging_config import get_default_portable_packaging_profile

def test_packaging_quality():
    profile = get_default_portable_packaging_profile()

    assert not check_environment_snapshot_quality(None, None)["valid"]
    assert check_dependency_inventory_quality(pd.DataFrame([{"a": 1}]))["valid"]
    assert check_install_verification_quality(pd.DataFrame([{"a": 1}]))["valid"]
    assert check_bundle_manifest_quality(pd.DataFrame(), {}, profile)["valid"]
    assert check_packaging_safety_quality(None, {"is_safe": True})["valid"]

    req = build_packaging_quality_report({})
    assert req["passed"]
