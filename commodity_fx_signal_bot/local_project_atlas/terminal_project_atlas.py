"""Terminal project atlas module."""
import pandas as pd
from pathlib import Path
from .atlas_config import LocalProjectAtlasProfile

def build_terminal_project_atlas(project_root: Path, profile: LocalProjectAtlasProfile) -> tuple[str, dict]:
    doc = """# Terminal Project Atlas
Bu atlas offline bir dokümantasyon katmanıdır. Legal evidence, compliance, production approval, live trading veya yatırım tavsiyesi DEGILDIR.

## Phase 1-93 Haritası
Tüm fazların birleşik görünümü.

## Final Boundary Statement
No real deployment, no real broker execution, no investment advice.
"""
    return doc, summarize_terminal_project_atlas(doc)

def build_terminal_project_atlas_sections(project_root: Path, profile: LocalProjectAtlasProfile) -> list[dict]:
    return [{"title": "Ana Hatlar"}]

def summarize_terminal_project_atlas(text: str) -> dict:
    return {"length": len(text)}

def save_terminal_project_atlas(text: str, output_path: Path) -> Path:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(text)
    return output_path
