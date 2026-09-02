from local_delivery.handoff_package_index import build_handoff_package_index, classify_handoff_item_label, classify_handoff_source_layer
from local_delivery.delivery_config import get_default_local_delivery_profile
from pathlib import Path

def test_build_index():
    prof = get_default_local_delivery_profile()
    df, summary = build_handoff_package_index(Path("."), prof)
    assert summary is dict or isinstance(summary, dict)

def test_classify_labels():
    lbl = classify_handoff_item_label(Path("docs/readme.md"), Path("."))
    assert lbl == "delivery_doc_item"


def test_dummy(): pass
