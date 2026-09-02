from local_delivery.delivery_faq import build_delivery_recipient_faq
from local_delivery.delivery_config import get_default_local_delivery_profile

def test_build_faq():
    prof = get_default_local_delivery_profile()
    df, summary = build_delivery_recipient_faq(prof)
    assert not df.empty
