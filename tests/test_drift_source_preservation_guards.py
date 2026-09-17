# -*- coding: utf-8 -*-
"""Unit tests for Phase 142 Drift Source Preservation Guards."""

import pytest
from advanced_model_drift_monitoring.drift_source_preservation_guards import (
    build_drift_source_preservation_guards,
    validate_storage_operation_safety,
)


def test_source_preservation_guards():
    guards = build_drift_source_preservation_guards()
    assert len(guards) == 1
    assert guards[0].is_active is True


def test_validate_storage_operation_safety():
    assert validate_storage_operation_safety("read_csv")["is_safe"] is True
    assert validate_storage_operation_safety("append_audit_record")["is_safe"] is True
    assert validate_storage_operation_safety("delete")["is_safe"] is False
    assert validate_storage_operation_safety("overwrite_source")["is_safe"] is False
