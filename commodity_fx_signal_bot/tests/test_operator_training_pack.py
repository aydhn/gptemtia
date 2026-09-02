from pathlib import Path
from local_training.training_config import get_default_local_training_profile
from local_training.operator_training_pack import build_operator_training_pack, build_operator_training_sections

def test_operator_pack():
    prof = get_default_local_training_profile()
    txt, sum = build_operator_training_pack(Path("."), prof)
    assert isinstance(txt, str)
    secs = build_operator_training_sections(Path("."), prof)
    assert isinstance(secs, list)
    assert "yatırım tavsiyesi" in txt or "Yatırım tavsiyesi" in txt
