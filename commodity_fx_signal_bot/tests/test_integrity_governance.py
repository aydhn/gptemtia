import pandas as pd

from governance.integrity_governance import (
    build_integrity_governance_table,
    check_artifact_integrity_from_record,
)


def test_integrity():
    rec = {
        "path": "test.csv",
        "size_bytes": 100,
        "extension": ".csv",
        "schema_fingerprint": "hash1",
        "content_fingerprint": "hash2",
        "warnings": []
    }
    check = check_artifact_integrity_from_record(rec)
    assert check["is_intact"]

    rec["size_bytes"] = 0
    check2 = check_artifact_integrity_from_record(rec)
    assert not check2["is_intact"]

def test_build_table():
    inv_df = pd.DataFrame([{
        "artifact_id": "a1", "artifact_type": "feat", "relative_path": "path",
        "path": "path", "size_bytes": 100, "extension": ".txt", "content_fingerprint": "hash"
    }])
    df = build_integrity_governance_table(inv_df)
    assert not df.empty
    assert df.iloc[0]["is_intact"]
