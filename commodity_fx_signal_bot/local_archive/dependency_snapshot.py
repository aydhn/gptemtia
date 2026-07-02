from pathlib import Path
import pandas as pd
from typing import Tuple, Dict
from .archive_config import LocalArchiveProfile

def build_archive_dependency_snapshot_summary(project_root: Path, profile: LocalArchiveProfile) -> Tuple[pd.DataFrame, Dict]:
    sources = ["requirements.txt", "requirements-dev.txt", "pyproject.toml", ".env.example"]
    found = []
    for s in sources:
        p = project_root / s
        if p.exists():
            found.append({"source_file": s, "status": "found"})
        else:
            found.append({"source_file": s, "status": "missing"})
    df = pd.DataFrame(found)
    return df, {"total_sources_checked": len(df)}
