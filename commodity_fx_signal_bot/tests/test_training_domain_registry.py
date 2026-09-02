from local_training.training_config import get_default_local_training_profile
from local_training.training_domain_registry import build_training_domain_registry, build_default_training_domains

def test_domain_registry():
    prof = get_default_local_training_profile()
    df, summary = build_training_domain_registry(prof)
    assert not df.empty
    doms = build_default_training_domains(prof)
    assert len(doms) > 0
    for d in doms:
        assert "cloud" not in d.domain_name
        assert "external" not in d.domain_name
