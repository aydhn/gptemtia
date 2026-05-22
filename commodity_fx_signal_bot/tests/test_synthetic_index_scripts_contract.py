import subprocess
import sys

def test_script_imports():
    # If it can be imported, basic syntax is okay
    import scripts.run_synthetic_benchmark_report
    import scripts.run_composite_index_report
    import scripts.run_relative_strength_report
    import scripts.run_universe_rotation_report
    import scripts.run_leadership_laggard_report
    import scripts.run_synthetic_index_status

    assert hasattr(scripts.run_synthetic_benchmark_report, "main")
    assert hasattr(scripts.run_composite_index_report, "main")
    assert hasattr(scripts.run_relative_strength_report, "main")
    assert hasattr(scripts.run_universe_rotation_report, "main")
    assert hasattr(scripts.run_leadership_laggard_report, "main")
    assert hasattr(scripts.run_synthetic_index_status, "main")

def test_script_help():
    # Run one script with --help to ensure argparse works
    result = subprocess.run(
        [sys.executable, "-m", "scripts.run_synthetic_benchmark_report", "--help"],
        capture_output=True,
        text=True,
        cwd="."
    )
    assert result.returncode == 0
    assert "Run synthetic benchmark report" in result.stdout
