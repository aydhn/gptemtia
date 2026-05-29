import pytest
from analyst_ux.ux_labels import (
    list_analyst_intent_labels, list_alias_type_labels,
    list_prompt_pack_labels, list_suggestion_safety_labels,
    validate_analyst_intent, validate_alias_type,
    validate_prompt_pack_label, validate_suggestion_safety, LabelError
)

def test_labels_not_empty():
    assert len(list_analyst_intent_labels()) > 0
    assert len(list_alias_type_labels()) > 0
    assert len(list_prompt_pack_labels()) > 0
    assert len(list_suggestion_safety_labels()) > 0

def test_validate_analyst_intent_valid():
    validate_analyst_intent("status_check_intent")

def test_validate_analyst_intent_invalid():
    with pytest.raises(LabelError):
        validate_analyst_intent("fake_intent")

def test_validate_suggestion_safety_valid():
    validate_suggestion_safety("safe_offline_suggestion")

def test_suggestion_safety_wording():
    labels = list_suggestion_safety_labels()
    assert "safe_offline_suggestion" in labels
    assert "blocked_live_suggestion" in labels
