import pytest
from pathlib import Path
from local_consistency.consistency_config import get_default_local_consistency_profile
from local_consistency.reference_checker import build_missing_and_broken_reference_report, extract_path_references_from_text

def test_extract_path_references_from_text():
    refs = extract_path_references_from_text("See docs/README.md", "some_file.md")
    assert isinstance(refs, list)

def test_build_missing_and_broken_reference_report():
    profile = get_default_local_consistency_profile()
    df, summary = build_missing_and_broken_reference_report(Path("."), profile)
    assert df is not None
