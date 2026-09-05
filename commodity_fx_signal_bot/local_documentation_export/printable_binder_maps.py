"""Printable binder maps."""
import pandas as pd
from .export_config import LocalDocumentationExportProfile
from .export_models import PrintableBinderItem, build_printable_binder_item_id

def build_default_printable_binder_items(profile: LocalDocumentationExportProfile) -> list[PrintableBinderItem]:
    return [
        PrintableBinderItem(
            binder_id=build_printable_binder_item_id("Architecture", "Core"),
            section_title="Architecture",
            section_area="Core",
            source_refs=["docs/ARCHITECTURE.md"],
            reading_priority=1,
            format_label="format_printable",
            warnings=["PDF binary değildir"]
        )
    ]

def build_printable_binder_section_registry(profile: LocalDocumentationExportProfile) -> tuple[pd.DataFrame, dict]:
    items = build_default_printable_binder_items(profile)
    df = pd.DataFrame([i.__dict__ for i in items])
    return df, summarize_printable_binder_map(df)

def build_printable_binder_reading_order(profile: LocalDocumentationExportProfile) -> tuple[pd.DataFrame, dict]:
    df = pd.DataFrame([{"order": 1, "item": "Architecture"}])
    return df, summarize_printable_binder_map(df)

def build_printable_binder_table_of_contents(profile: LocalDocumentationExportProfile) -> tuple[pd.DataFrame, dict]:
    df = pd.DataFrame([{"toc_item": "Architecture"}])
    return df, summarize_printable_binder_map(df)

def build_printable_binder_appendix_registry(profile: LocalDocumentationExportProfile) -> tuple[pd.DataFrame, dict]:
    df = pd.DataFrame([{"appendix_item": "Glossary"}])
    return df, summarize_printable_binder_map(df)

def summarize_printable_binder_map(df: pd.DataFrame) -> dict:
    return {"count": len(df)}
