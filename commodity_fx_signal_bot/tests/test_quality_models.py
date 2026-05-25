from quality_gates.quality_models import (
    build_quality_check_id,
    build_release_candidate_id,
    clamp_quality_score,
    QualityCheckResult,
    quality_check_result_to_dict
)

def test_build_quality_check_id():
    id1 = build_quality_check_id("type", "name")
    id2 = build_quality_check_id("type", "name")
    assert id1 == id2
    assert isinstance(id1, str)

def test_build_release_candidate_id():
    id1 = build_release_candidate_id("profile", "time")
    id2 = build_release_candidate_id("profile", "time")
    assert id1 == id2
    assert id1.startswith("rc_")

def test_clamp_quality_score():
    assert clamp_quality_score(None) is None
    assert clamp_quality_score(-0.5) == 0.0
    assert clamp_quality_score(1.5) == 1.0
    assert clamp_quality_score(0.5) == 0.5

def test_dataclass_to_dict():
    result = QualityCheckResult("id", "type", "status", "name", True, 1.0, "time", "time", 1.0, {}, [])
    d = quality_check_result_to_dict(result)
    assert d["check_id"] == "id"
    assert "check_type" in d
