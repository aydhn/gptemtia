from config.settings import Settings
from governance.governance_config import get_default_governance_profile
from governance.governance_pipeline import GovernancePipeline


class MockDataLake:
    pass

def test_pipeline_init(tmp_path):
    settings = Settings()
    dl = MockDataLake()
    prof = get_default_governance_profile()
    p = GovernancePipeline(dl, settings, tmp_path, prof)
    assert p.project_root == tmp_path
