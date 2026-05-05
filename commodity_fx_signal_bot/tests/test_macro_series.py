from macro.macro_series import (
    get_macro_series_by_source,
    get_macro_series_spec,
    validate_macro_series_specs,
)


def test_validate_macro_series_specs():
    validate_macro_series_specs()


def test_get_macro_series_spec():
    s = get_macro_series_spec("TR_CPI")
    assert s.code == "TR_CPI"
    assert s.source == "evds"


def test_get_macro_series_by_source():
    series = get_macro_series_by_source("fred")
    assert any(s.code == "US_CPI" for s in series)
