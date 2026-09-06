import pandas as pd
from pathlib import Path
from advanced_regime_featurestore_integration.regime_featurestore_health import (
    build_regime_featurestore_health_check,
    summarize_regime_featurestore_health,
)


def test_build_regime_featurestore_health_check():
    df, summary = build_regime_featurestore_health_check()
    assert isinstance(df, pd.DataFrame)
    assert len(df) == 16
    assert summary["domain"] == "health_domain"
    assert summary["current_phase"] == 134
    assert summary["target_final_phase"] == 160
    assert summary["next_phase"] == 135
    assert summary["all_healthy"] is True
    assert summary["healthy_checks"] == 16


def test_summarize_regime_featurestore_health():
    df, _ = build_regime_featurestore_health_check()
    summary = summarize_regime_featurestore_health(df)
    assert summary["total_checks"] == 16
    assert summary["all_healthy"] is True
