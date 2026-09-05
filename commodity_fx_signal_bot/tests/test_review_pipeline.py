
from pathlib import Path
from config.settings import Settings
from data.storage.data_lake import DataLake
from local_review_governance.review_pipeline import LocalReviewGovernancePipeline
from local_review_governance.review_config import get_default_local_review_governance_profile

def test_pipeline():
    s = Settings()
    d = DataLake(s)
    p = get_default_local_review_governance_profile()
    pipe = LocalReviewGovernancePipeline(d, s, Path("."), p)
    assert pipe is not None
