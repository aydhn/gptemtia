"""PDF ready maps."""
import pandas as pd
from .export_config import LocalDocumentationExportProfile

def build_default_pdf_ready_print_items(profile: LocalDocumentationExportProfile) -> pd.DataFrame:
    return pd.DataFrame([{"item": "PDF_READY_DOCUMENTATION_PACKET.md"}])

def build_default_pdf_ready_limitations(profile: LocalDocumentationExportProfile) -> pd.DataFrame:
    return pd.DataFrame([
        {"limitation": "no PDF binary generated"},
        {"limitation": "no browser automation"},
        {"limitation": "no wkhtmltopdf/chromium/playwright invocation"},
        {"limitation": "no official PDF release"},
        {"limitation": "no legal/compliance proof"},
        {"limitation": "no production approval"},
        {"limitation": "manual review required"}
    ])

def build_pdf_ready_print_checklist(profile: LocalDocumentationExportProfile) -> tuple[pd.DataFrame, dict]:
    df = build_default_pdf_ready_print_items(profile)
    return df, summarize_pdf_ready_maps(df)

def build_pdf_ready_limitation_register(profile: LocalDocumentationExportProfile) -> tuple[pd.DataFrame, dict]:
    df = build_default_pdf_ready_limitations(profile)
    return df, summarize_pdf_ready_maps(df)

def summarize_pdf_ready_maps(df: pd.DataFrame) -> dict:
    return {"count": len(df)}
