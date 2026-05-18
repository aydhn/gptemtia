import pytest

from observability.error_taxonomy import (
    list_error_definitions,
    get_error_definition,
    classify_exception,
    build_error_taxonomy_report
)

def test_list_error_definitions():
    defs = list_error_definitions()
    assert len(defs) > 0
    assert any(d.error_code == "DATA_001" for d in defs)

def test_get_error_definition():
    d = get_error_definition("DATA_001")
    assert d.error_code == "DATA_001"
    assert d.category == "data_error"

    # Unknown code should return SYS_000
    unknown = get_error_definition("XYZ_999")
    assert unknown.error_code == "SYS_000"

def test_classify_exception():
    try:
        raise FileNotFoundError("test_file.txt missing")
    except Exception as e:
        info = classify_exception(e)
        assert info["error_code"] == "PATH_001"
        assert info["category"] == "io_error"

    try:
        raise ValueError("Invalid config xyz")
    except Exception as e:
        info = classify_exception(e)
        assert info["error_code"] == "CFG_002"

    try:
        raise RuntimeError("Something bad happened")
    except Exception as e:
        info = classify_exception(e)
        assert info["error_code"] == "SYS_000"
        assert info["exception_type"] == "RuntimeError"

def test_build_error_taxonomy_report():
    df, summary = build_error_taxonomy_report()
    assert not df.empty
    assert "error_code" in df.columns
    assert summary["total_errors_defined"] > 0
    assert "data_error" in summary["by_category"]
