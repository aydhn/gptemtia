from local_delivery.recipient_orientation import build_recipient_orientation_guide
from local_delivery.delivery_config import get_default_local_delivery_profile
from pathlib import Path

def test_build_orientation():
    prof = get_default_local_delivery_profile()
    text, summary = build_recipient_orientation_guide(Path("."), prof)
    assert isinstance(text, str)
