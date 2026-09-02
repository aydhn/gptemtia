import pandas as pd
from typing import Tuple, Dict
from pathlib import Path
from .synthesis_config import LocalSynthesisProfile


def classify_command_catalog_safety(command: str) -> dict: return {"safe": True}
def detect_forbidden_command_catalog_terms(command: str) -> list[str]: return []

def build_final_command_catalog(project_root: Path, profile: LocalSynthesisProfile) -> Tuple[pd.DataFrame, Dict]:
    df = pd.DataFrame(columns=["item", "info"])
    return df, summarize_final_command_catalog(df)

def summarize_final_command_catalog(df: pd.DataFrame) -> Dict:
    return {"count": len(df)}
