import pytest
from pathlib import Path
from local_archive.archive_candidate_inventory import classify_archive_candidate_priority, detect_archive_candidate_reasons

def test_classify_priority():
    root = Path("/app")
    p1 = Path("/app/docs/OPERATOR_MANUAL.md")
    assert classify_archive_candidate_priority(p1, root) == "high"

    p2 = Path("/app/data/lake/file.parquet")
    assert classify_archive_candidate_priority(p2, root) == "low" # only json is medium, rest is low for now

def test_detect_reasons():
    root = Path("/app")
    p1 = Path("/app/docs/OPERATOR_MANUAL.md")
    reasons = detect_archive_candidate_reasons(p1, root)
    assert "docs_required" in reasons
    assert "operator_manual" in reasons
