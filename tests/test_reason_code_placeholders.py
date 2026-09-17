# -*- coding: utf-8 -*-
"""Unit tests for Phase 143 Reason Code Placeholders."""

import pytest
from advanced_explainability_attribution.reason_code_placeholders import (
    build_reason_code_placeholder_registry,
    summarize_reason_code_placeholders,
)


def test_reason_code_placeholders():
    df, summary = build_reason_code_placeholder_registry()
    assert len(df) >= 3
    assert summary["all_placeholder_only"] is True
    assert summary["all_reason_codes_generated_false"] is True
    assert summary["all_non_signal"] is True
