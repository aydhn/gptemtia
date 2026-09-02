from local_acceptance.acceptance_models import (
    build_acceptance_domain_id,
    build_acceptance_checklist_item_id,
    build_reviewer_question_id,
    build_evidence_trace_id,
    AcceptanceDomain,
    acceptance_domain_to_dict
)

def test_build_ids():
    assert len(build_acceptance_domain_id("test")) == 8
    assert len(build_acceptance_checklist_item_id("dom", "item")) == 8
    assert len(build_reviewer_question_id("q")) == 8
    assert len(build_evidence_trace_id("file", "name")) == 8

def test_to_dict():
    d = AcceptanceDomain("id", "label", "name", "desc", [], [])
    res = acceptance_domain_to_dict(d)
    assert res["domain_id"] == "id"
