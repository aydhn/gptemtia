from knowledge_base.analyst_notes import build_default_analyst_notes

def test_default_notes():
    notes = build_default_analyst_notes()
    assert len(notes) > 0
    assert "tavsiyesi" in notes[0].warnings[0].lower()
