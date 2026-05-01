import pytest


def test_divergence_feature_preview_importable():
    from scripts.run_divergence_feature_preview import main

    assert callable(main)


def test_divergence_batch_build_importable():
    from scripts.run_divergence_batch_build import main

    assert callable(main)


def test_divergence_event_preview_importable():
    from scripts.run_divergence_event_preview import main

    assert callable(main)


def test_divergence_status_importable():
    from scripts.run_divergence_status import main

    assert callable(main)
