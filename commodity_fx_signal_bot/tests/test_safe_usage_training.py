from pathlib import Path
from local_training.training_config import get_default_local_training_profile
from local_training.safe_usage_training import build_safe_usage_training_pack, build_safe_usage_rules, build_forbidden_action_training

def test_safe_usage():
    prof = get_default_local_training_profile()
    txt, sum = build_safe_usage_training_pack(Path("."), prof)
    assert isinstance(txt, str)
    assert not build_safe_usage_rules(prof).empty
    assert not build_forbidden_action_training(prof).empty
