# -*- coding: utf-8 -*-
"""Unit tests for Phase 143 Attribution Method Policies."""

import pytest
from advanced_explainability_attribution.attribution_method_policies import (
    build_attribution_method_policy_registry,
    summarize_attribution_method_policies,
)


def test_attribution_method_policies():
    df, summary = build_attribution_method_policy_registry()
    assert len(df) == 8
    assert summary["all_execution_blocked"] is True
    assert summary["all_blocked_status"] is True
    assert summary["all_non_signal"] is True
