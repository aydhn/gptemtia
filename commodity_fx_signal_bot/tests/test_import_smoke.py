from devtools.import_smoke import list_project_packages, import_module_safely, run_import_smoke_test

def test_list_project_packages():
    assert len(list_project_packages(None)) > 0

def test_import_module_safely():
    res = import_module_safely("os")
    assert res["success"] is True
    res2 = import_module_safely("nonexistent_module_for_test")
    assert res2["success"] is False

def test_run_import_smoke_test():
    df, summary = run_import_smoke_test(["os"])
    assert summary["total"] == 1
