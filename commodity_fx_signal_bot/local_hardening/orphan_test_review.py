
import pandas as pd
from pathlib import Path
from .hardening_config import LocalHardeningProfile

def discover_test_files_for_orphan_review(project_root: Path, profile: LocalHardeningProfile) -> pd.DataFrame: return pd.DataFrame()
def map_tests_to_source_modules(test_df: pd.DataFrame, project_root: Path) -> pd.DataFrame: return pd.DataFrame()
def summarize_orphan_test_candidates(test_df: pd.DataFrame) -> dict: return {"total": len(test_df)}
def build_orphan_test_candidate_report(project_root: Path, profile: LocalHardeningProfile) -> tuple[pd.DataFrame, dict]:
    df = pd.DataFrame()
    return df, summarize_orphan_test_candidates(df)
