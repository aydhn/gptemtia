import os
from pathlib import Path

def write_file(path_str, content):
    path = Path(path_str)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content.strip(), encoding="utf-8")
    print(f"Created {path_str}")

def generate_core2():
    write_file("commodity_fx_signal_bot/local_continuity_intelligence/operator_memory_book.py", '''
from pathlib import Path
import pandas as pd

def build_final_local_operator_memory_book(project_root: Path, profile) -> tuple[str, dict]:
    sections = build_operator_memory_book_sections(project_root, profile)
    text = "\\n\\n".join([f"# {s['title']}\\n{s['content']}" for s in sections])
    return text, summarize_operator_memory_book(text)

def build_operator_memory_book_sections(project_root: Path, profile) -> list[dict]:
    return [
        {"title": "Amaç ve kapsam", "content": "Local continuity memory book."},
        {"title": "Bu memory book ne değildir?", "content": "Gerçek persistent memory değildir. Yatırım tavsiyesi yoktur."},
        {"title": "Proje kimliği", "content": "Emtia-doviz offline bot."},
        {"title": "Phase 1-92 hafıza özeti", "content": "Phase 1-92 summary."},
        {"title": "Ana modül aileleri", "content": "Modules."},
        {"title": "Ana çıktı aileleri", "content": "Outputs."},
        {"title": "Kritik sınırlar", "content": "Boundaries."},
        {"title": "Operator için ilk okuma", "content": "Operator reading."},
        {"title": "Analyst için ilk okuma", "content": "Analyst reading."},
        {"title": "Maintainer için ilk okuma", "content": "Maintainer reading."},
        {"title": "Codex agent için ilk okuma", "content": "Codex reading."},
        {"title": "En çok karıştırılabilecek kavramlar", "content": "Concepts."},
        {"title": "No-go/safe-go özeti", "content": "No-go summary."},
        {"title": "Final boundary statement", "content": "Bu dokuman bir local continuity denemesidir."}
    ]

def summarize_operator_memory_book(text: str) -> dict:
    return {"length": len(text)}

def save_operator_memory_book(text: str, output_path: Path) -> Path:
    output_path.write_text(text, encoding="utf-8")
    return output_path
''')

    write_file("commodity_fx_signal_bot/local_continuity_intelligence/operator_memory_maps.py", '''
import pandas as pd
from .continuity_models import OperatorMemoryItem

def build_operator_memory_index(profile) -> tuple[pd.DataFrame, dict]:
    df = pd.DataFrame([i.__dict__ for i in build_default_operator_memory_items(profile)])
    return df, summarize_operator_memory_map(df)
def build_operator_memory_topic_map(profile) -> tuple[pd.DataFrame, dict]:
    return build_operator_memory_index(profile)
def build_operator_memory_reading_route(profile) -> tuple[pd.DataFrame, dict]:
    return build_operator_memory_index(profile)
def build_default_operator_memory_items(profile) -> list[OperatorMemoryItem]:
    return [OperatorMemoryItem("m1", "t1", "a1", "s1", [], "note", ["No cloud sync"])]
def summarize_operator_memory_map(df: pd.DataFrame) -> dict:
    return {"total": len(df)}
''')

    write_file("commodity_fx_signal_bot/local_continuity_intelligence/operator_memory_cards.py", '''
import pandas as pd
def build_operator_memory_quick_reference_cards(profile) -> tuple[pd.DataFrame, dict]:
    df = build_default_quick_reference_cards(profile)
    return df, summarize_operator_memory_cards(df)
def build_default_quick_reference_cards(profile) -> pd.DataFrame:
    return pd.DataFrame([{"what it is": "a", "what it is not": "b", "where to read": "c", "safe command family": "d", "unsafe command family": "e", "manual review note": "f"}])
def summarize_operator_memory_cards(df: pd.DataFrame) -> dict:
    return {"total": len(df)}
''')

    write_file("commodity_fx_signal_bot/local_continuity_intelligence/lessons_learned_codex.py", '''
from pathlib import Path
def build_lessons_learned_codex(project_root: Path, profile) -> tuple[str, dict]:
    sections = build_lessons_learned_sections(profile)
    text = "\\n\\n".join([f"# {s['title']}\\n{s['content']}" for s in sections])
    return text, summarize_lessons_learned_codex(text)
def build_lessons_learned_sections(profile) -> list[dict]:
    return [
        {"title": "Bu codex ne anlatır?", "content": "Lessons learned."},
        {"title": "Bu codex ne değildir?", "content": "Official lessons report değildir. Legal/compliance evidence değildir. Yatırım tavsiyesi yoktur."},
        {"title": "Architecture lessons", "content": "Arch lessons."},
        {"title": "DataLake/reporting lessons", "content": "DL lessons."},
        {"title": "Quality/testing lessons", "content": "Quality lessons."},
        {"title": "Safety/governance lessons", "content": "Safety lessons."},
        {"title": "Redteam/incident/release/longterm/completion/preservation lessons", "content": "Misc lessons."},
        {"title": "Operator handoff lessons", "content": "Handoff lessons."},
        {"title": "Future maintenance lessons", "content": "Maint lessons."},
        {"title": "Anti-misuse lessons", "content": "Anti-misuse lessons."},
        {"title": "Final boundary statement", "content": "Boundary."}
    ]
def summarize_lessons_learned_codex(text: str) -> dict:
    return {"length": len(text)}
''')

    write_file("commodity_fx_signal_bot/local_continuity_intelligence/lessons_learned_maps.py", '''
import pandas as pd
from .continuity_models import LessonLearnedItem
def build_lessons_learned_category_registry(profile) -> tuple[pd.DataFrame, dict]:
    df = pd.DataFrame([i.__dict__ for i in build_default_lessons(profile)])
    return df, summarize_lessons_learned_map(df)
def build_lessons_learned_phase_map(profile) -> tuple[pd.DataFrame, dict]:
    return build_lessons_learned_category_registry(profile)
def build_lessons_learned_risk_map(profile) -> tuple[pd.DataFrame, dict]:
    return build_lessons_learned_category_registry(profile)
def build_lessons_learned_quality_map(profile) -> tuple[pd.DataFrame, dict]:
    return build_lessons_learned_category_registry(profile)
def build_lessons_learned_safety_map(profile) -> tuple[pd.DataFrame, dict]:
    return build_lessons_learned_category_registry(profile)
def build_default_lessons(profile) -> list[LessonLearnedItem]:
    return [LessonLearnedItem("l1", "c1", "p1", "t1", "s1", "f1", ["Safety certification değildir."])]
def summarize_lessons_learned_map(df: pd.DataFrame) -> dict:
    return {"total": len(df)}
''')

if __name__ == "__main__":
    generate_core2()
    print("Core 2 generated")
