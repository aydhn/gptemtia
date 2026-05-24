from knowledge_base.decision_journal import build_default_decision_journal_entries

def test_default_entries():
    entries = build_default_decision_journal_entries()
    assert len(entries) > 0
    assert "decision_note" in entries[0].status
