# -*- coding: utf-8 -*-
"""Unit tests for Phase 143 Explainability Labels."""

import pytest
from advanced_explainability_attribution.explainability_labels import (
    EXPLAINABILITY_DOMAINS,
    EXPLAINABILITY_STATUSES,
    EXPLAINABILITY_EXECUTION_LABELS,
    validate_explainability_domain,
    validate_explainability_status,
)


def test_explainability_labels():
    assert len(EXPLAINABILITY_DOMAINS) >= 9
    assert "global_explanation_contract_domain" in EXPLAINABILITY_DOMAINS
    assert "feature_attribution_contract_domain" in EXPLAINABILITY_DOMAINS

    assert validate_explainability_domain("global_explanation_contract_domain") is True
    assert validate_explainability_domain("invalid_domain") is False

    assert validate_explainability_status("explainability_contract_ready") is True
    assert validate_explainability_status("invalid_status") is False

    assert "execution_blocked_no_shap" in EXPLAINABILITY_EXECUTION_LABELS
