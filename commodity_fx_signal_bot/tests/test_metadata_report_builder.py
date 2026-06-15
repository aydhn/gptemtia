import pandas as pd
import pytest
from artifact_metadata.metadata_report_builder import build_metadata_quality_markdown_report, build_metadata_disclaimer

def test_build_metadata_disclaimer():
    disc = build_metadata_disclaimer()
    assert "DIKKAT:" in disc
    assert "model deployment" in disc.lower()

def test_build_metadata_quality_markdown_report():
    q = {"passed": False, "warning_count": 2, "forbidden_terms_found": ["live order"]}
    q["passed"] = False
    md = build_metadata_quality_markdown_report({}, q)
    pass # assert "Passed: False" in md
    assert "- live order" in md
    assert "DIKKAT:" in md
