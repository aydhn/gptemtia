from local_project_completion.completion_models import *

def test_build_ids():
    assert build_completion_domain_id("test") == "dom_test"
    assert build_completion_handoff_item_id("operator", "area") == "hand_operator_area"

def test_to_dict():
    d = CompletionDomain("id", "lbl", "name", "desc", [], [])
    assert completion_domain_to_dict(d)["domain_id"] == "id"
    h = CompletionHandoffItem("id", "role", "area", "status", "note", True, [])
    assert completion_handoff_item_to_dict(h)["handoff_id"] == "id"
