import pytest
from config.symbols import SymbolSpec
from asset_profiles.asset_class_registry import (
    group_symbols_by_asset_class,
    get_group_members,
    filter_symbols_for_group_analysis,
)


@pytest.fixture
def mock_symbols():
    return [
        SymbolSpec("TEST1", "T1", "metals", "sub", "USD"),
        SymbolSpec("TEST2", "T2", "metals", "sub", "USD"),
        SymbolSpec("TEST3", "T3", "metals", "sub", "USD"),
        SymbolSpec("BENCH1", "B1", "benchmark", "sub", "USD", benchmark_enabled=True),
        SymbolSpec("MACRO1", "M1", "macro", "sub", "USD"),
    ]


def test_group_symbols_by_asset_class(mock_symbols):
    grouped = group_symbols_by_asset_class(mock_symbols)
    assert "metals" in grouped
    assert len(grouped["metals"]) == 3
    assert "benchmark" in grouped
    assert "macro" in grouped


def test_get_group_members(mock_symbols):
    members = get_group_members(mock_symbols, "metals")
    assert len(members) == 3
    assert all(s.asset_class == "metals" for s in members)


def test_filter_symbols_for_group_analysis(mock_symbols):
    filtered = filter_symbols_for_group_analysis(mock_symbols, min_members=3)
    assert "metals" in filtered
    assert len(filtered["metals"]) == 3

    # Benchmarks and macro should be excluded
    assert "benchmark" not in filtered
    assert "macro" not in filtered

    # Should exclude if min_members not met
    filtered2 = filter_symbols_for_group_analysis(mock_symbols, min_members=4)
    assert "metals" not in filtered2
