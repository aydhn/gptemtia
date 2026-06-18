import pytest
from local_consistency.consistency_config import get_default_local_consistency_profile
from local_consistency.check_registry import build_consistency_check_registry, build_cross_layer_consistency_matrix

def test_build_consistency_check_registry():
    profile = get_default_local_consistency_profile()
    df, summary = build_consistency_check_registry(profile)
    assert not df.empty
    assert summary["total_checks"] > 0

def test_build_cross_layer_consistency_matrix():
    profile = get_default_local_consistency_profile()
    df, summary = build_consistency_check_registry(profile)
    matrix_df, matrix_summary = build_cross_layer_consistency_matrix(df)
    assert matrix_summary is not None
