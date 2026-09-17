# -*- coding: utf-8 -*-
"""Unit tests for baseline model manual review queue."""

import pytest
import pandas as pd
from advanced_baseline_ml_models.baseline_model_manual_review import (
    MANUAL_REVIEW_TASKS,
    build_baseline_model_manual_review_queue,
    summarize_baseline_model_manual_review_queue,
)


def test_build_baseline_model_manual_review_queue():
    df, summary = build_baseline_model_manual_review_queue()
    assert isinstance(df, pd.DataFrame)
    assert len(df) == len(MANUAL_REVIEW_TASKS)
    assert len(df) == 5
    assert summary["total_review_items"] == 5
    assert summary["all_auto_execution_blocked"] is True
    assert summary["high_priority_items"] == 2
    assert summary["non_signal"] is True
    assert (df["auto_execution_blocked"] == True).all()
    assert (df["status"] == "PENDING_INSPECTION").all()


def test_summarize_baseline_model_manual_review_queue_empty():
    empty_df = pd.DataFrame(columns=[
        "item_id", "review_topic", "target_reference", "severity",
        "review_instructions", "status", "auto_execution_blocked",
        "non_signal", "production_ready", "broker_ready"
    ])
    summary = summarize_baseline_model_manual_review_queue(empty_df)
    assert summary["total_review_items"] == 0
    assert summary["all_auto_execution_blocked"] is True
    assert summary["high_priority_items"] == 0
