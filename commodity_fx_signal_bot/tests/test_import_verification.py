from portable_packaging.import_verification import (
    build_core_module_list,
    verify_module_import,
    verify_core_module_imports,
    verify_pipeline_imports
)

def test_import_verification(tmp_path):
    assert len(build_core_module_list()) > 0

    res = verify_module_import("os", tmp_path)
    assert res["importable"]

    df, _ = verify_core_module_imports(tmp_path)
    assert not df.empty

    df, _ = verify_pipeline_imports(tmp_path)
    assert not df.empty
