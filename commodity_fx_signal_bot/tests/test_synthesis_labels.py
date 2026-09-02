import pytest
from local_synthesis.synthesis_labels import (
    list_phase_family_labels, list_index_item_labels, list_synthesis_status_labels,
    list_closure_checklist_labels, list_synthesis_risk_labels,
    validate_phase_family_label, validate_index_item_label, validate_synthesis_status,
    validate_closure_checklist_label, validate_synthesis_risk
)

def test_labels_not_empty():
    assert len(list_phase_family_labels()) > 0
    assert len(list_index_item_labels()) > 0
    assert len(list_synthesis_status_labels()) > 0
    assert len(list_closure_checklist_labels()) > 0
    assert len(list_synthesis_risk_labels()) > 0

def test_validate_labels():
    validate_phase_family_label("core_research_family")
    validate_synthesis_status("synthesis_ready")

def test_synthesis_ready_not_production():
    assert "production_release" not in list_synthesis_status_labels()
