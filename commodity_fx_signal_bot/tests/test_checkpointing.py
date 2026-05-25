import pytest
from pathlib import Path
import tempfile
import json
from performance.checkpointing import (
    build_checkpoint_key,
    create_checkpoint_manifest,
    save_checkpoint_manifest,
    load_checkpoint_manifest,
    calculate_checkpoint_progress,
    build_resume_plan_from_checkpoint
)

def test_build_checkpoint_key():
    k1 = build_checkpoint_key("mod", "run", 1)
    k2 = build_checkpoint_key("mod", "run", 1)
    assert k1 == k2
    assert len(k1) <= 16

def test_checkpoint_manifest():
    manifest = create_checkpoint_manifest("run1", "mod1", 100, 50, ["path1", "path2"])
    assert manifest["status"] == "in_progress"
    assert manifest["completed_items"] == 50
    assert len(manifest["checkpoint_paths"]) == 2

def test_save_load_manifest():
    with tempfile.TemporaryDirectory() as tmpdir:
        manifest = create_checkpoint_manifest("run1", "mod1", 100, 50, [])
        path = save_checkpoint_manifest(manifest, Path(tmpdir))

        assert path.exists()

        loaded = load_checkpoint_manifest(path)
        assert loaded["run_name"] == "run1"

def test_checkpoint_progress():
    manifest = create_checkpoint_manifest("run1", "mod1", 100, 50, [])
    assert calculate_checkpoint_progress(manifest) == 0.5

    manifest_empty = create_checkpoint_manifest("run1", "mod1", 0, 0, [])
    assert calculate_checkpoint_progress(manifest_empty) == 0.0

def test_build_resume_plan():
    manifest = create_checkpoint_manifest("run1", "mod1", 100, 50, [])
    df, summary = build_resume_plan_from_checkpoint(manifest)

    assert not df.empty
    assert df.iloc[0]["remaining"] == 50
    assert summary["can_resume"] == True
    assert summary["progress_pct"] == 50.0
