"""Unit tests for Phase 119 validation rules registry."""

import pytest
import pandas as pd
from advanced_cross_asset_alignment.cross_asset_alignment_validation_rules import (
    build_cross_asset_alignment_validation_rule_registry,
    VALIDATION_RULES,
)


def test_validation_rule_registry():
    assert len(VALIDATION_RULES) == 8
    df, summary = build_cross_asset_alignment_validation_rule_registry()
    assert len(df) == 8
    assert summary["total_rules"] == 8
    assert summary["all_enforced"] is True
    assert summary["status"] == "READY"
