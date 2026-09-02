"""
Reproducibility Pointers.
"""
import pandas as pd
from pathlib import Path
from local_archival.archival_config import LocalArchivalProfile

def build_default_reproducibility_pointers(profile: LocalArchivalProfile) -> pd.DataFrame:
    pointers = [
        {"pointer": "README.md", "type": "docs"},
        {"pointer": "INSTALLATION.md", "type": "docs"},
        {"pointer": "CONFIGURATION.md", "type": "docs"},
        {"pointer": "SAFE_USAGE_GUIDE.md", "type": "docs"},
        {"pointer": "PROJECT_COMPLETION_DOSSIER.md", "type": "docs"},
        {"pointer": "FINAL_DELIVERY_BUNDLE_MANIFEST.md", "type": "docs"},
        {"pointer": "INDEPENDENT_REVIEWER_PACK.md", "type": "docs"},
        {"pointer": "RC_DRY_RUN_FREEZE_MANIFEST.md", "type": "docs"},
        {"pointer": "acceptance evidence binder", "type": "docs"},
        {"pointer": "final hash catalog", "type": "archival"},
        {"pointer": "provenance lockfile", "type": "archival"}
    ]
    return pd.DataFrame(pointers)

def build_reproducibility_pointer_registry(project_root: Path, profile: LocalArchivalProfile) -> tuple[pd.DataFrame, dict]:
    df = build_default_reproducibility_pointers(profile)
    return df, summarize_reproducibility_pointers(df)

def summarize_reproducibility_pointers(pointer_df: pd.DataFrame) -> dict:
    return {"total_pointers": len(pointer_df) if pointer_df is not None else 0}
