from pathlib import Path
from local_training.training_config import get_default_local_training_profile
from local_training.non_use_policy_training import build_non_use_policy_training_pack, build_non_use_policy_examples, build_safe_vs_unsafe_prompt_examples

def test_non_use():
    prof = get_default_local_training_profile()
    txt, sum = build_non_use_policy_training_pack(Path("."), prof)
    assert isinstance(txt, str)
    assert not build_non_use_policy_examples(prof).empty
    assert not build_safe_vs_unsafe_prompt_examples(prof).empty
