import subprocess
import sys


def test_run_sizing_candidate_preview_help():
    result = subprocess.run(
        [sys.executable, "scripts/run_sizing_candidate_preview.py", "-h"],
        capture_output=True,
        text=True,
        cwd=".",
    )
    assert result.returncode == 0
    assert "Preview Sizing Candidates for a Symbol" in result.stdout


def test_run_sizing_batch_build_help():
    result = subprocess.run(
        [sys.executable, "scripts/run_sizing_batch_build.py", "-h"],
        capture_output=True,
        text=True,
        cwd=".",
    )
    assert result.returncode == 0
    assert "Batch Build Sizing Candidates" in result.stdout


def test_run_sizing_pool_preview_help():
    result = subprocess.run(
        [sys.executable, "scripts/run_sizing_pool_preview.py", "-h"],
        capture_output=True,
        text=True,
        cwd=".",
    )
    assert result.returncode == 0
    assert "Preview Sizing Pool" in result.stdout


def test_run_sizing_status_help():
    result = subprocess.run(
        [sys.executable, "scripts/run_sizing_status.py", "-h"],
        capture_output=True,
        text=True,
        cwd=".",
    )
    assert result.returncode == 0
    assert "Check Sizing Status" in result.stdout
