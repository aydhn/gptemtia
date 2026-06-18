import pytest
import pandas as pd
from local_consistency.consistency_report_builder import (
    build_consistency_check_registry_markdown_report,
    build_system_coherence_markdown_report
)

def test_build_markdown_reports():
    md1 = build_consistency_check_registry_markdown_report({"total_checks": 0})
    md2 = build_system_coherence_markdown_report({"score": 1.0})
    assert "Bu rapor offline/local consistency" in md1
    assert "Bu rapor offline/local consistency" in md2
