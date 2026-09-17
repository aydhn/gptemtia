# -*- coding: utf-8 -*-
"""Unit tests for Phase 143 Attribution Scope Policies."""

import pytest
from advanced_explainability_attribution.attribution_scope_policies import (
    build_attribution_scope_policy_registry,
    summarize_attribution_scope_policies,
)


def test_attribution_scope_policies():
    df, summary = build_attribution_scope_policy_registry()
    assert len(df) >= 3
    assert summary["all_execution_blocked"] is True
    assert summary["all_manual_review_required"] is True
    assert summary["all_non_signal"] is True
