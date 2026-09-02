
import pandas as pd
from pathlib import Path
from .hardening_config import LocalHardeningProfile

def build_rc_freeze_manifest_items(project_root: Path, profile: LocalHardeningProfile) -> tuple[pd.DataFrame, dict]: return pd.DataFrame(), {}
def validate_rc_freeze_manifest_safety(manifest: dict, profile: LocalHardeningProfile) -> dict: return {}
def summarize_rc_freeze_manifest(manifest: dict, item_df: pd.DataFrame) -> dict: return {"total": 0}
def build_rc_dry_run_freeze_manifest(project_root: Path, profile: LocalHardeningProfile) -> tuple[dict, dict]:
    manifest = {"status": "rc_dry_run"}
    return manifest, summarize_rc_freeze_manifest(manifest, pd.DataFrame())
