import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent))
from pathlib import Path
from documentation.doc_consistency import (
    check_phase_log_consistency,
    check_readme_doc_consistency,
    check_script_reference_consistency,
    check_module_map_consistency
)

def test_check_phase_log_consistency(tmp_path):
    phase_log = tmp_path / "docs" / "PHASE_LOG.md"
    phase_log.parent.mkdir()
    phase_log.write_text("## Phase 54")

    df = check_phase_log_consistency(tmp_path, 54)
    assert "passed" in df.columns

def test_check_readme_doc_consistency(tmp_path):
    readme = tmp_path / "README.md"
    readme.write_text("This has Documentation Pack mention.")

    df = check_readme_doc_consistency(tmp_path)
    assert "passed" in df.columns

def test_check_script_reference_consistency(tmp_path):
    df = check_script_reference_consistency(tmp_path)
    assert "passed" in df.columns

def test_check_module_map_consistency(tmp_path):
    df = check_module_map_consistency(tmp_path)
    assert "passed" in df.columns
