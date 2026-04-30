import pytest


def test_run_trend_feature_preview_importable():
    import scripts.run_trend_feature_preview as script
    assert hasattr(script, "parse_args")
    assert hasattr(script, "main")


def test_run_trend_batch_build_importable():
    import scripts.run_trend_batch_build as script
    assert hasattr(script, "parse_args")
    assert hasattr(script, "main")


def test_run_trend_event_preview_importable():
    import scripts.run_trend_event_preview as script
    assert hasattr(script, "parse_args")
    assert hasattr(script, "main")


def test_run_trend_status_importable():
    import scripts.run_trend_status as script
    assert hasattr(script, "parse_args")
    assert hasattr(script, "main")
