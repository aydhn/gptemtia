"""
Backup, packaging, and secrets timeline module.
"""

from pathlib import Path
import pandas as pd

from local_timeline.timeline_config import LocalTimelineProfile

def classify_backup_packaging_secrets_event(path: Path, project_root: Path) -> str:
    rel = path.relative_to(project_root).as_posix()
    if "backup" in rel:
        return "backup_event"
    if "packaging" in rel:
        return "packaging_event"
    if "secret" in rel:
        return "secrets_event"
    return "security_event"

def build_recovery_security_activity_summary(df: pd.DataFrame) -> pd.DataFrame:
    if df.empty:
        return pd.DataFrame()

    if 'relative_path' not in df:
        return pd.DataFrame()

    df['category'] = df['relative_path'].apply(lambda x: classify_backup_packaging_secrets_event(Path(x), Path(".")))
    summary = df.groupby('category').size().reset_index(name='event_count')
    return summary

def build_backup_packaging_secrets_event_timeline(project_root: Path, profile: LocalTimelineProfile) -> tuple[pd.DataFrame, dict]:
    return pd.DataFrame(), {"status": "extracted in pipeline"}

def summarize_backup_packaging_secrets_timeline(df: pd.DataFrame) -> dict:
    if df.empty:
        return {"total_events": 0}
    return {
        "total_events": len(df),
        "unique_files": df['relative_path'].nunique() if 'relative_path' in df else 0
    }
