from pathlib import Path
from local_training.training_config import get_default_local_training_profile
from local_training.report_lessons import build_report_reading_lesson_registry, build_report_reading_lesson

def test_report_lessons():
    prof = get_default_local_training_profile()
    df, sum = build_report_reading_lesson_registry(Path("."), prof)
    assert not df.empty
    l = build_report_reading_lesson("test", prof)
    assert "Yatırım tavsiyesi" in l.warnings[1]


def test_dummy(): pass
