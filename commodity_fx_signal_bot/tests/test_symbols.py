"""
Tests for symbol universe management.
"""

from config.symbols import (
    DEFAULT_SYMBOL_UNIVERSE,
    get_all_candidate_symbols,
    get_analysis_symbols,
    get_benchmark_symbols,
    get_enabled_symbols,
    get_paper_trade_symbols,
    get_symbols_by_data_source,
    summarize_universe,
    validate_symbol_universe,
)


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


def test_summarize_universe():
    summary = summarize_universe()
    assert "total" in summary
    assert "enabled" in summary
    assert "analysis_enabled" in summary
    assert "paper_trade_enabled" in summary
    assert "benchmark_enabled" in summary
    assert "by_asset_class" in summary
    assert "by_data_source" in summary
    assert "by_liquidity_tier" in summary


def test_get_analysis_symbols():
    symbols = get_analysis_symbols()
    assert isinstance(symbols, list)
    for spec in symbols:
        assert spec.analysis_enabled is True


def test_get_paper_trade_symbols():
    symbols = get_paper_trade_symbols()
    assert isinstance(symbols, list)
    for spec in symbols:
        assert spec.paper_trade_enabled is True


def test_get_benchmark_symbols():
    symbols = get_benchmark_symbols()
    assert isinstance(symbols, list)
    for spec in symbols:
        assert spec.benchmark_enabled is True


def test_get_symbols_by_data_source():
    symbols = get_symbols_by_data_source("yahoo")
    assert isinstance(symbols, list)
    for spec in symbols:
        assert spec.data_source == "yahoo"


def test_get_all_candidate_symbols():
    spec = DEFAULT_SYMBOL_UNIVERSE[0]  # Usually GC=F
    candidates = get_all_candidate_symbols(spec)
    assert candidates[0] == spec.symbol
    assert tuple(candidates[1:]) == spec.aliases


def test_get_default_timeframes_for_asset_class():
    from config.symbols import get_default_timeframes_for_asset_class

    tfs = get_default_timeframes_for_asset_class("metals")
    assert "4h" in tfs
    assert "1d" in tfs


def test_get_allowed_timeframes_for_symbol():
    from config.symbols import SymbolSpec, get_allowed_timeframes_for_symbol

    spec = SymbolSpec("TEST", "Test", "metals", "test", "USD")
    tfs = get_allowed_timeframes_for_symbol(spec)
    assert "4h" in tfs

    spec_pref = SymbolSpec(
        "TEST2", "Test2", "metals", "test", "USD", preferred_timeframes=("1d",)
    )
    tfs_pref = get_allowed_timeframes_for_symbol(spec_pref)
    assert tfs_pref == ("1d",)

    spec_excl = SymbolSpec(
        "TEST3", "Test3", "metals", "test", "USD", excluded_timeframes=("4h",)
    )
    tfs_excl = get_allowed_timeframes_for_symbol(spec_excl)
    assert "4h" not in tfs_excl
    assert "1d" in tfs_excl
