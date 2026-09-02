from local_delivery.bundle_manifest import build_final_delivery_bundle_manifest, build_delivery_bundle_manifest_items
from local_delivery.delivery_config import get_default_local_delivery_profile
from pathlib import Path

def test_build_manifest():
    prof = get_default_local_delivery_profile()
    man, val = build_final_delivery_bundle_manifest(Path("."), prof)
    assert "local_only_delivery_statement" in man
    df, sum2 = build_delivery_bundle_manifest_items(Path("."), prof)
    assert not df.empty
