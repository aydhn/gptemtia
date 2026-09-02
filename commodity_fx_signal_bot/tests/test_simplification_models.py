from local_simplification.simplification_models import (
    build_simplification_domain_id,
    build_complexity_item_id,
    build_simplification_candidate_id,
    build_slimming_plan_item_id,
    SlimmingPlanItem,
    slimming_plan_item_to_dict
)

def test_build_ids():
    assert build_simplification_domain_id("test") == "domain_test"
    assert build_complexity_item_id("a", "b") == "comp_a_b"
    assert build_simplification_candidate_id("a", "b") == "cand_a_b"
    assert build_slimming_plan_item_id("a", "b") == "plan_b_a"

def test_slimming_plan_item_not_real_cleanup():
    item = SlimmingPlanItem("1", "title", "cat", "hint", "action", True, [], ["Not real cleanup"])
    d = slimming_plan_item_to_dict(item)
    assert d["dry_run_only"] is True
