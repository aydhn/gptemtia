from pathlib import Path
import pandas as pd
from typing import Tuple, Dict
from .archive_config import LocalArchiveProfile

def build_security_sensitive_archive_boundary_report(project_root: Path, profile: LocalArchiveProfile) -> Tuple[pd.DataFrame, Dict]:
    records = []
    for f in project_root.glob(".env*"):
        try: records.append({"relative_path": str(f.relative_to(project_root)), "boundary_status": "out_of_bounds_sensitive"})
        except ValueError: pass
    for pattern in ["*.key", "*.pem"]:
        for f in project_root.rglob(pattern):
            if f.is_file():
                try: records.append({"relative_path": str(f.relative_to(project_root)), "boundary_status": "out_of_bounds_sensitive"})
                except ValueError: pass
    df = pd.DataFrame(records)
    return df, {"out_of_bounds_items": len(df)}
