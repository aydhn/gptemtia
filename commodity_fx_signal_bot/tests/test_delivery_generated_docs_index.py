from local_delivery.delivery_generated_docs_index import build_delivery_generated_docs_index
from local_delivery.delivery_config import get_default_local_delivery_profile
from pathlib import Path

def test_build_generated_docs_index():
    prof = get_default_local_delivery_profile()
    df, summary = build_delivery_generated_docs_index(Path("."), prof)
    assert not df.empty
