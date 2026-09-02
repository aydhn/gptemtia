from local_delivery.delivery_scripts_tests_index import build_delivery_scripts_tests_index
from local_delivery.delivery_config import get_default_local_delivery_profile
from pathlib import Path

def test_build_scripts_index():
    prof = get_default_local_delivery_profile()
    df, summary = build_delivery_scripts_tests_index(Path("."), prof)
    assert not df.empty
