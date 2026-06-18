from local_readiness.readiness_config import get_default_local_readiness_profile
from local_readiness.docs_readiness import build_documentation_readiness_report
from config.paths import PROJECT_ROOT

def test_docs_readiness():
    profile = get_default_local_readiness_profile()
    df, s = build_documentation_readiness_report(PROJECT_ROOT, profile)
    assert not df.empty
