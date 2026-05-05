import pytest


def test_scripts_importable():
    import scripts.run_signal_candidate_preview
    import scripts.run_signal_batch_build
    import scripts.run_signal_pool_preview
    import scripts.run_signal_status
