import subprocess
import sys
from pathlib import Path


def run_script(script_name: str) -> subprocess.CompletedProcess:
    root = Path(__file__).resolve().parent.parent
    cmd = [sys.executable, "-m", f"scripts.{script_name}"]
    return subprocess.run(cmd, cwd=str(root), capture_output=True, text=True)


def test_script_contracts():
    scripts = [
        "run_data_normalization_profile_registry",
        "run_normalization_rule_registry",
        "run_symbol_normalization_enforcement",
        "run_time_frequency_unit_normalization",
        "run_news_calendar_normalization",
        "run_normalized_output_manifest",
        "run_data_normalization_scoring",
        "run_data_normalization_health_check",
        "run_data_normalization_validation_report",
        "run_data_normalization_status",
    ]
    for sc in scripts:
        res = run_script(sc)
        assert res.returncode == 0, f"Script {sc} failed:\nSTDOUT: {res.stdout}\nSTDERR: {res.stderr}"
