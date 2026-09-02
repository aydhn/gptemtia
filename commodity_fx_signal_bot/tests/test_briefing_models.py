from local_briefing.briefing_models import build_audience_id, build_briefing_section_id, build_deck_slide_id, build_decision_question_id

def test_models():
    assert build_audience_id("test") == build_audience_id("test")
    assert build_briefing_section_id("a", "b", "c") == build_briefing_section_id("a", "b", "c")
    assert build_deck_slide_id(1, "a") == build_deck_slide_id(1, "a")
    assert build_decision_question_id("q") == build_decision_question_id("q")
