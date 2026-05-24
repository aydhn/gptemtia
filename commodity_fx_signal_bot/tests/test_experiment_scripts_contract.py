import pytest

def test_run_hypothesis_registry_report_importable():
    try:
        import scripts.run_hypothesis_registry_report
    except Exception as e:
        pytest.fail(f"Could not import run_hypothesis_registry_report: {e}")

def test_run_experiment_tracking_report_importable():
    try:
        import scripts.run_experiment_tracking_report
    except Exception as e:
        pytest.fail(f"Could not import run_experiment_tracking_report: {e}")

def test_run_research_version_report_importable():
    try:
        import scripts.run_research_version_report
    except Exception as e:
        pytest.fail(f"Could not import run_research_version_report: {e}")

def test_run_ablation_study_report_importable():
    try:
        import scripts.run_ablation_study_report
    except Exception as e:
        pytest.fail(f"Could not import run_ablation_study_report: {e}")

def test_run_experiment_comparison_report_importable():
    try:
        import scripts.run_experiment_comparison_report
    except Exception as e:
        pytest.fail(f"Could not import run_experiment_comparison_report: {e}")

def test_run_experiment_leaderboard_importable():
    try:
        import scripts.run_experiment_leaderboard
    except Exception as e:
        pytest.fail(f"Could not import run_experiment_leaderboard: {e}")

def test_run_experiment_status_importable():
    try:
        import scripts.run_experiment_status
    except Exception as e:
        pytest.fail(f"Could not import run_experiment_status: {e}")
