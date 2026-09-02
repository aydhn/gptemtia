import pandas as pd

def build_briefing_disclaimer() -> str:
    return "\n> **UYARI:** Bu cikti offline/local stakeholder communication ve executive briefing raporudur. Yatirim tavsiyesi, canli emir, broker talimati, model deployment, production release, resmi yonetim kurulu karari veya yatirim komitesi onayi degildir.\n"

def build_communication_profile_markdown_report(summary: dict, profile_df: pd.DataFrame | None = None) -> str:
    text = "# Communication Profile Registry\n"
    text += build_briefing_disclaimer()
    if profile_df is not None:
        text += profile_df.to_markdown(index=False)
    return text

def build_executive_summary_markdown_report(summary: dict, text: str | None = None) -> str:
    out = text if text else "# Executive Summary Pack\n"
    out += build_briefing_disclaimer()
    return out

def build_deck_source_markdown_report(summary: dict, slide_df: pd.DataFrame | None = None) -> str:
    text = "# Non-Technical Briefing Deck Source\n"
    text += build_briefing_disclaimer()
    if slide_df is not None:
        for _, row in slide_df.iterrows():
            text += f"## Slide {row['slide_number']}: {row['title']}\n"
            text += "\n".join([f"- {x}" for x in row['bullets']]) + "\n\n"
    return text

def build_decision_context_markdown_report(summary: dict, matrix_df: pd.DataFrame | None = None) -> str:
    text = "# Decision Context Binder\n"
    text += build_briefing_disclaimer()
    if matrix_df is not None:
        text += matrix_df.to_markdown(index=False)
    return text

def build_stakeholder_communication_markdown_report(summary: dict, template_df: pd.DataFrame | None = None) -> str:
    text = "# Stakeholder Communication Kit\n"
    text += build_briefing_disclaimer()
    if template_df is not None:
        text += template_df.to_markdown(index=False)
    return text

def build_briefing_quality_markdown_report(summary: dict, quality: dict | None = None) -> str:
    text = "# Briefing Quality Report\n"
    text += build_briefing_disclaimer()
    if quality:
        for k, v in quality.items():
            text += f"- **{k}**: {v}\n"
    return text

def build_briefing_status_markdown_report(summary: dict, status_df: pd.DataFrame | None = None) -> str:
    text = "# Briefing Status\n"
    text += build_briefing_disclaimer()
    if status_df is not None:
        text += status_df.to_markdown(index=False)
    return text
