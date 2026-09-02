from pathlib import Path
from local_training.training_config import get_default_local_training_profile
from local_training.developer_training_pack import build_developer_training_pack

def test_developer_pack():
    prof = get_default_local_training_profile()
    txt, sum = build_developer_training_pack(Path("."), prof)
    assert isinstance(txt, str)
    assert "deployment instruction değildir" in txt.lower() or "deployment" in txt.lower()
