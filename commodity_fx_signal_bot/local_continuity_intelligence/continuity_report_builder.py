import pandas as pd

def build_continuity_domain_registry_markdown_report(summary: dict, domain_df: pd.DataFrame = None) -> str:
    return build_continuity_disclaimer() + "\n\n# Continuity Domain Registry"
def build_operator_memory_book_markdown_report(summary: dict, memory_text: str = None) -> str:
    return build_continuity_disclaimer() + "\n\n# Operator Memory Book"
def build_lessons_learned_codex_markdown_report(summary: dict, lessons_text: str = None) -> str:
    return build_continuity_disclaimer() + "\n\n# Lessons-Learned Codex"
def build_decision_rationale_markdown_report(summary: dict, decision_text: str = None) -> str:
    return build_continuity_disclaimer() + "\n\n# Decision Rationale Capsule"
def build_future_reader_guide_markdown_report(summary: dict, reader_text: str = None) -> str:
    return build_continuity_disclaimer() + "\n\n# Future-Reader Guide"
def build_continuity_binder_markdown_report(summary: dict, binder_text: str = None) -> str:
    return build_continuity_disclaimer() + "\n\n# Continuity Intelligence Binder"
def build_continuity_quality_markdown_report(summary: dict, quality: dict = None) -> str:
    return build_continuity_disclaimer() + "\n\n# Continuity Quality"
def build_continuity_status_markdown_report(summary: dict, status_df: pd.DataFrame = None) -> str:
    return build_continuity_disclaimer() + "\n\n# Continuity Status"
def build_continuity_disclaimer() -> str:
    return "Bu çıktı offline/local continuity intelligence ve operator memory rehearsal raporudur. Gerçek operator memory sistemi, official decision record, production approval, canlı emir, broker talimatı, model deployment veya yatırım tavsiyesi değildir."