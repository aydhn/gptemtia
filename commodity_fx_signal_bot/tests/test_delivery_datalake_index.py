from local_delivery.delivery_datalake_index import build_delivery_datalake_index
from local_delivery.delivery_config import get_default_local_delivery_profile
from pathlib import Path

def test_build_datalake_index():
    prof = get_default_local_delivery_profile()
    df, summary = build_delivery_datalake_index(Path("."), prof)
    assert not df.empty
