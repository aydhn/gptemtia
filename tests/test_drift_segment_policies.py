# -*- coding: utf-8 -*-
"""Unit tests for Phase 142 Drift Segment Policies."""

import pytest
from advanced_model_drift_monitoring.drift_segment_policies import (
    build_drift_segment_policies,
    validate_drift_segment_policy,
)


def test_drift_segment_policies():
    policies = build_drift_segment_policies()
    assert len(policies) == 5
    for p in policies:
        val = validate_drift_segment_policy(p)
        assert val["valid"] is True
        assert p.execution_enabled is False
