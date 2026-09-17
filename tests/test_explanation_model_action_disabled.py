# -*- coding: utf-8 -*-
"""Unit tests for Phase 143 Explanation Model Action Disabled Safeguard."""

import pytest
from advanced_explainability_attribution.explanation_model_action_disabled import (
    verify_explanation_model_action_disabled,
    summarize_explanation_model_action_disabled,
)


def test_explanation_model_action_disabled():
    df, summary = verify_explanation_model_action_disabled()
    assert len(df) == 4
    assert summary["all_disabled"] is True
    assert summary["none_attempted"] is True
    assert summary["all_policy_enforced"] is True
    assert summary["all_non_signal"] is True
