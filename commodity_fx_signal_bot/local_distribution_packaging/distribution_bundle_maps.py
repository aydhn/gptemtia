import pandas as pd
from pathlib import Path
from .packaging_config import LocalDistributionPackagingProfile

def build_distribution_bundle_folder_map(profile: LocalDistributionPackagingProfile) -> tuple[pd.DataFrame, dict]:
    df = pd.DataFrame([{"folder": "dist/", "type": "rehearsal"}])
    return df, summarize_distribution_bundle_map(df)

def build_distribution_bundle_source_registry(project_root: Path, profile: LocalDistributionPackagingProfile) -> tuple[pd.DataFrame, dict]:
    df = pd.DataFrame([{"source": "src/", "included": True}])
    return df, summarize_distribution_bundle_map(df)

def build_distribution_bundle_output_registry(profile: LocalDistributionPackagingProfile) -> tuple[pd.DataFrame, dict]:
    df = pd.DataFrame([{"output": "dist_bundle/", "status": "rehearsal"}])
    return df, summarize_distribution_bundle_map(df)

def build_distribution_bundle_safety_boundary_registry(profile: LocalDistributionPackagingProfile) -> tuple[pd.DataFrame, dict]:
    df = pd.DataFrame([{"boundary": "No real archive", "enforced": True}])
    return df, summarize_distribution_bundle_map(df)

def summarize_distribution_bundle_map(df: pd.DataFrame) -> dict:
    return {"status": "generated", "rows": len(df)}
