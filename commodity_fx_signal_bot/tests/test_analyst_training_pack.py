from pathlib import Path
from local_training.training_config import get_default_local_training_profile
from local_training.analyst_training_pack import build_analyst_training_pack

def test_analyst_pack():
    prof = get_default_local_training_profile()
    txt, sum = build_analyst_training_pack(Path("."), prof)
    assert isinstance(txt, str)
    assert "yatırım danışmanlığı değildir" in txt.lower() or "yatırım danışmanlığı" in txt.lower()
    assert "kesin al/sat" in txt.lower()
