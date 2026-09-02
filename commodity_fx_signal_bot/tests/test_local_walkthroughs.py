from pathlib import Path
from local_training.training_config import get_default_local_training_profile
from local_training.local_walkthroughs import build_local_walkthrough_lessons, build_walkthrough_steps, validate_walkthrough_steps_safety

def test_local_walkthroughs():
    prof = get_default_local_training_profile()
    df, sum = build_local_walkthrough_lessons(Path("."), prof)
    assert not df.empty
    steps = build_walkthrough_steps("repo", prof)
    assert isinstance(steps, list)
    val = validate_walkthrough_steps_safety(steps, prof)
    assert val["is_safe"]
