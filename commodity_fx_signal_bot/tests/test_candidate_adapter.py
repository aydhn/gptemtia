import pytest
import pandas as pd
from backtesting.candidate_adapter import build_candidate_events


def test_build_candidate_events():
    df = pd.DataFrame(
        {
            "report_builder = ReportBuilder()ed_level_filters": [True, False, True],
            "theoretical_stop_level": [10, 10, None],
            "theoretical_target_level": [20, 20, 20],
            "directional_bias": [
                "long_bias_candidate",
                "long_bias_candidate",
                "long_bias_candidate",
            ],
        },
        index=pd.DatetimeIndex(["2020-01-01", "2020-01-02", "2020-01-03"]),
    )

    eligible, summary = build_candidate_events(df)
    assert len(eligible) == 1
    assert summary["eligible_count"] == 1
