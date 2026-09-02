import pandas as pd
from typing import Tuple, Dict
from pathlib import Path
from .synthesis_config import LocalSynthesisProfile

def build_final_operator_navigation_guide(project_root: Path, profile: LocalSynthesisProfile) -> Tuple[str, Dict]:
    return "# Operator Guide\nRead-only manual review.", {"length": 50}

def build_final_stakeholder_navigation_guide(project_root: Path, profile: LocalSynthesisProfile) -> Tuple[str, Dict]:
    return "# Stakeholder Guide\nRead-only.", {"length": 50}

def build_final_developer_navigation_guide(project_root: Path, profile: LocalSynthesisProfile) -> Tuple[str, Dict]:
    return "# Developer Guide\nRead-only.", {"length": 50}

def build_navigation_index(project_root: Path, profile: LocalSynthesisProfile) -> Tuple[pd.DataFrame, Dict]:
    df = pd.DataFrame(columns=["guide", "path"])
    return df, summarize_navigation_guides(df)

def summarize_navigation_guides(index_df: pd.DataFrame) -> Dict:
    return {"count": len(index_df)}
