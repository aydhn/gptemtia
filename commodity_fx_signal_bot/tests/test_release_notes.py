import pandas as pd
from pathlib import Path
from quality_gates.release_notes import (
    collect_phase_summaries,
    build_release_notes_draft,
    build_known_limitations_section,
    build_safety_boundaries_section,
    save_release_notes_draft
)

def test_collect_phase_summaries():
    df = collect_phase_summaries(Path("."))
    assert isinstance(df, pd.DataFrame)

def test_build_release_notes_draft():
    draft = build_release_notes_draft({}, pd.DataFrame())
    assert isinstance(draft, str)
    assert "live trade" not in draft.lower()

def test_build_known_limitations_section():
    limitations = build_known_limitations_section({})
    assert isinstance(limitations, str)

def test_build_safety_boundaries_section():
    safety = build_safety_boundaries_section()
    assert isinstance(safety, str)

def test_save_release_notes_draft():
    path = save_release_notes_draft("draft", Path("mock.md"))
    assert path == Path("mock.md")
