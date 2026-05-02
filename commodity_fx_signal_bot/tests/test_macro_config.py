import pytest

from macro.macro_config import (
    MacroProfile,
    get_default_macro_profile,
    get_macro_profile,
    validate_macro_profiles,
)


def test_validate_macro_profiles():
    # Should not raise exception
    validate_macro_profiles()


def test_get_default_macro_profile():
    p = get_default_macro_profile()
    assert isinstance(p, MacroProfile)
    assert p.name == "turkey_inflation_fx"


def test_unknown_profile():
    with pytest.raises(ValueError):
        get_macro_profile("unknown_profile")
