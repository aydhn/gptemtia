import pytest
import pandas as pd
from signals.signal_quality import (
    check_score_ranges,
    check_candidate_duplicates,
    check_missing_candidate_fields,
    build_signal_quality_report,
)


def test_signal_quality_checks():
    df = pd.DataFrame(
        {
            "candidate_id": ["1", "1", "2"],
            "candidate_score": [-0.5, 0.5, 1.5],
            "symbol": ["A", "A", "A"],
            "timeframe": ["1d", "1d", "1d"],
            "timestamp": ["1", "2", "3"],
        }
    )

    assert check_score_ranges(df)["invalid_score_count"] == 2
    assert check_candidate_duplicates(df)["duplicate_candidate_count"] == 1
    assert len(check_missing_candidate_fields(df)["missing_required_fields"]) == 0

    q = build_signal_quality_report(df, {})
    assert q["report_builder = ReportBuilder()ed"] == False
