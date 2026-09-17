# -*- coding: utf-8 -*-
"""Unit tests for Phase 143 Attribution Calculation Disabled Safeguard."""

import pytest
from advanced_explainability_attribution.attribution_calculation_disabled import (
    verify_attribution_calculation_disabled,
    summarize_attribution_calculation_disabled,
)


def test_attribution_calculation_disabled():
    df, summary = verify_attribution_calculation_disabled()
    assert len(df) == 4
    assert summary["all_disabled"] is True
    assert summary["none_attempted"] is True
    assert summary["all_policy_enforced"] is True
    assert summary["all_non_signal"] is True
