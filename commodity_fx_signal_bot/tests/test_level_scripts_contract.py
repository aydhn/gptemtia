import pytest


def test_scripts_import():
    import scripts.run_level_candidate_preview
    import scripts.run_level_batch_build
    import scripts.run_reward_risk_preview
    import scripts.run_level_status

    assert True
