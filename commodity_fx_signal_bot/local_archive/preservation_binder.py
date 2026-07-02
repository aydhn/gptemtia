from pathlib import Path
import pandas as pd
from typing import Tuple, Dict
from .archive_config import LocalArchiveProfile

def build_long_horizon_preservation_binder(domain_df: pd.DataFrame, item_df: pd.DataFrame, snapshot_df: pd.DataFrame, manifest: Dict, risk_df: pd.DataFrame, profile: LocalArchiveProfile) -> Tuple[str, Dict]:
    text = f"# Long-Horizon Preservation Binder\n\nProfile: {profile.name}\nNOT a cloud backup."
    return text, {"binder_length_chars": len(text)}
