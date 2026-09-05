import os
from pathlib import Path

def write_file(path_str, content):
    path = Path(path_str)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content.strip(), encoding="utf-8")
    print(f"Created {path_str}")

def generate_core3():
    write_file("commodity_fx_signal_bot/local_continuity_intelligence/decision_rationale.py", '''
import pandas as pd
from pathlib import Path
from .continuity_models import DecisionRationaleItem

def build_decision_rationale_capsule(project_root: Path, profile) -> tuple[str, dict]:
    sections = build_decision_rationale_sections(profile)
    text = "\\n\\n".join([f"# {s['title']}\\n{s['content']}" for s in sections])
    return text, summarize_decision_rationale_capsule(text)

def build_decision_rationale_sections(profile) -> list[dict]:
    return [
        {"title": "Decision rationale", "content": "Official ADR değildir. Legal/compliance/broker/deploy/advice karar kaydı yoktur."}
    ]

def build_decision_rationale_registry(profile) -> tuple[pd.DataFrame, dict]:
    df = pd.DataFrame([i.__dict__ for i in build_default_decision_rationales(profile)])
    return df, summarize_decision_rationale_registry(df)

def build_default_decision_rationales(profile) -> list[DecisionRationaleItem]:
    return [DecisionRationaleItem("d1", "a1", "t1", "s1", [], "note", ["Manual review boundary"])]

def summarize_decision_rationale_capsule(text: str) -> dict:
    return {"length": len(text)}

def summarize_decision_rationale_registry(df: pd.DataFrame) -> dict:
    return {"total": len(df)}
''')

    write_file("commodity_fx_signal_bot/local_continuity_intelligence/decision_tradeoffs.py", '''
import pandas as pd
def build_decision_tradeoff_matrix(profile) -> tuple[pd.DataFrame, dict]:
    df = build_default_tradeoff_items(profile)
    return df, summarize_decision_tradeoffs(df)
def build_default_tradeoff_items(profile) -> pd.DataFrame:
    return pd.DataFrame([{"tradeoff": "t1"}])
def summarize_decision_tradeoffs(df: pd.DataFrame) -> dict:
    return {"total": len(df)}
''')

    write_file("commodity_fx_signal_bot/local_continuity_intelligence/decision_recaps.py", '''
def build_architecture_decision_recap(profile) -> tuple[str, dict]:
    return "recap", {"len": 5}
def build_governance_decision_recap(profile) -> tuple[str, dict]:
    return "recap", {"len": 5}
def build_safety_boundary_decision_recap(profile) -> tuple[str, dict]:
    return "recap", {"len": 5}
def build_datalake_reporting_decision_recap(profile) -> tuple[str, dict]:
    return "recap", {"len": 5}
def build_testing_quality_decision_recap(profile) -> tuple[str, dict]:
    return "recap", {"len": 5}
def summarize_decision_recaps(recaps: dict) -> dict:
    return {"total": len(recaps)}
''')

    write_file("commodity_fx_signal_bot/local_continuity_intelligence/future_reader_guide.py", '''
from pathlib import Path
def build_future_reader_guide(project_root: Path, profile) -> tuple[str, dict]:
    sections = build_future_reader_sections(profile)
    text = "\\n\\n".join([f"# {s['title']}\\n{s['content']}" for s in sections])
    return text, summarize_future_reader_guide(text)
def build_future_reader_sections(profile) -> list[dict]:
    return [
        {"title": "Gelecekte bu projeyi okuyan kişi nereden başlamalı?", "content": "Start here."},
        {"title": "Bu sistem ne yapar?", "content": "Does stuff."},
        {"title": "Bu sistem ne yapmaz?", "content": "Does not deploy. No live trading."},
        {"title": "İlk saat planı", "content": "Read this."},
        {"title": "İlk gün planı", "content": "Read that."},
        {"title": "İlk hafta planı", "content": "Read more."},
        {"title": "Hangi raporlar önce okunmalı?", "content": "Reports."},
        {"title": "Hangi komutlar sadece rapor üretir?", "content": "Commands."},
        {"title": "Hangi sınırlar kesinlikle korunmalı?", "content": "Boundaries."},
        {"title": "Hangi çıktılar official approval değildir?", "content": "These."},
        {"title": "Manual review noktaları", "content": "Review here."}
    ]
def summarize_future_reader_guide(text: str) -> dict:
    return {"length": len(text)}
''')

    write_file("commodity_fx_signal_bot/local_continuity_intelligence/future_reader_maps.py", '''
import pandas as pd
from .continuity_models import FutureReaderItem
def build_future_reader_onboarding_map(profile) -> tuple[pd.DataFrame, dict]:
    df = pd.DataFrame([i.__dict__ for i in build_default_future_reader_items(profile)])
    return df, summarize_future_reader_map(df)
def build_future_reader_role_guide(profile) -> tuple[pd.DataFrame, dict]:
    return build_future_reader_onboarding_map(profile)
def build_future_reader_first_hour_guide(profile) -> tuple[pd.DataFrame, dict]:
    return build_future_reader_onboarding_map(profile)
def build_future_reader_first_day_guide(profile) -> tuple[pd.DataFrame, dict]:
    return build_future_reader_onboarding_map(profile)
def build_future_reader_first_week_guide(profile) -> tuple[pd.DataFrame, dict]:
    return build_future_reader_onboarding_map(profile)
def build_default_future_reader_items(profile) -> list[FutureReaderItem]:
    return [FutureReaderItem("r1", "r2", "g1", "s1", True, ["No live/broker/deploy"])]
def summarize_future_reader_map(df: pd.DataFrame) -> dict:
    return {"total": len(df)}
''')

    write_file("commodity_fx_signal_bot/local_continuity_intelligence/continuity_binder.py", '''
from pathlib import Path
def build_continuity_intelligence_binder(project_root: Path, profile) -> tuple[str, dict]:
    sections = build_continuity_binder_sections(project_root, profile)
    text = "\\n\\n".join([f"# {s['title']}\\n{s['content']}" for s in sections])
    return text, summarize_continuity_binder(text)
def build_continuity_binder_sections(project_root: Path, profile) -> list[dict]:
    return [
        {"title": "Continuity amacı", "content": "Purpose."},
        {"title": "Bu binder ne değildir?", "content": "Official knowledge management policy değildir. Cloud memory yoktur."},
        {"title": "Operator memory recap", "content": "Recap."},
        {"title": "Lessons-learned recap", "content": "Recap."},
        {"title": "Decision rationale recap", "content": "Recap."},
        {"title": "Future-reader recap", "content": "Recap."},
        {"title": "Knowledge graph rehearsal recap", "content": "Recap."},
        {"title": "Concept/glossary recap", "content": "Recap."},
        {"title": "Interpretation guide recap", "content": "Recap."},
        {"title": "Reminder map recap", "content": "Recap."},
        {"title": "No-go/safe-go recap", "content": "Recap."},
        {"title": "Exceptions/gaps/risks recap", "content": "Recap."},
        {"title": "Final boundary statement", "content": "Boundary."}
    ]
def summarize_continuity_binder(text: str) -> dict:
    return {"length": len(text)}
''')

if __name__ == "__main__":
    generate_core3()
    print("Core 3 generated")
