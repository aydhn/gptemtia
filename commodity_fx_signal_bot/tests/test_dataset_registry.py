import pandas as pd
from ml.dataset_registry import build_dataset_id, build_dataset_metadata

def test_build_dataset_id():
    id1 = build_dataset_id("SYM", "1d", "prof", ["t1"])
    id2 = build_dataset_id("SYM", "1d", "prof", ["t1"])
    assert id1 == id2

def test_build_dataset_metadata():
    dataset = pd.DataFrame(index=[1, 2])
    meta = build_dataset_metadata("SYM", "1d", "prof", dataset, ["f1"], ["t1"], ["s1"], {}, {})
    assert meta.symbol == "SYM"
    assert meta.row_count == 2
