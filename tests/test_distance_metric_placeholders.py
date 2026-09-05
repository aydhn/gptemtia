from advanced_regime_rule_free.distance_metric_placeholders import (
    build_distance_metric_placeholder_registry,
    summarize_distance_metric_placeholders,
)


def test_build_distance_metric_placeholder_registry():
    df, summary = build_distance_metric_placeholder_registry()
    assert len(df) == 5
    assert summary["all_placeholders_only"] is True
    assert summary["all_execution_forbidden"] is True
    assert summary["metrics_status"] == "VALID"

    metrics = df["algorithm_id"].tolist()
    assert "euclidean_placeholder" in metrics
    assert "cosine_placeholder" in metrics
    assert "manhattan_placeholder" in metrics
    assert "correlation_distance_placeholder" in metrics
    assert "dynamic_time_warping_placeholder" in metrics
