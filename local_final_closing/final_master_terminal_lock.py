import pandas as pd
from pathlib import Path
from local_final_closing.final_closing_config import LocalFinalClosingProfile

def build_final_master_terminal_lock_sections(project_root: Path, profile: LocalFinalClosingProfile) -> list[dict]:
    return [
        {"title": "Amaç ve kapsam", "content": "Offline/local final master terminal lock rehearsal amacı ve kapsamı."},
        {"title": "Bu terminal lock ne değildir?", "content": "Bu terminal lock gerçek project lock değildir. Dosya kilitleme/chmod/read-only yok. Git tag/release yok. Production/live/broker/advice yok."},
        {"title": "Phase 1-100 final recap", "content": "Phase 1-100 final recap of all capabilities."},
        {"title": "Non-production boundary", "content": "This project is bounded to non-production."},
        {"title": "Local-only boundary", "content": "This project is bounded to local-only environments."},
        {"title": "No broker/live/advice boundary", "content": "This project has no broker, no live trading, and provides no investment advice."},
        {"title": "No build/deploy/release boundary", "content": "This project does not build, deploy, or release."},
        {"title": "Manual review statement", "content": "Manual review is strictly required."},
        {"title": "Final safety statement", "content": "Safety measures apply up to final layer."},
        {"title": "Closing governance super-binder recap", "content": "Closing governance super-binder covers all checkpoints."},
        {"title": "Post-Phase-100 reading order", "content": "Reading order after phase 100."},
        {"title": "Final boundary statement", "content": "This is not an official closeout. Manual review is required. No investment advice."}
    ]

def build_final_master_terminal_lock_rehearsal(project_root: Path, profile: LocalFinalClosingProfile) -> tuple[str, dict]:
    sections = build_final_master_terminal_lock_sections(project_root, profile)
    lines = ["# Final Master Terminal Lock Rehearsal\n"]
    for s in sections:
        lines.append(f"## {s['title']}\n{s['content']}\n")
    lines.append("Bu rapor offline/local final closing governance ve non-production seal rehearsal çıktısıdır; gerçek project lock, official constitution, official seal, official acceptance, legal/compliance approval, production approval, canlı sinyal, broker talimatı, model deployment veya yatırım tavsiyesi değildir.")
    text = "\n".join(lines)
    return text, summarize_final_master_terminal_lock(text)

def summarize_final_master_terminal_lock(text: str) -> dict:
    return {"length": len(text)}

def build_final_master_terminal_lock_index(profile: LocalFinalClosingProfile) -> tuple[pd.DataFrame, dict]:
    df = pd.DataFrame([{"index_id": "idx_1", "name": "Final Master Terminal Lock Index"}])
    return df, summarize_final_master_terminal_lock_index(df)

def summarize_final_master_terminal_lock_index(df: pd.DataFrame) -> dict:
    return {"total_items": len(df) if df is not None else 0}
