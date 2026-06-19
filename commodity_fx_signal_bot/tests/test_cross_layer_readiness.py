from local_readiness.readiness_config import get_default_local_readiness_profile
from local_readiness.cross_layer_readiness import build_metadata_evidence_graph_timeline_consistency_readiness_report
from config.paths import PROJECT_ROOT

def test_cross_layer_readiness():
    profile = get_default_local_readiness_profile()
    df, s = build_metadata_evidence_graph_timeline_consistency_readiness_report(PROJECT_ROOT, profile)
    assert not df.empty
