import pandas as pd
from pathlib import Path
from local_delivery.delivery_config import LocalDeliveryProfile

def build_recipient_orientation_sections(profile: LocalDeliveryProfile) -> list[dict]:
    return [
        {"title": "Where to Start", "content": "Start with README and SAFE_USAGE_GUIDE."},
        {"title": "First 60 Minutes", "content": "Review the manifest and indices."}
    ]

def build_recipient_orientation_guide(project_root: Path, profile: LocalDeliveryProfile) -> tuple[str, dict]:
    sections = build_recipient_orientation_sections(profile)
    text = "\n\n".join([f"# {s['title']}\n{s['content']}" for s in sections])
    return text, summarize_recipient_orientation_guide(text)

def summarize_recipient_orientation_guide(text: str) -> dict:
    return {"length": len(text)}
