import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent))
import pandas as pd
from documentation.doc_index_builder import (
    build_documentation_index,
    build_script_reference,
    build_output_reference,
    build_safe_command_reference,
    build_module_map
)

def test_build_documentation_index():
    idx = build_documentation_index(pd.DataFrame())
    assert "Kullanıcı Kılavuzu" in idx

def test_build_script_reference(tmp_path):
    scripts_dir = tmp_path / "scripts"
    scripts_dir.mkdir()
    (scripts_dir / "run_test.py").touch()

    ref = build_script_reference(tmp_path)
    assert "run_test" in ref

def test_build_output_reference(tmp_path):
    ref = build_output_reference(tmp_path)
    assert "data/lake" in ref

def test_build_safe_command_reference(tmp_path):
    ref = build_safe_command_reference(tmp_path)
    assert "make setup" in ref
    assert "live" not in ref

def test_build_module_map(tmp_path):
    ref = build_module_map(tmp_path)
    assert "data" in ref
