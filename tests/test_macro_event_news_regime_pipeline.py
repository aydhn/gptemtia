"""Tests for Phase 132 Macro/Event/News Regime Pipeline."""

from pathlib import Path
from advanced_macro_event_news_regime.macro_event_news_regime_pipeline import (
    MacroEventNewsRegimePipeline,
)


def test_pipeline_execution():
    pipeline = MacroEventNewsRegimePipeline()
    status_df, summary = pipeline.build_macro_event_news_regime_status(save=False)

    assert not status_df.empty
    assert len(status_df) == 8
    assert summary["pipeline_status"] == "COMPLETED"
    assert summary["current_phase"] == 132
    assert summary["next_phase"] == 133
    assert summary["health_status"] == "HEALTHY"
    assert summary["validation_status"] == "VALIDATION_PASS"
    assert summary["context_score"] >= 0.85
    assert summary["non_signal"] is True
    assert summary["source_preserved"] is True
