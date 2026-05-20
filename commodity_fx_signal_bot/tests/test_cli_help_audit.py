from pathlib import Path
from devtools.cli_help_audit import (
    check_script_has_main_guard, check_script_has_argparse, audit_cli_help
)
import pandas as pd

def test_check_main_guard_argparse(tmp_path):
    p = tmp_path / "test.py"
    p.write_text("import argparse\nif __name__ == '__main__':\n  pass")
    assert check_script_has_main_guard(p)["has_main_guard"] is True
    assert check_script_has_argparse(p)["has_argparse"] is True

def test_audit_cli_help(tmp_path):
    df, summary = audit_cli_help(tmp_path)
    assert "total" in summary
