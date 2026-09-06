import pandas as pd
from advanced_regime_featurestore_integration.regime_featurestore_metadata_manifest import (
    create_regime_featurestore_metadata_manifest,
    build_regime_featurestore_metadata_manifest,
    summarize_regime_featurestore_metadata_manifest,
)


def test_create_regime_featurestore_metadata_manifest():
    manifest = create_regime_featurestore_metadata_manifest()
    assert manifest.current_phase == 134
    assert manifest.target_final_phase == 160
    assert manifest.next_phase == 135
    assert manifest.contract_count == 10
    assert manifest.catalog_count == 8
    assert manifest.accepted_reference_count == 21
    assert manifest.non_signal is True
    assert manifest.source_preserved is True
    assert manifest.official_approval is False
    assert manifest.production_ready is False
    assert manifest.broker_ready is False
    assert manifest.contains_target_or_prediction is False
    assert manifest.contains_trading_recommendation is False
    assert manifest.contains_full_article_text is False


def test_build_regime_featurestore_metadata_manifest():
    df, summary = build_regime_featurestore_metadata_manifest()
    assert isinstance(df, pd.DataFrame)
    assert len(df) == 1
    assert summary["readiness_score"] == 1.0
    assert summary["non_signal"] is True
    assert summary["current_phase"] == 134


def test_summarize_regime_featurestore_metadata_manifest():
    df, _ = build_regime_featurestore_metadata_manifest()
    summary = summarize_regime_featurestore_metadata_manifest(df)
    assert summary["current_phase"] == 134
    assert summary["non_signal"] is True
    assert summary["production_ready"] is False
    assert summary["manifest_valid"] is True
