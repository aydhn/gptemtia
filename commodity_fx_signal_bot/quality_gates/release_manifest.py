import pandas as pd
from pathlib import Path
from .quality_config import QualityGateProfile
from .quality_models import QualityCheckResult, ReleaseCandidateManifest

def build_release_candidate_manifest(profile: QualityGateProfile, quality_results: list[QualityCheckResult], project_root: Path) -> ReleaseCandidateManifest:
    return ReleaseCandidateManifest(
        rc_id="mock_rc_id",
        profile_name=profile.name,
        created_at_utc="2024-05-25T00:00:00Z",
        status_label="rc_ready_offline",
        quality_score=1.0,
        included_modules=[],
        included_reports=[],
        included_manifests=[],
        checklist_summary={},
        warnings=[],
    )

def build_release_artifact_list(project_root: Path) -> pd.DataFrame:
    return pd.DataFrame()

def build_release_manifest_json(manifest: ReleaseCandidateManifest, artifact_df: pd.DataFrame) -> dict:
    return {}

def save_release_candidate_manifest(manifest_json: dict, output_path: Path) -> Path:
    return output_path

def summarize_release_manifest(manifest_json: dict) -> dict:
    return {}
