from local_training.training_models import build_training_domain_id, build_onboarding_path_id, build_training_lesson_id, build_training_faq_id, TrainingLesson, training_lesson_to_dict

def test_ids_deterministic():
    assert build_training_domain_id("test") == build_training_domain_id("test")
    assert build_onboarding_path_id("test", "test") == build_onboarding_path_id("test", "test")
    assert build_training_lesson_id("test", "test") == build_training_lesson_id("test", "test")
    assert build_training_faq_id("test") == build_training_faq_id("test")

def test_dataclass_to_dict():
    tl = TrainingLesson("id", "name", "dom", "role", "obj", ["step"], ["safe"], ["out"], "stat", ["warn"])
    d = training_lesson_to_dict(tl)
    assert "lesson_id" in d
    assert "safe_commands" in d
    assert "safe" in d["safe_commands"]
