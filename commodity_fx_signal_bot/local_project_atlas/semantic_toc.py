"""Offline semantic table of contents module."""
import pandas as pd
from pathlib import Path
from .atlas_config import LocalProjectAtlasProfile

def build_offline_semantic_table_of_contents(project_root: Path, profile: LocalProjectAtlasProfile) -> tuple[str, dict]:
    doc = """# Offline Semantic Table of Contents
This is a documented map of the project structure. It is NOT vector/embedding search.
## Modül Aileleri
- core
- ml
- data
- reports
## Rapor Aileleri
- output
## Manuel Review Noktaları
- Her phase geçişi
"""
    return doc, summarize_semantic_toc(doc)

def build_semantic_toc_sections(profile: LocalProjectAtlasProfile) -> list[dict]:
    return [{"section": "Modüller"}, {"section": "Raporlar"}]

def build_semantic_toc_registry(profile: LocalProjectAtlasProfile) -> tuple[pd.DataFrame, dict]:
    df = pd.DataFrame(build_semantic_toc_sections(profile))
    return df, summarize_semantic_toc_registry(df)

def summarize_semantic_toc(text: str) -> dict:
    return {"length": len(text)}

def summarize_semantic_toc_registry(df: pd.DataFrame) -> dict:
    return {"sections": len(df)}
