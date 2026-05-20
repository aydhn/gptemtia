from devtools.test_matrix import discover_tests, infer_test_category, infer_related_module, build_test_matrix, export_test_matrix_markdown

def test_infer_test_category():
    assert infer_test_category("test_data.py") == "data"
    assert infer_test_category("test_unknown.py") == "unknown"

def test_infer_related_module():
    assert infer_related_module("test_config.py") == "config"

def test_build_test_matrix(tmp_path):
    df, summary = build_test_matrix(tmp_path)
    assert "total_test_files" in summary
    assert isinstance(export_test_matrix_markdown(df), str)
