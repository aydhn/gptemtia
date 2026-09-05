from advanced_regime_rule_free.dimensionality_reduction_placeholders import (
    build_dimensionality_reduction_placeholder_registry,
    summarize_dimensionality_reduction_placeholders,
)


def test_build_dimensionality_reduction_placeholder_registry():
    df, summary = build_dimensionality_reduction_placeholder_registry()
    assert len(df) == 4
    assert summary["all_placeholders_only"] is True
    assert summary["all_execution_forbidden"] is True
    assert summary["status"] == "VALID"

    algos = df["algorithm_id"].tolist()
    assert "pca_placeholder" in algos
    assert "umap_placeholder" in algos
    assert "tsne_placeholder" in algos
    assert "autoencoder_placeholder" in algos
