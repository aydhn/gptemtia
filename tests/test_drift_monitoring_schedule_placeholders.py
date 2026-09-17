# -*- coding: utf-8 -*-
"""Unit tests for Phase 142 Drift Schedule Placeholders."""

import pytest
from advanced_model_drift_monitoring.drift_monitoring_schedule_placeholders import (
    build_drift_monitoring_schedule_placeholders,
    validate_drift_monitoring_schedule_placeholder,
)


def test_drift_monitoring_schedule_placeholders():
    schedules = build_drift_monitoring_schedule_placeholders()
    assert len(schedules) == 4
    for s in schedules:
        val = validate_drift_monitoring_schedule_placeholder(s)
        assert val["valid"] is True
        assert s.execution_enabled is False
