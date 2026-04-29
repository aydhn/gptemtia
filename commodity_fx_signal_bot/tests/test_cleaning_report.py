import pandas as pd

from data.cleaning.cleaning_report import (
    build_cleaning_report,
    save_cleaning_report_json,
    save_cleaning_report_text,
)
from data.cleaning.quality_scoring import DataQualityScore


def test_build_cleaning_report():
    df = pd.DataFrame({"close": [1, 2, 3]})
    score_before = DataQualityScore(
        "TEST", "1d", 3, 50.0, "D", False, [], [], 0.0, 0, 0, 0
    )
    score_after = DataQualityScore(
        "TEST", "1d", 3, 100.0, "A", True, [], [], 0.0, 0, 0, 0
    )

    report = build_cleaning_report(
        "TEST",
        "1d",
        df,
        df,
        {"duplicate_rows_removed": 0},
        score_before,
        score_after,
        {"total_gaps": 0},
        {"total_outliers": 0},
        {"errors": []},
        {"errors": []},
    )

    assert report.symbol == "TEST"
    assert report.quality_before == "D"
    assert report.quality_after == "A"
    assert report.score_after == 100.0


def test_save_cleaning_report(tmp_path):
    df = pd.DataFrame({"close": [1, 2, 3]})
    score_before = DataQualityScore(
        "TEST", "1d", 3, 50.0, "D", False, [], [], 0.0, 0, 0, 0
    )
    score_after = DataQualityScore(
        "TEST", "1d", 3, 100.0, "A", True, [], [], 0.0, 0, 0, 0
    )

    report = build_cleaning_report(
        "TEST",
        "1d",
        df,
        df,
        {"duplicate_rows_removed": 0},
        score_before,
        score_after,
        {"total_gaps": 0},
        {"total_outliers": 0},
        {"errors": []},
        {"errors": []},
    )

    json_path = tmp_path / "report.json"
    save_cleaning_report_json(report, json_path)
    assert json_path.exists()

    txt_path = tmp_path / "report.txt"
    save_cleaning_report_text(report, txt_path)
    assert txt_path.exists()
