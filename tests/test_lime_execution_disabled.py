# -*- coding: utf-8 -*-
"""Unit tests for Phase 143 LIME Execution Disabled Safeguard."""

import pytest
from advanced_explainability_attribution.lime_execution_disabled import (
    verify_lime_execution_disabled,
    summarize_lime_execution_disabled,
)


def test_lime_execution_disabled():
    df, summary = verify_lime_execution_disabled()
    assert len(df) == 4
    assert summary["all_disabled"] is True
    assert summary["none_attempted"] is True
    assert summary["all_policy_enforced"] is True
    assert summary["all_non_signal"] is True
