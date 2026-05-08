import pandas as pd
from ml.splitters import chronological_train_test_split, chronological_train_validation_test_split, apply_embargo, build_split_manifest

def test_chronological_train_test_split():
    df = pd.DataFrame({"A": range(10)})
    train, test, _ = chronological_train_test_split(df, 0.2)
    assert len(train) == 8
    assert len(test) == 2
    assert train.iloc[-1]["A"] == 7
    assert test.iloc[0]["A"] == 8

def test_chronological_train_validation_test_split():
    df = pd.DataFrame({"A": range(10)})
    train, val, test, _ = chronological_train_validation_test_split(df, 0.2, 0.2)
    assert len(train) == 6
    assert len(val) == 2
    assert len(test) == 2

def test_apply_embargo():
    train = pd.DataFrame({"A": range(10)})
    test = pd.DataFrame({"A": range(10, 12)})
    emb_train, _ = apply_embargo(train, test, 2)
    assert len(emb_train) == 8
    assert emb_train.iloc[-1]["A"] == 7

def test_build_split_manifest():
    train = pd.DataFrame({"A": [1]}, index=[0])
    test = pd.DataFrame({"A": [2]}, index=[1])
    manifest = build_split_manifest("SYM", "1d", "prof", "tar", train, None, test, 0, False, [])
    assert manifest.symbol == "SYM"
    assert manifest.train_start == "0"
