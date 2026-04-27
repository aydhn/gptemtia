"""
Tests for symbol universe management.
"""
import pytest
from config.symbols import DEFAULT_SYMBOL_UNIVERSE, get_enabled_symbols, validate_symbol_universe

def test_universe_not_empty():
    assert len(DEFAULT_SYMBOL_UNIVERSE) > 0

def test_no_duplicate_symbols():
    is_valid, errors = validate_symbol_universe()
    assert is_valid is True, f"Validation failed with errors: {errors}"
    assert len(errors) == 0

def test_symbol_spec_has_required_fields():
    for spec in DEFAULT_SYMBOL_UNIVERSE:
        assert hasattr(spec, "symbol")
        assert hasattr(spec, "name")
        assert hasattr(spec, "asset_class")
        assert hasattr(spec, "sub_class")
        assert hasattr(spec, "currency")

        assert spec.symbol != ""
        assert spec.name != ""

def test_get_enabled_symbols():
    enabled = get_enabled_symbols()
    assert isinstance(enabled, list)
    for spec in enabled:
        assert spec.enabled is True
