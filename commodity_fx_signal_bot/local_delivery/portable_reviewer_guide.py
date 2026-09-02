import pandas as pd
from pathlib import Path
from local_delivery.delivery_config import LocalDeliveryProfile

def build_portable_reviewer_guide_sections(project_root: Path, index_df: pd.DataFrame, profile: LocalDeliveryProfile) -> list[dict]:
    return [
        {"title": "Purpose and Scope", "content": "This guide provides an overview of the local delivery package."},
        {"title": "Not a Real Archive", "content": "This is not a real zip or archive file. No data is transferred."},
        {"title": "Review Order", "content": "Follow the reading order in the index."},
        {"title": "What NOT to do", "content": "Do not attempt to upload to cloud or publish package."}
    ]

def build_portable_reviewer_archive_guide(project_root: Path, index_df: pd.DataFrame, profile: LocalDeliveryProfile) -> tuple[str, dict]:
    sections = build_portable_reviewer_guide_sections(project_root, index_df, profile)
    text = "\n\n".join([f"# {s['title']}\n{s['content']}" for s in sections])
    return text, summarize_portable_reviewer_archive_guide(text)

def save_portable_reviewer_archive_guide(text: str, output_path: Path) -> Path:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(text)
    return output_path

def summarize_portable_reviewer_archive_guide(text: str) -> dict:
    return {"length": len(text)}
