from local_readiness.readiness_config import get_default_local_readiness_profile
from local_readiness.phase_evidence_binder import build_phase_completion_evidence_binder
from config.paths import PROJECT_ROOT

def test_phase_evidence_binder():
    profile = get_default_local_readiness_profile()
    text, summary = build_phase_completion_evidence_binder(PROJECT_ROOT, profile)
    assert len(text) > 0
    assert "Phase 1-69" in text
    assert summary["text_length"] > 0
