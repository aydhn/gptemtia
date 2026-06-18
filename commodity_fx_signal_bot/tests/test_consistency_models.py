import pytest
from local_consistency.consistency_models import (
    ConsistencyCheck,
    ConsistencyFinding,
    ContradictionFinding,
    ReferenceFinding,
    ReconciliationRecommendation,
    build_consistency_check_id,
    build_consistency_finding_id,
    build_contradiction_id,
    build_reference_id,
    build_reconciliation_recommendation_id,
    consistency_check_to_dict,
    consistency_finding_to_dict,
    contradiction_finding_to_dict,
    reference_finding_to_dict,
    reconciliation_recommendation_to_dict
)

def test_build_ids_deterministic():
    assert build_consistency_check_id("a", "b", "c") == build_consistency_check_id("a", "b", "c")
    assert build_consistency_finding_id("a", "b", "c", "d") == build_consistency_finding_id("a", "b", "c", "d")
    assert build_contradiction_id("a", "b", "c") == build_contradiction_id("a", "b", "c")
    assert build_reference_id("a", "b") == build_reference_id("a", "b")
    assert build_reconciliation_recommendation_id("a", "b") == build_reconciliation_recommendation_id("a", "b")

def test_dataclass_to_dict():
    c = ConsistencyCheck("id", "type", "name", "src", "tgt", "desc", [], "status", [])
    d = consistency_check_to_dict(c)
    assert d["check_id"] == "id"
