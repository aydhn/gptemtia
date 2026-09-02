from local_delivery.delivery_no_go_safe_go import build_delivery_no_go_safe_go_summary
from local_delivery.delivery_config import get_default_local_delivery_profile
from pathlib import Path

def test_build_no_go_safe_go():
    prof = get_default_local_delivery_profile()
    df, summary = build_delivery_no_go_safe_go_summary(Path("."), prof)
    assert not df.empty
