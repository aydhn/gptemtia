from pathlib import Path
from maintenance.safe_file_ops import validate_file_op_safety, execute_delete_file

def test_safe_file_ops(tmp_path):
    root = tmp_path

    assert validate_file_op_safety(Path("README.md"), root)["safe"] is False
    assert validate_file_op_safety(Path("test.py"), root)["safe"] is False
    assert validate_file_op_safety(Path("tests/test_foo.py"), root)["safe"] is False
    assert validate_file_op_safety(Path("data.csv"), root)["safe"] is True

    test_file = root / "test.csv"
    test_file.touch()

    # Should not delete if allow_delete is False
    res = execute_delete_file(test_file, root, allow_delete=False)
    assert res["success"] is False
    assert test_file.exists()

    # Should delete if allow_delete is True and safe
    res = execute_delete_file(test_file, root, allow_delete=True)
    assert res["success"] is True
    assert not test_file.exists()
