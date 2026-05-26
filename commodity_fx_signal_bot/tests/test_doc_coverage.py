import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent))
from documentation.doc_coverage import (
    build_expected_documentation_matrix,
    check_module_documentation_coverage,
    check_script_documentation_coverage,
    check_output_documentation_coverage
)
from pathlib import Path

def test_expected_matrix_not_empty():
    matrix = build_expected_documentation_matrix()
    assert not matrix.empty
    assert len(matrix) >= 28

def test_check_module_documentation_coverage(tmp_path):
    readme = tmp_path / "README.md"
    readme.write_text("data features ml")

    df = check_module_documentation_coverage(tmp_path)
    assert not df.empty

    data_status = df[df["module_name"] == "data"]["status"].iloc[0]
    assert data_status == "covered"

def test_check_script_documentation_coverage(tmp_path):
    df = check_script_documentation_coverage(tmp_path)
    assert df.empty

def test_check_output_documentation_coverage(tmp_path):
    df = check_output_documentation_coverage(tmp_path)
    assert df.empty
