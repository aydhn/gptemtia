import pytest


def test_script_imports():
    try:
        import scripts.run_mtf_alignment_preview
        import scripts.run_mtf_batch_build
        import scripts.run_mtf_event_preview
        import scripts.run_mtf_status
    except ImportError as e:
        pytest.fail(f"Could not import MTF scripts: {e}")
