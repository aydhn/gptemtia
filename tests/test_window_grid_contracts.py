from advanced_feature_grid.window_grid_contracts import (
    build_window_grid_contract_registry,
    validate_window_grid,
    summarize_window_grid_contracts,
)


def test_window_grid_contracts():
    df, summary = build_window_grid_contract_registry()
    assert not df.empty
    assert summary["total_contracts"] >= 8
    assert summary["all_strictly_backward_looking"] is True
    assert summary["non_signal"] is True

    # Validate window grid function
    res_valid = validate_window_grid([5, 10, 20, 50], min_window=2, max_window=200)
    assert res_valid["valid"] is True
    assert res_valid["sanitized_windows"] == [5, 10, 20, 50]

    # Validate out of bounds
    res_invalid = validate_window_grid([1, 5, 500], min_window=2, max_window=100)
    assert res_invalid["valid"] is False
    assert len(res_invalid["errors"]) == 2
