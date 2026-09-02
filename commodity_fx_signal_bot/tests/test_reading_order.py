from local_delivery.reading_order import build_delivery_package_reading_order
from local_delivery.delivery_config import get_default_local_delivery_profile

def test_build_reading_order():
    prof = get_default_local_delivery_profile()
    df, summary = build_delivery_package_reading_order(prof)
    assert not df.empty
