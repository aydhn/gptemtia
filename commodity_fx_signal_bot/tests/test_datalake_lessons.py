from pathlib import Path
from local_training.training_config import get_default_local_training_profile
from local_training.datalake_lessons import build_datalake_reading_lesson_registry, build_datalake_domain_lesson

def test_datalake_lessons():
    prof = get_default_local_training_profile()
    df, sum = build_datalake_reading_lesson_registry(Path("."), prof)
    assert not df.empty
    l = build_datalake_domain_lesson("test", prof)
    assert "DataLake lesson raw data extraction değildir." in l.warnings[0]


def test_dummy(): pass
