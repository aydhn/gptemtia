
from pathlib import Path
from local_closure.lessons_learned import build_lessons_learned_compendium, build_default_lessons_learned, export_lessons_learned_markdown
from local_closure.closure_config import get_default_local_closure_profile

def test_lessons():
    p = get_default_local_closure_profile()
    df, summary = build_lessons_learned_compendium(Path.cwd(), p)
    assert not df.empty
    assert summary["total_lessons"] > 0
    
    md = export_lessons_learned_markdown(df, summary)
    assert "UYARI" in md
