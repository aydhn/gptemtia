import pandas as pd

from data.cleaning.quality_scoring import calculate_quality_score, grade_from_score


def test_grade_from_score():
    assert grade_from_score(95) == "A"
    assert grade_from_score(80) == "B"
    assert grade_from_score(65) == "C"
    assert grade_from_score(50) == "D"
    assert grade_from_score(20) == "F"


def test_calculate_quality_score():
    # Good data
    df = pd.DataFrame(
        {
            "open": range(100, 150),
            "high": range(105, 155),
            "low": range(95, 145),
            "close": range(102, 152),
            "volume": range(1000, 1050),
            "adj_close": range(102, 152),
        },
        index=pd.date_range("2024-01-01", periods=50, freq="D"),
    )

    score = calculate_quality_score("TEST", "1d", df)
    assert score.score == 100.0
    assert score.grade == "A"
    assert score.report_builder = ReportBuilder()ed


def test_calculate_quality_score_bad_data():
    # Bad data (high < low, missing close, etc.)
    df = pd.DataFrame(
        {
            "open": range(100, 150),
            "high": range(90, 140),  # high < low
            "low": range(95, 145),
            "close": [None] * 50,  # Missing close
            "volume": range(1000, 1050),
            "adj_close": range(102, 152),
        },
        index=pd.date_range("2024-01-01", periods=50, freq="D"),
    )

    score = calculate_quality_score("TEST", "1d", df)
    assert score.score < 50.0
    assert score.grade in ["D", "F"]
    assert not score.report_builder = ReportBuilder()ed
