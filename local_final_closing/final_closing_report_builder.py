import pandas as pd
import json

def build_final_closing_disclaimer() -> str:
    return "> [!WARNING]\n> Bu çıktı offline/local final closing governance ve non-production seal rehearsal raporudur. Gerçek project lock, official constitution, official seal, official acceptance, canlı emir, broker talimatı, model deployment veya yatırım tavsiyesi değildir.\n\n"

def build_final_closing_domain_registry_markdown_report(summary: dict, domain_df: pd.DataFrame | None = None) -> str:
    return build_final_closing_disclaimer() + "# Final Closing Domain Registry\n\n" + (domain_df.to_markdown() if domain_df is not None else "")

def build_final_master_terminal_lock_markdown_report(summary: dict, lock_text: str | None = None) -> str:
    return build_final_closing_disclaimer() + (lock_text or "# Final Master Terminal Lock")

def build_project_constitution_markdown_report(summary: dict, constitution_text: str | None = None) -> str:
    return build_final_closing_disclaimer() + (constitution_text or "# Project Constitution")

def build_non_production_seal_markdown_report(summary: dict, seal_text: str | None = None) -> str:
    return build_final_closing_disclaimer() + (seal_text or "# Non-Production Seal")

def build_terminal_archive_index_markdown_report(summary: dict, archive_text: str | None = None) -> str:
    return build_final_closing_disclaimer() + (archive_text or "# Terminal Archive Index")

def build_closing_super_binder_markdown_report(summary: dict, binder_text: str | None = None) -> str:
    return build_final_closing_disclaimer() + (binder_text or "# Closing Super-Binder")

def build_final_closeout_quality_markdown_report(summary: dict, quality: dict | None = None) -> str:
    return build_final_closing_disclaimer() + "# Final Closeout Quality Report\n\n```json\n" + json.dumps(quality or {}, indent=2) + "\n```"

def build_final_closeout_status_markdown_report(summary: dict, status_df: pd.DataFrame | None = None) -> str:
    return build_final_closing_disclaimer() + "# Final Closeout Status\n\n" + (status_df.to_markdown() if status_df is not None else "")
