from local_delivery.delivery_domain_registry import build_delivery_domain_registry
from local_delivery.delivery_config import get_default_local_delivery_profile

def test_build_delivery_domain_registry():
    prof = get_default_local_delivery_profile()
    df, summary = build_delivery_domain_registry(prof)
    assert not df.empty
    assert summary["total_domains"] > 0
