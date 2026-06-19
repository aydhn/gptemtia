from local_readiness.readiness_models import (
    build_readiness_gate_id,
    build_acceptance_criterion_id,
    build_operator_checklist_item_id,
    build_handoff_manifest_id,
    ReadinessGate,
    OperatorChecklistItem,
    readiness_gate_to_dict
)

def test_build_ids_deterministic():
    assert build_readiness_gate_id("docs gate", "docs") == "docs_docs_gate_gate"
    assert build_acceptance_criterion_id("my crit", "tests") == "tests_my_crit_crit"
    assert "manifest_prof_" in build_handoff_manifest_id("prof", "1234")

def test_operator_checklist_safe_command():
    item = OperatorChecklistItem("1", "chk", "dom", "ins", "out", "pen", "python -m x", [])
    assert "live" not in (item.safe_command or "")

def test_to_dict():
    gate = ReadinessGate("1", "g", "d", "desc", [], "gate_passed", False, [])
    d = readiness_gate_to_dict(gate)
    assert d["gate_id"] == "1"
