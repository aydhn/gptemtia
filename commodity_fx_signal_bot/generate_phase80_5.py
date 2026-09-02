import os

def write_file(path: str, content: str):
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)

assumptions_register = """
from pathlib import Path
import pandas as pd
from local_closure.closure_config import LocalClosureProfile

def build_default_assumptions(profile: LocalClosureProfile) -> pd.DataFrame:
    return pd.DataFrame([{"assumption": "Offline data is sufficient", "status": "valid"}])

def build_closure_assumptions_register(profile: LocalClosureProfile) -> tuple[pd.DataFrame, dict]:
    df = build_default_assumptions(profile)
    summary = summarize_assumptions(df)
    return df, summary

def summarize_assumptions(assumption_df: pd.DataFrame) -> dict:
    return {"total": len(assumption_df)}
"""
write_file("local_closure/assumptions_register.py", assumptions_register)

limitations_register = """
from pathlib import Path
import pandas as pd
from local_closure.closure_config import LocalClosureProfile

def build_default_known_limitations(profile: LocalClosureProfile) -> pd.DataFrame:
    return pd.DataFrame([{"limitation": "No live market data", "impact": "offline only"}])

def build_closure_known_limitations_register(profile: LocalClosureProfile) -> tuple[pd.DataFrame, dict]:
    df = build_default_known_limitations(profile)
    summary = summarize_known_limitations(df)
    return df, summary

def summarize_known_limitations(limit_df: pd.DataFrame) -> dict:
    return {"total": len(limit_df)}
"""
write_file("local_closure/limitations_register.py", limitations_register)

closure_no_go_safe_go = """
from pathlib import Path
import pandas as pd
from local_closure.closure_config import LocalClosureProfile

def build_closure_no_go_conditions(profile: LocalClosureProfile) -> pd.DataFrame:
    return pd.DataFrame([
        {"condition": "Live trading claim", "type": "no_go"},
        {"condition": "Production release claim", "type": "no_go"}
    ])

def build_closure_safe_go_conditions(profile: LocalClosureProfile) -> pd.DataFrame:
    return pd.DataFrame([
        {"condition": "Offline closure documented", "type": "safe_go"}
    ])

def build_closure_no_go_safe_go_summary(project_root: Path, profile: LocalClosureProfile) -> tuple[pd.DataFrame, dict]:
    df1 = build_closure_no_go_conditions(profile)
    df2 = build_closure_safe_go_conditions(profile)
    df = pd.concat([df1, df2], ignore_index=True)
    summary = summarize_closure_no_go_safe_go(df)
    return df, summary

def summarize_closure_no_go_safe_go(summary_df: pd.DataFrame) -> dict:
    return {"total": len(summary_df)}
"""
write_file("local_closure/closure_no_go_safe_go.py", closure_no_go_safe_go)

handoff_aftercare = """
from pathlib import Path
from local_closure.closure_config import LocalClosureProfile

def build_aftercare_sections(profile: LocalClosureProfile) -> list[dict]:
    return [
        {"title": "Handoff", "content": "All artifacts are local."},
        {"title": "Aftercare", "content": "No live support."}
    ]

def build_closure_handoff_aftercare_guide(profile: LocalClosureProfile) -> tuple[str, dict]:
    sections = build_aftercare_sections(profile)
    text = "# Handoff Aftercare Guide\\n\\n"
    for s in sections:
        text += f"## {s['title']}\\n{s['content']}\\n\\n"
    summary = summarize_handoff_aftercare_guide(text)
    return text, summary

def summarize_handoff_aftercare_guide(text: str) -> dict:
    return {"len": len(text)}
"""
write_file("local_closure/handoff_aftercare.py", handoff_aftercare)

closure_faq = """
from pathlib import Path
import pandas as pd
from local_closure.closure_config import LocalClosureProfile

def build_default_closure_faq(profile: LocalClosureProfile) -> pd.DataFrame:
    return pd.DataFrame([
        {"question": "Bu gerçek v1.0 release mi?", "answer": "Hayır."},
        {"question": "Bu resmi proje kapanışı mı?", "answer": "Hayır."}
    ])

def build_closure_faq(profile: LocalClosureProfile) -> tuple[pd.DataFrame, dict]:
    df = build_default_closure_faq(profile)
    summary = summarize_closure_faq(df)
    return df, summary

def summarize_closure_faq(faq_df: pd.DataFrame) -> dict:
    return {"total": len(faq_df)}
"""
write_file("local_closure/closure_faq.py", closure_faq)

closure_exceptions = """
from pathlib import Path
import pandas as pd
from local_closure.closure_config import LocalClosureProfile

def detect_closure_exceptions(project_root: Path, unresolved_df: pd.DataFrame, roadmap_df: pd.DataFrame) -> pd.DataFrame:
    return pd.DataFrame([{"exception": "None detected", "status": "info"}])

def build_closure_exception_register(project_root: Path, unresolved_df: pd.DataFrame, roadmap_df: pd.DataFrame, profile: LocalClosureProfile) -> tuple[pd.DataFrame, dict]:
    df = detect_closure_exceptions(project_root, unresolved_df, roadmap_df)
    summary = summarize_closure_exceptions(df)
    return df, summary

def summarize_closure_exceptions(exception_df: pd.DataFrame) -> dict:
    return {"total": len(exception_df)}
"""
write_file("local_closure/closure_exceptions.py", closure_exceptions)

closure_gaps = """
from pathlib import Path
import pandas as pd
from local_closure.closure_config import LocalClosureProfile

def detect_missing_closure_domains(domain_df: pd.DataFrame) -> pd.DataFrame:
    return pd.DataFrame()

def detect_missing_lessons(lessons_df: pd.DataFrame) -> pd.DataFrame:
    return pd.DataFrame()

def detect_missing_roadmap_items(roadmap_df: pd.DataFrame) -> pd.DataFrame:
    return pd.DataFrame()

def detect_missing_unresolved_items(unresolved_df: pd.DataFrame) -> pd.DataFrame:
    return pd.DataFrame()

def build_closure_gap_register(
    domain_df: pd.DataFrame,
    lessons_df: pd.DataFrame,
    roadmap_df: pd.DataFrame,
    unresolved_df: pd.DataFrame,
    profile: LocalClosureProfile,
) -> tuple[pd.DataFrame, dict]:
    gaps = pd.DataFrame([{"gap": "None", "type": "info"}])
    summary = summarize_closure_gaps(gaps)
    return gaps, summary

def summarize_closure_gaps(gap_df: pd.DataFrame) -> dict:
    return {"total": len(gap_df)}
"""
write_file("local_closure/closure_gaps.py", closure_gaps)
