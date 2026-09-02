from local_training.training_config import get_default_local_training_profile
from local_training.knowledge_transfer_checklist import build_knowledge_transfer_checklist, build_role_specific_transfer_checklist

def test_checklist():
    prof = get_default_local_training_profile()
    df, sum = build_knowledge_transfer_checklist(prof)
    assert not df.empty
    assert not build_role_specific_transfer_checklist("test", prof).empty


def test_dummy(): pass
