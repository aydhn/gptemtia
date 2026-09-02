import pandas as pd

def build_usability_disclaimer() -> str:
    return "Bu çıktı offline/local usability review ve operator ergonomics rehearsal raporudur. Gerçek kullanıcı testi, telemetry, production usability approval, canlı emir, broker talimatı, model deployment veya yatırım tavsiyesi değildir."

def build_usability_domain_registry_markdown_report(summary: dict, domain_df: pd.DataFrame | None = None) -> str:
    return f"# Usability Domain Registry\n\n{build_usability_disclaimer()}\n"

def build_final_local_usability_review_markdown_report(summary: dict, review_text: str | None = None) -> str:
    return f"# Final Local Usability Review\n\n{build_usability_disclaimer()}\n\n{review_text or ''}"

def build_command_discoverability_markdown_report(summary: dict, command_text: str | None = None) -> str:
    return f"# Command Discoverability Guide\n\n{build_usability_disclaimer()}\n\n{command_text or ''}"

def build_documentation_navigation_markdown_report(summary: dict, nav_text: str | None = None) -> str:
    return f"# Documentation Navigation Assistant Pack\n\n{build_usability_disclaimer()}\n\n{nav_text or ''}"

def build_operator_paths_markdown_report(summary: dict, path_df: pd.DataFrame | None = None) -> str:
    return f"# Operator Paths\n\n{build_usability_disclaimer()}\n"

def build_usability_quality_markdown_report(summary: dict, quality: dict | None = None) -> str:
    return f"# Usability Quality Report\n\n{build_usability_disclaimer()}\n"

def build_usability_status_markdown_report(summary: dict, status_df: pd.DataFrame | None = None) -> str:
    return f"# Usability Status\n\n{build_usability_disclaimer()}\n"
