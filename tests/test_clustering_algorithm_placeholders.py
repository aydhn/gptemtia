from advanced_regime_rule_free.clustering_algorithm_placeholders import (
    build_clustering_algorithm_placeholder_registry,
    summarize_clustering_algorithm_placeholders,
)


def test_build_clustering_algorithm_placeholder_registry():
    df, summary = build_clustering_algorithm_placeholder_registry()
    assert len(df) == 6
    assert summary["all_placeholders_only"] is True
    assert summary["all_execution_forbidden"] is True
    assert summary["all_non_signal"] is True
    assert summary["status"] == "VALID"

    algos = df["algorithm_id"].tolist()
    assert "kmeans_placeholder" in algos
    assert "dbscan_placeholder" in algos
    assert "gaussian_mixture_placeholder" in algos
    assert "hdbscan_placeholder" in algos
    assert "hierarchical_placeholder" in algos
    assert "self_organizing_map_placeholder" in algos
