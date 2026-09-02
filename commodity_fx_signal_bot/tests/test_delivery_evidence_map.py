from local_delivery.delivery_evidence_map import build_delivery_evidence_map
from local_delivery.delivery_config import get_default_local_delivery_profile
from pathlib import Path

def test_build_evidence_map():
    prof = get_default_local_delivery_profile()
    df, summary = build_delivery_evidence_map(Path("."), prof)
    assert not df.empty
