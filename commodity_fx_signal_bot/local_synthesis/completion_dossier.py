import pandas as pd
from typing import Tuple, Dict, List
from pathlib import Path
from .synthesis_config import LocalSynthesisProfile
from .synthesis_models import FinalBinderSection

def build_completion_dossier_sections(family_df: pd.DataFrame, capability_df: pd.DataFrame, boundary_df: pd.DataFrame, output_df: pd.DataFrame) -> List[FinalBinderSection]:
    return []

def save_project_completion_dossier(text: str, output_path: Path) -> Path:
    output_path.write_text(text, encoding="utf-8")
    return output_path

def build_project_completion_dossier(family_df: pd.DataFrame, capability_df: pd.DataFrame, boundary_df: pd.DataFrame, output_df: pd.DataFrame, profile: LocalSynthesisProfile) -> Tuple[str, Dict]:
    text = "# Project Completion Dossier\nOffline/local only. No investment advice. No production release."
    return text, summarize_project_completion_dossier(text)

def summarize_project_completion_dossier(text: str) -> Dict:
    return {"length": len(text)}
