import pandas as pd
from local_final_closing.final_closing_config import LocalFinalClosingProfile
from local_final_closing.final_closing_models import FinalTerminalLockItem, build_final_terminal_lock_item_id, final_terminal_lock_item_to_dict

def build_default_final_terminal_lock_items(profile: LocalFinalClosingProfile) -> list[FinalTerminalLockItem]:
    return [
        FinalTerminalLockItem(
            lock_id=build_final_terminal_lock_item_id("core", "master_lock"),
            lock_area="core",
            lock_title="master_lock",
            source_ref="local_final_closing",
            status_label="final_closing_rehearsal_ready",
            manual_review_required=True,
            warnings=["Gerçek project lock değildir", "Dosya kilitleme/chmod/git tag/release yoktur", "Yatırım tavsiyesi yoktur"]
        )
    ]

def build_final_master_terminal_lock_boundary_ledger(profile: LocalFinalClosingProfile) -> tuple[pd.DataFrame, dict]:
    items = build_default_final_terminal_lock_items(profile)
    df = pd.DataFrame([final_terminal_lock_item_to_dict(i) for i in items])
    return df, summarize_final_master_terminal_lock_map(df)

def build_final_master_terminal_lock_non_production_ledger(profile: LocalFinalClosingProfile) -> tuple[pd.DataFrame, dict]:
    items = build_default_final_terminal_lock_items(profile)
    df = pd.DataFrame([final_terminal_lock_item_to_dict(i) for i in items])
    return df, summarize_final_master_terminal_lock_map(df)

def build_final_master_terminal_lock_safety_ledger(profile: LocalFinalClosingProfile) -> tuple[pd.DataFrame, dict]:
    items = build_default_final_terminal_lock_items(profile)
    df = pd.DataFrame([final_terminal_lock_item_to_dict(i) for i in items])
    return df, summarize_final_master_terminal_lock_map(df)

def build_final_master_terminal_lock_manual_review_ledger(profile: LocalFinalClosingProfile) -> tuple[pd.DataFrame, dict]:
    items = build_default_final_terminal_lock_items(profile)
    df = pd.DataFrame([final_terminal_lock_item_to_dict(i) for i in items])
    return df, summarize_final_master_terminal_lock_map(df)

def summarize_final_master_terminal_lock_map(df: pd.DataFrame) -> dict:
    return {"total_ledgers": len(df) if df is not None else 0}
