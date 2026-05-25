import pandas as pd
from pathlib import Path
from quality_gates.quality_config import QualityGateProfile
from quality_gates.quality_models import ReleaseCandidateManifest
from quality_gates.release_manifest import (
    build_release_candidate_manifest,
    build_release_artifact_list,
    build_release_manifest_json,
    save_release_candidate_manifest,
    summarize_release_manifest
)

def test_build_release_candidate_manifest():
    profile = QualityGateProfile(name="mock", description="mock")
    manifest = build_release_candidate_manifest(profile, [], Path("."))
    assert isinstance(manifest, ReleaseCandidateManifest)
    assert manifest.status_label == "rc_ready_offline"
    assert manifest.status_label != "production_ready"

def test_build_release_artifact_list():
    df = build_release_artifact_list(Path("."))
    assert isinstance(df, pd.DataFrame)

def test_build_release_manifest_json():
    profile = QualityGateProfile(name="mock", description="mock")
    manifest = build_release_candidate_manifest(profile, [], Path("."))
    j = build_release_manifest_json(manifest, pd.DataFrame())
    assert isinstance(j, dict)

def test_save_release_candidate_manifest():
    path = save_release_candidate_manifest({}, Path("mock.json"))
    assert path == Path("mock.json")

def test_summarize_release_manifest():
    summary = summarize_release_manifest({})
    assert isinstance(summary, dict)
