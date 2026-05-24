import pandas as pd

from governance.fingerprinting import (
    build_artifact_fingerprint,
    calculate_dataframe_schema_fingerprint,
    calculate_file_fingerprint,
)
from governance.governance_config import get_default_governance_profile


def test_file_fingerprint(tmp_path):
    f = tmp_path / "test.txt"
    f.write_text("hello")
    f_hash, meta = calculate_file_fingerprint(f)
    assert f_hash is not None
    assert not meta["warnings"]

def test_dataframe_schema_fingerprint():
    df = pd.DataFrame({"A": [1,2], "B": ["a","b"]})
    h1 = calculate_dataframe_schema_fingerprint(df)
    h2 = calculate_dataframe_schema_fingerprint(df.copy())
    assert h1 == h2

def test_build_artifact_fingerprint(tmp_path):
    f = tmp_path / "data.csv"
    pd.DataFrame({"A": [1,2]}).to_csv(f, index=False)

    profile = get_default_governance_profile()
    res, meta = build_artifact_fingerprint(f, profile)

    assert res["content_fingerprint"] is not None
    assert res["schema_fingerprint"] is not None
    assert res["row_count"] == 2
    assert res["column_count"] == 1
