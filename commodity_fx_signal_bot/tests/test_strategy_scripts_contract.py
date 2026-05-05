import pytest


def test_script_imports():
    try:
        import scripts.run_strategy_batch_build
        import scripts.run_strategy_candidate_preview
        import scripts.run_strategy_pool_preview
        import scripts.run_strategy_status  # noqa: F401
    except Exception as e:
        pytest.fail(f"Script import failed: {e}")
