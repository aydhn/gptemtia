"""Unit tests for Phase 119 FX - News metadata alignment registry."""

import pytest
import pandas as pd
from advanced_cross_asset_alignment.fx_news_metadata_alignment import build_fx_news_metadata_alignment_registry


def test_fx_news_metadata_alignment_registry():
    df, summary = build_fx_news_metadata_alignment_registry()
    assert len(df) == 4
    assert summary["total_alignments"] == 4
    assert summary["all_non_signal"] is True
    assert summary["all_no_full_text"] is True
    assert summary["status"] == "READY"

    tags = set(df["news_tag"])
    assert "CENTRAL_BANK" in tags
    assert "INFLATION" in tags
