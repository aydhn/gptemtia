from pathlib import Path
from local_training.training_config import get_default_local_training_profile
from local_training.troubleshooting_lessons import build_troubleshooting_lesson_registry, build_common_troubleshooting_lessons

def test_troubleshooting_lessons():
    prof = get_default_local_training_profile()
    df, sum = build_troubleshooting_lesson_registry(Path("."), prof)
    assert not df.empty
    ls = build_common_troubleshooting_lessons(prof)
    assert len(ls) > 0
