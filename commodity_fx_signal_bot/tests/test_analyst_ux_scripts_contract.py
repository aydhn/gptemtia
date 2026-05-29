import pytest
import subprocess
from pathlib import Path

def test_analyst_ux_scripts():
    root = Path(__file__).resolve().parent.parent
    scripts = [
        "scripts/run_ux_alias_report.py",
        "scripts/run_prompt_pack_report.py",
        "scripts/run_productivity_checklist.py",
        "scripts/run_analyst_task_board.py",
        "scripts/run_operator_productivity_status.py"
    ]

    for script in scripts:
        script_path = root / script
        assert script_path.exists()

        # Test help command to ensure no immediate crash and arg parsing works
        result = subprocess.run(["python", str(script_path), "--help"], capture_output=True, text=True)
        assert result.returncode == 0
        assert "usage:" in result.stdout.lower()

    # Special test for suggestions which requires --query
    sugg_script = root / "scripts/run_safe_command_suggestions.py"
    result = subprocess.run(["python", str(sugg_script), "--help"], capture_output=True, text=True)
    assert result.returncode == 0
    assert "usage:" in result.stdout.lower()
