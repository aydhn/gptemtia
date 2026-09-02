from pathlib import Path
from local_training.training_config import get_default_local_training_profile
from local_training.cross_layer_lessons import build_cross_layer_lesson_registry, build_cross_layer_lesson

def test_cross_layer_lessons():
    prof = get_default_local_training_profile()
    df, sum = build_cross_layer_lesson_registry(Path("."), prof)
    assert not df.empty
    l = build_cross_layer_lesson("test", prof)
    assert "Cross-layer lesson canlı sistem eğitimi değildir." in l.warnings[0]
