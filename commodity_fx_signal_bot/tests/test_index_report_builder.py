import pandas as pd
from synthetic_indices.index_config import get_default_synthetic_index_profile
from synthetic_indices.index_report_builder import (
    build_synthetic_benchmark_markdown_report,
    build_synthetic_index_disclaimer
)

def test_report_builder():
    profile = get_default_synthetic_index_profile()
    summary = {"symbols_processed": 10, "warnings": []}
    df = pd.DataFrame({"A": [1, 2], "B": [3, 4]})
    tables = {"Data": df}

    report = build_synthetic_benchmark_markdown_report(summary, tables, profile)

    # Must contain disclaimer
    disclaimer = build_synthetic_index_disclaimer()
    assert disclaimer in report

    # Must contain summary
    assert "symbols_processed" in report

    # Must contain table
    assert "Data" in report
    assert "A" in report
