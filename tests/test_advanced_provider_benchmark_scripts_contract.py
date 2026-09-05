import subprocess
import sys
from pathlib import Path


def run_script(script_name: str) -> subprocess.CompletedProcess:
    root = Path(__file__).resolve().parent.parent
    cmd = [sys.executable, "-m", f"scripts.{script_name}"]
    return subprocess.run(cmd, cwd=str(root), capture_output=True, text=True)


def test_provider_benchmark_script_contracts():
    scripts = [
        "run_provider_benchmark_profile_registry",
        "run_provider_benchmark_metrics",
        "run_provider_coverage_capability_benchmark",
        "run_provider_quality_normalization_lineage_benchmark",
        "run_domain_provider_benchmarks",
        "run_cross_domain_provider_benchmark",
        "run_provider_benchmark_scoring",
        "run_provider_benchmark_health_check",
        "run_provider_benchmark_validation_report",
        "run_provider_benchmark_status",
    ]
    for sc in scripts:
        res = run_script(sc)
        assert res.returncode == 0, f"Script {sc} failed:\nSTDOUT: {res.stdout}\nSTDERR: {res.stderr}"
