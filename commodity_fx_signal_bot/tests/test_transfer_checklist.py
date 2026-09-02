from local_delivery.transfer_checklist import build_final_local_transfer_checklist
from local_delivery.delivery_config import get_default_local_delivery_profile
from pathlib import Path

def test_build_checklist():
    prof = get_default_local_delivery_profile()
    df, summary = build_final_local_transfer_checklist(Path("."), prof)
    assert not df.empty
