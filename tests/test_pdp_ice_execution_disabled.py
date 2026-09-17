# -*- coding: utf-8 -*-
"""Unit tests for Phase 143 PDP and ICE Execution Disabled Safeguard."""

import pytest
from advanced_explainability_attribution.pdp_ice_execution_disabled import (
    verify_pdp_ice_execution_disabled,
    summarize_pdp_ice_execution_disabled,
)


def test_pdp_ice_execution_disabled():
    df, summary = verify_pdp_ice_execution_disabled()
    assert len(df) == 4
    assert summary["all_disabled"] is True
    assert summary["none_attempted"] is True
    assert summary["all_policy_enforced"] is True
    assert summary["all_non_signal"] is True
