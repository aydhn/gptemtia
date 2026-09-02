from pathlib import Path
from local_training.training_config import get_default_local_training_profile
from local_training.command_lessons import build_safe_command_lesson_registry, classify_training_command_safety, detect_forbidden_training_command_terms

def test_command_lessons():
    prof = get_default_local_training_profile()
    df, sum = build_safe_command_lesson_registry(Path("."), prof)
    assert not df.empty
    assert classify_training_command_safety("python -m script")["is_safe"]
    assert not classify_training_command_safety("buy something")["is_safe"]
    assert "buy" in detect_forbidden_training_command_terms("buy something")
