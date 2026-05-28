from final_review.final_review_models import (
    build_audit_id, build_final_risk_id, build_final_gap_id, build_acceptance_snapshot_id,
    clamp_review_score, AuditResult, audit_result_to_dict
)

def test_build_ids():
    assert build_audit_id("test", "test title").startswith("test_test_title")
    assert build_final_risk_id("cat", "risk title").startswith("risk_cat_risk_title")
    assert build_final_gap_id("cat", "gap title").startswith("gap_cat_gap_title")
    assert build_acceptance_snapshot_id("prof", "2024-01-01T00:00:00").startswith("snapshot_prof_20240101T000000")

def test_clamp_review_score():
    assert clamp_review_score(1.5) == 1.0
    assert clamp_review_score(-0.5) == 0.0
    assert clamp_review_score(0.5) == 0.5
    assert clamp_review_score(None) is None

def test_audit_result_to_dict():
    ar = AuditResult(
        audit_id="1", audit_type="test", status="passed", title="title",
        score=1.0, passed=True, checked_items=1, warning_count=0,
        failure_count=0, summary={}, warnings=[], failures=[]
    )
    d = audit_result_to_dict(ar)
    assert d["audit_id"] == "1"
