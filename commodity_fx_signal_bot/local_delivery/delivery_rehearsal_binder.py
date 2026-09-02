import pandas as pd
from pathlib import Path
from local_delivery.delivery_config import LocalDeliveryProfile

def build_delivery_rehearsal_sections(
    manifest: dict,
    index_df: pd.DataFrame,
    checklist_df: pd.DataFrame,
    risk_df: pd.DataFrame,
) -> list[dict]:
    return [
        {"title": "Purpose and Scope", "content": "Delivery Rehearsal Binder content."},
        {"title": "Not a Real Delivery", "content": "This is not an official handoff."}
    ]

def build_delivery_rehearsal_binder(
    manifest: dict,
    index_df: pd.DataFrame,
    checklist_df: pd.DataFrame,
    risk_df: pd.DataFrame,
    profile: LocalDeliveryProfile,
) -> tuple[str, dict]:
    sections = build_delivery_rehearsal_sections(manifest, index_df, checklist_df, risk_df)
    text = "\n\n".join([f"# {s['title']}\n{s['content']}" for s in sections])
    return text, summarize_delivery_rehearsal_binder(text)

def save_delivery_rehearsal_binder(text: str, output_path: Path) -> Path:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(text)
    return output_path

def summarize_delivery_rehearsal_binder(text: str) -> dict:
    return {"length": len(text)}
