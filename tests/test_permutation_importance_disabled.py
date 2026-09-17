# -*- coding: utf-8 -*-
"""Unit tests for Phase 143 Permutation Importance Disabled Safeguard."""

import pytest
from advanced_explainability_attribution.permutation_importance_disabled import (
    verify_permutation_importance_disabled,
    summarize_permutation_importance_disabled,
)


def test_permutation_importance_disabled():
    df, summary = verify_permutation_importance_disabled()
    assert len(df) == 4
    assert summary["all_disabled"] is True
    assert summary["none_attempted"] is True
    assert summary["all_policy_enforced"] is True
    assert summary["all_non_signal"] is True
