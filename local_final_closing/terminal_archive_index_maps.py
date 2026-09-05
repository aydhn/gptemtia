import pandas as pd
from pathlib import Path
from local_final_closing.final_closing_config import LocalFinalClosingProfile
from local_final_closing.final_closing_models import TerminalArchiveIndexItem, build_terminal_archive_index_item_id, terminal_archive_index_item_to_dict

def build_default_terminal_archive_index_items(profile: LocalFinalClosingProfile) -> list[TerminalArchiveIndexItem]:
    return [
        TerminalArchiveIndexItem(
            archive_index_id=build_terminal_archive_index_item_id("core", "archive"),
            archive_area="core",
            archive_title="archive",
            source_ref=".",
            output_ref="none",
            exclusion_reason="raw secret",
            warnings=["no real archive", "no ZIP/TAR"]
        )
    ]

def build_terminal_archive_index_source_map(project_root: Path, profile: LocalFinalClosingProfile) -> tuple[pd.DataFrame, dict]:
    items = build_default_terminal_archive_index_items(profile)
    df = pd.DataFrame([terminal_archive_index_item_to_dict(i) for i in items])
    return df, summarize_terminal_archive_index_map(df)

def build_terminal_archive_index_output_map(profile: LocalFinalClosingProfile) -> tuple[pd.DataFrame, dict]:
    items = build_default_terminal_archive_index_items(profile)
    df = pd.DataFrame([terminal_archive_index_item_to_dict(i) for i in items])
    return df, summarize_terminal_archive_index_map(df)

def build_terminal_archive_index_report_map(profile: LocalFinalClosingProfile) -> tuple[pd.DataFrame, dict]:
    items = build_default_terminal_archive_index_items(profile)
    df = pd.DataFrame([terminal_archive_index_item_to_dict(i) for i in items])
    return df, summarize_terminal_archive_index_map(df)

def build_terminal_archive_index_documentation_map(profile: LocalFinalClosingProfile) -> tuple[pd.DataFrame, dict]:
    items = build_default_terminal_archive_index_items(profile)
    df = pd.DataFrame([terminal_archive_index_item_to_dict(i) for i in items])
    return df, summarize_terminal_archive_index_map(df)

def build_terminal_archive_index_governance_map(profile: LocalFinalClosingProfile) -> tuple[pd.DataFrame, dict]:
    items = build_default_terminal_archive_index_items(profile)
    df = pd.DataFrame([terminal_archive_index_item_to_dict(i) for i in items])
    return df, summarize_terminal_archive_index_map(df)

def build_terminal_archive_index_exclusion_register(profile: LocalFinalClosingProfile) -> tuple[pd.DataFrame, dict]:
    items = build_default_terminal_archive_index_items(profile)
    df = pd.DataFrame([terminal_archive_index_item_to_dict(i) for i in items])
    return df, summarize_terminal_archive_index_map(df)

def summarize_terminal_archive_index_map(df: pd.DataFrame) -> dict:
    return {"total_items": len(df) if df is not None else 0}
