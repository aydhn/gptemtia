from advanced_data_lineage.data_lineage_config import get_default_data_lineage_profile
from advanced_data_lineage.provenance_scoring import (
    build_provenance_confidence_score_report,
    calculate_provenance_confidence_score,
    summarize_provenance_confidence_scores,
)


def test_provenance_scoring():
    profile = get_default_data_lineage_profile()
    df, summary = build_provenance_confidence_score_report(profile)
    assert len(df) >= 8
    assert 0.0 <= summary["mean_provenance_score"] <= 1.0
    assert summary["high_confidence_count"] >= 5

    sc = calculate_provenance_confidence_score(df, "advanced_fx_providers_engine", profile)
    assert 0.0 <= sc <= 1.0
