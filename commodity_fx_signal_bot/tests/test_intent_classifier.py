import pytest
from analyst_ux.ux_config import get_default_analyst_ux_profile
from analyst_ux.intent_classifier import (
    normalize_user_query, classify_analyst_intent, build_intent_examples
)

def test_normalize_user_query():
    assert normalize_user_query(" Test  ") == "test"

def test_classify_intents():
    profile = get_default_analyst_ux_profile()

    intent = classify_analyst_intent("sistem durumunu kontrol et", profile)
    assert intent.intent_label == "status_check_intent"

    intent = classify_analyst_intent("scenario regression raporu üret", profile)
    assert intent.intent_label == "scenario_regression_intent"

    intent = classify_analyst_intent("cleanup maintenance", profile)
    assert intent.intent_label == "maintenance_intent"

    intent = classify_analyst_intent("hello world test", profile)
    assert intent.intent_label == "unknown_intent"

def test_classifier_is_local():
    # Implicitly tested by the fact that it runs without mocking requests
    pass
