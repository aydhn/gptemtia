import pandas as pd
from maintenance.duplicate_detection import detect_duplicate_files_by_name_size

def test_duplicate_detection():
    inv_data = [
        {"artifact_id": "1", "path": "test/a.txt", "relative_path": "a.txt", "size_bytes": 2048, "modified_at_utc": "1"},
        {"artifact_id": "2", "path": "other/a.txt", "relative_path": "other/a.txt", "size_bytes": 2048, "modified_at_utc": "2"},
        {"artifact_id": "3", "path": "test/b.txt", "relative_path": "b.txt", "size_bytes": 2048, "modified_at_utc": "3"},
        {"artifact_id": "4", "path": "test/c.txt", "relative_path": "c.txt", "size_bytes": 100, "modified_at_utc": "4"}, # Too small
    ]
    inv_df = pd.DataFrame(inv_data)

    dupes = detect_duplicate_files_by_name_size(inv_df)
    assert len(dupes) == 2
    assert dupes.iloc[0]["recommended_action"] == "review_required_action"
